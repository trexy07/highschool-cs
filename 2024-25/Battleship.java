import java.io.IOException;
import java.util.Scanner;
import input.RawConsoleInput;

import java.io.DataOutputStream;
import java.io.FileOutputStream;
// import java.io.FileNotFoundException;
import java.io.File;

// import perlin.*;
import drawing.*;

public class Battleship {

    private static       Board    p1;
    private static       Board    p2;
    private static       Board    currentPlayer;
    private static       Board    otherPlayer;
    private static       DataOutputStream save;

    private static       int      sizeX       = 0;
    private static       int      sizeY       = 0;
    private static       int      lineCount   = 0;
    private static       String   hit_miss    = "";
    
    private static       boolean  moved       = false;
    private static       boolean  clear       = false;

    public  static final int      CYCLE_DELAY = 100; // responsiveness
    public  static final int      BLINK_RATE  = 300; // icon blink rate
    public  static final int      RENDER_RATE = 1000;// background move rate

    public static void main(String[] args) {
        
        // find terminal size
        try                                            {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
            // System.out.println("Terminal size: " + sizeX*2 + "x" + sizeY);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        // minimum terminal sizes: 44:13 or 11:25 
        if ((sizeX <44 || sizeY < 13 ) && (sizeX < 22 || sizeY<25) ) {
            System.out.println("\033[32mThe Terminal is too small; current size is " + sizeX + ":" + sizeY+ "\nminimum size is 44:13 or 22:25\033[0m");
            return;
        }

        // escape codes before start
        // ?1000h mouse reporting
        // ?1006h mouse format
        // 2j clear screen
        System.out.print("\033[?1000h\033[?1006h\033[H\033[2J");
        System.out.flush();


        // get player names or skip to debug
        if ("debug" == "debug") {
            try{
                new File("save.bin").createNewFile();
                save = new DataOutputStream(new FileOutputStream("save.bin"));
            } catch (IOException e){
                System.out.println("File not found");
            }
            p1   = new Board("player1",save);
            p2   = new Board("player2",save);
            currentPlayer = p1;
            otherPlayer = p2;

        } else               { // player names
            Scanner scan = new Scanner(System.in); // Create a Scanner obj

            // ask to save
            System.out.print("\033[32mdo you want to save the game? (y/N)\033[0m");
            String saveGame = scan.nextLine(); // Read user input
            if (saveGame.equals("y") || saveGame.equals("Y")) {
                try {
                    
                    new File("save.bin").createNewFile();
                    save = new DataOutputStream(new FileOutputStream("save.bin"));
                    
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            System.out.print("\033[32m");
            rollingPrint("Japan’s navy under control of General... ");
            System.out.println("(input player 1 name)");

            String name1 = scan.nextLine(); // Read user input
            // p1 = new Board(name1);
            p1 = new Board(name1, save);
            currentPlayer = p1;

            System.out.print("\033[H\033[2J");
            System.out.flush();            
            System.out.println("\033[32mJapan’s navy under control of General " + name1 + ".");
            
            lineCount=0;
            rollingPrint("The battle ships anchor off the coast of Pearl Harbor, Hawaii.\nGeneral... ");
            System.out.println("(input player 2 name)");

            String name2 = scan.nextLine(); // Read user input
            // p2 = new Board(name2);
            p2 = new Board(name2, save);
            otherPlayer = p2;

            System.out.print("\033[H\033[2J");
            System.out.flush();

            System.out.println("Japan’s navy under control of General " + name1 + ".");
            System.out.print("The battle ships anchor off the coast of Pearl Harbor, Hawaii.\nGeneral " + name2);
            
            lineCount=8+name2.length();
            rollingPrint(" sits unassuming of the looming attack on his ships.\nGeneral " +
                name1 + " has the advantage to attack first.\nThe harbor is fogged over, General " +
                name1 + " is tasked with picking targets.\n\n-General " +
                name1 + "! Input wasd to select target, then hit enter.");
        }



        Thread renderingThread     = new Thread(() -> { // render (background) thread
            Perlin      p           = new Perlin(sizeX, sizeY-1);

            int         cycleTime   = 0;
            boolean     turn        = true;
            
            String[][]  output      = p1.printBoard(true);
            String[][]  canvas      = Board.overlayBoard(sizeX,sizeY-1,  sizeX / 4 - 5, (sizeY-1) / 2 - 5, output);

            output = p2.printBoard(false);
            canvas = Board.overlayBoard(3 * sizeX / 4 - 5, (sizeY-1) / 2 - 5, canvas, output);


            while (true) {
                try   {
                    String prefix;
                    String render;
                    if (sizeY>sizeX/2){ // render vertically 
                        // H move cursor to top left
                        // 2j clear screen
                        // 32m green text
                        
                        prefix = "\033[H\033[2J\033[32m-" + hit_miss + " General " + currentPlayer.name + "! Input wasd to select target, then hit enter.";

                        output = p1.printBoardName((p1==currentPlayer) ? turn:false);
                        canvas = Board.overlayBoard(sizeX, sizeY-1, sizeX / 2 - 5, (sizeY-1) / 4 - 6,output);

                        output = p2.printBoardName((p2==currentPlayer) ? turn:false);
                        canvas = Board.overlayBoard(sizeX / 2 - 5, 3 * (sizeY-1) / 4  - 6, canvas, output);
                        
                    } else { // render horizontally
                        // H move cursor to top left
                        // 2j clear screen
                        // 32m green text
                        prefix = "\033[H\033[2J\033[32m-" + hit_miss + " General " + currentPlayer.name + "! Input wasd to select target, then hit enter.";
                        
                        output = p1.printBoardName((p1==currentPlayer) ? turn:false);
                        canvas = Board.overlayBoard(sizeX,sizeY-1,sizeX / 4 - 5, (sizeY-1) / 2 - 6, output);

                        output = p2.printBoardName((p2==currentPlayer) ? turn:false);
                        canvas = Board.overlayBoard(3 * sizeX / 4 - 5, (sizeY-1) / 2 - 6, canvas, output);

                        

                    }


                    if (cycleTime % RENDER_RATE == 0)       {
                        render = p.nextFrame(canvas);
                        System.out.print(prefix + render.substring(0, render.length()-5)+"\033[0m");
                        System.out.flush();

                    } else if (moved)                       {
                        render = p.render(canvas);
                        System.out.print(prefix + render.substring(0, render.length()-5)+"\033[0m");//"
                        System.out.flush();


                    } //else if (cycleTime % BLINK_RATE == 0) {
                    //     render = p.render(canvas);
                    //     System.out.print(prefix + render.substring(0, render.length()-5)+"\033[0m");
                    //     System.out.flush();

                    // }
                    moved = false;

                    cycleTime += CYCLE_DELAY;
                    Thread.sleep(CYCLE_DELAY);
                } catch (InterruptedException e) {
                    // render one last time

                    if (sizeY>sizeX/2){
                        output = p1.printBoardName(false);
                        canvas = Board.overlayBoard(sizeX, sizeY-1, sizeX / 2 - 5, (sizeY-1) / 4 - 6,output);

                        output = p2.printBoardName(false);
                        canvas = Board.overlayBoard(sizeX / 2 - 5, 3 * (sizeY-1) / 4 - 6, canvas, output);
                    } else {
                        output = p1.printBoardName(false);
                        canvas = Board.overlayBoard(sizeX,sizeY-1,sizeX / 4 - 5, (sizeY-1) / 2 - 6, output);

                        output = p2.printBoardName(false);
                        canvas = Board.overlayBoard(3 * sizeX / 4 - 5, (sizeY-1) / 2 - 6, canvas, output);
                    }

                    String render = p.nextFrame(canvas);

                    System.out.print(render.substring(0, render.length()-5)+"\033[0m");
                    System.out.flush();
                    clear=true; // make sure the drawing thread is complete
                    break;
                }
            }
        });

        renderingThread.setDaemon(true);
        renderingThread.start();

        System.out.println("----starting----");
        try{
            save.writeLong(System.currentTimeMillis()); // game start time
        } catch (IOException e){
            e.printStackTrace();
        }

        while (true) { // input (main) thread
            // System.out.println(hit_miss);
            if (hit_miss == null ){ // game over
                // System.out.println(clear);
                if (!clear){ // drawing thread not complete
                    continue;
                } else { // drawing thread complete; ending
                // System.out.println("breaking");
                    System.out.println("\n\033[32m-The "+ (currentPlayer != p1 ? "Japanese" : "American") +" navy was defeated by the general "+ currentPlayer.name +"!\033[0m");

                    System.out.flush();
                    break;
                    
                    // System.exit(0);
                }
            }
            // int key = 0;
            // try                     {
            //     key = RawConsoleInput.read(true); // wait or don't wait
            // } catch (IOException e) {
            //     e.printStackTrace();
            // }
            int key = RawConsoleInput.read(true);
            // System.out.println("You pressed: " + key);
            if (key == 3) {
                // System.out.print("\033[?1000l");
                // System.out.print("\033[?1006l");
                System.out.println("\033[?1000l\033[?1006l\033[0m");
                break;
            }
            // System.out.println("You pressed: " + (char) key);
            // boolean moved=false;
            if (key == 27) { // ESC
                key = RawConsoleInput.read(true);
                // System.out.println("escaped");
                if (key == '[') {
                    key = RawConsoleInput.read(true);
                    if (key == '<') { // Mouse SGR Mode
                        int[] data      = new int[4];
                        int   dataIndex = 0;

                        while ((key = RawConsoleInput.read(true)) != -1 ) {
                            if        (key == 'm' || key == 'M') {
                                data[3] = (key == 'm') ? 1 : 0;
                                break;
                            } else if (key == ';'              ) {
                                dataIndex++;
                            } else                               {
                                data[dataIndex] = data[dataIndex] * 10 + (key - '0');
                            }
                        }
                        // System.out.println("Mouse Event: " + event.toString());
                        if (data[3] == 1) {
                            continue;
                        }
                        int x;
                        int y;
                        // System.out.println("\n"+data[1] + " " + data[2]);

                        if (sizeY>sizeX/2){ // vertical clicking
                            // offset the points to click
                            x = (data[1]+1)/2 - sizeX/2+3;
                            y = data[2] - (p1 == currentPlayer ?1:2) * (sizeY-1) / 3  + 4;
                        } else{ // horizontal clicking
                            // offset the points to click
                            x = (data[1]+1)/2 - sizeX * (p1 == currentPlayer?1:3)/4 + 3;
                            y = data[2] - sizeY/2 + 2;
                        }

                        // System.out.println(0 <= x && x <= 9 && 0 <= y && y <= 9);
                        if (0 <= x && x <= 9 && 0 <= y && y <= 9){
                            System.out.println("counted");
                            currentPlayer.target[1] = x;
                            currentPlayer.target[0] = y;
                            moved = true;
                        }

                    }
                }
            } else if (key == 'w' ) {
                currentPlayer.target[0] = Math.max(0, currentPlayer.target[0] - 1);
                moved = true;
            } else if (key == 's' ) {
                currentPlayer.target[0] = Math.min(9, currentPlayer.target[0] + 1);
                moved = true;
            } else if (key == 'a' ) {
                currentPlayer.target[1] = Math.max(0, currentPlayer.target[1] - 1);
                moved = true;
            } else if (key == 'd' ) {
                currentPlayer.target[1] = Math.min(9, currentPlayer.target[1] + 1);
                moved = true;
            } else if (key == '\n') {
                hit_miss = currentPlayer.hit();

                if (hit_miss == null){ // current player loses
                    try {
                        save.writeByte(127);
                        save.writeLong(System.currentTimeMillis()); // game end time
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    System.out.print("\033[?1000l\033[?1006l\033[H\033[2J\033[32m");
                    // System.out.print("\033[?1000l\033[?1006l\033[32m");
                    
                    System.out.print("-The "+ (currentPlayer == p1 ? "Japanese" : "American") +" navy was defeated by the general "+ otherPlayer.name +"!");
                    // renderingThread.stop();
                    renderingThread.interrupt();
                    // System.out.println("\033[?1000l\033[?1006l\033[0m");
                    // System.exit(0);
                    // break;
                }

                // switch players
                Board temp = currentPlayer;
                currentPlayer = otherPlayer;
                otherPlayer = temp;

            }
        }
    }


    public static void rollingPrint(String output, int delay) {
        int outputLength = output.length();
        for (int i = 0; i < outputLength; i++) {
            lineCount++;
            // System.out.print("\n"+output.indexOf(" ")+','+lineCount);
            if (lineCount+output.indexOf(" ")>sizeX*2){
                System.out.println();
                lineCount=0;
                // System.out.print("hit");

            }
            char out = output.charAt(0);
            output = output.substring(1);
            System.out.print(out);

            int time = delay;

            // if (out ==' ') time+=100;
            if (out == ','                            ) time += 100;
            if (out == '.' || out == '!' || out == '?') time += 400;
            try                              {
                Thread.sleep(time);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void rollingPrint(String output) {
        rollingPrint(output, 50);
    }
}