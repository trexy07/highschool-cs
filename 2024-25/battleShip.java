import java.io.IOException;
import java.util.Scanner;
import input.RawConsoleInput;
// import /.board;

public class battleShip{

    private static board p1;
    private static board p2;
    private static int sizeX=0;
    private static int sizeY=0;
    private static board currentPlayer;

    private static boolean moved=false;

    public static int CYCLE_DELAY=50;
    public static int BLINK_RATE=350;
    public static int RENDER_RATE=1000;

    public static void main(String[] args){

        System.out.print("\033[H\033[2J");
        System.out.flush();

        try {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
            // System.out.println("Terminal size: " + sizeX*2 + "x" + sizeY);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        
        if (sizeY <= 10){
            System.out.println("Terminal too small "+sizeX+":"+sizeY);
            return;
        }

        if ("debug"=="debug"){
            p1 = new board(1, "player1");
            p2 = new board(2, "player2");
            currentPlayer = p1;
        }else{// player names
            Scanner scan = new Scanner(System.in);  // Create a Scanner obj
            System.out.print("\033[32m");
            rollingPrint("Japan’s navy under control of General... ");
            System.out.println("(input player 1 name)");

            String name1 = scan.nextLine();  // Read user input
            p1 = new board(1, name1);
            currentPlayer = p1;

            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("\033[32mJapan’s navy under control of General " + name1 +".");
            rollingPrint("The battle ships anchor off the coast of Pearl Harbor, Hawaii.\nGeneral... ");
            System.out.println("(input player 2 name)");

            String name2 = scan.nextLine();  // Read user input
            p2 = new board(2, name2);


            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Japan’s navy under control of General " + name1 +".");
            System.out.print("The battle ships anchor off the coast of Pearl Harbor, Hawaii.\nGeneral " + name2);

            rollingPrint(" sits unassuming of the looming attack on his ships.\nGeneral "
            + name1 + " has the advantage to attack first.\nThe harbor is fogged over, General "
            + name1 + " is tasked with picking targets.\n\n-General "
            + name1 + "! Input wasd to select target, then hit enter.");
        }

        perlin p = new perlin();
        

        Thread backgroundThread = new Thread(() -> {
            int cycleTime=0;
            boolean turn = true;
            
            String[][] output = p1.printBoard(true);
            String[][]canvas = board.overlayBoard(sizeX/4-5, sizeY/2-5, output);

            output = p2.printBoard(false);
            canvas = board.overlayBoard(3 * sizeX / 4 - 5, sizeY/2-5, canvas, output);


            // String[][] canvas= new String[sizeY][sizeX]; // x and y 
            while (true) {
                try {
                    // if (cycleTime<=0 || moved){
                        // System.out.print();
                        if (cycleTime %  BLINK_RATE == 0){
                            turn=!turn;
                        }
                    
                        output = p1.printBoard(turn);
                        canvas = board.overlayBoard(sizeX/4-5, sizeY/2-5, output);

                        // blink=!blink;

                        output = p2.printBoard(turn);
                        canvas = board.overlayBoard(3 * sizeX / 4 - 5, sizeY/2-5, canvas, output);
                        

                        

                        if (cycleTime % RENDER_RATE == 0){
                            // rendered=p.nextFrame(canvas);
                            System.out.print("\033[H\033[2J" + p.nextFrame(canvas));
                            System.out.flush();

                            // System.out.print(p.nextFrame(canvas));
                            // System.out.print("next frame"+", "+cycleTime);
                            // if (cycleTime%350==0){
                            // System.out.print("switched to: "+turn+", "+cycleTime);
                            
                            // }
                            // cycleTime=1000;
                        } else if (moved){
                            // rendered=
                            System.out.print("\033[H\033[2J" + p.render(canvas));
                            System.out.flush();

                            // System.out.print(p.render(canvas));
                            // System.out.print("moved"+", "+cycleTime);
                            moved=false;
                        } else if (cycleTime % BLINK_RATE == 0){
                            System.out.print("\033[H\033[2J" + p.render(canvas));
                            System.out.flush();

                            // System.out.print(p.render(canvas));
                            // System.out.print("switched to: "+turn+", "+cycleTime);
                            // turn=!turn;
                        }
                    // } 


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
            int key =0 ;
            try {
                key = RawConsoleInput.read(true); // wait or don't wait
            } catch (IOException e) {
                    e.printStackTrace();
            }
            // System.out.println("You pressed: " + key);
            if ( key == 3) {
                break;
            }
            // System.out.println("You pressed: " + (char) key);
            // boolean moved=false;
            if (key=='w'){
                currentPlayer.target[0] = Math.max(0, currentPlayer.target[0]-1);
                moved=true;
            } else if (key=='s'){
                currentPlayer.target[0] = Math.min(9, currentPlayer.target[0]+1);
                moved=true;
            } else if (key=='a'){
                currentPlayer.target[1] = Math.max(0, currentPlayer.target[1]-1);
                moved=true;
            } else if (key=='d'){
                currentPlayer.target[1] = Math.min(9, currentPlayer.target[1]+1);
                moved=true;
            } else if (key=='\n'){
                currentPlayer.hit();
            }




        }
    }

    public static void rollingPrint(String output, int delay){
        for (int i = 0; i < output.length(); i++){
            char out = output.charAt(i);
            System.out.print(out);

            int time=delay;

            // if (out ==' ') time+=100;
            if (out ==',') time+=100;
            if (out =='.' || out == '!' || out == '?') time+=400;
            try {
                Thread.sleep(time);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void rollingPrint(String output){
        rollingPrint(output, 50);
    }
}