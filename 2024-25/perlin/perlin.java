
import java.util.Random;
import java.io.IOException;
//// fix statics, they are properties of the whole class not just one instance
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

    // size of the render, default is an ansi terminal
    private static int sizeX = 80 / 2;
    private static int sizeY = 24;

    private int[] mainWind; // how the grid moves
    private double[][] mainGrid; // the grid of floats

    private double[][] wetNoise; // water noise generated from the grid
    private double[][] windNoise; // wind noise generated from the grid

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
        this.mainGrid = new double[sizeY + 4][sizeX + 4];
        Random random = new Random();
        for (int y = 0; y < sizeY + 4; y++) {
            for (int x = 0; x < sizeX + 4; x++) {
                this.mainGrid[y][x] = random.nextDouble() * 2 - 1;
            }
        }

        //create random wind
        this.mainWind = new int[2];
        Random rand = new Random();
        do {
            this.mainWind[0] = rand.nextInt(3) - 1;
            this.mainWind[1] = rand.nextInt(3) - 1;
        } while (this.mainWind[0] == 0 && this.mainWind[1] == 0);

        this.wetNoise = generateNoise(this.mainGrid, PATTERNS[6], 36); // water noise
        this.windNoise = generateNoise(this.mainGrid, PATTERNS[0], 9); // wind noise

    }

    public static void main(String[] args) { // if __name__ == "__main__" but in java
        perlin p = new perlin();

        p.loop();

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

    public void loop() { // default loop that moves the animation and renders it every second
        while (true) {
            try {
                Thread.sleep(1000); // wait a second
            } catch (InterruptedException e) {
                // System.out.println("broken");
                // e.printStackTrace();
            }

            translate(this.mainGrid, this.mainWind); // move the floats around the grid

            this.wetNoise = generateNoise(this.mainGrid, PATTERNS[6], 36); // water noise
            this.windNoise = generateNoise(this.mainGrid, PATTERNS[0], 9); // wind noise

            //clears the screen
            System.out.print("\033[H\033[2J");
            System.out.flush();

            // writes to the screen
            String output = render(this.wetNoise, this.windNoise);
            System.out.print(output);
        }

    }

    public String nextFrame() { // moves the animation, and returns the render 

        translate(this.mainGrid, this.mainWind); // move the floats around the grid

        this.wetNoise = generateNoise(this.mainGrid, PATTERNS[6], 36); // water noise
        this.windNoise = generateNoise(this.mainGrid, PATTERNS[0], 9); // wind noise

        //outputs the rendered frame
        return render(this.wetNoise, this.windNoise);

    }

    public String nextFrame(String[][] overlay) { // moves the animation, and returns the render with an overlay 

        translate(this.mainGrid, this.mainWind); // move the floats around the grid

        this.wetNoise = generateNoise(this.mainGrid, PATTERNS[6], 36); // water noise
        this.windNoise = generateNoise(this.mainGrid, PATTERNS[0], 9); // wind noise

        //outputs the rendered frame
        return render(this.wetNoise, this.windNoise, overlay);

    }

    private static double[][] generateNoise(double[][] grid, int[][] blend, int fade) { // takes a grid of floats and mixes them in a pattern
        double[][] grid2 = new double[sizeY][sizeX];

        for (int x = 0; x < sizeX - 1; x++) {
            for (int y = 0; y < sizeY - 1; y++) {
                double val = grid[y][x];
                for (int[] row : blend) {
                    int nx = x + row[0];
                    int ny = y + row[1];
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

    public String render() { //default args for outside rendering 
        return render(this.wetNoise, this.windNoise);

    }

    public String render(String[][] overlay) { //render with text that replaces the wind
        return render(this.wetNoise, this.windNoise, overlay);
    }

    private static String render(double[][] grid1, double[][] grid2) { // layers the bottom and top noise 

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

    private static String render(double[][] grid1, double[][] grid2, String[][] overlay) { // renders with an overlay and chosen noise 
        String output = "";
        String square;

        for (int y = 0; y < sizeY; y++) {
            output += "\n";
            // System.out.println();

            for (int x = 0; x < sizeX; x++) {
                square = overlay[y][x];
                if (square == null) {

                    if (grid2[y][x] > MINIMUM_WIND) {
                        output += "\033[48;2;" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + "m  \033[0m";
                        // System.out.print("\033[48;2;" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + "m  \033[0m");
                    } else {
                        output += "\033[48;2;0;0;" + (int) ((grid1[y][x] + 1) * 127.5) + "m  \033[0m";
                        // System.out.print("\033[48;2;0;0;" + (int) ((grid1[y][x] + 1) * 127.5) + "m  \033[0m");
                    }
                } else {
                    // System.out.println("overlay");
                    output += "\033[48;2;0;0;" + (int) ((grid1[y][x] + 1) * 127.5) + "m" + square + "\033[0m";
                }
            }
            // System.out.println();
        }
        return output;

    }

    private static void translate(double[][] grid, int[] wind) { // moves a grid of floats in a direction, and adds new floats to the edge
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
