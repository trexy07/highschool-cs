import java.util.Random;
import java.io.IOException;


public class perlin {
    private static final double MINIMUM_WIND = 0.1; // -1 to 1, used to mask the wind
    
    // patterns for generating the noise
    private static final int[][][] PATTERNS = {
            {
                {-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {0, 0}, {1, 0}, {-1, 1}, {0, 1}, {1, 1}
            },
            {
                {-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {1, 0}, {-1, 1}, {0, 1}, {1, 1}
            },
            {
                {0, -1}, {-1, 0}, {0, 0}, {1, 0}, {0, 1}
            },
            {
                {-1, -1}, {1, -1}, {0, 0}, {-1, 1}, {1, 1}
            },
            {
                {-1, -1}, {0, 0}, {1, 1}
            },
            {
                {-1, 1}, {0, 0}, {1, -1}
            },
            {
                {-2, -2}, {-1, -2}, {0, -2}, {1, -2}, {2, -2}, {-2, -1}, {-1, -1}, {0, -1}, {1, -1}, {2, -1},
                {-2, 0}, {-1, 0}, {0, 0}, {1, 0}, {2, 0}, {-2, 1}, {-1, 1}, {0, 1}, {1, 1}, {2, 1},
                {-2, 2}, {-1, 2}, {0, 2}, {1, 2}, {2, 2}
            },
            {
                {-2, -2}, {-1, -2}, {0, -2}, {1, -2}, {2, -2}, {-2, -1}, {2, -1}, {-2, 0}, {2, 0},
                {-2, 1}, {2, 1}, {-2, 2}, {-1, 2}, {0, 2}, {1, 2}, {2, 2}
            },
            {
                {-1, -2}, {0, -2}, {1, -2}, {-2, -1}, {2, -1}, {-2, 0}, {2, 0}, {-1, 1}, {0, 1}, {1, 1}
            },
            {
                {-1, -2}, {0, -2}, {1, -2}, {-2, -1}, {-1, -1}, {0, -1}, {1, -1}, {2, -1},
                {-2, 0}, {-1, 0}, {0, 0}, {1, 0}, {2, 0}, {-2, 1}, {-1, 1}, {0, 1}, {1, 1}, {2, 1},
                {-1, 2}, {0, 2}, {1, 2}
            }
        };
    

    
    // size of the terminal
    private static int sizeX = 160/2;
    private static int sizeY = 16; 
    
    private static int[] mainWind; // how the grid moves
    private static double[][] mainGrid; // the grid of floats

    private static double[][] wetNoise; // water noise generated from the grid
    private static double[][] windNoise; // wind noise generated from the grid


    public perlin() { //constructor or __init__ in python
        // constructor

        // get terminal size
        try {
            int[] terminalSize = TerminalSize.getTerminalSize(); // import from other file
            sizeX = terminalSize[1] / 2;
            sizeY = terminalSize[0];
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        //create grid of random floats
        mainGrid = new double[sizeY + 4][sizeX + 4];
        Random random = new Random();
        for (int y = 0; y < sizeY + 4; y++) {
            for (int x = 0; x < sizeX + 4; x++) {
                mainGrid[y][x] = random.nextDouble() * 2 - 1;
            }
        }

        //create random wind
        mainWind= new int[2];
        Random rand = new Random();
        do {
            mainWind[0] = rand.nextInt(3) - 1;
            mainWind[1] = rand.nextInt(3) - 1;
        } while (mainWind[0] == 0 && mainWind[1] == 0);

        wetNoise = generateNoise(mainGrid, PATTERNS[6], 36); // water noise
        windNoise = generateNoise(mainGrid, PATTERNS[0], 9); // wind noise

    }

    public static void main(String[] args) { // if __name__ == "__main__" but in java
        perlin p = new perlin();

        p.loop();
    }

    public static void loop(){
        while (true) {
            try {
            Thread.sleep(1000); // wait a second
            } catch (InterruptedException e) {
                System.out.println("broken");
                e.printStackTrace();
            }
 

            translate(mainGrid, mainWind); // move the floats around the grid

            wetNoise = generateNoise(mainGrid, PATTERNS[6], 36); // water noise
            windNoise = generateNoise(mainGrid, PATTERNS[0], 9); // wind noise

            //clears the screen
            System.out.print("\033[H\033[2J");  
            System.out.flush();

            // writes to the screen
            String output = render(wetNoise, windNoise);
            System.out.print(output);
        }

    }

    public static String nextFrame(){

        translate(mainGrid, mainWind); // move the floats around the grid

        wetNoise = generateNoise(mainGrid, PATTERNS[6], 36); // water noise
        windNoise = generateNoise(mainGrid, PATTERNS[0], 9); // wind noise

        //outputs the rendered frame
        return render(wetNoise, windNoise);
        
    }

    private static double[][] generateNoise(double[][] grid, int[][] blend, int fade) {
        double[][] grid2 = new double[sizeY][sizeX];

        for (int x = 0; x < sizeX - 1; x++) {
            for (int y = 0; y < sizeY - 1; y++) {
                double val = grid[y][x];
                for (int i = 0; i < blend.length; i++) {
                    int nx = x + blend[i][0];
                    int ny = y + blend[i][1];
                    if (nx >= 0 && nx < sizeX && ny >= 0 && ny < sizeY) {
                        grid2[ny][nx] += val;
                    }
                }
            }
        }

        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                grid2[y][x] /= fade;
            }
        }
        return grid2;
    }
    
    public static String render(){
        return render(wetNoise, windNoise);

    }
    private static String render(double[][] grid1, double[][] grid2) {

        String output = "";
        for (int y = 0; y < sizeY; y++) {
            output += "\n";
            // System.out.println();
            for (int x = 0; x < sizeX; x++) {
                if (grid2[y][x] > MINIMUM_WIND) {
                    output += "\033[48;2;" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + "m  \033[0m";
                    // System.out.print("\033[48;2;" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + "m  \033[0m");
                } else {
                    output += "\033[48;2;0;0;" + (int) ((grid1[y][x] + 1) * 127.5) + "m  \033[0m";
                    // System.out.print("\033[48;2;0;0;" + (int) ((grid1[y][x] + 1) * 127.5) + "m  \033[0m");
                }
            }
            // System.out.println();
        }
        return output;
    }

    private static void translate(double[][] grid, int[] wind) {
        if (wind[0] == -1) {
            for (int y = 0; y < sizeY + 1; y++) {
                for (int x = 0; x < sizeX - 1; x++) {
                    grid[y][x] = grid[y][x + 1];
                }
                grid[y][sizeX - 1] = Math.random() * 2 - 1;
            }
        } else if (wind[0] == 1) {
            for (int y = 0; y < sizeY + 1; y++) {
                for (int x = sizeX - 1; x > 0; x--) {
                    grid[y][x] = grid[y][x - 1];
                }
                grid[y][0] = Math.random() * 2 - 1;
            }
        }

        if (wind[1] == -1) {
            for (int x = 0; x < sizeX; x++) {
                for (int y = 0; y < sizeY; y++) {
                    grid[y][x] = grid[y + 1][x];
                }
                grid[sizeY][x] = Math.random() * 2 - 1;
            }
        } else if (wind[1] == 1) {
            for (int x = 0; x < sizeX; x++) {
                for (int y = sizeY; y > 0; y--) {
                    grid[y][x] = grid[y - 1][x];
                }
                grid[0][x] = Math.random() * 2 - 1;
            }
        }
    }
}