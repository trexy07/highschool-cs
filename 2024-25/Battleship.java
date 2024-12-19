import java.io.IOException;
import java.util.Scanner;
import input.RawConsoleInput;
import perlin.*;

public class Battleship {

    private static       Board    p1;
    private static       Board    p2;
    private static       Board    currentPlayer;
    private static       Board    otherPlayer;

    private static       int      sizeX       = 0;
    private static       int      sizeY       = 0;
    private static       int      lineCount   = 0;
    private static       String   hit_miss    = "";
    
    private static       boolean  moved       = false;
    private static       boolean  mouse       = false;

    public  static final int      CYCLE_DELAY = 100; // responsiveness
    public  static final int      BLINK_RATE  = 300; // icon blink rate
    public  static final int      RENDER_RATE = 1000;// background move rate

    private static       String   hitChars    = "";

    public static void main(String[] args) {
        // escape codes
        // ?1000h mouse reporting
        // ?1006h mouse format
        // 2j clear screen
        // 32m green text
        System.out.print("\033[?1000h\033[?1006h\033[H\033[2J");
        System.out.flush();
        
        

        try                                            {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
            // System.out.println("Terminal size: " + sizeX*2 + "x" + sizeY);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        for (String arg : args) {
            if (arg.equals("mouse")){
                System.out.println("Mouse input flag");
                if (sizeY <= 23){
                    System.out.println("Terminal too small, currently " + sizeX + ":" + sizeY+ "required ?:24");
                    return;
                }
                mouse = true;
            }
        }

        if (sizeY <= 11) {
            System.out.println("Terminal too small, currently " + sizeX + ":" + sizeY+ "required 44:12");
            return;
        }

        if ("debug" == "debug") {
            p1 = new Board("player1");
            p2 = new Board("player2");
            currentPlayer = p1;
            otherPlayer = p2;

        } else               { // player names
            Scanner scan = new Scanner(System.in); // Create a Scanner obj
            System.out.print("\033[32m");
            rollingPrint("Japan’s navy under control of General... ");
            System.out.println("(input player 1 name)");

            String name1 = scan.nextLine(); // Read user input
            p1 = new Board(name1);
            currentPlayer = p1;

            System.out.print("\033[H\033[2J");
            System.out.flush();            
            System.out.println("\033[32mJapan’s navy under control of General " + name1 + ".");
            
            lineCount=0;
            rollingPrint("The battle ships anchor off the coast of Pearl Harbor, Hawaii.\nGeneral... ");
            System.out.println("(input player 2 name)");

            String name2 = scan.nextLine(); // Read user input
            p2 = new Board(name2);
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

        Perlin p = new Perlin(sizeX, sizeY-1);


        Thread backgroundThread     = new Thread(() -> {
            int         cycleTime   = 0;
            boolean     turn        = true;
            
            String[][]  output      = p1.printBoard(true);
            // String[][] canvas = Board.overlayBoard(       sizeX / 4 - 5, sizeY / 2 - 5, output);
            String[][]  canvas      = Board.overlayBoard(sizeX,sizeY-1,  sizeX / 4 - 5, (sizeY-1) / 2 - 5, output);

            output = p2.printBoard(false);
            canvas = Board.overlayBoard(3 * sizeX / 4 - 5, (sizeY-1) / 2 - 5, canvas, output);


            // String[][] canvas= new String[sizeY][sizeX]; // x and y 
            while (true) {
                try   {
                    String prefix;
                    String render;
                    if (mouse || sizeY>sizeX/2){
                        // H move cursor to top left
                        // 2j clear screen
                        // 32m green text
                        prefix = "\033[H\033[2J";
                        if (mouse){
                            String[][] greyCanvas = new String[sizeY ][sizeX ];
                            for (int i = 0; i < sizeY / 2; i++) {
                                for (int j = 0; j < sizeX; j++) {
                                    if (i==sizeY/4-5 && j==sizeX/2-5){
                                        greyCanvas[i][j] = "  "; // light grey escape code followed by 2 spaces
                                    } else {
                                        greyCanvas[i][j] = "\033[48;5;236m  "; // light grey escape code followed by 2 spaces
                                    }
                                }
                            }
                            // System.out.println("grey");
                            // System.out.println(greyCanvas[1][1]);
                            canvas = Board.overlayBoard(sizeX, sizeY-1, 0,(sizeY-1)/2, greyCanvas);

                        } else{
                            canvas = Board.overlayBoard(sizeX, sizeY-1, 0,0, new String[0][0]);

                        }

                        output = otherPlayer.printBoard(turn);
                        canvas = Board.overlayBoard(sizeX / 2 - 5, (sizeY-1) / 4 - 5, canvas,output);

                        output = currentPlayer.printBoard(false);
                        canvas = Board.overlayBoard(sizeX / 2 - 5, 3 * (sizeY-1) / 4  - 5, canvas, output);
                        
                    } else {
                        // H move cursor to top left
                        // 2j clear screen
                        // 32m green text
                        prefix = "\033[H\033[2J\033[32m-" + hit_miss + "General " + currentPlayer.name + "! Input wasd to select target, then hit enter.";
                        
                        output = p1.printBoard((p1==currentPlayer) ? turn:false);
                        canvas = Board.overlayBoard(sizeX,sizeY-1,sizeX / 4 - 5, (sizeY-1) / 2 - 5, output);

                        output = p2.printBoard((p2==currentPlayer) ? turn:false);
                        canvas = Board.overlayBoard(3 * sizeX / 4 - 5, (sizeY-1) / 2 - 5, canvas, output);

                        

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
                    e.printStackTrace();
                }
            }
        });

        backgroundThread.setDaemon(true);
        backgroundThread.start();

        System.out.println("----starting----");

        while (true) {
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
                System.out.println("\033[?1000l\033[?1006l\033[0m]");
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
                        // System.out.println(data[0] + " " + data[1] + " " + data[2] + " " + data[3]);
                        if (data[3] == 1) {
                            continue;
                        }
                        
                        // System.out.println((data[1]+1)/2 - sizeX/3 + 9);
                        int x = (data[1]+1)/2 - sizeX * (p1 == currentPlayer?1:3)/4 + 3;
                        int y = data[2] - sizeY/2 + 3;
                        System.out.println(" "+x+", "+y);

                        if (0 <= x && x <= 9 && 0 <= y && y <= 9){
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

                // switch players
                Board temp = currentPlayer;
                currentPlayer = otherPlayer;
                otherPlayer = temp;

            }
            hitChars += (char) key;
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