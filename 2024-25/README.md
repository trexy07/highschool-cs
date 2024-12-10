## the game battle ship for AP cs A
```
Batteship
│   README.md # this
|   compile.sh # compiles the game's files & runs
│   run.sh  # runs the game after compilation
|   Board.java # stores the game data
|   Battleship.java # game logic and displaying
|
└───input
│   │   RawConsoleInput.java # immediate user input
│   │   jna-jpms-5.10.0.jar # allows code to use os specific methods
│
└───perlin # make patterns for the background
    │   Perlin.java # averages points
    │   TerminalSize.java # gets size of the terminal
```
run compile.sh with "./compile.sh"
