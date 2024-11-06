import java.io.IOException;

public class rawTest {

    public static void main(String[] args) throws IOException {
        Thread helloThread = new Thread(() -> {
            while (true) {
                try {
                    Thread.sleep(5000);
                    System.out.println("hello");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        helloThread.setDaemon(true);
        helloThread.start();

        System.out.println("Press any key to see it printed. Press esc to quit.");

        while (true) {
            int key = RawConsoleInput.read(true);
            if ( key == 3) {
                break;
            }
            System.out.println("You pressed: " + (char) key);
        }
    }
}