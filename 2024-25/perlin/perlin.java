import java.util.Random;
import java.io.IOException;


public class perlin {
    private static final double MINIMUM_WIND = 0.1; // -1 to 1, 
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
    
    // private static int SIZEX = 60/2;
    // private static int SIZEY = 30;
    private static int SIZEX = 160/2;
    private static int SIZEY = 16;
    


    public static void main(String[] args) {
        

        try {
            int[] terminalSize = TerminalSize.getTerminalSize();
            SIZEX = terminalSize[1] / 2;
            SIZEY = terminalSize[0];
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            // Default values if terminal size cannot be determined
            // SIZEX = 160 / 2;
            // SIZEY = 16;
        }
        

        System.out.println("test");
        System.out.println(SIZEX + " " + SIZEY);

        double[][] grid = new double[SIZEY + 4][SIZEX + 4];
        Random random = new Random();
        for (int y = 0; y < SIZEY + 4; y++) {
            for (int x = 0; x < SIZEX + 4; x++) {
                grid[y][x] = random.nextDouble() * 2 - 1;
            }
        }

        // int[] wind = PATTERNS[6];
        int[] wind = new int[2];
        Random rand = new Random();
        do {
            wind[0] = rand.nextInt(3) - 1;
            wind[1] = rand.nextInt(3) - 1;
        } while (wind[0] == 0 && wind[1] == 0);

        while (true) {
            try {
            Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println("broken");
                e.printStackTrace();
            }
            // Thread.sleep(1000);

            // try {
            //     Thread.sleep(1000);
            // } catch (Exception e) {
            //     System.out.println("broken");
            //     System.out.println(e);
            //     // return;
            //     e.printStackTrace();
            //     return;
            // }
            translate(grid, wind);

            // double[][] wetNoise = perlin(grid, PATTERNS[6], 36); // wet noise
            // double[][] windNoise = perlin(grid, PATTERNS[0], 9); // wind noise
            double[][] wetNoise = perlin(grid, PATTERNS[6], 36); // wet noise
            double[][] windNoise = perlin(grid, PATTERNS[0], 9); // wind noise

            System.out.print("\033[H\033[2J");  
            System.out.flush();

            mergePrint(wetNoise, windNoise);
            // System.out.print("\033[H\033[2J");
            // System.out.flush(); // writes all to the screen
        }
    }

    private static double[][] perlin(double[][] grid, int[][] blend, int fade) {
        double[][] grid2 = new double[SIZEY][SIZEX];

        for (int x = 0; x < SIZEX - 1; x++) {
            for (int y = 0; y < SIZEY - 1; y++) {
                double val = grid[y][x];
                for (int i = 0; i < blend.length; i++) {
                    int nx = x + blend[i][0];
                    int ny = y + blend[i][1];
                    if (nx >= 0 && nx < SIZEX && ny >= 0 && ny < SIZEY) {
                        grid2[ny][nx] += val;
                    }
                }
            }
        }

        for (int x = 0; x < SIZEX; x++) {
            for (int y = 0; y < SIZEY; y++) {
                grid2[y][x] /= fade;
            }
        }
        return grid2;
    }

    private static void mergePrint(double[][] grid1, double[][] grid2) {
        for (int y = 0; y < SIZEY; y++) {
            System.out.println();
            for (int x = 0; x < SIZEX; x++) {
                if (grid2[y][x] > MINIMUM_WIND) {
                    System.out.print("\033[48;2;" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + ";" + (int) ((grid2[y][x] + 1) * 127.5) + "m  \033[0m");
                } else {
                    System.out.print("\033[48;2;0;0;" + (int) ((grid1[y][x] + 1) * 127.5) + "m  \033[0m");
                }
            }
            // System.out.println();
        }
    }

    private static void translate(double[][] grid, int[] wind) {
        if (wind[0] == -1) {
            for (int y = 0; y < SIZEY + 1; y++) {
                for (int x = 0; x < SIZEX - 1; x++) {
                    grid[y][x] = grid[y][x + 1];
                }
                grid[y][SIZEX - 1] = Math.random() * 2 - 1;
            }
        } else if (wind[0] == 1) {
            for (int y = 0; y < SIZEY + 1; y++) {
                for (int x = SIZEX - 1; x > 0; x--) {
                    grid[y][x] = grid[y][x - 1];
                }
                grid[y][0] = Math.random() * 2 - 1;
            }
        }

        if (wind[1] == -1) {
            for (int x = 0; x < SIZEX; x++) {
                for (int y = 0; y < SIZEY; y++) {
                    grid[y][x] = grid[y + 1][x];
                }
                grid[SIZEY][x] = Math.random() * 2 - 1;
            }
        } else if (wind[1] == 1) {
            for (int x = 0; x < SIZEX; x++) {
                for (int y = SIZEY; y > 0; y--) {
                    grid[y][x] = grid[y - 1][x];
                }
                grid[0][x] = Math.random() * 2 - 1;
            }
        }
    }
}