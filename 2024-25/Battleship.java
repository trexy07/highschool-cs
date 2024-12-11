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

    public  static final int      CYCLE_DELAY = 50;
    public  static final int      BLINK_RATE  = 350;
    public  static final int      RENDER_RATE = 1000;

    public static void main(String[] args) {

        System.out.print("\033[H\033[2J");
        System.out.flush();

        try                                            {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
            // System.out.println("Terminal size: " + sizeX*2 + "x" + sizeY);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        if (sizeY <= 11) {
            System.out.println("Terminal too small, currently " + sizeX + ":" + sizeY+ "required 44:12");
            return;
        }

        if ("no" == "debug") {
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
            String[][]  canvas      = Board.overlayBoard( sizeX,sizeY-1,  sizeX / 4 - 5, (sizeY-1) / 2 - 5, output);

            output = p2.printBoard(false);
            canvas = Board.overlayBoard(3 * sizeX / 4 - 5, (sizeY-1) / 2 - 5, canvas, output);


            // String[][] canvas= new String[sizeY][sizeX]; // x and y 
            while (true) {
                try                              {
                    // if (cycleTime<=0 || moved){
                    // System.out.print();
                    if (cycleTime % BLINK_RATE == 0) {
                        turn = !turn;
                    }
                    String prefix = "\033[H\033[2J\033[32m-" + hit_miss + "General " + currentPlayer.name + "! Input wasd to select target, then hit enter.";
                    output = p1.printBoard((p1==currentPlayer) ? turn:false);
                    canvas = Board.overlayBoard( sizeX,sizeY-1,sizeX / 4 - 5, (sizeY-1) / 2 - 5, output);

                    output = p2.printBoard((p2==currentPlayer) ? turn:false);
                    canvas = Board.overlayBoard(3 * sizeX / 4 - 5, (sizeY-1) / 2 - 5, canvas, output);

                    if (cycleTime % RENDER_RATE == 0)       {

                        System.out.print(prefix + p.nextFrame(canvas));
                        System.out.flush();

                    } else if (moved)                       {
                        System.out.print(prefix + p.render(canvas));//"
                        System.out.flush();
                        moved = false;

                    } else if (cycleTime % BLINK_RATE == 0) {
                        System.out.print(prefix + p.render(canvas));
                        System.out.flush();

                    }

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
            int key = 0;
            try                     {
                key = RawConsoleInput.read(true); // wait or don't wait
            } catch (IOException e) {
                e.printStackTrace();
            }
            // System.out.println("You pressed: " + key);
            if (key == 3) {
                break;
            }
            // System.out.println("You pressed: " + (char) key);
            // boolean moved=false;
            if        (key == 'w' ) {
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