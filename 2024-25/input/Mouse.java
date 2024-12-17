package input;
import java.io.IOException;
// import RawConsoleInput;
import input.RawConsoleInput;


public class Mouse {

    public static void main(String[] args) throws IOException {

        // Print all arguments
        
        
        // Enable mouse reporting in SGR mode
        System.out.print("\033[?1000h"); // Enable mouse tracking
        System.out.print("\033[?1006h"); // Enable SGR extended mouse mode
        // System.out.print("\033[?1015h"); // Enable SGR extended mouse mode

        System.out.println("Mouse input enabled. Press 'q' to quit.");

        while (true) {
            int input = read();
            // int input = System.in.read();

            // If the user presses 'q', exit the program
            if (input == 'q' || input == 3) {
                break;
            }
            int[] data = checkMouse((char)input);
            if (data[0] != -1){
                System.out.println(data[0] + " " + data[1] + " " + data[2] + " " + data[3]);
            }

        }

        // Disable mouse reporting
        System.out.print("\033[?1000l");
        System.out.print("\033[?1006l");
        

        System.out.println("Mouse input disabled. Goodbye!");
    }

    public static int read() throws IOException {
        // return read();
        int key = RawConsoleInput.read(true);
        // if ( key == 3) {
            
        //     System.out.print("\033[?1000l");
        //     System.out.print("\033[?1006l");
        //     System.out.println("Mouse input disabled. Goodbye!");
        // }
        return key;
    }
    public static int[] checkMouse(char last) throws IOException {
        int[] data = new int[4];
        data[0] = -1;

        // Check for mouse-related sequences
        if (last == 27) { // ESC
            int key = read();
            if (key == '[') {
                key = read();

                // StringBuilder event = new StringBuilder();
                // int ch;

                if (key == '<') { // Mouse SGR Mode
                    // StringBuilder event = new StringBuilder();
                    // int key;
                    // int[] data = new int[4];
                    int dataIndex = 0;

                    while ((key = read()) != -1) {
                        if        (key == 'm' || key == 'M') {
                            // event.append((char) key);
                            data[3] = (key == 'm') ? 1 : 0;
                            break;
                        } else if (key == ';'             ) {
                            dataIndex++;
                        } else                             {
                            data[dataIndex] = data[dataIndex] * 10 + (key - '0');
                        }
                    }
                    // System.out.println("Mouse Event: " + event.toString());
                    // System.out.println(data[0] + " " + data[1] + " " + data[2] + " " + data[3]);
                    
                }
            }
        }

        return (int[]) data;
    }
}
