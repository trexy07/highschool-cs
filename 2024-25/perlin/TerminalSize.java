import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class TerminalDimensions {

    public static int[] getTerminalSize() throws IOException, InterruptedException {
        ProcessBuilder processBuilder = new ProcessBuilder("sh", "-c", "stty size < /dev/tty");
        Process process = processBuilder.start();
        process.waitFor();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String[] size = reader.readLine().split(" ");
        int rows = Integer.parseInt(size[0]);
        int cols = Integer.parseInt(size[1]);

        return new int[]{rows, cols};
    }

    public static void main(String[] args) {
        try {
            int[] size = getTerminalSize();
            System.out.println("Terminal width: " + size[1]);
            System.out.println("Terminal height: " + size[0]);
            // System.out.println(size);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}