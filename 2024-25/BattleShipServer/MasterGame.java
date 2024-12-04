class MasterGame{

    public String p1Name;
    public String p2Name;
    private String[][] p1State;
    private String[][] p2State;
    public boolean turn=true;

    public MasterGame(String p1, String locations){

        this.p1State = new String[10][10];
        this.p2State = new String[10][10];
        for (int i = 0; i < 10; i++){
            for (int j = 0; j < 10; j++){
                this.p1State[i][j] = "00"; // each spot is boat/no boat and hit/none
                this.p2State[i][j] = "00";
            }
        }
        loadPlayer(p1, locations, p1State);
    }
    public void loadPlayer(String p1, String locations, String[][] board){
        // locations
        // [   "ship type+ x+y+dir"*5     ]
        // ship type: 1-5
        // x|y: 0-9
        // dir: 0-1
        for(int i = 0;i<5;i++){
            int type =(locations.charAt(i*4))-'0';
            int x =(locations.charAt(i*4+1))-'0';
            int y =(locations.charAt(i*4+2))-'0';
            int rotation =(locations.charAt(i*4+3))-'0';
            System.out.println(  String.valueOf(type)+x+y+rotation);

            int length = type + (type<=2?1:0);
            System.out.println(length);



            boolean fail = false;

            // check ship placement
            for (int j = 0; j < length; j++){
                
                if (rotation==0){
                    // System.out.println(board[y][x+j]);
                    if (board[y][x+j] != "00"){
                        // System.out.println("fail");
                        fail = true;
                        break;
                    }
                } else {
                    // System.out.println(board[y+j][x]);
                    if (board[y+j][x] != "00"){
                        // System.out.println("fail");
                        fail = true;
                        break;
                    }
                }
                
            }
            if (fail){
                System.out.println("fail");
                return;
            }




        }


    }
    public static void main(String[] args){
        MasterGame a= new MasterGame("geff","17802230356044905440");

    }


}