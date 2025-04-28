import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;


class ServerTest {
    // public static int[][] targets ={{4,4},{5,4},{6,4},{7,4},{8,4},   {4,9},{5,9},{6,9},{7,9}    ,{5,6},{6,6},{7,6}    ,{2,3},{3,3},{4,3}   ,{7,8},{8,8}};
    public static int[][] targets ={{4,4},{5,4},{6,4},{7,4},{8,4},   {4,9},{5,9},{6,9},{7,9}    ,{5,6},{6,6},{7,6}    ,{2,3},{3,3},{4,3}   ,{7,8}};

    public static void main(String[] args) {
        try                  {
            Server.main(args);
            Thread.sleep(1000);
        }catch (Exception e) {
            System.out.println("serverFault");
            e.printStackTrace();
            System.exit(1);
        }
        //17802230356044905440
        // start
        // 780 230 560 490 440
        // 780230560490440
        // 781230560490440
        // 440 490 560 230 780
        // sent as 5 x (X + Y + rotation bit )
        String[] res=sendRequest("http://localhost:8000/start?name=jeff&locations=780230560490440");
        System.out.println(res[1]);

        // join
        res=sendRequest("http://localhost:8000/join?id=0&name=not%20jeff&locations=780230560490440");
        System.out.println(res[1]);

        // bonus join (409)
        res=sendRequest("http://localhost:8000/join?id=0&name=not%20jeff&locations=780230560490440");
        System.out.println(res[1]);

        // get data
        res=sendRequest("http://localhost:8000/data?id=0");
        System.out.println(res[1]);

        // hit
        res=sendRequest("http://localhost:8000/hit?id=0&player=T&x=7&y=8");
        System.out.println(res[1]);
        
        // out of turn (425)
        res=sendRequest("http://localhost:8000/hit?id=0&player=T&x=7&y=8");
        System.out.println(res[1]);

        // player 2 hit
        res=sendRequest("http://localhost:8000/hit?id=0&player=F&x=7&y=8");
        System.out.println(res[1]);

        // re-hit (208, random hit) //already hit 8,9 -miss :( at 1,2 -?
        res=sendRequest("http://localhost:8000/hit?id=0&player=T&x=7&y=8");
        System.out.println("random"+res[1]);


        // hit loop
        int i =0;
        for (int[] target : targets) {
            res=sendRequest("http://localhost:8000/hit?id=0&player=F&x="+target[0]+"&y="+target[1]);
            System.out.println(res[1]);
            res=sendRequest("http://localhost:8000/hit?id=0&player=T&x="+target[0]+"&y="+target[1]);
            System.out.println(res[1]);
        }

        // for (int x : Server.rows.get(0)[0].hits ){
        //     System.out.print(x + " ");
        // }
        
        //restart server to test volatility 
        Server.server.stop(1);
        System.out.println("server closed");
        // Server.main(args);
        try                  {
            Server.main(args);
            Thread.sleep(1000);
        }catch (Exception e) {
            System.out.println("serverFault");
            e.printStackTrace();
            System.exit(1);
        }

        // for (int x : Server.rows.get(0)[0].hits ){
        //     System.out.print(x + " ");
        // }

        res=sendRequest("http://localhost:8000/hit?id=0&player=F&x=8&y=8");
        System.out.println(res[1]);
        res=sendRequest("http://localhost:8000/hit?id=0&player=T&x=8&y=8");
        System.out.println(res[1]);
        
        
    


        System.exit(0);
    }
    
    public static String[] sendRequest(String urlString) {
        return sendRequest("GET", urlString);
    }

    public static String[] sendRequest(String method, String urlString) {
        String[]          result     = new String[2];
        HttpURLConnection connection = null;
        BufferedReader    reader     = null;


        try {
            // URL url = new URI(urlString).toURL();
            URL url = new URI(urlString).toURL();
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod(method);

            int responseCode = connection.getResponseCode(); // receiving
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