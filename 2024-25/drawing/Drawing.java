package drawing;

import java.util.Map;
import java.util.HashMap;

public class Drawing{

    static Map<Integer, String> quarterMap = new HashMap<>(Map.ofEntries(
            Map.entry(0, " "),
            Map.entry(1111, "█"), //	█
            Map.entry(1000, "▘"),
            Map.entry(100, "▝"),
            Map.entry(10, "▖"),
            Map.entry(1, "▗"),
            Map.entry(1100, "▀"),
            Map.entry(110, "▞"), //shouldn't hit
            Map.entry(11, "▄"),
            Map.entry(1001, "▚"), //shouldn't hit
            Map.entry(1010, "▌"),
            Map.entry(101, "▐"),
            Map.entry(1110, "▛"),
            Map.entry(1101, "▜"),
            Map.entry(111, "▟"),
            Map.entry(1011, "▙")
    ));
    static final double radiusOffset = -.25;

    public static void main(String[] args){
        // overlay(20, 20, 5, 5, stripes(20, 20, 2));
        // overlay(20, 20, 5, 5, circle(5));
        // circle(5);
        // pickQuarter(0, 0, 3);
        stripes(20, 20, 2);
        
    }


    public static String[][] overlay(int newX, int newY, int startX, int startY, String[][] overlay){
        String[][] canvas = new String[newY][newX];
        return overlay(startX, startY, canvas, overlay);
    }

    // public static String[][] overlay(int startX, int startY, String[][] overlay){
    //     String[][] canvas = new String[sizeY][sizeX];
    //     return overlay(startX, startY, canvas, overlay);
    // }

    public static String[][] overlay(int startX, int startY, String[][] canvas, String[][] overlay){
        for (int i = 0; i < overlay.length; i++) {
            for (int j = 0; j < overlay[i].length; j++) {
                if (overlay[i][j] != null) {
                    canvas[startY + i][startX + j] = overlay[i][j];
                }
            }
        }
        return canvas;
    }

    public static String pickQuarter(int x, int y, double radius){
        //▖, ▗, ▘, ▝, ▙, ▛, ▜, ▟, 
        //▄, ▀, 	
        //▌, ▐, 
        //▚, ▞, 
        //█, " ", 
        //-.25, +.25 v & h
        // boolean[] qs = new boolean[4];
        
        // int q=0;
        // int q2=0
        int[] qs = new int[2];
        for (int i=-1; i<1; i++){
            
            // for (double xOff = -.25; xOff <= .25; xOff+=.5){
            for (double yOff = -.25; yOff <= .25; yOff+=.5){
                for (double xOff = -.125; xOff <= .125; xOff+=.25){
                
                    // q*=10;
                    qs[i+1]*=10;
                    if (Math.pow(x+xOff+  (double)i/2+.25  , 2) + Math.pow(y+yOff, 2) <= Math.pow(radius, 2)+radiusOffset){
                        // System.out.print(", q: " + q);
                        // qs[q]=true

                        // q+=1;
                        qs[i+1]++;
                    }
                    // q++;
                }
            }
        }

        return quarterMap.get(qs[0]) + quarterMap.get(qs[1]);



    }
    
    public static String[][] circle(double radius){
        String[][] circle = new String[(int) (2*radius)+1][(int) (2*radius)+1];
        for (int y =-1 * (int) radius; y < radius+1; y++){
            for (int x = -1 * (int) radius; x < radius+1; x++){
                
                if (Math.pow(x, 2) + Math.pow(y, 2) <= Math.pow(radius, 2)+1){
                    // circle[(int)(y+radius)][(int)(x+radius)] = "Xx";
                    circle[(int)(y+radius)][(int)(x+radius)] = pickQuarter(x,y,radius);
                    
                } else {
                    circle[(int)(y+radius)][(int)(x+radius)] = "no";
                }
                System.out.print(circle[(int)(y+radius)][(int)(x+radius)]);
                // System.out.println("x: " + (x) + " y: " + (y));
            }
            System.out.println();
        }
        return circle;
    }

    public static String[][] stripes(int width, int height, int stripeWidth,double angle){
        String[][] stripes = new String[height][width];

        // line y = mx + b
        // y = tan(angle) * x + height


        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {


                stripes[i][j] = j % stripeWidth == 0 ? "x" : " ";
                // stripes[i][j] = j % stripeWidth == 0 ? "▚" : " ";

                System.out.print(stripes[i][j]);
            }
            System.out.println();
        }
        return stripes;
    }



}