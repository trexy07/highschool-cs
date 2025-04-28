import java.io.IOException;
import java.util.ArrayList;
// import java.io.BufferedWriter;
// import java.io.FileWriter;
// import java.io.FileOutputStream;
import java.io.DataOutputStream;

import java.io.BufferedWriter;
import java.io.FileWriter;

// import perlin.*;
import drawing.*;

public class Board{

    // each spot is boat/no boat and hit/none
    /*
    boat id's:
    No. Class of ship   Size
    0   Empty           1
    1   Destroyer       2
    2   Submarine       3
    3   Cruiser         3
    4   Battleship      4
    5   Carrier         5
    
    hits:
    1 = hit
    0 = not hit
    
    each square = boat id + hit

    */
    public              String[][] board;
    public              String     name;
    
    public static       int        sizeX;
    public static       int        sizeY;

    public              int[]      target = {0,0};
    // public        int        hits   = 5+4+3+3+2;
    public              int        hits[]   = {2,3,3,4,5};
    public              String[]   ships;
    public static final String[]   AMERICAN ={"USS Shaw","USS Narwhal","USS Helena","USS Arizona","USS Enterprise"}; // real ships near/at pearl harbor
    public static final String[]   JAPANESE ={"IJN Akebono","IJN I-19", "IJN Chikuma","IJN Nagato","IJN Akagi"};
    

    // public              ArrayList<Integer>    history; // not needed?
    // public        BufferedWriter        save;
    // public        FileOutputStream      save;
    public              DataOutputStream      save;
    public              byte[]                locations = new byte[5];


    public Board(String name){
        //"this" is used to specify the instance variable, if theres a local of the same name
        this.name  = name;
        this.board = new String[10][10];
        // this.history = new ArrayList<Integer>();

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
        this.ships = AMERICAN;
    }

    public Board(String name, DataOutputStream save){
        this(name);
        this.save = save;
        
        try{
            this.save.writeBytes(name);
            this.save.write(127);
            this.save.write(this.locations);//(char[])
            this.save.write(127);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Board(String name, String locations){ // board constructor for the server to use
        this.name  = name;
        this.board = new String[10][10];
        // this.history = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){
                this.board[i][j] = "00";
            }
        }

        sizeX = 10;
        sizeY = 10;
        this.setBoard(locations);
        this.ships = AMERICAN;
    }

    public Board(String name, String locations, DataOutputStream save){
        this(name,locations);
        this.save = save;
        
        try{
            this.save.writeBytes(name);
            this.save.write(127);
            this.save.write(this.locations);
            this.save.write(127);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void side(boolean force){
        ships = force ? AMERICAN : JAPANESE;
    }

    public String toString(){
        return "board("+name+")";
    }

    public void setBoard(){
        // System.out.println("Placing ships");

        // Random rn = new Random();

        for (int i = 5; i>0; i--){
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
                    } else          {
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
                    } else          {
                        // System.out.println("x: "+x+" y: "+(y+j));
                        board[y+j][x] = i+"0";
                    }
                   
                }

                // record ship placement
                this.locations[i-1] = (byte)(x + y*10 + rotation*-128);

            }

        }
        
    }

    public void setBoard(String locations){
        // locations
        // [   "ship type+ x+y+dir"*5     ]
        // ship type: 1-5 -- no more ship type
        // x|y: 0-9
        // dir: 0-1
        for(int i = 0; i<5; i++){
        // if (false){ int i = 0;
            // old mode
            // int type     = (locations.charAt(i*4  )) - '0';
            // int x        = (locations.charAt(i*4+1)) - '0';
            // int y        = (locations.charAt(i*4+2)) - '0';
            // int rotation = (locations.charAt(i*4+3)) - '0';

            // new mode
            int x        = (locations.charAt(i*3)) - '0';
            int y        = (locations.charAt(i*3+1)) - '0';
            int rotation = (locations.charAt(i*3+2)) - '0';

            // System.out.println(  x+","+y+","+rotation);
            // System.out.println(  String.valueOf(type)+x+y+rotation);

            // int length   = type + (type<=2?1:0);
            int length   = i + (i<2?2:1);
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
                } else          {
                    // System.out.println(board[y+j][x]);
                    if (board[y+j][x] != "00"){
                        // System.out.println("fail");
                        fail = true;
                        break;
                    }
                }
                
            }
            if (fail){ // ship placement invalid
                System.out.println("placement fail");
                return;
            }

            // actually place the ship
            for (int j = 0; j < length; j++){
                if (rotation==0){
                    // System.out.println("x: "+(x+j)+" y: "+y);
                    board[y][x+j] = i+1+"0";
                } else          {
                    // System.out.println("x: "+x+" y: "+(y+j));
                    board[y+j][x] = i+1+"0";
                }
                
            }

            // record ship placement
            // System.out.println(x + y*10);
            // System.out.println(rotation);
            // System.out.println(x + y*10 + rotation*-128);
            this.locations[i] = (byte)(x + y*10 + rotation*-128);
        }

        // try{
        //     this.save.write(locations);
        // } catch (IOException e) {
        //     e.printStackTrace();
        // }
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
                    // output[i+1][j] = "\033[5m🎯\033[25m"; // blink escape code doesn't work in vscode

                    // System.out.print("🎯 ");
                } else if (square.substring(1).equals("0"))   { // not hit
                    output[i][j] = "  ";
                    // System.out.print("☁️ ");
                    // System.out.print("  ");
                } else                                        { //hit
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

    public String[][] printBoardName(boolean blink){
        String[][] output= new String[12][11];

        if (name.length()%2==1){
            name+=" ";
        }
        if (name.length()>22){
            name = name.substring(0,22);
        }
        for (int i = 0; i < name.length(); i+=2){
            output[0][i/2] = "\033[38;2;255;215;0m" + name.substring(i,i+2) + "\033[0m";
        }

        for (int i = 1; i <= 10; i++){
            // output[0][i] = "\033[38;2;255;215;0m" + ((char) (0x24b0 + i+5))+" \033[0m"; //hollow arial
            output[i+1][0] = "\033[38;2;255;215;0m" + ((char) (0xff20 + i))+"\033[0m"; //double width
        }

        for (int i = 1; i <= 10; i++){
            // output[i][0] = "\033[38;2;255;215;0m" + ((char) (0x2770 + i+5))+" \033[0m"; //negatives
            // output[0][i] = ((char) (0x2780 + i-1))+" "; //hollow sans-serif
            output[1][i] = "\033[38;2;255;215;0m" + ((char) (0xff10 + i-1))+"\033[0m"; //double width
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
                    output[i+1][j] = "🎯";
                    // output[i+1][j] = "\033[5m🎯\033[25m"; // blink escape code doesn't work in vscode
                    // System.out.print("🎯 ");
                } else if (square.substring(1).equals("0"))   { // not hit
                    output[i+1][j] = "  ";
                    // System.out.print("☁️ ");
                    // System.out.print("  ");
                } else                                        { //hit
                    // output[i][j] = "B";
                    if (square.substring(0,1).equals("0")){ // splash
                        output[i+1][j] = "💦";
                        // System.out.print("💦 ");
                    } else {
                        output[i+1][j] = "💥";
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
        // return printBoard(false);
        return printBoardName(false);
    }
    
    public String hit(){
        return hit(this.target[1],this.target[0]);
    }

    public String hit(int x, int y){
        this.target[0]=y;this.target[1]=x;
        String prefix = "";

        // if (this.board[this.target[0]][this.target[1]].substring(1).equals("0")){ // not hit
        if (this.board[this.target[0]][this.target[1]].charAt(1) =='0'){ // not hit
            this.board[this.target[0]][this.target[1]] = this.board[this.target[0]][this.target[1]].substring(0,1)+"1";
        } else{
            //pick random spot
            x = (int) (Math.random() * 10);
            y = (int) (Math.random() * 10); // can hit already hit square and breaks
            while (this.board[y][x].charAt(1) =='1'){ // already hit
                x = (int) (Math.random() * 10);
                y = (int) (Math.random() * 10);
            }
            // prefix = "already hit; firing at "+ (this.target[1]+1) + ","   + (this.target[0]+1)+" -";
            prefix = "already hit "+ (this.target[1]) + "," + (this.target[0]) + " -";
            // System.out.println("Random hit: "+x+" "+y);
            this.target[0]=y;this.target[1]=x;
            this.board[y][x] =this.board[y][x].substring(0,1)+"1";
            
        }

        // this.history.add(this.target[0]*10+this.target[1]); // not needed?
        if (save!=null)
            try{
                this.save.write(this.target[0]*10+this.target[1]); // save hit to file
                this.save.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }

        if (this.board[this.target[0]][this.target[1]].charAt(0) !='0'){ // check hit or miss
            // hits--;
            hits[this.board[this.target[0]][this.target[1]].charAt(0)-'1']--; // get ship id and decrement hits
            prefix += "hit :) ";
            if (hits[this.board[this.target[0]][this.target[1]].charAt(0)-'1']==0){
                prefix += "& sunk the " + ships[this.board[this.target[0]][this.target[1]].charAt(0)-'1'] + "! ";
            }

        }
        else{
            prefix += "miss :( ";
        }

        for(int hit:hits){ //check if all ships are sunk
            if (hit!=0){ // game not over
                // return prefix + ( this.board[this.target[0]][this.target[1]].charAt(0) =='0' ? "miss :( " :  "hit :) ") // calculate hit or miss
                return "0"+ prefix // message to player/s
                + "at " + (this.target[1]) + ","   + (this.target[0]) +" ";// report x&y position
            }
        }
        // return null; // game over

        return "1"+ prefix // message to player/s
        + "at " + (this.target[1]) + ","   + (this.target[0]) +" ";// report x&y position

        // if (hits==0){ // game over
        // // if (hits==5+4+3+3+1){ // short cut
        //     return null;
        // }
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

        // Board b = new Board("Bob","1780 2230 3560 4490 5440");
        // Board b = new Board("Bob","780230560490440");
        // Board b = new Board("Bob","110");
        // Board a = new Board("Alice");

        if (sizeY <= 10){
            System.out.println("Terminal too small "+sizeX+":"+sizeY);
            return;
        }


        // Perlin p = new Perlin();
        // Noise p = new Noise();
        

        // while (true) {
        //     String[][] output = b.printBoard();
        //     String[][] canvas = overlayBoard(sizeX/4-5, sizeY/2-5, output);

        //     output = a.printBoard();
        //     canvas = overlayBoard(3 * sizeX / 4 - 5, sizeY/2-5, canvas, output);

        //     System.out.print(p.nextFrame(canvas));

        //     try                              {
        //         Thread.sleep(1000); // wait for 1 second
        //     } catch (InterruptedException e) {
        //         e.printStackTrace();
        //     }
        // }
        // p.loop();

        // System.out.println(b.board[0][0]); // should fail because board is private
    }
}
