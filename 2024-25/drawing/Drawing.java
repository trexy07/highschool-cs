package drawing;

import java.util.Map;
import java.util.HashMap;

// import java.util.function.Predicate;
import java.util.function.BiFunction;



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
        circle(5);
        // pickQuarter(0, 0, 3);
        // stripes(20, 20, 2);
        // checkGrid(
        //     20, 
        //     20, 
        //     (x2,y2) -> (Math.tan(-Math.PI/4)*x2+y2+20)%(2*2)<=2, 
        //     (x2,y2) -> (Math.tan(-Math.PI/4)*x2+y2+20)%(2*2)<=2+1
        // );
        
    }

    // makes a new canvas of null strings and overlays the overlay
    public static String[][] overlay(int newX, int newY, int startX, int startY, String[][] overlay){
        String[][] canvas = new String[newY][newX];
        return overlay(startX, startY, canvas, overlay);
    }

    // assumes canvas size is the terminal size
    // public static String[][] overlay(int startX, int startY, String[][] overlay){
    //     String[][] canvas = new String[sizeY][sizeX];
    //     return overlay(startX, startY, canvas, overlay);
    // }

    // overlays the overlay onto an existing canvas
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


    // divides each square of 2 chars into 2x 4 quarters
    public static String pickQuarter(int x, int y, BiFunction<Double,Double, Boolean> condition){
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

                    // if (Math.pow(x+xOff+  (double)i/2+.25  , 2) + Math.pow(y+yOff, 2) <= Math.pow(radius, 2)+radiusOffset){
                    if (condition.apply(x+xOff+  (double)i/2+.25,  y+yOff)){
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


    // given a size, checks each square for a condition, checks sub squares
    public static String[][] checkGrid(int width, int height, BiFunction<Double,Double, Boolean> condition){
        return checkGrid(width, height, condition, condition);
    }

    // given a size, checks each square for a condition, then precisely check sub squares
    public static String[][] checkGrid(int width, int height, BiFunction<Double,Double, Boolean> precise, BiFunction<Double,Double, Boolean> broad){
        String[][] grid = new String[height][width];


        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {

                if (broad.apply((double)x, (double)y)){
                    // System.out.print("██");
                    grid[y][x] = pickQuarter(x, y, precise);

                } else {
                    // System.out.print("  ");
                    grid[y][x] = "  ";
                }
                // stripes[i][j] = j % stripeWidth == 0 ? "x" : " ";
                // stripes[i][j] = j % stripeWidth == 0 ? "▚" : " ";
                // stripes[y][x] = (Math.tan(angle)*x+y+height)%(2*stripeWidth)<stripeWidth ? "██" : "  ";
                // stripes[y][x] = (Math.tan(angle)*x+y+height)%(2*stripeWidth)<=stripeWidth+1 ? pickQuarter(x,y, (x2,y2) -> (Math.tan(angle)*x2+y2+height)%(2*stripeWidth)<stripeWidth    ) : "  ";

                System.out.print(grid[y][x]);
            }
            System.out.println();
        }
        return grid;
    }

    // given a size and offset, checks each square for a condition, checks sub squares
    public static String[][] checkGrid(int startX, int startY, int width, int height, BiFunction<Double,Double, Boolean> condition){
        return checkGrid(startX, startY, width, height, condition, condition);
    }

    // given a size and offset, checks each square for a condition, then precisely check sub squares
    public static String[][] checkGrid(int startX, int startY, int width, int height, BiFunction<Double,Double, Boolean> precise, BiFunction<Double,Double, Boolean> broad){
        String[][] grid = new String[height][width];


        for (int y = startY; y < height+startY; y++) {
            for (int x = startX; x < width+startX; x++) {

                if (broad.apply((double)x, (double)y)){
                    grid[y -(int)startY][x -(int)startX] = pickQuarter(x, y, precise);

                } else {
                    grid[y -(int)startY][x -(int)startX] = "  ";
                }

                System.out.print(grid[y -(int)startY][x -(int)startX]);
            }
            System.out.println();
        }
        return grid;
    }
    
    // given radius, makes circle out of text
    public static String[][] circle(double radius){
        return checkGrid(
            -(int)radius,
            -(int)radius,
            (int) (2*radius)+1, 
            (int) (2*radius)+1, 
            (x2,y2) -> Math.pow(x2, 2) + Math.pow(y2, 2) <= Math.pow(radius, 2)+radiusOffset,
            (x2,y2) -> Math.pow(x2, 2) + Math.pow(y2, 2) <= Math.pow(radius, 2)+1
        );
    }


    // given size, makes 45° small stripes out of text
    public static String[][] stripes(int width, int height){
        return stripes(width, height, 1, -Math.PI/4);
    }

    // given size and stripe width, makes 45° stripes out of text
    public static String[][] stripes(int width, int height, int stripeWidth){
        return stripes(width, height, stripeWidth, -Math.PI/4);
    }

    // given size, stripe width, and angle, makes angled stripes out of text
    public static String[][] stripes(int width, int height, int stripeWidth,double angle){
        return checkGrid(
            width, height, 
            (x2,y2) -> (Math.tan(angle)*x2+y2+height)%(2*stripeWidth)<=stripeWidth,
            (x2,y2) -> (Math.tan(angle)*x2+y2+height)%(2*stripeWidth)<=stripeWidth+1
        );
    }

    
    



    

}