import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;


class ServerTest {
    public static void main(String[] args) {
        try {
            Server.main(args);
            Thread.sleep(1000);
        }catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
        // start
        String[] res=sendRequest("http://localhost:8000/start?name=jeff&locations=17802230356044905440");
        System.out.println(res[1]);

        // join
        res=sendRequest("http://localhost:8000/join?id=0&name=not%20jeff&locations=17802230356044905440");
        System.out.println(res[1]);

        // join
        res=sendRequest("http://localhost:8000/receive?id=0");
        System.out.println(res[1]);

        // hit
        res=sendRequest("http://localhost:8000/hit?id=0&player=T&x=7&y=8");
        System.out.println(res[1]);
        
        // out of turn
        res=sendRequest("http://localhost:8000/hit?id=0&player=T&x=7&y=8");
        System.out.println(res[1]);

        // player 2 hit
        res=sendRequest("http://localhost:8000/hit?id=0&player=F&x=7&y=8");
        System.out.println(res[1]);

        // re-hit (random hit)
        res=sendRequest("http://localhost:8000/hit?id=0&player=T&x=7&y=8");
        System.out.println(res[1]);


        System.exit(0);
    }
    public static String[] sendRequest(String urlString) {
        return sendRequest("GET", urlString);
    }

    public static String[] sendRequest(String method, String urlString) {
        String[]          result     = new String[2];
        HttpURLConnection connection = null;
        BufferedReader    reader;


        try {
            // URL url = new URI(urlString).toURL();
            URL url = new URI(urlString).toURL();
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod(method);

            int responseCode = connection.getResponseCode(); // reciving
            result[0] = String.valueOf(responseCode);


            // InputStream stream = 
            // System.out.println("response code: " + responseCode);

            if ((300 < responseCode || responseCode < 200)) {
                System.out.println("response code: " + responseCode);
                // System.out.println("response message: " + connection.getResponseMessage());
                reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
                // return {}
            } else {
                reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            }

            StringBuilder response = new StringBuilder();
            String        line;

            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            result[1] = response.toString();
        } catch (Exception e){
            System.out.println("caught Error: " );
            e.printStackTrace();
            // System.out.println(response.toString());
            System.exit(1);
        } finally {
            if (reader     != null) {
                try                     {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (connection != null) {
                connection.disconnect();
            }
        }

        return result;
    }
}