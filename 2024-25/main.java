import java.io.IOException;

public class main {
    public static void main(String[] args) {
        try {
            // Set terminal width and height
            String command = "resize";//&& stty rows 33 && stty cols 1000";
            ProcessBuilder processBuilder = new ProcessBuilder("bash", "-c", command);
            System.out.println(processBuilder.inheritIO().start().waitFor());


            // String command2 = "tput lines";
            // ProcessBuilder processBuilder2 = new ProcessBuilder("bash", "-c", command);
            // System.out.println(processBuilder2.inheritIO().start().waitFor());
            
            System.out.println("Terminal size changed successfully.");
            
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    System.out.print(j);
                    }
            }
            System.out.print("over");

        } catch (IOException | InterruptedException e) {
            System.out.println("broken");

            e.printStackTrace();
        }
    }
}
