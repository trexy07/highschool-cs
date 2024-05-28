class Node():
    def __init__(self,v=0,l=None,r=None):
        self.value=v
        self.left=l
        self.right=r
    def __repr__(self):
        return f"Node({self.value}, {repr(self.left)}, {repr(self.right)})"
    def __eq__(self,other):
        return isinstance(other,Node) and self.value==other.value
