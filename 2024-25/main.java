import java.io.IOException;

public class main {
    public static void main(String[] args) {
        // String message = new String("AP Practice");
        // String note = new String("AP Practice");
        // String memo = new String("memo");
        // int i = 5;

        // if (message.equals(note) && !message.equals("memo"))
        // {
        //     message = note;

        //     if (message == note && message.length() > i)
        //     {
        //     i = 3;
        //     memo = message.substring(i);
        //     }
        // }
        // System.out.println(message == note && message == memo);
        // System.out.println(message.equals(note) && message.equals(memo));
        // System.out.println(message == note && memo.equals("AP Practice"));
        // System.out.println(message != note || message == memo);
        // System.out.println(message.equals(memo) || memo.equals(note));
        // System.out.println(message+","+note+","+memo);
        
        try {
            // Set terminal width and height
            String command = "resize";//&& stty rows 33 && stty cols 1000";
            ProcessBuilder processBuilder = new ProcessBuilder("bash", "-c", command);
            // System.out.println(processBuilder.inheritIO().start().waitFor());

            System.out.println("line");

            String command2 = "tput cols";
            ProcessBuilder processBuilder2 = new ProcessBuilder("bash", "-c", command2);
            processBuilder2.inheritIO().start().waitFor();
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
