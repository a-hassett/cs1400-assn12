# Alexandra Hassett, CS 1400

import random


class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return self.__x, self.__y

    def x(self):
        return self.__x

    def y(self):
        return self.__y

###################################################################################################################


class Pawn(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def location(self):
        return super().location()

    # prints picture of a pawn
    def pic(self):
        if super().color() == "w":
            return "\u2659"
        if super().color() == "b":
            return "\u265f"

    # pawns can move down one space if white and up one space if black
    def validMove(self, x, y):
        if super().color() == "w" and super().x() == x and super().y() == y + 1:
            return True
        elif super().color() == "b" and super().x() == x and super().y() == y - 1:
            return True
        else:
            return False


class Queen(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def location(self):
        return super().location()

    # prints picture of a queen
    def pic(self):
        if super().color() == "w":
            return "\u2655"
        if super().color() == "b":
            return "\u265b"

    # queens can move diagonally or horizontally in any direction
    def validMove(self, x, y):
        if abs(super().x() - x) == abs(super().y() - y):
            return True
        elif super().x() == x:
            return True
        elif super().y() == y:
            return True
        else:
            return False


class King(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def location(self):
        return super().location()

    # prints picture of a king
    def pic(self):
        if super().color() == "w":
            return "\u2654"
        if super().color() == "b":
            return "\u265a"

    # kings can move one square horizontally or diagonally in any direction
    def validMove(self, x, y):
        if abs(super().x() - x) < 2 and abs(super().y() - y) < 2:
            return True
        else:
            return False


class Rook(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def location(self):
        return super().location()

    # prints picture of a rook
    def pic(self):
        if super().color() == "w":
            return "\u2656"
        if super().color() == "b":
            return "\u265c"

    # rooks can move horizontally or vertically
    def validMove(self, x, y):
        if super().x() == x or super().y() == y:
            return True
        else:
            return False


class Knight(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def location(self):
        return super().location()

    # prints picture of a knight
    def pic(self):
        if super().color() == "w":
            return "\u2658"
        if super().color() == "b":
            return "\u265e"

    # knights can move to a space that is one square vertical, two squares horizontal or vice versa
    def validMove(self, x, y):
        if abs(super().x() - x) == 1 and abs(super().y() - y) == 2:
            return True
        elif abs(super().x() - x) == 2 and abs(super().y() - y) == 1:
            return True
        else:
            return False


class Bishop(ChessPiece):
    def __init__(self, c, x, y):
        super().__init__(c, x, y)

    def location(self):
        return super().location()

    # prints picture of a bishop
    def pic(self):
        if super().color() == "w":
            return "\u2657"
        if super().color() == "b":
            return "\u265d"

    # bishops can move diagonally
    def validMove(self, x, y):
        if abs(super().x() - x) == abs(super().y() - y):
            return True
        else:
            return False

###################################################################################################################


def printValidMoves(cp):
    # prints the chess board and piece, showing its valid moves
    print("\t", cp.pic(), "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(8):
            if cp.x() == j and cp.y() == i:
                print(cp.pic(), "", end=" ")
            elif cp.validMove(j, i):
                print("* ", end=" ")
            else:
                print(". ", end=" ")
        print()
    print("\t  ", end="")
    for i in range(8):
        print(str(i) + " ", end=" ")
    print()
    print()


def randomChessPiece():
    # randomizes the color, location, and type of the piece
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1:
        return Pawn(c, x, y)
    if t == 2:
        return Queen(c, x, y)
    if t == 3:
        return King(c, x, y)
    if t == 4:
        return Rook(c, x, y)
    if t == 5:
        return Knight(c, x, y)
    else:
        return Bishop(c, x, y)


def main():
    # prints valid moves for 10 different chess pieces randomly created by the randomChessPiece function
    clist = []

    for i in range(10):
        clist.append(randomChessPiece())

    for i in range(len(clist)):
        printValidMoves(clist[i])


main()
