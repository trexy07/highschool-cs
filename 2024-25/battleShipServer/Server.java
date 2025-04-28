import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;
import java.util.Timer;
import java.util.TimerTask;

import java.nio.charset.StandardCharsets;

// import java.util.Calendar;

import java.io.DataOutputStream;
import java.io.File;
import java.nio.file.Files;
import java.io.FileOutputStream;

public class Server {
    
    // game data
    private static Map<Integer, Board[]> rows;
    // public static  Map<Integer, Board[]> rows;
    private static Map<Integer, Boolean> turns;
    private static Map<Integer, String > hits;
    private static Map<Integer, Integer> activity;
    private static ArrayList<Integer>    freeIds;

    private static Map<Integer, DataOutputStream> saves;
    private static DataOutputStream save;
    private static DataOutputStream open;

    // server data
    private static int                   nextId = 0;

    public static HttpServer server;

    public static void main(String[] args) throws Exception {
        // data for each running game
        rows      = new HashMap<>();
        turns     = new HashMap<>();
        hits      = new HashMap<>();
        activity  = new HashMap<>();
        freeIds   = new ArrayList<>();

        saves     = new HashMap<>();

        File saveFile = new File("save.bin");
        if (!saveFile.exists()) {
            saveFile.createNewFile();
        }
        save = new DataOutputStream(new FileOutputStream("save.bin", true));

        
        File folder = new File("saves");
        if (!folder.exists() ) {
            folder.mkdir();
        }
        int max = -1;
        for (File file : folder.listFiles()) {
            if (file.isFile()) {
                System.out.println(file.getName());
                int id = Integer.parseInt(file.getName().split("\\.")[0]);
                if (id > max) {
                    max = id;
                }
                // saves.put(id, new DataOutputStream(new FileOutputStream("saves/" + id + ".bin", true)));
                

                // String savedData = new String(Files.readAllBytes(file.toPath()),StandardCharsets.US_ASCII);
                // saveData.split("\\|");
                byte[] savedData = Files.readAllBytes(file.toPath());
                // List<byte[]> segments = new ArrayList<>();


                // List<Byte>[] segments = new ArrayList[6];
                List<byte[]> segments = new ArrayList<>();
                
                List<Byte> temp = new ArrayList<>();
                
                for (byte b : savedData) {
                    if (b == 127) {
                        // System.out.println(temp.toArray(new Byte[6]).getClass());
                        // segments.add(temp.toArray(new byte[6]));
                        byte[] segment = new byte[temp.size()];
                        for (int i = 0; i < temp.size(); i++) {
                            segment[i] = temp.get(i);
                        }
                        segments.add(segment);

                        temp.clear();
                    
                        // byte[] segment = new byte[segments.size()];
                        // for (int i = 0; i < segments.size(); i++) {
                        //     segment[i] = segments.get(i);
                        // }
                        // segments.add(segment);
                    } else {
                        // temp.add(b);
                        temp.add((Byte) b);
                        // System.out.println(b);
                    }
                }

                byte[] tempSegment = new byte[temp.size()];
                for (int i = 0; i < temp.size(); i++) {
                    tempSegment[i] = temp.get(i);
                }
                segments.add(tempSegment);

                System.out.println(segments.size());
                if (segments.size() != 6) {
                    System.out.println("corrupt save file");
                    continue;
                }

                String name1= new String(segments.get(0),StandardCharsets.US_ASCII);
                String name2= new String(segments.get(2),StandardCharsets.US_ASCII);

                String[] ships= new String[2];
                for (int s =1; s<4; s+=2) {
                    byte[] segment = segments.get(s);
                    ships[(s-1)/2] = "";
                    for (int i = 0; i <5; i++) {
                        int rotation = (segment[i] < 0) ? 1 : 0;

                        // remove rotation bit
                        int value = segment[i] - (rotation * -128);

                        // get x and y
                        int y = value / 10;
                        int x = value % 10;

                        
                        // System.out.println("x: " + x);
                        // System.out.println("y: " + y);
                        // System.out.println("rot: " + rotation);
                        ships[(s-1)/2] += x +""+ y +""+ rotation;
                    }
                }
                System.out.println(ships[0]);
                System.out.println(ships[1]);
                
                DataOutputStream thisSave = new DataOutputStream(new FileOutputStream("saves/" + id + ".bin", true));
                // Board A = new Board(data[0], data[1], thisSave);
                // Board b = new Board(data[2], data[3], thisSave);

                Board american = new Board(name1, ships[0]);
                Board japan    = new Board(name2, ships[1]);

                int i=0;
                for (byte b : segments.get(5)){
                    // System.out.println(b);
                    // System.out.println(b%10+", "+b/10);
                    hits.put(i,  i%2==0 ? american.hit(b%10,b/10) : japan.hit(b%10,b/10));
                    // swap between players and hit
                    i++;
                }

                rows.put(id, new Board[]{ american, japan });
                turns.put(id, i%2==0);
                // hits      = new HashMap<>();
                activity.put(id, 7);
                // freeIds   = new ArrayList<>();

                saves.put(id, thisSave);
                american.save = thisSave;
                japan.save   = thisSave;


                // a.save = thisSave;//put saves back
                // b.save = thisSave;

                // saves.put(id, new DataOutputStream(new FileOutputStream("saves/" + id + ".bin", true)));
                // saves.put(id, thisSave);




            }
        } 
        nextId=max+1;
        System.out.println("max id: " + max);
        for (int i = 0; i <= max; i++) {
            if (!rows.containsKey(i)) {
                freeIds.add(i);
            }
        }

        
        // create the server
        server = HttpServer.create(new InetSocketAddress(8000), 0);
        Handler handler = new Handler();
        server.createContext("/", handler);
        server.setExecutor(null); // creates a default executor
        server.start();

        


        Timer timer = new Timer();
        // Schedule the task to run every 24 hours
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
            new Handler().age();
            }
        }, 0, 24 * 60 * 60 * 1000);
        // }, 0, 5* 1000);  // testing timer
    }
    
    static class Handler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            try{
                String path = t.getRequestURI().getPath();
                if        (path.equals("/start"  )) {
                    handleStart(t);
                } else if (path.equals("/join"   )) {
                    handleJoin(t);
                } else if (path.equals("/hit"    )) {
                    handleHit(t);
                } else if (path.equals("/data")) {
                    handleData(t);
                } else                              {
                    System.out.println("no endpoint: " + path);
                    respond(t,404,"no endpoint: " + path);
                }
            } catch (Exception e) {
                System.out.println("serverFaultInside");
                e.printStackTrace();
                System.exit(1);
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
            int id;
            if (freeIds.size() > 0){ // re use ids
                id = freeIds.remove(0); //acts like pop if I is an int
            } else {
                id = nextId++;
            }
            DataOutputStream tempSave = null;
            try{
                new File("saves/" + id + ".bin").createNewFile();
                tempSave= new DataOutputStream(new FileOutputStream("saves/" + id + ".bin"));
                saves.put(id,tempSave);
                // tempSave= new DataOutputStream(new FileOutputStream("saves/" + id + ".bin"));
                // saves.put(id,new DataOutputStream(new FileOutputStream("saves/" + id + ".bin")));
            } catch (IOException e){
                System.out.println("File not found");
            }

            rows    .put(id, new Board[]{ new Board(name,locations,tempSave),null  });
            // rows    .put(id, new Board[]{ new Board(name,locations),null  });
            turns   .put(id, true);
            hits    .put(id, "");
            activity.put(id, 7);

            

            // save(id, System.currentTimeMillis())
            // save(id, name);

            System.out.println(id +" started");

            respond(t,200,id+"");
            
            // nextId++;
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
            rows.get(id)[1] = new Board(name,locations,saves.get(id));
            // rows.get(id)[1] = new Board(name,locations);
            saveTime(id, System.currentTimeMillis());

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
                respond(t,406,"invalid id, x, or y");
                return;
            }
            // System.out.println(id + " " + x + " " + y);
            // System.out.println(activity.get(id));
            boolean player = args.get("player").equals("T");
            
            if        (!rows.containsKey(id))  {
                respond(t,406,"game not found");
                return;
            } else if (rows.get(id)[1] == null){
                respond(t,425,"game not filled");
                return;
            } else if (activity.get(id) == 0){
                respond(t,410,"game over");
                return;
            } else if (turns.get(id) != player){
                respond(t,425,"not your turn");
                return;
            } 
            
            Board[] row = rows.get(id);
            
            // System.out.println(row[player?1:0].name); // enemy name check
            String  hit = row[player?1:0].hit(x,y); // get the location it hit
            // if (hit == null){
            if (hit.charAt(0)=='1'){ // game over
                activity.put(id, 0);

                save.write(id);
                save.write(127);
                // Files.readAllBytes(id+".bin"), "utf-8")

                // Files.readAllBytes(id+".bin");
                
                // save.writeBytes(String();
                // save.write(y*10+x); // saves last hit location
                // saves.get(id).write(127);
                // saves.get(id).writeLong(System.currentTimeMillis());

                // saveTime(id, System.currentTimeMillis());

                File previousSave =new File("saves/" + id + ".bin");
                byte[] savedData = Files.readAllBytes(previousSave.toPath());
                save.write(savedData);

                saves.remove(id);
                // previousSave.delete();

                // save.write();
                
                save.write(127);
                save.writeLong(System.currentTimeMillis());

                save.write(255);
                respond(t,410,hit + "game over (just won)");
                return;
            } 
            activity.put(id, 7);


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


            // saves.get(id).write(  y*10+x); // saves hit locations // already done in the Board class

            respond(t, 200, hit);
        }

        //https://3bxtl7v5-8000.usw3.devtunnels.ms/data?id=0
        public void handleData(HttpExchange t) throws IOException{
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

        public void age(){
            System.out.println("aging");
            for (int id : activity.keySet()) {
                int newValue = activity.get(id) - 1;
                if (newValue < 0) {
                    activity.remove(id);
                    rows.remove(id);
                    turns.remove(id);
                    hits.remove(id);
                    freeIds.add(id);
                } else {
                    activity.put(id, newValue);
                }
            }
        }
        public void saveTime(int id, long data){
            try{
                saves.get(id).writeLong(data); // game start time
                saves.get(id).write(127);
            } catch (IOException e){
                e.printStackTrace();
            }
        } 
        // public void save(int id, int data){
        //     try{
        //         saves.get(id).write(data); // game start time
        //     } catch (IOException e){
        //         e.printStackTrace();
        //     }
        // } 
        // public void save(int id, String data){
        //     try{
        //         saves.get(id).writeBytes(data); // game start time
        //     } catch (IOException e){
        //         e.printStackTrace();
        //     }
        // } 
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
