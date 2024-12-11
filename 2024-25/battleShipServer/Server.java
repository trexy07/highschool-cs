import java.util.Map;
import java.util.HashMap;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

public class Server {
    
    // game data
    private static Map<Integer, Board[]> rows;
    private static Map<Integer, Boolean> turns;
    private static Map<Integer, String > hits;

    // server data
    private static int                   nextId = 0;

    public static void main(String[] args) throws Exception {
        // data for each running game
        rows  = new HashMap<>();
        turns = new HashMap<>();
        hits  = new HashMap<>();
        
        // create the server
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        server.createContext("/", new Handler());
        server.setExecutor(null); // creates a default executor
        server.start();
    }
    
    static class Handler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String path = t.getRequestURI().getPath();
            if        (path.equals("/start"  )) {
                handleStart(t);
            } else if (path.equals("/join"   )) {
                handleJoin(t);
            } else if (path.equals("/hit"    )) {
                handleHit(t);
            } else if (path.equals("/receive")) {
                handleReceive(t);
            } else                              {
                System.out.println("no endpoint: " + path);
                respond(t,404,"no endpoint: " + path);
            }
        }   

        //https://3bxtl7v5-8000.usw3.devtunnels.ms/start?name=jeff&locations=17802230356044905440
        public void handleStart(HttpExchange t) throws IOException{
            Map<String, String> args = arguments(t);

            // System.out.println(args);
            String name      = args.get("name");
            String locations = args.get("locations");

            if (name == null || locations == null){
                respond(t,400,"missing argument");
                return;
            }
            rows.put( nextId, new Board[]{ new Board(name,locations),null  });
            turns.put(nextId, true);
            hits.put( nextId, "");
            System.out.println(nextId +" started");

           

            respond(t,200,nextId+"");
            
            nextId++;
            return;
        }

        //https://3bxtl7v5-8000.usw3.devtunnels.ms/join?id=0&name=bob&locations=17802230356044905440
        public void handleJoin(HttpExchange t) throws IOException{
            Map<String, String> args = arguments(t);

            String name      = args.get("name");
            String locations = args.get("locations");

            if (args.get("id") == null || name == null || locations == null){
                respond(t,400,"missing argument");
                return;
            }
            int id = Integer. parseInt(args.get("id"));

            if (!rows.containsKey(id)){
                respond(t,406,"game not found");
                return;
            }
            if (rows.get(id)[1] != null){
                respond(t,409,"game full");
                return;
            }
            rows.get(id)[1] = new Board(name,locations);

            respond(t,200,"joined");
            return;
        }

        //https://3bxtl7v5-8000.usw3.devtunnels.ms/hit?id=0&player=T&x=7&y=8
        public void handleHit(HttpExchange t) throws IOException{
            Map<String, String> args = arguments(t);

            if (args.get("id") == null || args.get("player") == null || 
                args.get("x" ) == null || args.get("y"     ) == null){
                respond(t,400,"missing argument");
                return;
            } else if (!(args.get("player").equals("T") || args.get("player").equals("F"))){
                System.out.print(args.get("player"));
                System.out.println(args.get("player") == "F"   );
                
                respond(t,400,"invalid player");
                return;
            } else if (args.get("x").length() != 1 || args.get("y").length() != 1 ){ 
                //|| !Character.isDigit(args.get("x").charAt(0)) || !Character.isDigit(args.get("y").charAt(0))
                respond(t,400,"invalid x or y");
                return;
            }

            int id;
            int x;
            int y;

            try {
                id = Integer.parseInt(args.get("id"));
                x  = Integer.parseInt(args.get("x" ));
                y  = Integer.parseInt(args.get("y" ));
            } catch (NumberFormatException e){
                respond(t,400,"invalid id, x, or y");
                return;
            }
            // System.out.println(id + " " + x + " " + y);
            boolean player = args.get("player").equals("T");
            
            if        (!rows.containsKey(id))  {
                respond(t,406,"game not found");
                return;
            } else if (rows.get(id)[1] == null){
                respond(t,409,"game not filled");
                return;
            } else if (turns.get(id) != player){
                respond(t,425,"not your turn");
                return;
            } 

            Board[] row = rows.get(id);
            
            // System.out.println(row[player?1:0].name); // enemy name check
            String  hit = row[player?1:0].hit(x,y); // get the location it hit

            // // debug graphics
            // for (int i = 0; i<row[player?1:0].board.length; i++){
            //     for (int j = 0; j<row[player?1:0].board[i].length; j++){
            //         System.out.print(row[player?1:0].board[i][j]);
            //     }
            //     System.out.println();
            // }

            // store the last hit
            hits.put(id, hit);
            // change the turn
            turns.put(id, !turns.get(id));

            respond(t, 200, hit);
        }

        //https://3bxtl7v5-8000.usw3.devtunnels.ms/receive?id=0
        public void handleReceive(HttpExchange t) throws IOException{
            Map<String, String> args = arguments(t);

            // input validation
            if (args.get("id") == null){
                System.out.println("missing args");
                respond(t,400,"missing argument");
                return;
            }

            int id = Integer.parseInt(args.get("id"));

            // check the game is live
            if (!rows.containsKey(id)){
                System.out.println("not found" + id);
                respond(t,406,"game not found");
                return;
            }

            // get this match
            Board[] row = rows.get(id);

            // calculate the second player's name
            String name2 = row[1] == null ? "null" : row[1].name;
            
            // required to return names,turn,last hit position
            String response = row[0].name + "," + name2 + "," + 
                            turns.get(id) + "," + hits.get(id); // turn and last hit
            
            System.out.println(response);
            respond(t,200,response);
            return;

        }
    }
    
    public static Map<String, String> arguments(HttpExchange t){
        String query = t.getRequestURI().getQuery();

        Map<String, String> args = new HashMap<String, String>();

        String[] outputs=query.split("&");
        for (int i = 0; i<outputs.length; i++){
            // System.out.println(outputs[i]);
            String[] split=outputs[i].split("=");
            args.put(split[0], split[1]);
        }
        // if (outputs.length<0){
        //     args = new HashMap<String, String>();
        // }

        return args;
    }
    
    public static void respond(HttpExchange t, int code,String response) throws IOException{
        t.sendResponseHeaders(code, response.length());
        OutputStream os = t.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }
}
