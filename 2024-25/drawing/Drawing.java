package drawing;

import java.util.Map;
import java.util.HashMap;

import java.io.IOException;

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
    static final BiFunction<Double,Double, Double> mod = (a,b) -> (a-b*Math.floor(a/b));
    // static final BiFunction<Int,Int, Double> mod = (a,b) -> (a-b*Math.floor(a/b));


    public static void main(String[] args){
        // overlay(20, 20, 5, 5, stripes(20, 20, 2));
        // overlay(20, 20, 5, 5, circle(5));
        // circle(5);
        // circle(4,5);
        // pickQuarter(0, 0, 3);
        // stripes(10, 10, 2, -Math.PI/6);
        // String[][] canvas = stripes(6, 1, 2, -Math.PI/4);
        // String[][] canvas = fill(4, 2);
        
        
        String[][] canvas = stripes(6, 6, 2, -Math.PI/4);
        canvas = colorize(canvas, "\033[33;40m");
        String[][] canvas2 = fill(10, 10);
        canvas2 = colorize(canvas2, "\033[31m");
        String[][] canvas3 = overlay(0, 0, canvas2, canvas);
        print(canvas3);


        // String[][] canvas3 = colorize(canvas2, (x,y) -> ((mod.apply((double)x,2.0)<1) ? "\033[35m":""   ));

        

        
    }

    public static void print(String[][] output){
        for (int y = 0; y < output.length; y++) {
            for (int x = 0; x < output[y].length; x++) {
                System.out.print(output[y][x]);
            }
            System.out.println();
        }
    }

    // makes a new canvas of null strings and overlays the overlay
    public static String[][] overlay(int newX, int newY, int startX, int startY, String[][] overlay){
        String[][] canvas = new String[newY][newX];
        return overlay(startX, startY, canvas, overlay);
    }

    // assumes canvas size is the terminal size
    public static String[][] overlay(int startX, int startY, String[][] overlay){
        try {
            int[]      terminalSize = TerminalSize.getTerminalSize(); // import from other file
            String[][] canvas       = new String[terminalSize[0]][terminalSize[1] / 2];
            return overlay(startX, startY, canvas, overlay);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            String[][] canvas       = new String[80][40];
            return overlay(startX, startY, canvas, overlay);
        }
    }

    // public static String[][] overlay(int startX, int startY, String color, String[][] overlay){
    //     try {
    //         int[]      terminalSize = TerminalSize.getTerminalSize(); // import from other file
    //         String[][] canvas       = new String[terminalSize[0]][terminalSize[1] / 2];
    //         return overlay(startX, startY, color, canvas, overlay);
    //     } catch (IOException | InterruptedException e) {
    //         e.printStackTrace();
    //         String[][] canvas       = new String[80][40];
    //         return overlay(startX, startY, color, canvas, overlay);
    //     }
    // }

    // overlays the overlay onto an existing canvas
    public static String[][] overlay(int startX, int startY, String[][] canvas, String[][] overlay){
        // return overlay(startX, startY, "", canvas, overlay);
        for (int i = 0; i < overlay.length; i++) {
            for (int j = 0; j < overlay[i].length; j++) {
                if (overlay[i][j] != null) {
                    canvas[startY + i][startX + j] = overlay[i][j];
                    
                }
            }
        }
        return canvas;
    }

    // public static String[][] overlay(int startX, int startY, String color, String[][] canvas, String[][] overlay){
    //     for (int i = 0; i < overlay.length; i++) {
    //         for (int j = 0; j < overlay[i].length; j++) {
    //             if (overlay[i][j] != null) {
    //                 canvas[startY + i][startX + j] = color+overlay[i][j];
    //             }
    //         }
    //     }
    //     return canvas;
    // }

    public static String[][] colorize(String[][] canvas, String color){
        for (int y = 0; y < canvas.length; y++) {
            for (int x = 0; x < canvas[y].length; x++) {
                String block = canvas[y][x];
                if (block != null) {
                    while (block.indexOf("\033[")!=-1){

                        block =  block.substring(0, block.indexOf("\033[")  )
                              +  block.substring(   block.indexOf("m"    )+1);
                    }
                    canvas[y][x] = color+block.substring(0,1)+"\033[0m" + color + block.substring(1)+"\033[0m";

                    // canvas[y][x] = color+canvas[y][x]+"\033[0m";
                    System.out.print(canvas[y][x]);
                }
            }
            System.out.println();
        }
        return canvas;
    }

    public static String[][] colorize(String[][] canvas, BiFunction<Double,Integer, String> condition){
        for (int y = 0; y < canvas.length; y++) {
            for (int x = 0; x < canvas[y].length; x++) {
                String block = canvas[y][x];
                String result = "";
                if (block != null){
                    for (int i=-1;i<=1;i+=2){
                        // while (block.indexOf("\033[")!=-1){
                        String old = "";
                        if (block.indexOf("\033[")!=-1){
                            old   = block.substring(0,block.indexOf("m")+1  );
                            block = block.substring(block.indexOf("m")+1  );
                            // System.out.println("case1");
                            // System.out.print(old);
                            // System.out.println("\033[0m");
                            // System.out.println(block);

                        } else {
                            // System.out.println("case2");
                            old = "\033[0m";
                        }
                        
                        //       +  block.substring(   block.indexOf("m"    )+1);
                        String color = condition.apply(x + i*.25, y);
                        // if (result == null){
                        if (color==""){
                            result += old;
                            // result += block.substing;
                        } else {
                            result += color;
                            // result = result + chblock;
                        }
                        result += block.substring(0,1)+ "\033[0m";
                        block = block.substring(block.indexOf("m")+1);
                    }
                    
                
                }
                canvas[y][x] = result;
                System.out.print(result);
            }
            System.out.println();
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
        return checkGrid(0, 0, width, height, precise, broad);
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
                    // System.out.println("hit@"+x+","+y);
                } else {
                    // grid[y -(int)startY][x -(int)startX] = "Xx";
                    grid[y -(int)startY][x -(int)startX] = "  ";
                }

                System.out.print(grid[y -(int)startY][x -(int)startX]);
            }
            System.out.println();
        }
        return grid;
    }

    public static String[][] fill(double width, double height){
        return checkGrid(
            (int) Math.ceil(width), (int) Math.ceil(height), 
            (x2,y2) -> (x2<width-.5) && (y2<height-.5),
            (x2,y2) -> true
        );
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

    // given interior and exterior radius, makes circle outline out of text
    public static String[][] circle(double min,double max){
        return checkGrid(
            -(int)max,
            -(int)max,
            (int) (2*max)+1, 
            (int) (2*max)+1, 
            (x2,y2) -> Math.abs(Math.pow(x2, 2) + Math.pow(y2, 2) - (Math.pow(min, 2) + Math.pow(max, 2))/2 ) <= (Math.pow(max, 2) - Math.pow(min, 2))/2 + radiusOffset,
            (x2,y2) -> Math.abs(Math.pow(x2, 2) + Math.pow(y2, 2) - (Math.pow(min, 2) + Math.pow(max, 2))/2 ) <= (Math.pow(max, 2) - Math.pow(min, 2))/2 + 1
        );
    }


    // given size, makes 45° small stripes out of text
    public static String[][] stripes(int width, int height){
        return stripes(width, height, 1, -Math.PI/4);
    }

    // given size and stripe width, makes 45° stripes out of text
    public static String[][] stripes(int width, int height, double stripeWidth){
        return stripes(width, height, stripeWidth, -Math.PI/4);
    }

    // given size, stripe width, and angle, makes angled stripes out of text
    public static String[][] stripes(int width, int height, double stripeWidth, double angle){
        return stripes(width, height, stripeWidth, stripeWidth, angle);
    }

    // given size, stripe sizes, and angle, makes angled stripes out of text
    public static String[][] stripes(int width, int height,double gapWidth, double stripeWidth, double angle){
        double mx = Math.cos(angle);
        double my = Math.sin(angle);
        return checkGrid(
            width, height, 
            (x2,y2) -> mod.apply(my*x2+mx*y2+height  ,gapWidth+stripeWidth) < stripeWidth,
            (x2,y2) -> mod.apply(my*x2+mx*y2+height+1,gapWidth+stripeWidth) < stripeWidth+2         
        );
        // in normal algebra this function would be tan(-pi/4)*x+y+ width modulo 2*width < width, 
        // but java uses remainder instead of modulo, so a replacement function was added
    }
    
    



    

}