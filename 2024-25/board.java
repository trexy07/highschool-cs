import java.io.IOException;
import java.util.Scanner;

public class board{

    // each spot is boat/no boat and hit/none
    /*
    boat id's:
    No. Class of ship   Size
    0   Empty           1
    1   Carrier         5
    2   Battleship      4
    3   Destroyer       3
    4   Submarine       3
    5   Patrol Boat     2

    hits:
    1 = hit
    0 = not hit
    
    each square = boat id + hit

    */
    private String[][] board;
    
    public  int owner;
    public  String name;
    public static int sizeX;
    public static int sizeY;

    public board(int owner, String name){
        //"this" is used to specify the instance variable, if theres a local of the same name
        this.owner = owner; 
        this.name = name;
        this.board = new String[10][10];
        for (int i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){
                this.board[i][j] = "00"; // each spot is boat/no boat and hit/none
            }
        }

        try {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
            System.out.println("Terminal size: " + sizeX*2 + "x" + sizeY);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

    }

    public void placeShips(){
        System.out.println("Placing ships");
    }

    public String[][] printBoard(){
        String[][] output= new String[11][11];
        for (int i = 1; i <= 10; i++){
            // output[0][i] = "\033[38;2;255;215;0m" + ((char) (0x24b0 + i+5))+" \033[0m"; //hollow arial
            output[0][i] = "\033[38;2;255;215;0m" + ((char) (0xff20 + i))+"\033[0m"; //double width
        }

        for (int i = 1; i <= 10; i++){
            // output[i][0] = "\033[38;2;255;215;0m" + ((char) (0x2770 + i+5))+" \033[0m"; //negitives
            // output[0][i] = ((char) (0x2780 + i-1))+" "; //hollow sans-serif
            output[i][0] = "\033[38;2;255;215;0m" + ((char) (0xff10 + i-1))+"\033[0m"; //double width
        }

        for (int i = 1; i <= 10; i++){
            for (int j = 1; j <= 10; j++){
                String square = this.board[i-1][j-1];

                if (square.substring(1).equals("0")){ // not hit
                    output[i][j] = "  ";
                    // System.out.print("☁️ ");
                    // System.out.print("  ");
                } else { //hit
                    // output[i][j] = "B";
                    if (square.substring(0,1)!="0"){ // splash
                        output[i][j] = "💦 ";
                        // System.out.print("💦 ");
                    } else {
                        output[i][j] = "💥 ";
                        // System.out.print("💥 ");

                    }
                }
                // System.out.print(this.board[i][j]);
                // + this.board[i][j];


            }
            // System.out.println();
        }
        return output;
    }

    private static String[][] overlayBoard(int startX, int startY, String[][] overlay){
        String[][] canvas = new String[sizeY][sizeX];
        return overlayBoard(startX, startY, canvas, overlay);
    }

    private static String[][] overlayBoard(int startX, int startY, String[][] canvas, String[][] overlay){
        for (int i = 0; i < overlay.length; i++) {
            for (int j = 0; j < overlay[i].length; j++) {
                if (overlay[i][j] != null) {
                    canvas[startY + i][startX + j] = overlay[i][j];
                }
            }
        }
        return canvas;
    }

    public static void main(String[] args){
        board b = new board(1, "Bob");
        board a = new board(2, "Alice");
        perlin p = new perlin();
        
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String[][] output = b.printBoard();
            String[][] canvas = overlayBoard(sizeX/4-5, sizeY/2-5, output);

            output = a.printBoard();
            canvas = overlayBoard(3 * sizeX / 4 - 5, sizeY/2-5, canvas, output);

            System.out.print(p.nextFrame(canvas));

            try {
            Thread.sleep(1000); // wait for 1 second
            } catch (InterruptedException e) {
            e.printStackTrace();
            }

            System.out.print("next: "+scanner.next());

            // try {
            //     System.out.println("available: "+System.in.available());
            //     if (System.in.available() > 0) {
            //         int input = System.in.read();
            //         System.out.println("in: "+input);
            //         if (input == 65) {
            //             System.out.println("Detected 'a' key press");
            //         }
            //     }
            // } catch (IOException e) {
            //     e.printStackTrace();
            // }
            // try {
            //     int firstByte = System.in.read();
            //     System.out.println(firstByte);
            // } catch (IOException e) {
            //     e.printStackTrace();
            // }
        }
        // p.loop();




        // System.out.println(b.board[0][0]); // should fail because board is private
    }
}
