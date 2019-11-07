def checkwin(p,c,t):
    if (p[0] == "X" and p[1] == "X" and p[2] == "X") or (p[3] == "X" and p[4] == "X" and p[5] == "X") or (p[6] == "X" and p[7] == "X" and p[8] == "X") or (p[0] == "X" and p[3] == "X" and p[6] == "X") or (p[1] == "X" and p[4] == "X" and p[7] == "X") or (p[2] == "X" and p[5] == "X" and p[8] == "X") or (p[0] == "X" and p[4] == "X" and p[8] == "X") or (p[2] == "X" and p[4] == "X" and p[6] == "X"):
        return 1
    elif (c[0] == "O" and c[1] == "O" and c[2] == "O") or (c[3] == "O" and c[4] == "O" and c[5] == "O") or (c[6] == "O" and c[7] == "O" and c[8] == "O") or (c[0] == "O" and c[3] == "O" and c[6] == "O") or (c[1] == "O" and c[4] == "O" and c[7] == "O") or (c[2] == "O" and c[5] == "O" and c[8] == "O") or (c[0] == "O" and c[4] == "O" and c[8] == "O") or (c[2] == "O" and c[4] == "O" and c[6] == "O"):
        return 2
    else:
        if t == 9:
            return 3
        else:
            return 0
        
def debug(p,c,a):
    print()
    print("X = " , p)
    print("O = " , c)
    print(pmoves, len(pmoves))
    print()
numwinx = 0
numwiny = 0
numtie = 0 
import random as r
while True:
    X = [0,0,0,0,0,0,0,0,0]
    O = [0,0,0,0,0,0,0,0,0]
    pmoves = [0,1,2,3,4,5,6,7,8]
    grid = " 0 | 1 | 2  \n 3 | 4 | 5 \n 6 | 7 | 8"
    gd = ""
    print("TicTacToe")
    print(" 1 | 2 | 3  \n 4 | 5 | 6 \n 7 | 8 | 9")
    h = 0
    nx = 0
    ny = 0
    while h == 0:
        if nx + ny == 9 and h != 1:
            h = 1
        inp = int(input("Your Move(1-9)> ")) - 1
        if inp != "" and inp >= 0 and inp <9:
            if O[inp] != "O" and X[inp] != "X":
                X[inp] = "X"
                for g in X:
                    if g == "X":
                        grid = grid.replace(str(inp), "X")
                        gd = grid
                        for i in range(0,9):
                            if str(i) in gd:
                                gd=gd.replace(str(i), " ")                                
                nx +=1
                print(gd)
                #debug(X,O,pmoves)
            else:
                print("illegal move")
                continue
            res = checkwin(X,O,(nx+ny))
            if res == 1:
                h = 1
                numwinx +=1
                print("You Win. \n")
            elif res == 2:
                h = 1
                numwiny += 1
                print("I win \n")
            elif res == 3:
               h = 1
               numtie +=1
               print("hmm. it was a tie. \n")
               
            if h != 1:

                print("My turn,")
                pmoves.remove(inp)
                rd = r.randrange(0,len(pmoves))
                rd = int(pmoves[rd])
                O[rd] = "O"
                pmoves.remove(rd)
                ny +=1
                for g in O:
                    if g == "O":
                        grid = grid.replace(str(rd), "O")
                        gd = grid
                for i in range(0,9):
                    if str(i) in gd:
                        gd=gd.replace(str(i), " ")                    
                print(gd)
                #debug(X,O,pmoves)
        else:
            print("illegal move.")
            h = 1
            
        res = checkwin(X,O,(nx+ny))
        if res == 1 and h!= 1:
            h = 1
            numwinx +=1
            print("You Win. \n")
        elif res == 2 and h!= 1:
            h = 1
            numwiny += 1
            print("I win \n")
        elif res == 3 and h!= 1:
           h = 1
           numtie +=1
           print("hmm. it was a tie. \n")
    print("GAME OVER. GG")
    print("    SCORES \n    ======")
    print("You  -------- ", numwinx)
    print("Me   -------- ",numwiny)
    print("Ties -------- ", numtie)
    print()
    newgame = str(input("Play another round? (Y/N)> ")).upper()
    if newgame == "Y":
        print()
        print("=====NEW GAME=====")
        print()
    elif newgame == "N":
        rt = r.randrange(-2,6)
        if rt == 0:
            print("Goodbye!")
            break
        elif rt == 1:
            print("Alringt, Bye!")
            break
        elif rt == 2:
            print("Good Game! Bye.")
            break
        elif rt == 3:
            print("It was fun!")
            break
        elif rt <= 4:
            print("OH NO YOU DONT ;)")
            print()
            print("=====NEW GAME=====")
            print()
        else:
            print("Let's play again sometime")
            break
