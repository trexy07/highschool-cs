#!/bin/bash
javac -cp input:input/jna-jpms-5.15.0.jar input/RawConsoleInput.java 
# javac drawing/Perlin.java 
# javac perlin/TerminalSize.java 
javac drawing/*.java
javac Board.java 
javac Battleship.java 
# java -cp .:input/jna-jpms-5.15.0.jar Battleship