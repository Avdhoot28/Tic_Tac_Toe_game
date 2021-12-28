import random
import copy
i = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]

def board(i):
    print("\t\t\t\t\t", "  For reference ")
    print()
    print(" ", i[0][0], " | ", i[0][1], " | ", i[0][2], "\t\t\t", " ", "1", " | ", "2", " | ", "3")
    print("-", "-", "-", "-", "-", "-", "-", "-", "-", "\t\t\t", "-", "-", "-", "-", "-", "-", "-", "-", "-")
    print(" ", i[1][0], " | ", i[1][1], " | ", i[1][2], "\t\t\t", " ", "4", " | ", "5", " | ", "6")
    print("-", "-", "-", "-", "-", "-", "-", "-", "-", "\t\t\t", "-", "-", "-", "-", "-", "-", "-", "-", "-")
    print(" ", i[2][0], " | ", i[2][1], " | ", i[2][2], "\t\t\t", " ", "7", " | ", "8", " | ", "9")
    print()

    if((i[0][0] == "X" and i[0][1] == "X" and i[0][2] == "X") or (i[1][0] == "X" and i[1][1] == "X" and i[1][2] == "X") or (i[2][0] == "X" and i[2][1] == "X" and i[2][2] == "X")):
        print("X won!")
        return True
    if((i[0][0] == "X" and i[1][0] == "X" and i[2][0] == "X") or (i[0][1] == "X" and i[1][1] == "X" and i[2][1] == "X") or (i[0][2] == "X" and i[1][2] == "X" and i[2][2] == "X")):
        print("X won!")
        return True
    if((i[0][0] == "X" and i[1][1] == "X" and i[2][2] == "X") or (i[2][0] == "X" and i[1][1] == "X" and i[0][2] == "X")):
        print("X won!")
        return True
    if((i[0][0] == "O" and i[0][1] == "O" and i[0][2] == "O") or (i[1][0] == "O" and i[1][1] == "O" and i[1][2] == "O") or (i[2][0] == "O" and i[2][1] == "O" and i[2][2] == "O")):
        print("O won!")
        return True
    if((i[0][0] == "O" and i[1][0] == "O" and i[2][0] == "O") or (i[0][1] == "O" and i[1][1] == "O" and i[2][1] == "O") or (i[0][2] == "O" and i[1][2] == "O" and i[2][2] == "O")):
        print("O won!")
        return True
    if((i[0][0] == "O" and i[1][1] == "O" and i[2][2] == "O") or (i[2][0] == "O" and i[1][1] == "O" and i[0][2] == "O")):
        print("O won!")
        return True
    return False

flag = 1

def checkWinO(i):
    if((i[0][0] == "O" and i[0][1] == "O" and i[0][2] == "O") or (i[1][0] == "O" and i[1][1] == "O" and i[1][2] == "O") or (i[2][0] == "O" and i[2][1] == "O" and i[2][2] == "O")):
        # print("O won!")
        return True
    if((i[0][0] == "O" and i[1][0] == "O" and i[2][0] == "O") or (i[0][1] == "O" and i[1][1] == "O" and i[2][1] == "O") or (i[0][2] == "O" and i[1][2] == "O" and i[2][2] == "O")):
        # print("O won!")
        return True
    if((i[0][0] == "O" and i[1][1] == "O" and i[2][2] == "O") or (i[2][0] == "O" and i[1][1] == "O" and i[0][2] == "O")):
        # print("O won!")
        return True
    return False

def checkWinX(i):
    if((i[0][0] == "X" and i[0][1] == "X" and i[0][2] == "X") or (i[1][0] == "X" and i[1][1] == "X" and i[1][2] == "X") or (i[2][0] == "X" and i[2][1] == "X" and i[2][2] == "X")):
        # print("X won!")
        return True
    if((i[0][0] == "X" and i[1][0] == "X" and i[2][0] == "X") or (i[0][1] == "X" and i[1][1] == "X" and i[2][1] == "X") or (i[0][2] == "X" and i[1][2] == "X" and i[2][2] == "X")):
        # print("X won!")
        return True
    if((i[0][0] == "X" and i[1][1] == "X" and i[2][2] == "X") or (i[2][0] == "X" and i[1][1] == "X" and i[0][2] == "X")):
        # print("X won!")
        return True
    return False

def play(x):
    for k in range(3):
        for l in range(3):
            if(x[k][l] == " "):
                x[k][l] = "O"
                if(checkWinO(x)):
                    return [k,l]
                x[k][l] = " "
    for k in range(3):
        for l in range(3):
            if(x[k][l] == " "):
                x[k][l] = "X"
                if(checkWinX(x)):
                    return [k,l]
                x[k][l] = " "

    return None

print()
board(i)

for j in range(9):
    
    if(flag):
        print()
        print("X chance")
        print()
        while(True):
            z = int(input("Enter choice - "))
            a = (z-1)//3
            b = (z-1)%3
            if(i[a][b] == " "):
                i[a][b] = "X"
                break
            else:
                print("invalid move! play again...")
        flag=0
    else:
        print()
        print("O chance")
        print()
        while(True):
            x = copy.deepcopy(i)
            Z = play(x)
            if(Z):
                a = Z[0]
                b = Z[1]
            else:
                z = random.randint(1,9)
                a = (z-1)//3
                b = (z-1)%3
            if(i[a][b] == " "):
                i[a][b] = "O"
                break
            else:
                print("invalid move! play again...")
        flag=1
    if(board(i)):
        break