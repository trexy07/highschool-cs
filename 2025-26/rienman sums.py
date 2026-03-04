import numpy as np
import trimesh
import sympy as sp
import shapely.geometry as geom
import math

X = sp.symbols('x')


# def f(x): return x**2 + 1
# def g(x): return x + 4

def f(x): return math.e**-((x**2)/2)
def g(x): return 0
# def f(x): return math.sin(x)
# def g(x): return x + 0.5
# def h(x):
#     return x # square

# square cross-section
def sq(dx, thickness):
    height=thickness  
    z_offset = height / 2
    return height, z_offset, trimesh.creation.box(
        extents=[dx, thickness, height]
    )

# equilateral triangle cross-section
def tri(dx, thickness):
    # For equilateral triangle: height = base * sqrt(3)/2
    height = thickness * np.sqrt(3) / 2
    z_offset = 0
    
    # Create triangle vertices (base on xy-plane, pointing up in z)
    # Base vertices at z=0, apex at z=height
    vertices = np.array([
        [-dx/2, -thickness/2, 0],
        [dx/2, -thickness/2, 0],
        [dx/2, thickness/2, 0],
        [-dx/2, thickness/2, 0],
        [-dx/2, 0, height],
        [dx/2, 0, height]
    ])
    
    faces = np.array([
        [0, 1, 4], [1, 5, 4],  # front face (triangles)
        [2, 3, 4], [2, 4, 5],  # back face (triangles)
        [0, 3, 2], [0, 2, 1],  # bottom face (base)
        [0, 4, 3], [1, 2, 5]   # side faces
    ])
    
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    return height, z_offset, mesh

# semi-circle cross-section
def semi_circle(dx, thickness, segments=32):
    # thickness is the diameter
    radius = thickness / 2
    height = thickness
    z_offset = 0  # Align flat edge with base

    # Create semi-circle in the xy-plane, extrude along x by dx
    theta = np.linspace(0, np.pi, segments)
    # Points along the semi-circle edge
    edge_points = np.array([
        [0, radius * np.cos(t), radius * np.sin(t)] for t in theta
    ])
    # Shift so center is at (0,0,0)
    edge_points[:,1] += 0

    # Create vertices for both ends of extrusion
    verts0 = edge_points.copy()
    verts0[:,0] = -dx/2
    verts1 = edge_points.copy()
    verts1[:,0] = dx/2

    # Combine vertices
    vertices = np.vstack([verts0, verts1])

    # Faces for sides
    faces = []
    for i in range(segments-1):
        # Side faces (quads split into two triangles)
        a, b = i, i+1
        faces.append([a, b, b+segments])
        faces.append([a, b+segments, a+segments])

    # Add flat-side rectangle along the diameter (missing side)
    a0, a1 = 0, segments - 1
    b0, b1 = a0 + segments, a1 + segments
    faces.append([a0, b1, a1])
    faces.append([a0, b0, b1])

    # Flat face (bottom)
    center0 = len(vertices)
    center1 = len(vertices)+1
    vertices = np.vstack([vertices, [[-dx/2, 0, 0], [dx/2, 0, 0]]])
    for i in range(segments-1):
        faces.append([center0, i+1, i])  # flip left end-cap
        faces.append([center1, i+segments, i+1+segments])

    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    return height, z_offset, mesh



solutions = sp.solve(f(X) - g(X), X)
print("Intersection points:", solutions)




# a, b = -2, 3
# a,b=float(solutions[0]), float(solutions[-1])
a,b=0,3
n = 200 # subdivisions
dx = (b - a) / n # dx

boxes = []

for i in range(n):
    x = a + i * dx

    F,G = f(x), g(x)
    lower = min(F, G)
    upper = max(F, G)

    thickness = upper - lower

    # height, z_offset, box = sq(dx, thickness)
    # height, z_offset, box = tri(dx, thickness)
    height, z_offset, box = semi_circle(dx, thickness)

    # Rainbow color: cycle hue from 0 to 1
    hue = (i % n) / n
    import colorsys
    red, green, blue = colorsys.hsv_to_rgb(hue, 1, 1)
    color = np.array([int(red*255), int(green*255), int(blue*255), 255])
    box.visual.face_colors = color

    box.apply_translation([
        x + dx / 2,
        lower + thickness / 2,
        z_offset  # Now this is 0, so flat edge sits at 'lower'
    ])

    boxes.append(box)

print("slices created:", len(boxes))


solid = trimesh.util.concatenate(boxes)
# solid.export("riemann_solid.stl")
solid.show()
