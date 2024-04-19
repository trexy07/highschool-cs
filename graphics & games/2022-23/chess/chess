### Make sure to select all, copy, and paste into your code.
### Don't forget to follow the rubric carefully when writing your code.
### The first requirement of the rubric is to follow the 
### Python Style Guide linked in the description of this project in Google 
### Classroom, so make sure to open the style guide and follow it carefully.

# disable inspector by default, can be toggled with keypress of "i"
app.inspectorEnabled = False

from builtins import round
import math
import string
import textwrap
from datetime import datetime

# todo
# implement no move -max
# lsoing from time limit - t
# placing pieces when captured

# classes{
#####
##### SPLASH SCREEN CLASS
#####
class SplashScreen:

    def __init__(self):
        ### Add code here to create your splasha screen
        self.drawing = Group(
            Rect(0, 0, 400, 400, fill='black'),
            Label("splash screen", 200, 200, fill="white", size=25),
        )

    def getVisible(self):
        return self.drawing.visible

    def setVisible(self, value):
        self.drawing.visible = bool(value)

    def delVisible(self):
        self.drawing.visible = False

    visible = property( #:
        getVisible,
        setVisible,
        delVisible,
        """Property wrapper for finna.drawing.visible."""
    )
    def restart(self):
        self.drawing.visible = True


#####
##### PAUSE MENU CLASS
#####    
class PauseMenu:

    def __init__(self):
        self.label=Label('Paused',200,100,size=50,fill='black',opacity=60)
        self.button=Group(Rect(200,200,250,50,fill='red',align='center'),Label("RESTART",200,200,size=50))
        self.drawing=Group(Rect(0,0,400,400,fill='grey',border='black',borderWidth=10),self.label,self.button,visible=False)

    def restart(self):
        self.drawing.toBack()
        self.visible = False

    def getVisible(self):
        return self.drawing.visible

    def setVisible(self, value):
        self.drawing.visible = bool(value)
        self.drawing.toFront()

    def delVisible(self):
        self.drawing.visible = False

    visible = property( #:
        getVisible,
        setVisible,
        delVisible,
        """Property wrapper for self.drawing.visible."""
    )

    def processOnMousePress(self, x, y, world):
        if self.button.contains(x,y) and app.getTextInput('type "RESTART" to restart')=="RESTART":

            world.restart()
        pass


class BaseChessClass:

    def unpackArgs(self, a, b=None):
        if b is not None:
            return a, b
        else:
            return a

    def copy(self):
        copied = type(self).__new__(type(self))
        for key, value in vars(self).items():
            if not (key.startswith("__") and key.endswith("__")):
                if hasattr(value, "copy"):
                    valueCopy = value.copy()
                else:
                    valueCopy = value
                setattr(copied, key, valueCopy)
        return copied


# Configuration names which mimic dunders are considered reserved, and their
# use is heavily discouraged.  Using them is possible, but accessing them via
# the getattribute syntax will not be possible when doing so. The getitem syntax
# will still work, however.  The names "internal" and "getConfigValue" are
# completely reserved, and will not worked if used as configuration names.
class Configuration(BaseChessClass):

    def __init__(self, *args, **kwargs):
        self.internal = kwargs
        for arg in args:
            self.internal |= arg

    def getConfigValue(self, configValueName):
        configValue = self.internal[configValueName]

        # If the value of an accessed configuration name starts with an "=", it
        # is treated specially.
        if type(configValue) is str and configValue.startswith("="):
            configVarname = configValue.removeprefix("=")

            # If the part of the string after the "=" contains a ".", then the
            # result of accessing the attribute with the name of the part of the
            # string after the "." on the variable with the name of the part of
            # the string before the "." is returned.
            if "." in configVarname:
                configVarname, _, attribute = configVarname.partition(".")
                return getattr(
                    self.getConfigValue("configVarname"),
                    attribute
                )

            # If the part of the string after the "=" does not contain a "."
            # character, then the variable with that name is returned.
            return self[configVarname]
        return configValue

    def __getattribute__(self, attrName):
        # If the attribute is a dunder, self.internal, self.getConfigValue, or
        # self.copy, then get and return the actual attribute.  Otherwise, get
        # the config value with the name f"{attrName}".
        if attrName in ("copy", "internal", "getConfigValue") or (
            attrName.startswith("__") and attrName.endswith("__")
        ):
            return object.__getattribute__(self, attrName)
        return self.getConfigValue(attrName)

    def __getitem__(self, itemName):
        return self.getConfigValue(itemName)

    def __setattr__(self, attr, value):
        # Only use self.internal after it has been created by .__init__.
        # Otherwise, self.internal cannot be set in .__init__, as self.internal
        # doesn't exist yet.
        if hasattr(self, "internal"):
            self.internal[attr] = value
        object.__setattr__(self, attr, value)

    def __setitem__(self, item, value):
        self.internal[item] = value

    def __ior__(self, other):
        self.internal |= other
        return self

    def __or__(self, other):
        copied = self.copy()
        copied |= other
        return copied


class DeepCopyList(list, BaseChessClass):
    # Override the .recursiveCopy method for the list so that all the items of
    # the list are also copied.
    def copy(self):
        copied = type(self)()
        for obj in self:
            if hasattr(obj, "copy"):
                objCopy = obj.copy()
            else:
                objCopy = obj
            copied.append(objCopy)
        return copied


class OffsetList(DeepCopyList):

    def __getitem__(self, item):
        if hasattr(item, "__index__"):
            return super().__getitem__(item.__index__() - 1)
        elif type(item) is slice:
            return super().__getitem__(slice(
                (item.start - 1) if item.start else None,
                (item.stop - 1) if item.stop else None,
                item.step,
            ))
        else:
            return super().__getitem__(item)

    def __setitem__(self, item, value):
        if hasattr(item, "__index__"):
            super().__setitem__(item.__index__() - 1, value)
        elif type(item) is slice:
            super().__setitem__(slice(
                (item.start - 1) if item.start else None,
                (item.stop - 1) if item.stop else None,
                item.step,
            ), value)
        else:
            return super().__setitem__(item, value)

    def index(self, obj):
        return super().index(obj) + 1


#pieces{

class Piece(BaseChessClass):
    pieceType = None
    moves = ""

    def __init__(self, side, col, row=None):
        self.side = side
        self.square = self.unpackArgs(col, row)
        self.col, self.row = self.square
        self.moved = False
        self.sprite = Group() # Each subclass will fill out self.sprite.

    def scaleSprite(self, scale):
        self.sprite.width *= scale
        self.sprite.height *= scale

    def moveTo(self, square, row=None):
        self.col, self.row = self.unpackArgs(square, row)
        # will force move to be true, can put seleted back into the 2D list
        #### self.moved=True

    def moveSprite(self, coord, y=None):
        self.sprite.centerX, self.sprite.centerY = self.unpackArgs(coord, y)


class King(Piece):
    pieceType = "king"
    moves = "AC"

    # Initialize the piece.
    def __init__(self, side, square, row=None):
        super().__init__(side, square, row)

    # Representation of the piece, for debug printing.
    def __repr__(self):
        return "♔" if self.side else "♚"

    # Render the piece sprite.
    def render(self, style, coord, y=None):
        # Get the arguments.
        x, y = self.unpackArgs(coord, y)
        # Get the correct fill.
        if self.side:
            pieceFill = style.whitePiecesColor
        else:
            pieceFill = style.blackPiecesColor
        # Draw the sprite.
        self.sprite = Group( #:
            Arc(x - 6.5, y + 4,20,30,0,200,fill=pieceFill),
            Arc(x + 6.5, y + 4,20,30,-200,210,fill=pieceFill),
            Oval(x + 0.5, y - 9, 20, 8,fill=pieceFill),
            Line(x + 0.5, y - 26, x + 0.5, y - 12,fill=pieceFill),
            Rect(x - 8.5, y + 14,15,5,fill=pieceFill),
            Rect(x - 13.5, y + 18,28,4,fill=pieceFill),
            Rect(x - 16.5, y + 21,33,6,fill=pieceFill),
            Arc(x - 3, y - 10,15,20,-30,200,fill=pieceFill,rotateAngle = -15),
            Arc(x + 3, y - 10,15,20,-200,240,fill=pieceFill,rotateAngle = 15),
            Rect(x - 7, y - 22,10,12,rotateAngle = -23,fill=pieceFill),
            Rect(x - 2, y - 22,10,12,rotateAngle = 25,fill=pieceFill),
            Line(x + 1, y - 21, x + 1, y - 31,lineWidth = 3,fill=pieceFill),
            Line(x - 4, y - 26, x + 6, y - 26,lineWidth = 3,fill=pieceFill),
            Oval(x, y + 18, 8,10,fill=pieceFill)
        )
        self.scaleSprite(style.pieceScale)


class Queen(Piece):
    pieceType = "queen"
    moves = "DH"

    # Initialize the piece.
    def __init__(self, side, square, row=None):
        super().__init__(side, square, row)

    # Representation of the piece, for debug printing.
    def __repr__(self):
        return "♕" if self.side else "♛"

    # Render the piece sprite.
    def render(self, style, coord, y=None):
        # Get the arguments.
        x, y = self.unpackArgs(coord, y)
        # Get the correct fill.
        if self.side:
            pieceFill = style.whitePiecesColor
        else:
            pieceFill = style.blackPiecesColor
        # Draw the sprite.
        self.sprite = Group( #:
            Circle(x + 0.5, y - 26,2,fill=pieceFill),
            Arc(x - 6.5, y + 4,20,30,0,200,fill=pieceFill),
            Arc(x + 6.5, y + 4,20,30,-200,210,fill=pieceFill),
            Oval(x + 0.5, y - 11,20,8,fill=pieceFill),
            Line(x + 0.5, y - 26, x + 0.5, y - 12,fill=pieceFill),
            Rect(x - 8.5, y + 12,15,5,fill=pieceFill),
            Rect(x - 13.5, y + 16,28,4,fill=pieceFill),
            Rect(x - 16.5, y + 19,33,6,fill=pieceFill),
            Arc(x - 3, y - 12,15,20,-30,200,fill=pieceFill,rotateAngle = -15),
            Arc(x + 3, y - 12,15,20,-200,240,fill=pieceFill,rotateAngle = 15),
            Oval(x, y + 20,8,10,fill=pieceFill)
        )
        self.scaleSprite(style.pieceScale)


class Rook(Piece):
    pieceType = "rook"
    moves = "H"

    # Initialize the piece.
    def __init__(self, side, square, row=None):
        super().__init__(side, square, row)
        self.rookSide = {
            1: "queen",
            8: "king",
        }.get(self.col)

    # Representation of the piece, for debug printing.
    def __repr__(self):
        return "♖" if self.side else "♜"

    # Render the piece sprite.
    def render(self, style, coord, y=None):
        # Get the arguments.
        x, y = self.unpackArgs(coord, y)
        # Get the correct fill.
        if self.side:
            pieceFill = style.whitePiecesColor
        else:
            pieceFill = style.blackPiecesColor
        # Draw the sprite.
        self.sprite = Group( #:
            Rect(x - 11.5, y - 25, 5, 10, fill=pieceFill),
            Rect(x - 3.5, y - 25, 6, 10, fill=pieceFill),
            Rect(x + 5.5, y - 25, 6, 10, fill=pieceFill),
            Rect(x - 11.5, y - 20, 23, 10, fill=pieceFill),
            Arc(x - 6.5, y + 3, 20, 30, 0, 200, fill=pieceFill, rotateAngle=4),
            Arc(x + 6.5, y + 3, 20, 30, -200, 210, fill=pieceFill, rotateAngle=-6),
            Circle(x, y - 14, 5, fill=pieceFill),
            Rect(x - 13.5, y + 15, 27, 5, fill=pieceFill),
            Rect(x - 16.5, y + 19, 33, 6, fill=pieceFill),
            Circle(x, y + 15, 5, fill=pieceFill),
            Circle(x, y + 6, 5, fill=pieceFill),
        )
        self.scaleSprite(style.pieceScale)


class Bishop(Piece):
    pieceType = "bishop"
    moves = "D"

    # Initialize the piece.
    def __init__(self, side, square, row=None):
        super().__init__(side, square, row)

    # Representation of the piece, for debug printing.
    def __repr__(self):
        return "♗" if self.side else "♝"

    # Render the piece sprite.
    def render(self, style, coord, y=None):
        # Get the arguments.
        x, y = self.unpackArgs(coord, y)
        # Get the correct fill.
        if self.side:
            pieceFill = style.whitePiecesColor
        else:
            pieceFill = style.blackPiecesColor
        # Draw the sprite.
        self.sprite = Group( #:
            Oval(x + 0.5, y - 15, 13, 18, fill=pieceFill),
            Circle(x + 0.5, y - 27,2,fill=pieceFill),
            Arc(x - 6.5, y + 3, 20, 30, 0, 200,fill=pieceFill),
            Arc(x + 6.5, y + 3, 20, 30, -200, 210,fill=pieceFill),
            Oval(x + 0.5, y - 10,18,5,fill=pieceFill),
            Line(x + 0.5, y - 27, x + 0.5, y - 12, fill=pieceFill),
            Rect(x - 8.5, y + 11,15,5,fill=pieceFill),
            Rect(x - 13.5, y + 14,28,4,fill=pieceFill),
            Rect(x - 16.5, y + 17,33,6,fill=pieceFill)
        )
        self.scaleSprite(style.pieceScale)


class Knight(Piece):
    pieceType = "knight"
    moves = "L"

    # Initialize the piece.
    def __init__(self, side, square, row=None):
        super().__init__(side, square, row)

    # Representation of the piece, for debug printing.
    def __repr__(self):
        return "♘" if self.side else "♞"

    # Render the piece sprite.
    def render(self, style, coord, y=None):
        # Get the arguments.
        x, y = self.unpackArgs(coord, y)
        # Get the correct fill.
        if self.side:
            pieceFill = style.whitePiecesColor
            borderFill = style.blackPiecesColor
        else:
            pieceFill = style.blackPiecesColor
            borderFill = style.whitePiecesColor
        # Draw the sprite.
        self.sprite = Group( #:
            # BORDER
            Arc(x - 5.5, y - 10, 41, 31, -10, 100, fill=borderFill),
            Oval(x - 0.5, y + 7, 24, 20, fill=borderFill),
            Arc(x - 0.5, y - 5, 32, 37, -10, 180, fill=borderFill),
            Rect(x - 12.5, y + 9, 24, 10, fill=borderFill),
            Rect(x - 15.5,y + 17, 30, 4, fill=borderFill),
            Rect(x - 17.5, y + 20, 34, 5.5, fill=borderFill),
            Oval(x - 7.5, y - 12, 12, 16, fill=borderFill),
            Rect(x - 17.5, y - 11, 10, 7, rotateAngle=-46, fill=borderFill),
            Circle(x - 15.5, y - 5, 3, fill=borderFill),
            Arc(x + 2.5, y - 7, 20,20,0,240,fill=borderFill),

            # PIECE
            Arc(x - 4.5, y - 10, 41, 31, -10, 100, fill=pieceFill),
            Oval(x + 0.5, y + 7, 24, 20, fill=pieceFill),
            Arc(x + 0.5, y - 5, 32, 37, -10, 180, fill=pieceFill),
            Rect(x - 11.5, y + 9, 24, 10, fill=pieceFill),
            Rect(x - 14.5,y + 17, 30, 4, fill=pieceFill),
            Rect(x - 16.5, y + 20, 34, 5.5, fill=pieceFill),
            Oval(x - 6.5, y - 12, 12, 16, fill=pieceFill),
            Rect(x - 16.5, y - 11, 10, 7, rotateAngle=-46, fill=pieceFill),
            Circle(x - 14.5, y - 5, 3, fill=pieceFill),
            Arc(x + 3.5, y - 7, 20,20,0,240,fill=pieceFill)
        )
        self.scaleSprite(style.pieceScale)


class Pawn(Piece):
    pieceType = "pawn"
    moves = "fde"

    # Initialize the piece.
    def __init__(self, side, square, row=None):
        super().__init__(side, square, row)
        self.doubled = False

    # Representation of the piece, for debug printing.
    def __repr__(self):
        return "♙" if self.side else "♟︎"

    # Render the piece sprite.
    def render(self, style, coord, y=None):
        # Get the arguments.
        x, y = self.unpackArgs(coord, y)
        # Get the correct fill.
        if self.side:
            pieceFill = style.whitePiecesColor
            borderFill = style.blackPiecesColor
        else:
            pieceFill = style.blackPiecesColor
            borderFill = style.whitePiecesColor
        # Draw the sprite.
        self.sprite = Group( #:
            # The border
            Circle(x - 2, y - 18, 7, fill=borderFill),
            Oval(x - 2, y - 11, 15, 5, fill=borderFill),
            Arc(x - 8, y + 5, 20, 30, 0, 200, fill=borderFill),
            Arc(x + 5, y + 5, 20, 30, -200, 210, fill=borderFill, rotateAngle=-10),
            Circle(x - 2, y - 9, 3, fill=pieceFill),
            Rect(x - 14, y + 16, 26, 3, fill=borderFill),
            Rect(x - 16, y + 18, 30, 2, fill=borderFill),
            Rect(x - 17, y + 19, 32, 5, fill=borderFill),
            Circle(x - 1, y - 18, 7, fill=pieceFill),
            Oval(x - 1, y - 11, 15, 5, fill=pieceFill),
            Arc(x - 7, y + 5, 20, 30, 0, 200, fill=pieceFill),
            Arc(x + 6, y + 5, 20, 30, -200, 210, fill=pieceFill, rotateAngle=-10),
            Circle(x - 1, y - 9, 3, fill=pieceFill),
            Rect(x - 13, y + 16, 26, 3, fill=pieceFill),
            Rect(x - 15, y + 18, 30, 2, fill=pieceFill),
            Rect(x - 16, y + 19, 32, 5, fill=pieceFill)
        )
        self.scaleSprite(style.pieceScale)


class EmptyPiece(Piece):
    pieceType = "empty"
    moves = ""

    # Initialize the piece.
    def __init__(self, side, square, row=None):
        super().__init__(side, square, row)

    # Representation of the piece, for debug printing.
    def __repr__(self):
        return "　"

    # Render the piece sprite.
    def render(self, style, coord, y=None):
        # Get the arguments.
        x, y = self.unpackArgs(coord, y)
        # Get the correct fill.
        if self.side:
            pieceFill = style.whitePiecesColor

        else:
            pieceFill = style.blackPiecesColor

        # Draw the sprite.
        self.sprite = Group( #:
            # Because this is an empty piece, there is no sprite. We still make
            # an empty group though, so that all the piece methods still work
            # correctly with the object.
        )
        self.scaleSprite(style.pieceScale)

#}

class Stream(BaseChessClass):

    def __init__(self, iterable):
        self.internal = list(iterable)

    def empty(self):
        return len(self.internal) == 0

    def get(self, index=None):
        if index is None:
            return self.internal.pop()
        else:
            return self.internal.pop(~index)

    def put(self, obj, index=None):
        if index is None:
            self.internal.append(obj)
        else:
            self.internal.insert(index, obj)

    def pop(self, index=None):
        if index is None:
            return self.internal.pop()
        else:
            return self.internal.pop(~index)

    def push(self, obj, index=None):
        if index is None:
            self.internal.append(obj)
        else:
            self.internal.insert(index, obj)

    def peek(self, index=0):
        if index < len(self.internal):
            return self.internal[~index]
        return None


class Handler(BaseChessClass):

    def reportError(self, errorType, errorMessage, retVal=None, throwError=True):
        if throwError:
            raise errorType(errorMessage)
        return retVal

    def getChar(self, stream, checkEmpty=True):
        if stream.empty():
            return self.reportError(
                ValueError,
                "encountered end of stream unexpectedly",
            )
        nextCharacter = stream.pop()
        if checkEmpty:
            if stream.empty():
                return self.reportError(
                    ValueError,
                    "encountered end of stream unexpectedly",
                    nextCharacter,
                )
        return nextCharacter

    def getIntStr(self, stream, base=10, checkSign=True, greedilySignParse=True, throwError=True):
        if not (2 <= base <= 36):
            raise ValueError("invalid base")
        if stream.empty():
            return self.reportError(
                ValueError,
                "invalid literal for int() with base {b}: {s!r}".format(
                    b = base, s = '',
                ),
                '',
                throwError = throwError
            )
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"[:base]
        if checkSign:
            if stream.peek() in "+-":
                signChar = stream.pop()
                signStr = signChar
                while greedilySignParse and stream.peek() == signChar:
                    signStr += stream.pop()
                else:
                    if stream.empty():
                        return self.reportError(
                            ValueError,
                            "invalid literal for int() with base {b}: {s!r}".format(
                                b = base, s = signStr,
                            ),
                            signStr,
                            throwError = throwError
                        )
                    elif stream.peek() in "+-":
                        intStr += stream.pop()
                        return self.reportError(
                            ValueError,
                            "invalid literal for int() with base {b}: {s!r}".format(
                                b = base, s = signStr,
                            ),
                            signStr,
                            throwError = throwError
                        )
            else:
                signStr = ""
        else:
            signStr = ""
        if stream.empty():
            return self.reportError(
                ValueError,
                "invalid literal for int() with base {b}: {s!r}".format(
                    b = base, s = intStr,
                ),
                intStr,
                throwError = throwError
            )
        elif stream.peek().lower() not in digits:
            signStr += stream.pop()
            return self.reportError(
                ValueError,
                "invalid literal for int() with base {b}: {s!r}".format(
                    b = base, s = signStr,
                ),
                intStr,
                throwError = throwError
            )
        intStr = ""
        while not stream.empty() and stream.peek().lower() in digits:
            intStr += stream.pop()
        return signStr+intStr

    def getFloatStr(self, stream, throwError=True):
        floatStr = self.getIntStr(stream, throwError=False)
        if stream.empty():
            if floatStr:
                return floatStr
            else:
                return self.reportError(
                    ValueError,
                    "invalid literal for float(): {s!r}".format(
                        s = floatStr,
                    ),
                    floatStr,
                    throwError = throwError
                )
        nextCharacter = self.getChar(stream).lower()
        if nextCharacter == "e":
            floatStr += nextCharacter
            intStr = self.getIntStr(
                stream,
                greedilySignParse=False,
                throwError=False
            )
            floatStr += intStr
            if not intStr:
                return self.reportError(
                    ValueError,
                    "invalid literal for float(): {s!r}".format(
                        s = floatStr,
                    ),
                    floatStr,
                    throwError = throwError
                )
        if stream.empty():
            return floatStr
        nextCharacter = self.getChar(stream).lower()
        if nextCharacter == ".":
            floatStr += nextCharacter
            intStr = self.getIntStr(
                stream,
                checkSign=False,
                throwError=False
            )
            floatStr += intStr
            if not intStr:
                return self.reportError(
                    ValueError,
                    "invalid literal for float(): {s!r}".format(
                        s = floatStr,
                    ),
                    floatStr,
                    throwError = throwError
                )
        return floatStr


class FENHandler(Handler):

    def __init__(self, FENString):
        ( #:
            self.FENPosition,
            self.activeColor,
            self.castlingRights,
            self.enPassantTarget,
            self.halfMoveClock,
            self.fullMoveClock,
        ) = self.FENParts = FENString.split()
        FENStream = Stream(reversed(self.FENPosition))
        columnIndex, rowIndex = 0, 0
        self.position = [
            [None for col in range(8)]
            for row in range(8)
        ]
        while (character := FENStream.peek()):
            if character == "/":
                columnIndex = 0
                rowIndex += 1
                FENStream.pop()
            elif character.isdigit():
                numStr = self.getIntStr(FENStream)
                for emptyColumnIndex in range(
                        columnIndex, columnIndex + int(numStr)
                    ):
                        self.position[rowIndex][emptyColumnIndex] = " "
            else:
                self.position[rowIndex][columnIndex] = FENStream.pop()
                columnIndex += 1

    def __getitem__(self, item):
        return self.position[item]


class PGNHandler(Handler):

    def __init__(self, PGNString):
        # Store the original PGN, so that if this is converted to a string, as
        # much information as possible can be kept from the original PGN. This
        # means that annotations and comments from the original PGN will be
        # kept, as well as any whitespace or extra symbols.
        self.PGNString = PGNString

        # List where all the move strings will be stored.
        self.moveStrings = []

        # Dictionary where tags will be stored.
        self.tags = {}
        
        # Parsing the string.
        PGNStream = Stream(PGNString)
        inFullLineComment = False
        inInlineComment = False
        inMoveNum = False
        currentMoveNum = ""
        inFirstPly = False
        inSecondPly = False
        currentPly = ""
        inTag = False
        inString = False
        escaped = False
        currentTag = ""
        currentString = ""
        moveCharacters = string.ascii_letters + string.digits + "-*=/()"
        while (character := PGNStream.peek()):
            if inFullLineComment:
                if character == "\n":
                    inFullLineComment = False
            elif inInlineComment:
                if character == "}":
                    inComment = False
            elif inTag and inString:
                if escaped:
                    if character not in '\"':
                        currentString += '\\'
                    currentString += character
                else:
                    if character == "\\":
                        escaped = True
                    elif character == '"':
                        inString = False
                    else:
                        currentString += character
            elif character == ";":
                inFullLineComment = True
            elif character == "{":
                inInlineComment = True
            elif inTag:
                if character == '"':
                    inString = True
                elif character == "]":
                    inTag = False
                    self.tags[currentTag] = currentString
                    currentTag = ""
                    currentString = ""
                elif character != " ":
                    currentTag += character
            elif inMoveNum:
                if character.isdigit():
                    currentMoveNum += character
                else:
                    inMoveNum = False
                    inFirstPly = True
            elif inFirstPly:
                if character in moveCharacters:
                    currentPly += character
                else:
                    # Don't continue if the currentPly is empty. Prevents spaces
                    # between the move number and the moves from being treated
                    # as a move.
                    if currentPly:
                        inFirstPly = False
                        inSecondPly = True
                        self.moveStrings.append(currentPly)
                        currentPly = ""
            elif inSecondPly:
                if character in moveCharacters:
                    currentPly += character
                else:
                    inSecondPly = False
                    self.moveStrings.append(currentPly)
                    currentPly = ""
            elif character == "[":
                inTag = True
            elif character.isdigit():
                inMoveNum = True
            PGNStream.pop()

        # The "FEN" tag needs to be handled specially because it's required.
        if "FEN" in self.tags:
            self.tags["FEN"] = FENHandler(self.FEN)
        # If there is no FEN tag, then simply assume that the starting position
        # is the standard one.
        else:
            self.FEN = FENHandler(
                "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - KQkq 0 1"
            )

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except:
            return self.tags[attr]

    def toString(self, moveList):
        # Convert to string.
        newMoveString = ""

        return f"{self.originalPGNString}\n"


class ChessMove(BaseChessClass):

    def __init__(self, moveString, boardState):
        # The format of moveString is SAN (Standard Algebraic Notation). For
        # information about how SAN works, see the following URL:
        #       <https://en.wikipedia.org/wiki/Algebraic_notation_(chess)>
        pass

    def apply(self, boardState):
        return
        if self.isCastle:
            pass
        else:
            if self.isCapture:
                boardState[self.targetRow][self.targetCol] = EmptyPiece(
                    None,
                    self.targetCol,
                    self.targetRow,
                )
            (
                boardState[self.pieceRow][self.pieceCol],
                boardState[self.targetRow][self.targetCol],
            ) = (
                boardState[self.targetRow][self.targetCol],
                boardState[self.pieceRow][self.pieceCol],
            )


class ChessBoard(BaseChessClass):

    def __init__(self, boardList, currentSide):
        self.boardList = OffsetList(map(OffsetList, boardList))
        self.currentSide = currentSide

    # Representation of the board, for debug printing.
    def __repr__(self):
        return "|\n|--|--|--|--|--|--|--|--|\n".join(
            "|" + "|".join(
                repr(piece) for piece in boardRow
            ) for boardRow in self.boardList[::-1]
        ) + "|"

    def __iter__(self):
        return iter(self.boardList)

    def __getitem__(self, item):
        return self.boardList[item]

    def __setitem__(self, item, value):
        self.boardList[item] = value

    def findPiece(self, side, pieceType, #:
        predicate=(lambda piece: True)
    ):
        for row in self.boardList:
            for piece in row:
                if (
                    piece.pieceType == pieceType
                        and
                    piece.side == side
                        and
                    predicate(piece)
                ):
                    return piece

    def swapPieces(self, firstCol, firstRow, secondCol, secondRow):
        firstPiece = self.boardList[firstRow][firstCol]
        secondPiece = self.boardList[secondRow][secondCol]
        (
            self.boardList[firstRow][firstCol],
            self.boardList[secondRow][secondCol],
        ) = (
            self.boardList[secondRow][secondCol],
            self.boardList[firstRow][firstCol],
        )
        firstPiece.moveTo(secondCol, secondRow)
        secondPiece.moveTo(firstCol, firstRow)




# end classes}
class ChessGame(BaseChessClass):

    #settings{
    variants = {
        ### ideas for other variants: {
        # tf2 pieces mixed in with the modes
        # tf2 cart thingy but both ways 
        # s & d
        # domination
        # tdm/bounty (better pieces are work more points)
        # gun game(have a small team of the same pieces + a king winer of the round chages the small team piece type  to make it harder)
        # clash royale
        # ray cA=sting knight
        # fort knight mode
        # rainbow 6
        # }
        "standard" : Configuration( #:
            boardSize = 8,
            rows = "=boardSize",
            cols = "=boardSize",
            PGN = PGNHandler(textwrap.dedent(
                f"""\
                [Event "online game"]
                [Site "online game"]
                [Date "{datetime.strftime(datetime.now(), "%Y.%m.%d")}"]
                [Round "1"]
                [White "unknown"]
                [Black "unknown"]
                [Result "*"]
                [Variant "standard"]
                [FEN "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - KQkq 0 1"]
                """
            )),
        ),
    }

    styles = {
        "defaultStyle" : Configuration( #:
            kingSide = "default",
            playerSide = "white",
            xOffset = 90,
            yOffset = 60,
            squareSize = 35,
            squareSizeHorizontal = "=squareSize",
            squareSizeVertical = "=squareSize",
            lightSquareColor = "green",
            darkSquareColor = "forestgreen",
            movableHighlightColor = "khaki",
            immovableHighlightColor = "dimGray",
            checkedHighlightColor = "royalBlue",
            checkingHighlightColor = "crimson",
            pieceScale = 0.6,
            whitePiecesColor = "ivory",
            blackPiecesColor = rgb(20, 20, 20),
            outlineProportion = 1/8,
            rowOutlineProportion = "=outlineProportion",
            colOutlineProportion = "=outlineProportion",
            outlineColor = "gray",
        ),
    }

    defaultConfig = Configuration( #:
        variant = variants["standard"],
        style = styles["defaultStyle"],
    )

    # Dictionary of {"piece character": piece class}
    stringsToPieces = {
        "K" : King,
        "Q" : Queen,
        "R" : Rook,
        "B" : Bishop,
        "N" : Knight,
        "P" : Pawn,
        " " : EmptyPiece,
        "-" : EmptyPiece,
    }
    piecesToStrings = {
        King        : 'K',
        Queen       : 'Q',
        Rook        : "R",
        Bishop      : "B",
        Knight      : "N",
        Pawn        : "P",
        EmptyPiece  : "-",
    }

    #}
    #funcs that work{
    def __init__(self, **kwargs):

        # Store the configuration that this was initialized with.
        self.config = self.defaultConfig | kwargs
        self.variant = self.config.variant
        self.style = self.config.style

        # [performance optimization]
        # Create and store these beforehand, rather than creating them whenever
        # they're needed for move validity checking.
        self.colNums = tuple(range(1, self.variant.cols + 1))
        self.rowNums = tuple(range(1, self.variant.rows + 1))

        # Creates self.boardOutline and self.boardSquares, and puts them both
        # into self.boardSprite.
        self.makeBoardSprite()

        # Get the game state from the PGN. boardState holds the current board,
        # and moveList holds all the moves that have been played so far.
        self.boardState, self.moveList = self.getGameFromPGN(self.variant.PGN)
        self.savedBoardState = None
        whiteKing = self.boardState.findPiece(True, "king")
        blackKing = self.boardState.findPiece(False, "king")
        self.kings = DeepCopyList([
            DeepCopyList([whiteKing.col, whiteKing.row]),
            DeepCopyList([blackKing.col, blackKing.row]),
        ])[::-1] # flip the list so that self.kings[True] is the whiteKing
        self.savedKings = None

        self.timeLeft=[20*60,20*60+.5]
        self.timeLabels=[Label("20:00",40,160,size=25,fill='red'),Label("20:00",40,240,size=25,fill='red'),]

        self.moveableSquares = 0

        self.selected=None
        self.savedSelected = None
        self.promo=False
        self.selectionMenu = Group(#:
            Rect(200,200,340,100,align='center',fill=None,border='black',borderWidth=10),

            #rook ↓
            Group(#:
                Rect(160-11.5,203-25,5,10,fill='blue'),
                Rect(160-3.5,203-25,6,10,fill='blue'),
                Rect(160+5.5,203-25,6,10,fill='blue'),
                Rect(160-11.5,203-20,23,10,fill='blue'),
                Arc(160-6.5,203+3,20,30,0,200,fill='blue',rotateAngle=4),
                Arc(160+6.5,203+3,20,30,-200,210,fill='blue',rotateAngle=-6),
                Circle(160+0,203-14,5,fill='blue'),
                Rect(160-13.5,203+15,27,5,fill='blue'),
                Rect(160-16.5,203+19,33,6,fill='blue'),
                Circle(160+0,203+10,5,fill='blue'),visible = True),

            #knight ↓
            Group(#:
                Arc(300-4.5,200-10.500975510527468,41,31,-10,100,fill='blue'),
                Oval(300+0.5,200+6.499024489472532,24,20,fill='blue'),
                Arc(300+0.5,200-5.500975510527468,32,37,-10,180,fill='blue'),
                Rect(300-11.5,200+8.499024489472532,24,10,fill='blue'),
                Rect(300-14.5,200+16.499024489472532,30,4,fill='blue'),
                Rect(300-16.5,200+20.499024489472532,34,5.5,fill='blue'),
                Oval(300-6.5,200-12.500975510527468,12,16,fill='blue'),
                Rect(300-16.5,200-11.500975510527468,10,7,rotateAngle = -46,fill='blue'),
                Circle(300-14.5,200-5.500975510527468,3,fill='blue'),
                Arc(300+3.5,200-7.500975510527468,20,20,0,240,fill='blue')),

            #bishop ↓
            Group(#:
                Oval(230+0.5,200-14,13,18,fill='blue'),
                Circle(230+0.5,200-26,2,fill='blue'),
                Arc(230-6.5,200+4,20,30,0,200,fill='blue'),
                Arc(230+6.5,200+4,20,30,-200,210,fill='blue'),
                Oval(230+0.5,200-11,18,5,fill='blue'),
                Line(230+0.5,200-28,230+0.5,200-12,fill='blue'),
                Rect(230-8.5,200+14,15,5,fill='blue'),
                Rect(230-13.5,200+18,28,4,fill='blue'),
                Rect(230-16.5,200+22,33,6,fill='blue')),

            #queen ↓
            Group(#:
                Circle(0.5,-26,2,fill='blue'),
                Arc(90-6.5,200+4,20,30,0,200,fill='blue'),
                Arc(90+6.5,200+4,20,30,-200,210,fill='blue'),
                Oval(90+0.5,200-11,20,8,fill='blue'),
                Line(90+0.5,200-26,90+0.5,200-12,fill='blue'),
                Rect(90-8.5,200+14,15,5,fill='blue'),
                Rect(90-13.5,200+18,28,4,fill='blue'),
                Rect(90-16.5,200+22,33,6,fill='blue'),
                Arc(90-3,200-12,15,20,-30,200,fill='blue',rotateAngle = -15),
                Arc(90+3,200-12,15,20,-200,240,fill='blue',rotateAngle = 15),
                Oval(90+0,200+20,8,10,fill='blue')),visible=False)
        
        self.box=Rect(90,60,35,35,border='magenta',fill=None,borderWidth=2)

        # [debug stuff]
        self.testingList = [self.style.movableHighlightColor]


    def makeBoardSprite(self):
        # Handy aliases.
        var = self.variant
        stl = self.style

        # Draw the outline.
        self.boardOutline = Rect( #:
            stl.xOffset - (stl.squareSizeHorizontal * stl.outlineProportion),
            stl.yOffset - (stl.squareSizeVertical * stl.outlineProportion),
            (var.cols * stl.squareSizeHorizontal) + (
                stl.squareSizeHorizontal * stl.outlineProportion * 2
            ),
            (var.rows * stl.squareSizeVertical) + (
                stl.squareSizeVertical * stl.outlineProportion * 2
            ),
            fill = stl.outlineColor,
        )

        # Draw the squares.
        self.boardSquares = Group()
        self.boardSquaresList=[[None for i in range(8)] for i in range(8)]
        for row in range(var.rows):
            for col in range(var.cols):
                # Determine the correct color for the square.
                if (col + row + (stl.kingSide == "default")) % 2 == 0:
                    squareColor = stl.lightSquareColor
                else:
                    squareColor = stl.darkSquareColor
                # Add the square to the group.
                square=Rect( #:
                    (col * stl.squareSizeHorizontal) + stl.xOffset,
                    (row * stl.squareSizeVertical) + stl.yOffset,
                    stl.squareSizeHorizontal, stl.squareSizeVertical,
                    fill = squareColor
                )
                square.ogFill=squareColor
                self.boardSquares.add(square)
                self.boardSquaresList[row][col-8] = square

        # Put the outline and the squares together in a group.
        self.boardSprite = Group( #:
            self.boardOutline,
            self.boardSquares,
        )


    def getGameFromPGN(self, PGN):

        # If the passed PGN is a string, then convert it to a PGNHandler object.
        if type(PGN) is str:
            PGN = PGNHandler(PGN)

        boardList = []

        # Convert from strings to Piece objects, and store the results in 
        # boardList.
        for rowNum, rowList in enumerate(PGN.FEN.position):
            boardRow = []
            for colNum, character in enumerate(rowList):
                boardRow.append(self.stringsToPieces[character.upper()](
                    character.islower() if character.isalpha() else None,
                    colNum + 1, rowNum + 1,
                ))
            boardList.append(boardRow)

        # Get the current side.
        currentSide = PGN.FEN.activeColor == "w"

        # Make a boardState object.
        boardState = ChessBoard(boardList, currentSide)
        moveList = []

        # Parse the move strings and store the result in the moveList.
        for moveString in PGN.moveStrings:
            move = ChessMove(moveString, boardState)
            move.apply(boardState)

        return boardState, moveList


    def squareToString(self, square, row=None):
        col, row = self.unpackArgs(square, row)
        return chr(col + 96) + str(row)

    def stringToSquare(self, string, row=None):
        col, row = self.unpackArgs(string, row)
        if type(col) is str:
            if col.isdigit():
                col = int(col)
            else:
                col = ord(col) - 96
        if type(row) is str:
            row = int(row)
        return col, row

    def squareToCoord(self, square, row=None):
        col, row = self.stringToSquare(square, row)
        col -= 0.5
        row -= 0.5
        if ((
            self.style.playerSide == "white"
        ) + (
            self.style.kingSide == "default"
        )) % 2:
            col = self.variant.cols - col
        if self.style.playerSide == "white":
            row = self.variant.rows - row
        x = (col * self.style.squareSizeHorizontal) + self.style.xOffset
        y = (row * self.style.squareSizeVertical) + self.style.yOffset
        return x, y

    def coordToSquare(self, coord, y=None):
        x, y = self.unpackArgs(coord, y)
        col = (x - self.style.xOffset) / self.style.squareSizeHorizontal
        row = (y - self.style.yOffset) / self.style.squareSizeVertical
        if ((
            self.style.playerSide == "white"
        ) + (
            self.style.kingSide == "default"
        )) % 2:
            col = self.variant.cols - col
        if self.style.playerSide == "white":
            row = self.variant.rows - row
        return round(col + 0.5), round(row + 0.5)


    def restart(self):
        # Delete old variables to clear up memory.
        del self.boardState, self.moveList

        # Get new game state.
        self.boardState, self.moveList = self.getGameFromPGN(self.variant.PGN)
        for row in self.boardSquaresList:
            for square in row:
                square.fill=square.ogFill

        self.selected = None

        self.timeLeft=[20*60,20*60+.5]
        self.timeLabels=[Label("20:00",40,160,size=25,fill='red'),Label("20:00",40,240,size=25,fill='red'),]
        self.timeLabels[0].toBack()
        self.timeLabels[1].toBack()
        
        self.box=Rect(90,60,35,35,border='magenta',fill=None,borderWidth=2)
        

    def render(self):
        for rowList in self.boardState:
            for piece in rowList:
                piece.render(self.style, self.squareToCoord(piece.col, piece.row))
    #}

    def save(self, *thingsToSave):
        if not thingsToSave:
            thingsToSave = ("boardState", "kings", "selected")
        savedVarNames = {
            "boardState": "savedBoardState",
            "kings": "savedKings",
            "selected": "savedSelected",
        }
        for thingToSave in thingsToSave:
            saveCopy = getattr(self, thingToSave)
            setattr(self, savedVarNames[thingToSave], saveCopy.copy())

    def restore(self, *thingsToSave):
        if not thingsToSave:
            thingsToSave = ("boardState", "kings", "selected")
        savedVarNames = {
            "boardState": "savedBoardState",
            "kings": "savedKings",
            "selected": "savedSelected",
        }
        for thingToSave in thingsToSave:
            saveCopy = getattr(self, savedVarNames[thingToSave])
            setattr(self, thingToSave, saveCopy.copy())


    def switch(self, pieceRow, pieceCol, targetRow, targetCol):
        (
            self.boardState[pieceRow][pieceCol],
            self.boardState[targetRow][targetCol]
        ) = (
            self.boardState[targetRow][targetCol],
            self.boardState[pieceRow][pieceCol]
        )
        self.boardState[pieceRow][pieceCol].moveTo(pieceRow, pieceCol)
        self.boardState[targetRow][targetCol].moveTo(targetCol, targetRow)


    def attackSwitch(self, pieceRow, pieceCol, targetRow, targetCol):
        # Set the attacked square to be an EmptyPiece.
        self.boardState[targetRow][targetCol] = EmptyPiece(
            None, targetCol, targetRow,
        )#  side,    col,       row
        self.switch(pieceRow, pieceCol, targetRow, targetCol)

    def checkmatePredicate(self, argument):
        self.save("boardState", "kings")
        col, row = self.kings[self.defendingSide]
        self.attackSwitch(argument[-1].row, argument[-1].col, row, col)
        if not self.checkChecks(self.defendingSide):# 2nd use of side 
            self.restore("boardState", "kings")
            # return False
        self.restore("boardState", "kings")


    def inCheckMate(self, side, squares):

            ### temp fixes
            self.defendingSide=side
            ###
            self.save("boardState", "kings")

            col, row=self.kings[side]

            directions=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
            for j in range(8):

                row2=row
                col2=col
                col2+=directions[j][0]
                row2+=directions[j][1]
                if col2 in (0,9) or row2 in (0,9):
                    continue

                if (self.boardState[row2][col2].pieceType == "empty" or 
                    self.boardState[row2][col2].side != side
                ):
                    print(self.boardState[row2][col2])

                    self.attackSwitch(row, col, row2, col2)

                    # records where the king is 
                    (
                        self.kings[side][0],
                        self.kings[side][1],
                    ) = (col2, row2)

                    if self.checkChecks(side):
                        # checkmate is posible
                        self.restore("boardState", "kings")
                    else: 
                        # the king could get out 
                        self.restore("boardState", "kings")
                        return False

            if len(squares)>=2:
                self.restore("boardState", "kings")
                return True

            ### see if a piece can move into (checking piece and squares between) from the square
            if self.checkChecks(side,predicate=self.checkmatePredicate)==(False,3):
                return False

            print(squares)
            squares=list(squares.values())[0]

            for col, row in squares:

                ### my code\/

                # pawns moving forward to block
                newRow=row
                for i in range(2):
                    newRow+=(side*2-1)
                    if ('f' in self.boardState[newRow][col].moves and 
                        self.boardState[newRow][col].side!=side and
                        self.boardState[row][col].pieceType=="empty" 
                    ):

                        # if i==0 or not self.boardState[blockerPieceRow][col].moved:

                            # self.switch(blockerPieceRow, col, row, col)

                            # if not self.checkChecks(side):
                                # self.restore("boardState", "kings")
                                # return False,3
                        # self.restore("boardState", "kings")

                    # if self.boardState[blockerPieceRow][col].pieceType!="empty":
                        # break


                        # # sets the attacked piece to blank
                        # self.boardState[row2][col2]=EmptyPiece(not self.boardState.currentSide,col2,row2)

                        # switches the moving piece and blank piece
                        self.switch(newRow, col, row, col)

                        if not self.checkChecks(side):
                            self.restore("boardState", "kings")
                            return False
                        else:
                            self.restore("boardState", "kings")

                # check for en passant
                if self.boardState[row][col].pieceType == "pawn":
                    if self.boardState[row][col].doubled:
                        for newCol in (-1,1):
                            newCOl+=col
                            if (self.boardState[row][newCol].pieceType == "pawn" and 
                                self.boardState[newRow][col].side!=side
                            ):

                                self.attackSwitch(row, newCol, row, col)

                                if not self.checkChecks(side):
                                    self.restore("boardState", "kings")
                                    return False
                                else:
                                    self.restore("boardState", "kings")

            self.restore("boardState", "kings")
            return True 

    def checkChecks(self, side, *squares, #:
            returnCheckingPieces=False,
            returnPassedSquares=False,
            predicate = None,
    ):
        sentinal = object()
        if predicate == None:
            predicate = (lambda checkingPieces:
                sentinal if checkingPieces else None
            )

        if returnCheckingPieces:
            oldPredicate = predicate
            predicate = (lambda checkingPieces:
                None if ((p := oldPredicate(checkingPieces)) is sentinal) else p
            )

        if not squares:
            squares = (self.kings[side],)

        if returnPassedSquares:
            checkingPieces = {}
        else:
            checkingPieces = []
        print(squares)
        for col, row in squares:

            # "Raycasting" movement types.
            raycasts = ( #:
                #("movementType", limit, ((raycast offsets)...), movement type permissions)
                ("D", ((+1, +1), (-1, +1), (+1, -1), (-1, -1))),
                ("H", ((+1, +0), (-1, -0), (+0, +1), (-0, -1))),
            )
            for movementType, raycastDirections in raycasts:
                for colChange, rowChange in raycastDirections:
                    scannerCol, scannerRow = col + colChange, row + rowChange
                    scannedSquares = []
                    while scannerCol in self.colNums and scannerRow in self.rowNums:
                        scannedSquares.append((scannerCol, scannerRow))
                        # print([scannerRow],[scannerCol])
                        scannedPiece = self.boardState[scannerRow][scannerCol]
                        if scannedPiece.pieceType != "empty":
                            if (
                                scannedPiece.side != side
                                and movementType in scannedPiece.moves
                            ):
                                if returnPassedSquares:
                                    checkingPieces[scannedPiece] = scannedSquares
                                else:
                                    checkingPieces.append(scannedPiece)
                                ret = predicate(checkingPieces)
                                if ret is not None and ret is not sentinal:
                                    return ret
                            break
                        scannerCol += colChange
                        scannerRow += rowChange

            # "Translating" movement types.
            translations = ( #:
                # Horizontal movement.
                ("d", (
                    (-1, +1 if side else -1),
                    (+1, +1 if side else -1),
                )),
                # Diagonal movement.
                ("L", (
                    (-2, +1),
                    (-1, +2),
                    (+1, +2),
                    (+2, +1),
                    (+2, -1),
                    (+1, -2),
                    (-1, -2),
                    (-2, -1),
                )),
            )
            for movementType, translation in translations:
                for colChange, rowChange in translation:
                    scannerCol, scannerRow = col + colChange, row + rowChange
                    scannedSquares = []
                    if scannerCol in self.colNums and scannerRow in self.rowNums:
                        scannedSquares.append((scannerCol, scannerRow))
                        scannedPiece = self.boardState[scannerRow][scannerCol]
                        if scannedPiece.pieceType != "empty":
                            if (
                                scannedPiece.side != side
                                and movementType in scannedPiece.moves
                            ):
                                if returnPassedSquares:
                                    checkingPieces[scannedPiece] = scannedSquares
                                else:
                                    checkingPieces.append(scannedPiece)
                                ret = predicate(checkingPieces)
                                if ret is not None and ret is not sentinal:
                                    return ret

        return checkingPieces


    def noMove(self, side):
        originalSide = self.boardState.currentSide
        self.boardState.currentSide = side
        for row in self.boardState:
            for piece in row:
                if piece.side == side:
                    self.selected = None
                    self.onMousePress(*self.squareToCoord(piece.col, piece.row))
                    for row in self.boardSquaresList:
                        for square in row:
                            square.fill=square.ogFill
                    if self.moveableSquares > 0:
                        self.boardState.currentSide = originalSide
                        return True
        return False


    def highlight(self, highlightType, *squares):
        if highlightType == "movable":
            highlightColor = self.style.movableHighlightColor
            self.moveableSquares += 1
        elif highlightType == "immovable":
            highlightColor = self.style.immovableHighlightColor
            self.moveableSquares -= 1
        elif highlightType == "checking":
            highlightColor = self.style.checkingHighlightColor
        elif highlightType == "checked":
            highlightColor = self.style.checkedHighlightColor
        else:
            highlightColor = highlightType
        for square in squares:
            if isinstance(square, Piece):
                col, row = square.col, square.row
            else:
                col, row = square
            self.boardSquaresList[8-row][col-1].fill = highlightColor


    def getMoves(self, piece):
        movableSquares = []

        if piece.side == self.boardState.currentSide:

            # Pawn direction.
            pD = +1 if piece.side else -1

            # Movement permissions.
            allPerms = (True, True)
            moveOnly = (False, True)
            capOnly = (True, False)

            # "Raycasting" movement types.
            raycastMoves = ( #:
                #("movementType", limit, ((raycast offsets)...), movement type permissions)
                ("D", 0, ((+1, +1), (-1, +1), (+1, -1), (-1, -1)), allPerms),
                ("H", 0, ((+1, +0), (-1, -0), (+0, +1), (-0, -1)), allPerms),
                ("f", 1 if piece.moved else 2, ((+0, pD)), moveOnly),
                ("d", 1, ((-1, pD), (+1, pD)), capOnly),
            )
            for movementType, movementLimit, raycastDirections, (canCap, canMove) in raycasts:
                for colChange, rowChange in raycastDirections:
                    raycastCol, raycastRow = piece.col + colChange, piece.row + rowChange
                    nSquares = 1
                    while (raycastCol in self.colNums and raycastRow in self.rowNums) and nSquares != limit:
                        if scannedPiece.pieceType == "empty":
                            if canMove:
                                movableSquares.append((raycastCol, raycastRow))
                            else:
                                break
                        elif scannedPiece.side != side:
                            if canCap:
                                movableSquares.append((raycastCol, raycastRow))
                            else:
                                break
                        else:
                            break
                        raycastCol += colChange
                        raycastRow += rowChange
                        nSquares += 1



            # moving like a knight            
            if "L" in moves:
                directions=[(2,1),(2,-1),(1,2),(-1,2),(-1,-2),(1,-2),(-2,1),(-2,-1)]
                for j in range(8):
                    row2=row
                    col2=col
                    col2+=directions[j][0]
                    row2+=directions[j][1]
                    if col2 in (-1,0,9,10) or row2 in (-1,0,9,10):
                        continue
                    if ((self.boardState[row2][col2].pieceType == "empty") or 
                        self.boardState[row2][col2].side != self.boardState.currentSide
                    ):
                        self.highlight("movable", (col2, row2))

            # moving like a king      
            if "A" in moves:
                directions=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
                for j in range(8):

                    row2=row+directions[j][0]
                    col2=col+directions[j][1]
                    if col2 in (0,9) or row2 in (0,9):
                        continue
                    if (self.boardState[row2][col2].pieceType == "empty" or 
                        self.boardState[row2][col2].side != self.boardState.currentSide
                    ):
                        self.highlight("movable", (col2, row2))

            # castling
            if "C" in moves:
                squares=((2,3,4),(7,6))

                # can't castle if in check 
                if not self.selected.moved and not self.checkChecks(self.boardState.currentSide):
                    for direction in range(2):

                        rook=self.boardState[self.selected.row][direction*7+1]
                        # the the rook hasnt moved
                        if rook.pieceType == 'rook' and not rook.moved:
                            checked=False
                            self.save("boardState", "kings")

                            # check if the squares passed through would cause a check
                            for col2 in squares[direction]:
                                if self.boardState[self.selected.row][col2].pieceType!='empty':
                                    break
                                else:
                                    # switch the pieces
                                    self.switch(self.selected.row, self.selected.col, self.selected.row, col2)

                                    (
                                        self.kings[self.boardState.currentSide][0],
                                        self.kings[self.boardState.currentSide][1],
                                    ) = (self.selected.col, self.selected.row)

                                    # cant castle if any square that the king move is in check
                                    if self.checkChecks(self.boardState.currentSide):
                                        # cancel the castling
                                        checked = True
                                        break
                                    self.restore("boardState", "kings")
                            else:
                                castlingMovement=(direction*4-2)
                                self.highlight("movable", (self.selected.col+castlingMovement, self.selected.row))
                                self.boardSquaresList[8-(self.selected.row)][self.selected.col+castlingMovement-1].castlingCol=direction*7+1
                            if checked:
                                castlingMovement=(direction*4-2)
                                self.highlight("immovable", (self.selected.col+castlingMovement, self.selected.row))

            if 'e' in moves:
                directions=[(-1,0),(1,0)]
                for j in range(2):

                    row2=row
                    col2=col
                    col2+=directions[j][0]
                    row2+=directions[j][1]
                    if col2 in (0,9)or row2 in (0,9):
                        continue
                    target=self.boardState[row2][col2]


                    if target.pieceType == "pawn" and target.doubled:
                        row2+=piece.side*2-1
                        self.highlight("movable", (col2, row2))
                        self.boardSquaresList[8-(row2)][col2-1].croissant=True


            ###### chage self.kings for each move 
            self.save("boardState", "kings", "selected")
            for row2 in self.rowNums:
                for col2 in self.colNums:

                    # finds all the highlighted squares where the piece can move
                    if self.boardSquaresList[8-(row2)][col2-1].fill == self.style.movableHighlightColor:

                        self.attackSwitch(
                            self.selected.row, self.selected.col,
                            row2, col2
                        )

                        # if the moving pice is a king record where he moved to 
                        if self.selected.pieceType == "king":
                            (
                                self.kings[self.boardState.currentSide][0],
                                self.kings[self.boardState.currentSide][1],
                            ) = (col2, row2)

                        # If moving to the highlighted square would cause a check dont let the user move there
                        if self.checkChecks(self.boardState.currentSide):
                            self.highlight("immovable", (col2, row2))

                        self.restore("boardState", "kings")

                    self.restore("selected")

            self.restore("boardState", "kings", "selected")

        return movableSquares


    def onMousePress(self, x, y):
        if self.selected==None:
            self.moveableSquares=0
            col, row = self.coordToSquare(x, y)
            if not (col in self.colNums and row in self.rowNums):
                return None
            piece = self.boardState[row][col]
            if piece.side == self.boardState.currentSide:
                self.selected = piece
                moves=piece.moves
                #D for diagonal
                #H for horizontal/vertical
                #L for knights
                #A for adjacent
                # C for castling 
                # f for forward
                # d for 1 diagonal/pawn
                # e 4 en passant

                # if the piece can move diagional ex:bishop 
                if "D" in moves:
                    directions=[(1,1),(-1,1),(1,-1),(-1,-1)]

                    for j in range(4):
                        desesected=False
                        row2=row
                        col2=col
                        for i in range(8):
                            if desesected:
                                if self.boardState[row2][col2].pieceType == "empty":
                                    self.highlight("movable", (col2, row2))
                                else:
                                    if self.boardState[row2][col2].side != self.boardState.currentSide:
                                        self.highlight("movable", (col2, row2))
                                    break
                                col2+=directions[j][0]
                                row2+=directions[j][1]
                                if col2 in (0,9)or row2 in (0,9):
                                    break
                            else:
                                desesected=True
                                col2+=directions[j][0]
                                row2+=directions[j][1]
                                if col2 in (0,9) or row2 in (0,9):
                                    break

                # moving horizontal like a rook
                if "H" in moves:
                    directions=[(1,0),(-1,0),(0,1),(0,-1)]

                    for j in range(4):
                        desesected=False

                        row2=row
                        col2=col

                        for i in range(8):
                            if desesected:
                                ######### if its an enemy piece; break
                                if self.boardState[row2][col2].pieceType == "empty":
                                    self.highlight("movable", (col2, row2))
                                else:
                                    if self.boardState[row2][col2].side != self.boardState.currentSide:
                                        self.highlight("movable", (col2, row2))
                                    break
                            else:
                                desesected=True
                            col2+=directions[j][0]
                            row2+=directions[j][1]
                            if col2 in (0,9)or row2 in (0,9):
                                break

                # moving like a knight            
                if "L" in moves:
                    directions=[(2,1),(2,-1),(1,2),(-1,2),(-1,-2),(1,-2),(-2,1),(-2,-1)]
                    for j in range(8):
                        row2=row
                        col2=col
                        col2+=directions[j][0]
                        row2+=directions[j][1]
                        if col2 in (-1,0,9,10) or row2 in (-1,0,9,10):
                            continue
                        if ((self.boardState[row2][col2].pieceType == "empty") or 
                            self.boardState[row2][col2].side != self.boardState.currentSide
                        ):
                            self.highlight("movable", (col2, row2))

                # moving like a king      
                if "A" in moves:
                    directions=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
                    for j in range(8):

                        row2=row
                        col2=col
                        col2+=directions[j][0]
                        row2+=directions[j][1]
                        if col2 in (0,9) or row2 in (0,9):
                            continue
                        if (self.boardState[row2][col2].pieceType == "empty" or 
                            self.boardState[row2][col2].side != self.boardState.currentSide
                        ):
                            self.highlight("movable", (col2, row2))

                # castling
                if "C" in moves:
                    squares=((2,3,4),(7,6))

                    # can't castle if in check 
                    if not self.selected.moved and not self.checkChecks(self.boardState.currentSide):
                        for direction in range(2):

                            rook=self.boardState[self.selected.row][direction*7+1]
                            # the the rook hasnt moved
                            if rook.pieceType == 'rook' and not rook.moved:
                                checked=False
                                self.save("boardState", "kings")

                                # check if the squares passed through would cause a check
                                for col2 in squares[direction]:
                                    if self.boardState[self.selected.row][col2].pieceType!='empty':
                                        break
                                    else:
                                        # switch the pieces
                                        self.switch(self.selected.row, self.selected.col, self.selected.row, col2)

                                        (
                                            self.kings[self.boardState.currentSide][0],
                                            self.kings[self.boardState.currentSide][1],
                                        ) = (self.selected.col, self.selected.row)

                                        # cant castle if any square that the king move is in check
                                        if self.checkChecks(self.boardState.currentSide):
                                            # cancel the castling
                                            checked = True
                                            break
                                        self.restore("boardState", "kings")
                                else:
                                    castlingMovement=(direction*4-2)
                                    self.highlight("movable", (self.selected.col+castlingMovement, self.selected.row))
                                    self.boardSquaresList[8-(self.selected.row)][self.selected.col+castlingMovement-1].castlingCol=direction*7+1
                                if checked:
                                    castlingMovement=(direction*4-2)
                                    self.highlight("immovable", (self.selected.col+castlingMovement, self.selected.row))
                if 'f' in moves:
                    row2=row+(piece.side*2-1)
                    col2=col
                    if (col2 in self.colNums and row2 in self.rowNums) and (
                        self.boardState[row2][col2].pieceType == "empty"
                    ):
                        self.highlight("movable", (col2, row2))
                    if not piece.moved:
                        row2+=(piece.side*2-1)

                        if (col2 in self.colNums and row2 in self.rowNums) and (
                           self.boardState[row2][col2].pieceType == "empty"
                        ):
                            self.boardSquaresList[8-(row2)][col2-1].doubled=True
                            self.highlight("movable", (col2, row2))

                if 'd' in moves:

                    directions=[(-1,piece.side*2-1),(1,piece.side*2-1)]
                    for j in range(2):

                        row2=row
                        col2=col
                        col2+=directions[j][0]
                        row2+=directions[j][1]

                        if col2 in (0,9)or row2 in (0,9):
                            continue

                        if (type(self.boardState[row2][col2]) !=EmptyPiece and 
                            self.boardState[row2][col2].side != self.boardState.currentSide
                        ):
                            self.highlight("movable", (col2, row2))
                if 'e' in moves:
                    directions=[(-1,0),(1,0)]
                    for j in range(2):

                        row2=row
                        col2=col
                        col2+=directions[j][0]
                        row2+=directions[j][1]
                        if col2 in (0,9)or row2 in (0,9):
                            continue
                        target=self.boardState[row2][col2]


                        if target.pieceType == "pawn" and target.doubled:
                            row2+=piece.side*2-1
                            self.highlight("movable", (col2, row2))
                            self.boardSquaresList[8-(row2)][col2-1].croissant=True


                ###### chage self.kings for each move 
                # i can try my version to save
                self.save("boardState", "kings", "selected")
                for row2 in self.rowNums:
                    for col2 in self.colNums:

                        # finds all the highlighted squares where the piece can move

                        if self.boardSquaresList[8-(row2)][col2-1].fill == self.style.movableHighlightColor:

                            self.attackSwitch(
                                self.selected.row, self.selected.col,
                                row2, col2
                            )

                            # if the moving pice is a king record where he moved to 
                            if self.selected.pieceType == "king":
                                (
                                    self.kings[self.boardState.currentSide][0],
                                    self.kings[self.boardState.currentSide][1],
                                ) = (col2, row2)

                            # If moving to the highlighted square would cause a check dont let the user move there
                            if self.checkChecks(self.boardState.currentSide):
                                self.highlight("immovable", (col2, row2))

                            self.restore("boardState", "kings")

                        self.restore("selected")

                self.restore("boardState", "kings", "selected")

        else: # If self.selected is not None.

            # if the piece is going to be promoted
            if self.promo:
                # depending on where the player clicks the new piece will be selected
                if x in range(30,85+30):

                    self.boardState[self.selected.row][self.selected.col]=Queen(self.selected.side,self.selected.col,self.selected.row)
                    self.selected.sprite.visible=False
                    # self.selected.moveTo(0,400)
                    self.selectionMenu.visible=False

                    self.boardState[self.selected.row][self.selected.col].render(self.style,self.squareToCoord(self.selected.col,self.selected.row))
                    self.selected=None
                    self.promo=False
                elif x in range(115,115+85):

                    self.boardState[self.selected.row][self.selected.col]=Rook(self.selected.side,self.selected.col,self.selected.row)
                    self.selected.sprite.visible=False
                    # self.selected.moveTo(0,400)
                    self.selectionMenu.visible=False

                    self.boardState[self.selected.row][self.selected.col].render(self.style,self.squareToCoord(self.selected.col,self.selected.row))
                    self.selected=None
                    self.promo=False
                elif x in range(200,200+85):

                    self.boardState[self.selected.row][self.selected.col]=Bishop(self.selected.side,self.selected.col,self.selected.row)
                    self.selected.sprite.visible=False
                    # self.selected.moveTo(0,400)
                    self.selectionMenu.visible=False

                    self.boardState[self.selected.row][self.selected.col].render(self.style,self.squareToCoord(self.selected.col,self.selected.row))
                    self.selected=None
                    self.promo=False
                elif x in range(285,285+85):

                    self.boardState[self.selected.row][self.selected.col]=Knight(self.selected.side,self.selected.col,self.selected.row)
                    self.selected.sprite.visible=False
                    # self.selected.moveTo(0,400)
                    self.selectionMenu.visible=False

                    self.boardState[self.selected.row][self.selected.col].render(self.style,self.squareToCoord(self.selected.col,self.selected.row))
                    self.selected=None
                    self.promo=False

            # otherwise move the piece to where the user clicked
            else:
                col, row = self.coordToSquare(x, y) 
                self.promo=False
                if col in self.colNums and row in self.rowNums:
                    if self.boardSquaresList[8-(row)][col-1].fill in self.testingList:

                        # if the square is 2 units away then mark that the pawn moved twice
                        try:
                            if self.boardSquaresList[8-(row)][col-1].doubled:
                                self.selected.doubled=True
                        except:
                            pass

                        # if the square is used for an en passant remove the piece behind it
                        try:
                            if self.boardSquaresList[8-(row)][col-1].croissant:

                                self.boardState[row+self.selected.side*-2+1][col].moveSprite(0,0)
                                self.boardState[row+self.selected.side*-2+1][col]=EmptyPiece(False,col,row+self.selected.side*-2+1)
                        except:
                            pass

                        # marks that the piece moved for doubling and castling
                        self.selected.moved=True
                        
                        # adds the selected piece back into the 2d list becuase it was unlinked by coping
                        self.boardState[self.selected.row][self.selected.col]=self.selected

                        # moves the captured sprite to the corner
                        self.boardState[row][col].moveSprite(0,0)

                        self.attackSwitch(
                            self.selected.row, self.selected.col,
                            row, col
                        )

                        # moves the selected sprite to were it was moved to
                        self.selected.moveSprite(self.squareToCoord(self.coordToSquare(x,y)))

                        # if the piece is a pawn and can be promoted; promote it
                        if (
                            self.selected.pieceType == "pawn"
                        ) and (row == (1,8)[self.boardState.currentSide]):
                            self.promo=True

                        # if its a king record where it is, and if the move is castling that move the rook too
                        elif self.selected.pieceType=='king':
                            (
                                self.kings[self.boardState.currentSide][0],
                                self.kings[self.boardState.currentSide][1],
                            ) = (col, row)

                            try:
                                castlingCol=self.boardSquaresList[8-(row)][col-1].castlingCol

                                col2=col+((castlingCol-1)//7)*-2+1

                                self.boardState[self.selected.row][castlingCol].moveSprite(self.squareToCoord(col2,row))
                                self.boardState.swapPieces(
                                    castlingCol, self.selected.row,
                                    col2, row)
                            except:
                                print('failed castling')

                        # switch the turns
                        self.boardState.currentSide = not self.boardState.currentSide

                        # print(self.noMove(True))


                # recolors the squares
                for row in self.boardSquaresList:
                    for square in row:
                        square.fill=square.ogFill
                        try:
                            square.doubled=False
                        except:
                            pass

                # if a piece isnt promoted:
                if not self.promo:
                    # deslects the piece
                    self.selected=None
                else:
                    ## show sprites to select promo
                    self.selectionMenu.visible=True
                    self.selectionMenu.toFront()

                # sets the enemy pawns double to false
                for row in self.boardState:
                    for piece in row:
                        if type(piece)==Pawn and piece.side == self.boardState.currentSide:
                            piece.doubled=False

            # highlight the squares when a piece is moved or deselected
            inCheck = self.checkChecks(self.boardState.currentSide)

            if inCheck:
                self.highlight(
                    "checking",
                    *self.checkChecks(
                        self.boardState.currentSide,
                        returnCheckingPieces=True,
                    )
                )
                self.highlight(
                    "checked",
                    self.kings[self.boardState.currentSide]
                )
                # checks if the games is in checkmate
                mate = self.inCheckMate(
                    self.boardState.currentSide,

                    # dictionary of passed through squares
                    self.checkChecks(
                        self.boardState.currentSide,
                        returnCheckingPieces=True,
                        returnPassedSquares=True,
                    )
                )
                if mate:
                    sleep(2)
                    side='White'
                    if self.boardState.currentSide:
                        side='Black'
                    app.world.pauseMenu.label.value=f"{side} Won"
                    app.world.pauseMenu.visible = True


    def onStep(self):

        self.timeLabels[self.boardState.currentSide].value = "{}:{}".format(
            str(int(
                self.timeLeft[self.boardState.currentSide] // 60
            )).rjust(2,'0'),
            str(math.ceil(
                self.timeLeft[self.boardState.currentSide] % 60
            ) - 1).rjust(2,'0'),
        )
        self.timeLeft[int(self.boardState.currentSide)] -=1/30
        if self.timeLeft[self.boardState.currentSide] <= 0:
            side='Black'
            if self.boardState.currentSide:
                side='White'
            app.world.pauseMenu.label.value=f"{side} Lost"
            app.world.pauseMenu.visible = True


    def onKeyPress(self,key):
        if key == "e":
            # e for export
            # stringsToPieces
            exportStr=''
            for row in self.boardState:
                for piece in row:
                    letter=self.piecesToStrings[type(piece)]
                    if piece.side:
                        letter=letter.upper()
                    else:
                        letter=letter.lower()
                    
                    exportStr+=letter
            app.getTextInput(
                f"copy the text between the quotes, it's your save; \"{exportStr}\""
            )
        if key =='i':
            self.restart() # reset everything so that it starts fresh
            row,col=1,1
            for char in app.getTextInput("paste your save"):
                piece=self.stringsToPieces[char.upper()](char.isupper(),col,row)
                self.boardState[row][col]=piece
                col+=1
                if col == 9:
                    col=1
                    row+=1
        if key in ("up", 'w'):
            self.box.centerY-=self.style.squareSizeVertical
        if key in ("down",'s'):
            self.box.centerY+=self.style.squareSizeVertical
        if key in ("left",'a'):
            self.box.centerX-=self.style.squareSizeHorizontal
        if key in ("right",'d'):
            self.box.centerX+=self.style.squareSizeHorizontal
        if key == "space":
            self.onMousePress(self.box.centerX, self.box.centerY)
        if key == "s":
            while True:
                inp = app.getTextInput("input squares, separated by a comma").split(",")
                try:
                    x, y = self.squareToCoord(self.stringToSquare(inp[0]))
                    self.onMousePress(x, y)
                    x, y = self.squareToCoord(self.stringToSquare(inp[1]))
                    self.onMousePress(x, y)
                    break
                except:
                    inp = app.getTextInput("input squares, separated by a comma").split(",")
        
        # if key=='s':
        #     for x,y in ((250,290),(250,217),(278,118),(280,185),(215,325),(312,215),(320,118),(314,180),(312,215)):#,(349,186)
        #         self.onMousePress(x,y)

#####
##### WORLD CLASS
#####   


class World:

    def __init__(self):
        self.rendered=False

        self.game = ChessGame()

        # Create the splash screen.
        self.splashScreen = SplashScreen()
        self.splashScreen.drawing.toFront()

        # Create the pause menu.
        self.pauseMenu = PauseMenu()

        # Show the splash screen when the app starts
        self.steps = 0
        self.splashScreenStepsToHide = 1 * app.stepsPerSecond


    def restart(self):
        # Clear all drawings
        app.group.clear()
        self.rendered=False
        # Restart the pause menu.
        self.pauseMenu.restart()

        # Restart the splash screen.
        self.splashScreen.restart()

        # Show the splash screen when the app starts
        self.steps = 0
        self.splashScreenStepsToHide = 1 * app.stepsPerSecond

        ### Add code here to create your interactive app
        self.game.restart()

    ##### EVENT PROCESSING #####
    ##### EVENT PROCESSING #####
    ##### EVENT PROCESSING #####
    ##### EVENT PROCESSING #####
    ##### EVENT PROCESSING #####
    def processOnStep(self):
        ### Add code here to respond to a step ###
        # Count total steps
        self.steps += 1

        # Check to see if it is time eto hide the splash screen
        if self.steps == self.splashScreenStepsToHide:
            self.splashScreen.visible = False
        if self.steps >= self.splashScreenStepsToHide:
            if not self.rendered:
                self.game.render()
                self.rendered=True

            self.game.onStep()
            self.game.boardSprite.visible=True
            # self.chessGame.boardG.visible=True

    def processOnMousePress(self, mouseX, mouseY):
        if (self.splashScreen.visible):
            # do not respond to events when splash screen is shown
            pass
        elif (self.pauseMenu.visible):
            # let pause screen handle this event
            self.pauseMenu.processOnMousePress(mouseX, mouseY, self)
        else:
            self.game.onMousePress(mouseX, mouseY)
            ### Add code here ###
            pass


    def processOnMouseRelease(self, mouseX, mouseY):
        if (self.splashScreen.visible):
            # do not respond to events when splash screen is shown
            pass
        else:
            ### Add code here ###
            pass


    def processOnMouseMove(self, mouseX, mouseY):
        if (self.splashScreen.visible):
            # do not respond to events when splash screen is shown
            pass
        else:
            ### Add code here ###
            pass


    def processOnMouseDrag(self, mouseX, mouseY):
        if (self.splashScreen.visible):
            # do not respond to events when splash screen is shown
            pass
        else:
            ### Add code here ###
            pass


    def processOnKeyPress(self, key):
        if (self.splashScreen.visible):
            # do not respond to events when splash screen is shown
            pass
        else:
            ### Add code here ###
            if (key == 'p'):
                # Toggle pause menu
                if (self.pauseMenu.visible):
                    # Pause menu is currently shown, so hide it
                    self.pauseMenu.visible = False
                else:
                    # Pause menu is currently hidden, so show it
                    self.pauseMenu.visible = True
                    self.pauseMenu.label.value="Paused"
            self.game.onKeyPress(key)


    def processOnKeyRelease(self, key):
        if (self.splashScreen.visible):
            # do not respond to events when splash screen is shown
            pass
        else:
            ### Add code here ###
            pass


    def processOnKeyHold(self, key):
        if (self.splashScreen.visible):
            # do not respond to events when splash screen is shown
            pass
        else:
            ### Add code here ###
            pass


### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
### DO NOT ADD OR MODIFY ANY CODE BELOW HERE  
### OKAY,  I WONT MODIFY ANY CODE BELOW HERE

#####
##### MAIN FUNCTION
#####
### Our main function just kickstarts the app and nothing else
def main():
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    # Create the world
    app.world = World()

main()


#####
##### EVENTS
#####
def onMousePress(mouseX, mouseY):
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnMousePress(mouseX, mouseY)


def onMouseRelease(mouseX, mouseY):
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnMouseRelease(mouseX, mouseY)


def onMouseMove(mouseX, mouseY):
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnMouseMove(mouseX, mouseY)


def onMouseDrag(mouseX, mouseY):
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnMouseDrag(mouseX, mouseY)


def onKeyPress(key):
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnKeyPress(key)


def onKeyRelease(key):
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnKeyRelease(key)


def onKeyHold(keys):
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnKeyHold(keys)


def onStep():
    ### DO NOT ADD OR MODIFY ANY CODE BELOW HERE
    app.world.processOnStep()

