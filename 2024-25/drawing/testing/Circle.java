import java.util.Map;
import java.util.HashMap;

public class Circle{

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
        circle(5);
        // pickQuarter(0, 0, 3);
    }

    public static String[][] circleV1(double radius){
        String[][] circle = new String[(int) (2*radius)+1][(int) (2*radius)+1];
        for (int y =-1 * (int) radius; y < radius+1; y++){
            for (int x = -1 * (int) radius; x < radius+1; x++){
                
                if (Math.pow(x, 2) + Math.pow(y, 2) <= Math.pow(radius, 2)){
                    circle[(int)(y+radius)][(int)(x+radius)] = "Xx";
                    
                } else {
                    circle[(int)(y+radius)][(int)(x+radius)] = "  ";
                }
                System.out.print(circle[(int)(y+radius)][(int)(x+radius)]);
                // System.out.println("x: " + (x) + " y: " + (y));
            }
            System.out.println();
        }
        return circle;
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

        // Map<Integer, String> quarterMap = new HashMap<>();
        // quarterMap.put(0000, " ");
        // quarterMap.put(1111, "X"); //█	

        // quarterMap.put(1000, "▘");
        // quarterMap.put(0100, "▝");
        // quarterMap.put(0010, "▖");
        // quarterMap.put(0001, "▗");

        // quarterMap.put(1100, "▀");
        // quarterMap.put(0110, "▞"); //shouldn't hit
        // quarterMap.put(0011, "▄");
        // quarterMap.put(1001, "▚"); //shouldn't hit
        // quarterMap.put(1010, "▌");
        // quarterMap.put(0101, "▐");
        
        // quarterMap.put(1110, "▛");
        // quarterMap.put(0111, "▜");
        // quarterMap.put(1011, "▟");
        // quarterMap.put(1101, "▙");
        
        
        

        
        // System.out.print(qs[0] + ", " + qs[1] + " ");
        // System.out.print(quarterMap.get(qs[0]));
        // System.out.println(quarterMap.get(qs[1]));
        return quarterMap.get(qs[0]) + quarterMap.get(qs[1]);



    }
    
    public static String[][] circle(double radius){
        String[][] circle = new String[(int) (2*radius)+1][(int) (2*radius)+1];
        for (int y =-1 * (int) radius; y < radius+1; y++){
            for (int x = -1 * (int) radius; x < radius+1; x++){
                
                if (Math.pow(x, 2) + Math.pow(y, 2) <= Math.pow(radius, 2)+2){
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
}