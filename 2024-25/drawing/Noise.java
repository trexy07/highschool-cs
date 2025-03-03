package drawing;
// import drawing.Perlin;

import java.util.Random;
import java.io.IOException;

public class Noise {

    private static final double     MINIMUM_WIND = 0.1; // -1 to 1, used to mask the wind

    // patterns for generating the noise
    private static final int[][][]  PATTERNS = {
        { // 3x3
            {-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {0, 0}, {1, 0}, {-1, 1}, {0, 1}, {1, 1}
        },
        { // hollow 3x3
            {-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {1, 0}, {-1, 1}, {0, 1}, {1, 1}
        },
        { // 3x3 plus
            {0, -1}, {-1, 0}, {0, 0}, {1, 0}, {0, 1}
        },
        { // 3x3 cross
            {-1, -1}, {1, -1}, {0, 0}, {-1, 1}, {1, 1}
        },
        { // up slash
            {-1, -1}, {0, 0}, {1, 1}
        },
        { // down slash
            {-1, 1}, {0, 0}, {1, -1}
        },
        { // 5x5
            {-2, -2}, {-1, -2}, {0, -2}, {1, -2}, {2, -2}, {-2, -1}, {-1, -1}, {0, -1}, {1, -1}, {2, -1},
            {-2, 0}, {-1, 0}, {0, 0}, {1, 0}, {2, 0}, {-2, 1}, {-1, 1}, {0, 1}, {1, 1}, {2, 1},
            {-2, 2}, {-1, 2}, {0, 2}, {1, 2}, {2, 2}
        },
        { // hollow 5x5 
            {-2, -2}, {-1, -2}, {0, -2}, {1, -2}, {2, -2}, {-2, -1}, {2, -1}, {-2, 0}, {2, 0},
            {-2, 1}, {2, 1}, {-2, 2}, {-1, 2}, {0, 2}, {1, 2}, {2, 2}
        },
        { // hollow circle 5x5
            {-1, -2}, {0, -2}, {1, -2}, {-2, -1}, {2, -1}, {-2, 0}, {2, 0}, {-2, 1}, {2, 1}, {-1, 2}, {0, 2}, {1, 2}
        },
        { // circle 5x5
            {-1, -2}, {0, -2}, {1, -2}, {-2, -1}, {-1, -1}, {0, -1}, {1, -1}, {2, -1},
            {-2, 0}, {-1, 0}, {0, 0}, {1, 0}, {2, 0}, {-2, 1}, {-1, 1}, {0, 1}, {1, 1}, {2, 1},
            {-1, 2}, {0, 2}, {1, 2}
        }
    };

    // size of the render, default is an ansi terminal
    private static       int        sizeX = 80 / 2;
    private static       int        sizeY = 24;

    private static       int        windowX = 0;
    private static       int        windowY = 0;

    private              int[]      mainWind; // how the grid moves

    private              String[][] newWater;
    private              String[][] newCloud;

    private              double[][] horizontal; // left or right edge
    private              double[][] vertical;   // top or bottom edge

    public Noise(int newX,int newY) { //constructor or __init__ in python
        // constructor receiving size
        sizeX = newX;
        sizeY = newY;

        construct();
    }

    public Noise() { 
        // constructor getting size
        try {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        construct();
    }

    private void construct(){
        //create grid of random floats
        double[][] grid = new double[sizeY + 4][sizeX + 4];
        Random random = new Random();
        for (int y = 0; y < sizeY + 4; y++) {
            for (int x = 0; x < sizeX + 4; x++) {
                grid[y][x] = random.nextDouble() * 2 - 1;
            }
        }

        // diffuse the random floats
        double[][] gridWet = new double[sizeY][sizeX];
        double[][] gridWind = new double[sizeY][sizeX];
        for (int x = 0; x < sizeX-1 ; x++) {
            for (int y = 0; y < sizeY-1; y++) {
                double val = grid[y][x];
                for (int[] row : PATTERNS[6]) { //5x5 for water
                    int nx = x + row[0];
                    int ny = y + row[1];
                    if (nx >= 0 && nx < sizeX && ny >= 0 && ny < sizeY) {
                        gridWet[ny][nx] += val;
                    }
                }
                for (int[] row : PATTERNS[0]) { //3x3 for clouds
                    int nx = x + row[0];
                    int ny = y + row[1];
                    if (nx >= 0 && nx < sizeX && ny >= 0 && ny < sizeY) {
                        gridWind[ny][nx] += val;
                    }
                }
            }
        }


        // average the random
        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                gridWet[y][x] /= 36;
                gridWind[y][x] /= 9;
            }
        }

        // generate the first frame based on random values - basically the render function
        newWater = new String[sizeY][sizeX];
        newCloud = new String[sizeY][sizeX];
        for (int y = 0; y < sizeY; y++) {
            for (int x = 0; x < sizeX; x++) {
                if (gridWind[y][x] > MINIMUM_WIND) {
                    newCloud[y][x]= "\033[48;2;" + (int) ((gridWind[y][x] + 1) * 127.5) + ";" + (int) ((gridWind[y][x] + 1) * 127.5) + ";" + (int) ((gridWind[y][x] + 1) * 127.5) + "m  ";
                } 
                newWater[y][x] = "\033[48;2;0;0;" + (int) ((gridWet[y][x] + 1) * 127.5) + "m  ";                
            }
        }
        

        // create random wind (movement)
        this.mainWind = new int[2];
        Random rand = new Random();
        do {
            this.mainWind[0] = rand.nextInt(3) - 1;
            this.mainWind[1] = rand.nextInt(3) - 1;
        } while (this.mainWind[0] == 0 && this.mainWind[1] == 0);


        // store data for edge generation
        horizontal = new double[sizeY+4][5];
        vertical = new double[5][sizeX+4];

        // get existing left or right edge
        if (mainWind[0] == -1) {//left
            for (int y =0; y<sizeY; y++){
                for (int x =0;x<2;x++){
                    horizontal[y+2][3+x] = grid[y][x];
                }
                for (int x =0;x<3;x++){
                    horizontal[y+2][x] = random.nextDouble() * 2 - 1;
                }
            }
        } else if (mainWind[0] == 1) { //right
            for (int y =0; y<sizeY; y++){
                for (int x =0;x<2;x++){
                    horizontal[y+2][x] = grid[y][sizeX-x];
                }
                for (int x =2;x<5;x++){
                    horizontal[y+2][x] = random.nextDouble() * 2 - 1;
                }
            }
        }
        // fill in buffer space with random noise
        for (int x= 0;x<5;x++){
            for (int y=0; y<2;y++){
                horizontal[y][x] = random.nextDouble() * 2 - 1;
            }
            for (int y=sizeY-2; y<sizeY;y++){
                horizontal[y][x] = random.nextDouble() * 2 - 1;
            }
        }

        // get existing top or bottom edge
        if (mainWind[1] == -1) {//top
            for (int x =0; x<sizeX; x++){
                for (int y =0;y<2;y++){
                    vertical[3+y][x+2] = grid[y][x];
                }
                for (int y =0;y<3;y++){
                    vertical[y+2][x] = random.nextDouble() * 2 - 1;
                }
            }
        } else if (mainWind[1] == 1) {//bottom
            for (int x =0; x<sizeX; x++){
                for (int y =0;y<2;y++){
                    vertical[y][x+2] = grid[sizeY-y][x];
                }
                for (int y =2;y<5;y++){
                    vertical[y][x+2] = random.nextDouble() * 2 - 1;
                }
            }
        }
        // fill in buffer space with random noise
        for (int y= 0;y<5;y++){
            for (int x=0; x<2;x++){
                vertical[y][x] = random.nextDouble() * 2 - 1;
            }
            for (int x=sizeX-2; x<sizeX;x++){
                vertical[y][x] = random.nextDouble() * 2 - 1;
            }
        }
    }

    public static void main(String[] args) { // if __name__ == "__main__" but in java

        // Noise p = new Noise();
        Noise p = new Noise(8, 8);

        // p.mainWind[0] = -1;
        // p.mainWind[1] = 0;

        System.out.println(p.render());
        System.out.println("----------------------------");
        System.out.println(p.nextFrame());

        // p.mainWind[0] = -1;
        System.out.println("----------------------------");
        System.out.println(p.nextFrame());
        System.out.println("----------------------------");
        System.out.println(p.nextFrame());
        
        // p.mainWind[1] = 0;

        // Perlin   p1 = new Perlin();
        // Noise p2 = new Noise();
        // int i =0;
        
        // long startTime = System.nanoTime();
        // for (i = 0; i < 1000; i++) {
        // }
        // long endTime = System.nanoTime();
        // long emptyDuration = (endTime - startTime);

        // long startTime2 = System.nanoTime();
        // for (i = 0; i < 1000; i++) {
        //     p2.nextFrame();
        // }
        // long endTime2 = System.nanoTime();
        // long duration2 = (endTime2 - startTime2)-emptyDuration;

        // long startTime1 = System.nanoTime();
        // for (i = 0; i < 1000; i++) {
        //     p1.nextFrame();
        // }
        // long endTime1 = System.nanoTime();
        // long duration1 = (endTime1 - startTime1)-emptyDuration;


        // System.out.println("empty: " + emptyDuration);  
        // System.out.println("Perlin: " + duration1 + " Noise: " + duration2);
        // System.out.println("diff: " + (duration1 - duration2));
        // System.out.println("percent:" + ((double) duration2 / duration1));
    }

    public String nextFrame() { // moves the animation, and returns the render 
        translate(); // move the window and generate new edges
        return render();
    }

    public String nextFrame(String[][] overlay) { // moves the animation, and returns the render with an overlay 
        translate(); // move the window and generate new edges
        return render(overlay);
    }

    private void gridCheck(int x, int y, StringBuilder output){
        if (newCloud[y][x] != null){ // a cloud of null means no clouds
            output.append(newCloud[y][x]);
        } else {
            output.append(newWater[y][x]);
        }
    }

    private void gridCheck(int x, int y, StringBuilder output, String[][] overlay){
        // get the overlay where it would be without the window
        String square = overlay[(y - windowY + sizeY)%sizeY][(x - windowX + sizeX)%sizeX]; 
        // if there is an overlay, use it, otherwise use the water or cloud normally
        if (square == null){
            if (newCloud[y][x] != null){ // a cloud of null means no clouds
                output.append(newCloud[y][x]);
            } else {
                output.append(newWater[y][x]);
            }
        } else{
            // put the water under the overlay
            String water=newWater[y][x];
            water = water.substring(0, water.length()-2);// remove the spaces
            output.append(water+square);
        }
    }

    public String render() { //default args for outside rendering 
        StringBuilder output = new StringBuilder();

        // get from the window to the end (vertical)
        for (    int y = windowY; y < sizeY; y++) {
            // horizontal window to end
            for (int x = windowX; x < sizeX; x++) {
                gridCheck(x, y, output);
            }
            // horizontal start to window
            for (int x = 0; x < windowX; x++) {
                gridCheck(x, y, output);
            }
            output.append("\033[0m\n");
        }
        // and get from the start to the window (vertical)
        for (    int y = 0; y < windowY; y++) {
            // horizontal window to end
            for (int x = windowX; x < sizeX; x++) { 
                gridCheck(x, y, output);
            }
            // horizontal start to window
            for (int x = 0; x < windowX; x++) { 
                gridCheck(x, y, output);
            }
            output.append("\033[0m\n");
        }
        output.deleteCharAt(output.length()-1);
        output.append("\033[0m");
        return output.toString();
    }

    public String render(String[][] overlay) { //render with text that replaces the wind
        StringBuilder output = new StringBuilder();

        // get from the window to the end (vertical)
        for (    int y = windowY; y < sizeY; y++) {
            // horizontal window to end
            for (int x = windowX; x < sizeX; x++) {
                // String square = overlay[y][x];
                // if (square == null) {
                //     if (newCloud[y][x] != null){ // a cloud of null means no clouds
                //         output.append(newCloud[y][x]);
                //     } else {
                //         output.append(newWater[y][x]);
                //     }
                // } else {
                //     output.append(square);
                // }
                gridCheck(x, y, output, overlay);
            }
            // horizontal start to window
            for (int x = 0; x < windowX; x++) {
                gridCheck(x, y, output, overlay);
            }
            output.append("\033[0m\n");
        }
        // and get from the start to the window (vertical)
        for (    int y = 0; y < windowY; y++) {
            // horizontal window to end
            for (int x = windowX; x < sizeX; x++) { 
                gridCheck(x, y, output, overlay);
            }
            // horizontal start to window
            for (int x = 0; x < windowX; x++) { 
                gridCheck(x, y, output, overlay);
            }
            output.append("\033[0m\n");
        }

        output.deleteCharAt(output.length()-1);
        output.append("\033[0m");
        return output.toString();
    }

    private void horizontalMove(){ // move the edge noises horizontally
        Random random = new Random();

        for (int y =0; y<sizeY+4;y++){
            if (mainWind[0]==-1){
                for (int x =4;x>=0;x--){
                    horizontal[y][x] = (x-1<=4 && x-1>=0) ?   horizontal[y][x-1]: random.nextDouble() * 2 - 1;
                }
            } else if (mainWind[0]==1){
                for (int x =0;x<5;x++){
                    horizontal[y][x] = (x+1<=4 && x+1>=0) ?   horizontal[y][x+1]: random.nextDouble() * 2 - 1;
                }
            }
        }
        for (int y=0;y<5;y++){
            if (mainWind[0]==-1){
                for (int x=sizeX+3;x>=0;x--){
                    vertical[y][x] = (x-1<sizeX+4 && x-1>=0) ?   vertical[y][x-1]: random.nextDouble() * 2 - 1;
                }
            } else if (mainWind[0]==1){
                for (int x=0;x<sizeX+4;x++){
                    vertical[y][x] = (x+1<sizeX+4 && x+1>=0) ?   vertical[y][x+1]: random.nextDouble() * 2 - 1;
                }
            }
        }
    }

    private void verticalMove(){// move the edge noises vertically
        Random random = new Random();

        for (int x =0; x<sizeX+4;x++){
            if (mainWind[1]==-1){
                for (int y =4;y>=0;y--){
                    vertical[y][x] = (y-1<=4 && y-1>=0) ?   vertical[y-1][x]: random.nextDouble() * 2 - 1;
                }
            } else if (mainWind[1]==1){
                for (int y =0;y<5;y++){
                    vertical[y][x] = (y+1<=4 && y+1>=0) ?   vertical[y+1][x]: random.nextDouble() * 2 - 1;
                }
            }
        }
        for (int x=0;x<5;x++){
            if (mainWind[1]==-1){
                for (int y=sizeY+3;y>=0;y--){
                    // System.out.println(y+","+x);
                    horizontal[y][x] = (y-1<sizeY+4 && y-1>=0) ?   horizontal[y-1][x]: random.nextDouble() * 2 - 1;
                }
            } else if (mainWind[1]==1){
                for (int y=0;y<sizeY+4;y++){
                    horizontal[y][x] = (y+1<sizeY+4 && y+1>=0) ?   horizontal[y+1][x]: random.nextDouble() * 2 - 1;
                }
            }
        }
    }

    private void translate() { // moves a grid of floats in a direction, and adds new floats to the edge
        if (mainWind[0]!=0){// if there is horizontal movement
            for (int i = 0; i<sizeY; i++){
                // average the water noise
                double total=0;
                for (int iMod = -2; iMod<3; iMod++){
                    for (int j = 0; j<5; j++){
                        total += horizontal[i+iMod+2][j];
                    }
                }
                total/=36;
                
                // set the water noise
                newWater [i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] =  "\033[48;2;0;0;" + (int) ((total + 1) * 127.5) + "m  ";


                //average the cloud noise
                total=0;
                for (int iMod = -1; iMod<2; iMod++){
                    for (int j = 1; j<4; j++){
                        total += horizontal[i+iMod+2][j];
                    }
                }
                total/=9;

                // set the cloud noise
                String value = ""+(int) ((total + 1) * 127.5);
                if (total > MINIMUM_WIND){
                    newCloud[i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] = "\033[48;2;" + value + ";" +value + ";" +value + "m  ";
                } else { // null if the cloud is too little
                    newCloud[i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] = null;
                }
            }
            // move the edge noises horizontally
            horizontalMove();
        }
        if (mainWind[1]!=0){
            for (int i = 0; i<sizeX; i++){
                // average the water noise
                double total=0;
                for (int iMod = -2; iMod<3; iMod++){
                    for (int j = 0; j<5; j++){
                        total += vertical[j][i+iMod+2];
                    }
                }
                total/=36;

                // set the water noise
                newCloud[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = "\033[48;2;0;0;" + (int) ((total + 1) * 127.5) + "m  ";


                //average the cloud noise
                total=0;
                for (int iMod = -1; iMod<2; iMod++){
                    for (int j = 1; j<4; j++){
                        total += vertical[j][i+iMod+2];
                    }
                }
                total/=9;

                // set the cloud noise
                String value = ""+(int) ((total + 1) * 127.5);
                if (total > MINIMUM_WIND){
                    newCloud[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = "\033[48;2;" + value + ";" +value + ";" +value + "m  ";
                } else { // null if the cloud is too little
                    newCloud[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = null;
                }   
            }
            // move the edge noises vertically 
            verticalMove();
        }

        windowX = (windowX + sizeX + mainWind[0]) % sizeX;
        windowY = (windowY + sizeY + mainWind[1]) % sizeY;
    }
}
