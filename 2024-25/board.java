import java.io.IOException;
import perlin.*;

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
    
    // public  int owner;
    public String name;
    public static int sizeX;
    public static int sizeY;

    public int[] target = {0,0};

    public board(String name){
        //"this" is used to specify the instance variable, if theres a local of the same name
        // this.owner = owner; 
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
            // System.out.println("Terminal size: " + sizeX*2 + "x" + sizeY);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        this.setBoard();

    }

    public board(String name, String locations){ // board constructor for the server to use
        // this.owner = owner; 
        this.name = name;
        this.board = new String[10][10];
        for (int i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){
                this.board[i][j] = "00";
            }
        }

        this.sizeX = 10;
        this.sizeY = 10;
        this.setBoard(locations);

    }

    public String toString(){
        return "board("+name+")";
    }

    public void setBoard(){
        // System.out.println("Placing ships");

        // Random rn = new Random();

        for (int i =5; i>0; i--){
            int length = i;
            if (i<=2)
                length++;
            int rotation; // 0 = --, 1 = |

            int x;
            int y;

            boolean pass = false;

            // until ship is placed correctly
            while (!pass){
                rotation = (int) (Math.random() * 2  ); // 0 = --, 1 = |


                // get x and y position
                if (rotation==0)
                    x = (int) (Math.random() * (10-length));
                else 
                    x = (int) (Math.random() * 10  );

                if (rotation==1)
                    y = (int) (Math.random() * (10-length));
                else 
                    y = (int) (Math.random() * 10  );

                // System.out.println(length +" "+rotation+" "+x+" "+y);

                boolean fail = false;

                // check ship placement
                for (int j = 0; j < length; j++){
                    
                    if (rotation==0){
                        // System.out.println(board[y][x+j]);
                        if (board[y][x+j] != "00"){
                            // System.out.println("fail");
                            fail = true;
                            break;
                        }
                    } else {
                        // System.out.println(board[y+j][x]);
                        if (board[y+j][x] != "00"){
                            // System.out.println("fail");
                            fail = true;
                            break;
                        }
                    }
                   
                }
                if (fail){
                    // System.out.println("fail");
                    continue;
                }

                pass = true; // it was placed correctly 

                // System.out.print("x"+x);
                // System.out.println("y"+y);

                // actually place the ship
                for (int j = 0; j < length; j++){
                    if (rotation==0){
                        // System.out.println("x: "+(x+j)+" y: "+y);
                        board[y][x+j] = i+"0";
                    } else {
                        // System.out.println("x: "+x+" y: "+(y+j));
                        board[y+j][x] = i+"0";
                    }
                   
                }

            }

        }
        
    }

    public void setBoard(String locations){
        // locations
        // [   "ship type+ x+y+dir"*5     ]
        // ship type: 1-5
        // x|y: 0-9
        // dir: 0-1
        for(int i = 0;i<5;i++){
            int type =(locations.charAt(i*4))-'0';
            int x =(locations.charAt(i*4+1))-'0';
            int y =(locations.charAt(i*4+2))-'0';
            int rotation =(locations.charAt(i*4+3))-'0';
            // System.out.println(  String.valueOf(type)+x+y+rotation);

            int length = type + (type<=2?1:0);
            // System.out.println(length);



            boolean fail = false;

            // check ship placement
            for (int j = 0; j < length; j++){
                
                if (rotation==0){
                    // System.out.println(board[y][x+j]);
                    if (board[y][x+j] != "00"){
                        // System.out.println("fail");
                        fail = true;
                        break;
                    }
                } else {
                    // System.out.println(board[y+j][x]);
                    if (board[y+j][x] != "00"){
                        // System.out.println("fail");
                        fail = true;
                        break;
                    }
                }
                
            }
            if (fail){
                System.out.println("fail");
                return;
            }




        }
    }

    public String[][] printBoard(boolean blink){
        String[][] output= new String[11][11];
        for (int i = 1; i <= 10; i++){
            // output[0][i] = "\033[38;2;255;215;0m" + ((char) (0x24b0 + i+5))+" \033[0m"; //hollow arial
            output[i][0] = "\033[38;2;255;215;0m" + ((char) (0xff20 + i))+"\033[0m"; //double width
        }

        for (int i = 1; i <= 10; i++){
            // output[i][0] = "\033[38;2;255;215;0m" + ((char) (0x2770 + i+5))+" \033[0m"; //negatives
            // output[0][i] = ((char) (0x2780 + i-1))+" "; //hollow sans-serif
            output[0][i] = "\033[38;2;255;215;0m" + ((char) (0xff10 + i-1))+"\033[0m"; //double width
        }

        for (int i = 1; i <= 10; i++){
            for (int j = 1; j <= 10; j++){
                String square = this.board[i-1][j-1];

                if (blink && target[0]==i-1 && target[1]==j-1){
                    // if (blink){
                    //     output[i][j] = "🎯";
                    // } else {
                    //     output[i][j] = "​ ";
                    // }
                    output[i][j] = "🎯";
                    // System.out.print("🎯 ");
                } else if (square.substring(1).equals("0")){ // not hit
                    output[i][j] = "  ";
                    // System.out.print("☁️ ");
                    // System.out.print("  ");
                } else { //hit
                    // output[i][j] = "B";
                    if (square.substring(0,1).equals("0")){ // splash
                        output[i][j] = "💦";
                        // System.out.print("💦 ");
                    } else {
                        output[i][j] = "💥";
                        // System.out.print("hit"+square);
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

    public String[][] printBoard(){
        return printBoard(false);
    }

    public String hit(){
        if (this.board[this.target[0]][this.target[1]].substring(1).equals("0")){ // not hit
            this.board[this.target[0]][this.target[1]] =this.board[this.target[0]][this.target[1]].substring(0,1)+"1";
        } else{
            //pick random spot
            int x = (int) (Math.random() * 10);
            int y = (int) (Math.random() * 10);
            while (this.board[y][x].charAt(0) =='1'){ // already hit
                x = (int) (Math.random() * 10);
                y = (int) (Math.random() * 10);
            }
            // System.out.println("Random hit: "+x+" "+y);
            this.target[0]=y;this.target[1]=x;
            this.board[y][x] =this.board[y][x].substring(0,1)+"1";
        }
        return this.board[this.target[0]][this.target[1]].charAt(0) =='0' ? "miss :( " : "hit :) ";
    }

    public static String[][] overlayBoard(int newX, int newY, int startX, int startY, String[][] overlay){
        String[][] canvas = new String[newY][newX];
        return overlayBoard(startX, startY, canvas, overlay);
    }

    public static String[][] overlayBoard(int startX, int startY, String[][] overlay){
        String[][] canvas = new String[sizeY][sizeX];
        return overlayBoard(startX, startY, canvas, overlay);
    }

    public static String[][] overlayBoard(int startX, int startY, String[][] canvas, String[][] overlay){
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

        // System.out.println("\033[38;2;255;215;0m" +"bonjour "+"\033[0m"); //double width

        board b = new board("Bob");
        board a = new board("Alice");

        if (sizeY <= 10){
            System.out.println("Terminal too small "+sizeX+":"+sizeY);
            return;
        }

        perlin p = new perlin();
        

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
            }
        // p.loop();




        // System.out.println(b.board[0][0]); // should fail because board is private
    }
}
