package drawing;
// import drawing.Perlin;

import java.util.Random;
import java.io.IOException;
//// fix statics, they are properties of the whole class not just one instance
public class Perlinv2 {

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
    // private              double[][] mainGrid; // the grid of floats

    // private              double[][] wetNoise; // water noise generated from the grid
    // private              double[][] windNoise; // wind noise generated from the grid

    private              String[][] newWet;
    private              String[][] newWind;

    private              double[][]    horizontal;
    private              double[][]    vertical;

    public Perlinv2(int newX,int newY) { //constructor or __init__ in python
        // constructor receiving size
        this.sizeX = newX;
        this.sizeY = newY;

        construct();
    }

    public Perlinv2() { 
        // constructor getting size
        try {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        this.sizeX = sizeX;
        this.sizeY = sizeY;

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

        double[][] gridWet = new double[sizeY][sizeX];
        double[][] gridWind = new double[sizeY][sizeX];
        for (int x = 0; x < sizeX-1 ; x++) {
            for (int y = 0; y < sizeY-1; y++) {
                double val = grid[y][x];
                for (int[] row : PATTERNS[6]) { //5x5
                    int nx = x + row[0];
                    int ny = y + row[1];
                    if (nx >= 0 && nx < sizeX && ny >= 0 && ny < sizeY) {
                        gridWet[ny][nx] += val;
                    }
                }
                for (int[] row : PATTERNS[0]) { //3x3
                    int nx = x + row[0];
                    int ny = y + row[1];
                    if (nx >= 0 && nx < sizeX && ny >= 0 && ny < sizeY) {
                        gridWind[ny][nx] += val;
                    }
                }
            }
        }


        
        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                gridWet[y][x] /= 36;
                gridWind[y][x] /= 9;
            }
        }


        newWet = new String[sizeY][sizeX];
        newWind = new String[sizeY][sizeX];
        for (int y = 0; y < sizeY; y++) {
            for (int x = 0; x < sizeX; x++) {

                if (gridWind[y][x] > MINIMUM_WIND) {
                    newWind[y][x]= "\033[48;2;" + (int) ((gridWind[y][x] + 1) * 127.5) + ";" + (int) ((gridWind[y][x] + 1) * 127.5) + ";" + (int) ((gridWind[y][x] + 1) * 127.5) + "m  ";
                    // newWind[y][x]= "\033[48;2;" + (int) ((gridWind[y][x] + 1) * 127.5) + ";" + (int) ((gridWind[y][x] + 1) * 127.5) + ";" + (int) ((gridWind[y][x] + 1) * 127.5) + "m"+x+""+y;
                } 
                newWet[y][x] = "\033[48;2;0;0;" + (int) ((gridWet[y][x] + 1) * 127.5) + "m  ";
                // newWet[y][x] = "\033[48;2;0;0;" + (int) ((gridWet[y][x] + 1) * 127.5) + "m"+x+""+y;
                
            }
            // System.out.println();
        }
        

        // //create random wind
        this.mainWind = new int[2];
        Random rand = new Random();
        do {
            this.mainWind[0] = rand.nextInt(3) - 1;
            this.mainWind[1] = rand.nextInt(3) - 1;
        } while (this.mainWind[0] == 0 && this.mainWind[1] == 0);

        // mainWind[0] = -1;
        // mainWind[1] = -1;

        

        // store data for edge generation
        horizontal = new double[sizeY+4][5];
        vertical = new double[5][sizeX+4];

        if (mainWind[0] == -1) {
            for (int y =0; y<sizeY; y++){
                for (int x =0;x<2;x++){
                    horizontal[y+2][3+x] = grid[y][x];
                }
                for (int x =0;x<3;x++){
                    horizontal[y+2][x] = random.nextDouble() * 2 - 1;
                }
            }
        } else if (mainWind[0] == 1) {
            for (int y =0; y<sizeY; y++){
                for (int x =0;x<2;x++){
                    horizontal[y+2][x] = grid[y][sizeX-x];
                }
                for (int x =2;x<5;x++){
                    horizontal[y+2][x] = random.nextDouble() * 2 - 1;
                }
            }
        }
        for (int x= 0;x<5;x++){
            for (int y=0; y<2;y++){
                horizontal[y][x] = random.nextDouble() * 2 - 1;
            }
            for (int y=sizeY-2; y<sizeY;y++){
                horizontal[y][x] = random.nextDouble() * 2 - 1;
            }
        }


        if (mainWind[1] == -1) {
            for (int x =0; x<sizeX; x++){
                for (int y =0;y<2;y++){
                    vertical[3+y][x+2] = grid[y][x];
                }
                for (int y =0;y<3;y++){
                    vertical[y+2][x] = random.nextDouble() * 2 - 1;
                }
            }
        } else if (mainWind[1] == 1) {
            for (int x =0; x<sizeX; x++){
                for (int y =0;y<2;y++){
                    vertical[y][x+2] = grid[sizeY-y][x];
                }
                for (int y =2;y<5;y++){
                    vertical[y][x+2] = random.nextDouble() * 2 - 1;
                }
            }
        }
        for (int y= 0;y<5;y++){
            for (int x=0; x<2;x++){
                vertical[y][x] = random.nextDouble() * 2 - 1;
            }
            for (int x=sizeX-2; x<sizeX;x++){
                vertical[y][x] = random.nextDouble() * 2 - 1;
            }
        }




        // this.wetNoise = generateNoise(this.mainGrid, PATTERNS[6], 36); // water noise
        // this.windNoise = generateNoise(this.mainGrid, PATTERNS[0], 9); // wind noise
    }

    public static void main(String[] args) { // if __name__ == "__main__" but in java

        // Perlinv2 p = new Perlinv2();
        Perlinv2 p = new Perlinv2(8, 8);

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
        // Perlinv2 p2 = new Perlinv2();
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
        // System.out.println("Perlin: " + duration1 + " Perlinv2: " + duration2);
        // System.out.println("diff: " + (duration1 - duration2));
        // System.out.println("percent:" + ((double) duration2 / duration1));

        // p.loop();

        // test to see if overlay works
        /*
        String[][] overlay = new String[sizeY][sizeX];
        overlay[5][5] = "💥";
        overlay[5][6] = "💦";

        String introString = "Welcome to battleship";
        if (introString.length() % 2 != 0){
            introString += " ";
        }
        for (int i=0; i<introString.length()-1; i+=2){
            overlay[0][i/2] = introString.substring(i, i+2);
        }

        System.out.println(p.render(overlay));
        */

    }

   

    public String nextFrame() { // moves the animation, and returns the render 

        // translate(this.mainGrid, this.mainWind); // move the floats around the grid
        translate(); // move the floats around the grid

        // this.wetNoise = generateNoise(this.mainGrid, PATTERNS[6], 36); // water noise
        // this.windNoise = generateNoise(this.mainGrid, PATTERNS[0], 9); // wind noise

        //outputs the rendered frame
        // return render(this.wetNoise, this.windNoise);
        return render();

    }

    public String nextFrame(String[][] overlay) { // moves the animation, and returns the render with an overlay 

        translate(); // move the floats around the grid

        // this.wetNoise = generateNoise(this.mainGrid, PATTERNS[6], 36); // water noise
        // this.windNoise = generateNoise(this.mainGrid, PATTERNS[0], 9); // wind noise

        //outputs the rendered frame
        // return render(this.wetNoise, this.windNoise, overlay);
        return render(overlay);

    }


    public String render() { //default args for outside rendering 
        StringBuilder output = new StringBuilder();
        // for (    int y = windowY; y != windowY-1; y=(y+1)%(sizeY-1)) {
        for (    int y = windowY; y < sizeY; y++) {
            for (int x = windowX; x < sizeX; x++) {
                if (newWind[y][x] != null){
                    // output += windNoise[y][x];
                    output.append(newWind[y][x]);
                } else {
                    output.append(newWet[y][x]);
                    // output += wetNoise[y][x];

                }
            }
            for (int x = 0; x < windowX; x++) {
                if (newWind[y][x] != null){
                    // output += windNoise[y][x];
                    output.append(newWind[y][x]);
                } else {
                    output.append(newWet[y][x]);
                    // output += wetNoise[y][x];

                }
            }
            output.append("\033[0m\n");
        }
        for (    int y = 0; y < windowY; y++) {
            for (int x = windowX; x < sizeX; x++) {
                if (newWind[y][x] != null){
                    // output += windNoise[y][x];
                    output.append(newWind[y][x]);
                } else {
                    output.append(newWet[y][x]);
                    // output += wetNoise[y][x];

                }
            }
            for (int x = 0; x < windowX; x++) {
                if (newWind[y][x] != null){
                    // output += windNoise[y][x];
                    output.append(newWind[y][x]);
                } else {
                    output.append(newWet[y][x]);
                    // output += wetNoise[y][x];

                }
            }
            output.append("\033[0m\n");
        }
        output.deleteCharAt(output.length()-1);
        output.append("\033[0m");
        return output.toString();
    }

    public String render(String[][] overlay) { //render with text that replaces the wind
        StringBuilder output = new StringBuilder();
        for (int y = windowY; y != windowY; y=(y+1)%sizeY) {
            for (int x = windowX; x != windowX; x=(x+1)%sizeX) {
                String square = overlay[y][x];
                if (square == null) {
                    if (newWind[y][x] != null){
                        // output += windNoise[y][x];
                        output.append(newWind[y][x]);
                    } else {
                        output.append(newWet[y][x]);
                        // output += wetNoise[y][x];
                    }
                } else {
                    output.append(square);
                }

            }
            output.append("\033[0m\n");
        }
        output.deleteCharAt(output.length()-1);
        output.append("\033[0m");
        return output.toString();
    }


    

    private void translate() { // moves a grid of floats in a direction, and adds new floats to the edge
        System.out.println(windowX);
        System.out.println(windowY);
        // -1 -> -1
        // 1 -> 0
        // (+1)/2
        Random random = new Random();


        if (mainWind[0]!=0){
            for (int i = 0; i<sizeY; i++){
                // newWet [i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] = "\033[41m  ";
                // newWind[i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] = "\033[41m  ";

                // average the water noise
                double total=0;
                for (int iMod = -2; iMod<3; iMod++){
                    for (int j = 0; j<5; j++){
                        total += horizontal[i+iMod+2][j];
                    }
                }
                
                total/=36;
                // output += "\033[48;2;0;0;" + (int) ((grid1[y][x] + 1) * 127.5) + "m  ";
                // output += "\033[48;2;0;0;" + (int) (total + 1) * 127.5) + "m  ";
                // output += "\033[48;2;" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + "m  ";

                // set the water noise
                newWet [i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] =  "\033[48;2;0;0;" + (int) ((total + 1) * 127.5) + "m  ";

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
                // System.out.println(value);
                if (total > MINIMUM_WIND){
                    newWind[i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] = "\033[48;2;" + value + ";" +value + ";" +value + "m  ";
                } else {
                    newWind[i][(windowX + sizeX + (mainWind[0]+1)/2-1) % sizeX] = null;
                }

                // move the edge noises horizontally 
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
        }
        if (mainWind[1]!=0){
            for (int i = 0; i<sizeX; i++){
                // newWind[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = "\033[42m  ";
                // newWind[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = "\033[42m  ";

                // average the water noise
                double total=0;
                for (int iMod = -2; iMod<3; iMod++){
                    for (int j = 0; j<5; j++){
                        total += vertical[j][i+iMod+2];
                    }
                }
                
                total/=36;

                // set the water noise
                newWind[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = "\033[48;2;0;0;" + (int) ((total + 1) * 127.5) + "m  ";

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
                // System.out.println(value);
                if (total > MINIMUM_WIND){
                    newWind[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = "\033[48;2;" + value + ";" +value + ";" +value + "m  ";
                } else {
                    newWind[(windowY + sizeY + (mainWind[1]+1)/2-1) % sizeY][i] = null;
                }

                // move the edge noises vertically 
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
        }

        windowX = (windowX + sizeX + mainWind[0]) % sizeX;
        windowY = (windowY + sizeY + mainWind[1]) % sizeY;

        // System.out.println(windowX);
        // System.out.println(windowY);
    }
}
