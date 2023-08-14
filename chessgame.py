BoardSize = 8
BOcHEss=[[" "]*BoardSize for i in range(BoardSize)]
def BoadInitializate():
    #create a 8x8 2d list to store the chess board
    print("Chess Board")
    start = 0
    end = 7
    #(0,0) sab say ooper left (0,7) sab say ooper right
    BOcHEss[start][0]="R" #fill in the 0 row with Rpook R
    BOcHEss[start][1]="N"#knight piece N
    BOcHEss[start][2]="B"#Bishop B
    BOcHEss[start][3]="Q"#queen 
    BOcHEss[start][4]="K"#King
    BOcHEss[start][5]="B"#2nd Bishopp
    BOcHEss[start][6]="N"#Knight 2
    BOcHEss[start][7]="R"#Rook 2nd
    #(7,0) sab say neechay left or (7,7) sab se neechay rgt
    BOcHEss[end][0]="r" #filling 7th row with rrok now small sab
    BOcHEss[end][1]="n"#knight
    BOcHEss[end][2]="b"#Bishop piecee i.e. b (small b)
    BOcHEss[end][3]="q"#queen
    BOcHEss[end][4]="k"#King
    BOcHEss[end][5]="b"#Bishop 2
    BOcHEss[end][6]="n"#2nd Knightt
    BOcHEss[end][7]="r"#Rok 2
    #(1,0) say (1,7) 
    for looppi in range(8): #pawn 1 0 say 1 7
        BOcHEss[1][looppi]="P"
    #(6,0) se (6,7) 
    for looppi in range(8): #this is for filling the 6th row with pawn pieces i.e. p (small p)
        BOcHEss[6][looppi]="p"
    
    #We have already filledd the 1st and 6thh row with pawn piece i.e. P and p respectively
    for looppi in range(2,6):
        for j in range(8):
            BOcHEss[looppi][j]="*"

    #BOcHEss[4][4]='K'
    #BOcHEss[4][4]="b"
    #Printing the chess board
def PrintingBoard(Boardd):
    for looppi in range(8):
        for j in range(8):
            print(Boardd[looppi][j],end=" ")
        print()
    return Boardd
                
    

def Can_Move_All(CBoard):
    ArrayMov = []
    for rowss in range(0, 8):#0 say 7 
        for colums in range(0, 8): # upto seven
            GPiece = CBoard[rowss][colums] #board par goti or nahi
            if GPiece != symboll: #not space
                if (GPiece.islower()):
                    if  GPiece == 'p':
                        temp = M_Pawnn(CBoard, rowss, colums)
                        ArrayMov =ArrayMov+ M_Pawnn(CBoard, rowss, colums)
                        print("p")
                        print(temp)
                    elif  GPiece == 'r':
                        temp = Rr_Moves(CBoard, rowss, colums)
                        ArrayMov += Rr_Moves(CBoard, rowss, colums)
                        print("r")
                        print(temp)
                        
                    elif GPiece == 'n':
                        ArrayMov += Knight_Can_Move(CBoard, rowss, colums)
                        print("n")
                        print(Knight_Can_Move(CBoard, rowss, colums))
                    elif  GPiece == 'b':
                        temp = Bishop_CanMove(CBoard, rowss, colums)
                        ArrayMov += Bishop_CanMove(CBoard, rowss, colums)
                        print("b")
                        print(temp)
                    elif  GPiece == 'q':
                        print("q")
                        temp = Queen_CanMove(CBoard, rowss, colums)
                        ArrayMov += Queen_CanMove(CBoard, rowss, colums)
                        print(temp)
                    elif  GPiece == 'k':
                        ArrayMov += get_valid_moves_king(CBoard, rowss, colums)
                        temppp = get_valid_moves_king(CBoard, rowss, colums)
                        print("k")
                        print(temppp)
                    
                
    return ArrayMov
def Can_Move_S(CBoard):
    ArrayMov = []
    for rowss in range(0, 8):#0 say 7 
        for colums in range(0, 8): # upto seven
            GPiece = CBoard[rowss][colums] #board par goti or nahi
            if GPiece != symboll: #not space
                if (GPiece.isupper()):
                    if GPiece == 'P':
                        st= M_Pawnn(CBoard, rowss, colums)
                        ArrayMov =ArrayMov+ M_Pawnn(CBoard, rowss, colums)
                        print("P,ArrayMov")
                        print(st)
                    elif GPiece == 'R':
                        st=Rr_Moves(CBoard, rowss, colums)
                        ArrayMov += Rr_Moves(CBoard, rowss, colums)
                        print("R,ArrayMov")
                        print(st)
                    elif GPiece == 'N':
                        st=Knight_Can_Move(CBoard, rowss, colums)
                        ArrayMov += Knight_Can_Move(CBoard, rowss, colums)
                        print("N,ArrayMov")
                        print(st)
                    elif GPiece == 'B':
                        st= Bishop_CanMove(CBoard, rowss, colums)
                        ArrayMov += Bishop_CanMove(CBoard, rowss, colums)
                        print("B,ArrayMov")
                        print(st)
                    elif GPiece == 'Q':
                        print("Q,ArrayMov")
                        print(Queen_CanMove(CBoard, rowss, colums))
                        ArrayMov += Queen_CanMove(CBoard, rowss, colums)
                    elif GPiece == 'K':
                        print("K,ArrayMov")
                        ArrayMov += get_valid_moves_king(CBoard, rowss, colums)
                        print(get_valid_moves_king(CBoard, rowss, colums))
                    
                
    return ArrayMov
def M_Pawnn(B, roww, Coll): 
    ArrStoreM = []
    symbol = '*'
    Start = 0
    end = 8
    if B[roww][Coll].isupper():
        #pawn mai aik chhez we ned to remember sirf forward movement hoti hai 
        if roww == 1:# agr pawn pehli row mai hai tu wo two steps chal sakta 
            #jabkay 2ono ka khaali hona zaroori
            if B[roww+1][Coll] == symbol and B[roww+2][Coll] == symbol:
                ArrStoreM.append((roww+2, Coll))
        if roww+1 < end: #aik step 
            if B[roww+1][Coll] == '*':
                ArrStoreM.append((roww+1, Coll))
        if roww+1 < end and Coll+1 < end: #hum check diagonal opponent pieve
            if B[roww+1][Coll+1].islower():
                ArrStoreM.append((roww+1, Coll+1))
        if roww+1 < end and Coll-1 >= Start: #diagonal me opponent goti
            if B[roww+1][Coll-1].islower():
                ArrStoreM.append((roww+1, Coll-1)) 
    elif B[roww][Coll].islower(): #small letterr
        if roww == 6: #small leeter kay liay pawn ki start 6 row banti hai
            one =1
            steri = "*"
            tw= 2
            if B[roww-one][Coll] == steri and B[roww-tw][Coll] == steri:
                var = (roww-tw, Coll)
                ArrStoreM.append(var)
        if roww-1 >= 0:
            if B[roww-1][Coll] == symbol:
                ArrStoreM.append((roww-1, Coll))
        if roww-1 >= 0 and Coll+1 < 8:
            if B[roww-1][Coll+1].isupper():
                ArrStoreM.append((roww-1, Coll+1))
        if roww-1 >= 0 and Coll-1 >= 0:
            if B[roww-1][Coll-1].isupper():
                ArrStoreM.append((roww-1, Coll-1))
    return ArrStoreM
def Rr_Moves(CBoard, roww, coll):
    ArrN=[]
    end = 8
    if CBoard[roww][coll].isupper():
        if roww+1<end:
            for i in range(roww+1,8):
                if CBoard[i][coll]=="*":
                    ArrN.append((i,coll))
                elif CBoard[i][coll].islower():
                    ArrN.append((i,coll))
                    break
                else:
                    break 
        if roww-1>=0:
            for i in range(roww-1,-1,-1):
                if CBoard[i][coll]=="*":
                    ArrN.append((i,coll))
                elif CBoard[i][coll].islower():
                    ArrN.append((i,coll))
                    break
                else:
                    break
        if coll+1<8:
            for i in range(coll+1,8):
                if CBoard[roww][i]=="*":
                    ArrN.append((roww,i))
                elif CBoard[roww][i].islower():
                    ArrN.append((roww,i))
                    break
                else:
                    break
        if coll-1>=0:
            for i in range(coll-1,-1,-1):
                if CBoard[roww][i]=="*":
                    ArrN.append((roww,i))
                elif CBoard[roww][i].islower():
                    ArrN.append((roww,i))
                    break
                else:
                    break
    else:
        #This is for the black rook
        if roww+1<8:
            for i in range(roww+1,8):
                if CBoard[i][coll]=="*":
                    ArrN.append((i,coll))
                elif CBoard[i][coll].isupper():
                    ArrN.append((i,coll))
                    break
                else:
                    break
        if roww-1>=0:
            for i in range(roww-1,-1,-1):
                if CBoard[i][coll]=="*":
                    ArrN.append((i,coll))
                elif CBoard[i][coll].isupper():
                    ArrN.append((i,coll))
                    break
                else:
                    break
        if coll+1<8:
            for i in range(coll+1,8):
                if CBoard[roww][i]=="*":
                    ArrN.append((roww,i))
                elif CBoard[roww][i].isupper():
                    ArrN.append((roww,i))
                    break
                else:
                    break
        if coll-1>=0:
            for i in range(coll-1,-1,-1): #it is -1 because we are going backwards from the column
                if CBoard[roww][i]=="*":
                    ArrN.append((roww,i))
                elif CBoard[roww][i].isupper():
                    ArrN.append((roww,i))
                    break
                else:
                    break
    return ArrN
def Knight_Can_Move(VCBoard, uR, uC):
    # This function returns a list of tuples of all the legal moves for a knight
    UPossibleM=[]
    #
    last = 8
    s = 0
    v1 = 0
    v2 = 1
    symbolSpace = "*"
    NArr=[(uR+2,uC+1),(uR+2,uC-1),(uR-2,uC+1),(uR-2,uC-1),(uR+1,uC+2),(uR+1,uC-2),(uR-1,uC+2),(uR-1,uC-2)]
    if VCBoard[uR][uC].isupper():
        for CMov in NArr:
            if CMov[v1]<last and CMov[v2]<last and CMov[v1]>=s  and CMov[v2]>=s:
                fir= CMov[v1]
                fir2= CMov[v2]
                if (VCBoard[fir][fir2]== symbolSpace) or (VCBoard[fir][fir2].islower()):
                    UPossibleM.append(CMov)
    else:
        for CMov in NArr:
            uff = CMov[v1]
            uff2 = CMov[v2]
            if ((uff<8) and (uff>=s) and (uff2<last) and (uff2>=s)):
                fir=CMov[v1]
                fir2 =CMov[v2]
                if VCBoard[fir][fir2]==symbolSpace or VCBoard[fir][fir2].isupper():
                    UPossibleM.append(CMov)
    return UPossibleM
def Bishop_CanMove(VCBoard, lR, lC):
    UPossibleM= []
    start = 0 
    end = 8
    NArr=[(lR+1,lC+1),(lR+1,lC-1),(lR-1,lC+1),(lR-1,lC-1)]
    looppRangeStart = 1
    loopRangeEndd = 8
    if VCBoard[lR][lC].isupper(): #Whitw ka 1st diagonal
        for D1 in range(looppRangeStart,loopRangeEndd):
            #positive both sides increment
            if lR+D1<end and lC+D1<end: #r n c in positive less than 8
                if VCBoard[lR+D1][lC+D1]=="*": #space 
                    UPossibleM.append((lR+D1,lC+D1)) #append
                elif VCBoard[lR+D1][lC+D1].islower():
                    UPossibleM.append((lR+D1,lC+D1))
                    break #break kar rahay 
                else:
                    break 
        for D1 in range(looppRangeStart,loopRangeEndd): #+1 say lai kar +7 tak 
            #rows positive and column negative
            if lR+D1<end and lC-D1>=start: #ro <8 and colu >= 0
                if VCBoard[lR+D1][lC-D1]=="*": 
                    UPossibleM.append((lR+D1,lC-D1))
                elif VCBoard[lR+D1][lC-D1].islower(): #piece
                    UPossibleM.append((lR+D1,lC-D1))
                    break #if goti
                else:
                    break
        for D1 in range(looppRangeStart,8): #+1 to +7 tak 
            #ro negative and cols positive
            if lR-D1>=start and lC+D1<end: #row >=0 and col < 8
                if VCBoard[lR-D1][lC+D1]==symboll: 
                    UPossibleM.append((lR-D1,lC+D1))
                elif VCBoard[lR-D1][lC+D1].islower(): 
                    UPossibleM.append((lR-D1,lC+D1))
                    break #we are breaking here bcz hum jump nahi karsaktay over piece
                else:
                    break
        for D1 in range(looppRangeStart,loopRangeEndd): #1 say seven plus 
            #r -ve and col -ve
            if lR-D1>=start and lC-D1>=start: #r >=0 and c >= 0
                if VCBoard[lR-D1][lC-D1]==symboll:
                    UPossibleM.append((lR-D1,lC-D1))
                elif VCBoard[lR-D1][lC-D1].islower(): #piece
                    UPossibleM.append((lR-D1,lC-D1))
                    break #agar opponent ka piece
                else:
                    break
    else:
        for D1 in range(looppRangeStart,loopRangeEndd):
            if lR+D1<end and lC+D1<end:
                if VCBoard[lR+D1][lC+D1]==symboll:
                    UPossibleM.append((lR+D1,lC+D1))
                elif VCBoard[lR+D1][lC+D1].isupper():
                    UPossibleM.append((lR+D1,lC+D1))
                    break
                else:
                    break
        for D1 in range(looppRangeStart,loopRangeEndd):
            if lR+D1<end and lC-D1>=start:
                if VCBoard[lR+D1][lC-D1]==symboll:
                    UPossibleM.append((lR+D1,lC-D1))
                elif VCBoard[lR+D1][lC-D1].isupper():
                    UPossibleM.append((lR+D1,lC-D1))
                    break
                else:
                    break
        
        for D1 in range(looppRangeStart,loopRangeEndd):
            if lR-D1>=start and lC+D1<end:
                if VCBoard[lR-D1][lC+D1]==symboll:
                    UPossibleM.append((lR-D1,lC+D1))
                elif VCBoard[lR-D1][lC+D1].isupper():
                    UPossibleM.append((lR-D1,lC+D1))
                    break
                else:
                    break
        for D1 in range(looppRangeStart,loopRangeEndd):
            if lR-D1>=start and lC-D1>=start:
                if VCBoard[lR-D1][lC-D1]==symboll:
                    UPossibleM.append((lR-D1,lC-D1))
                elif VCBoard[lR-D1][lC-D1].isupper():
                    UPossibleM.append((lR-D1,lC-D1))
                    break
                else:
                    break
            
    return UPossibleM   
def get_valid_moves_king(board, r, col):
    UPossibleM= []
    start = 0 
    end = 8
    v = symboll
    NArr=[(r-1,col+1),(r+1,col+1),(r+1,col-1),(r+1,col),(r-1,col-1),(r-1,col),(r,col+1),(r,col-1)]
    if(board[r][col].isupper()):
        for Cm2 in NArr:
            one = Cm2[0] 
            two = Cm2[1]
            if one<end and one>=start and two<end and two>=start:
                if board[one][two]==v:
                    UPossibleM.append(Cm2)
                elif board[Cm2[0]][Cm2[1]].islower():
                    UPossibleM.append(Cm2)
                    break
                else:
                    break
    elif (board[r][col].islower()):
        for Cm2 in NArr:
            one = Cm2[0] 
            two = Cm2[1]
            if one<end and two>=start and one>=start and two<end :
                if board[one][two]==v:
                    UPossibleM.append(Cm2)
                elif board[Cm2[0]][Cm2[1]].isupper():
                    UPossibleM.append(Cm2)
                    break
                else:
                    break
    return UPossibleM
def Queen_CanMove(board,rows,coll):
    UPossibleM= []
    if board[rows][coll].isupper():
        UPossibleM.extend(Bishop_CanMove(board,rows,coll))
        UPossibleM.extend(Rr_Moves(board,rows,coll))
    elif board[rows][coll].islower():
        UPossibleM.extend(Bishop_CanMove(board,rows,coll))
        UPossibleM.extend(Rr_Moves(board,rows,coll))
    return UPossibleM 
    
symboll = '*'
def Chess_Stateof_B(Bord):
    board_state = {}
    for rows in range(0, 8):
        for columnn in range(0, 8):
            goti = Bord[rows][columnn]
            if goti != symboll: #space check kar rahay 
                board_state[(rows, columnn)] = goti
    return board_state 
def movement(board, r, c, r1, c1):
    s =board[r][c]  
    print (s)
    if(s == symboll):
        return board
    elif (s=='p'):
        if(r1,c1) in M_Pawnn(board,r,c):
            print("Shere")
            board[r1][c1] = s
            board[r][c] = symboll
            print(board)
            return board
        else:
            print("Cantt Move")
            return board
    elif(s=='r'):
        if(r1,c1) in Rr_Moves(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
            return board
        else:
            print("Cant Move")
            return board
    elif(s=='n'):
        if (r1,c1) in Knight_Can_Move(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
            return board
        else: 
            print("Cant Move")
            return board
    elif (s=='b'):
        if (r1,c1) in Bishop_CanMove(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
            return board
        else:
            print("Cant Movee")
            return board
    elif (s=='q'):
        if(r1,c1) in Queen_CanMove(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
        else:
            print("Cant Move")
            return board
    elif (s=='k'):
        if(r1,c1) in get_valid_moves_king(board,r,c):
            board[r1][c1] = s
            board[r][c]= symboll
        else:
            print("Cant Move")
            return board
    else:
        print("Invalidd")
    return board
def movementt(board, r, c, r1, c1):
    s =board[r][c]  
    print (s)
    if(s == symboll):
        return board
    elif (s=='Q'):
        if(r1,c1) in M_Pawnn(board,r,c):
            print("Shere")
            board[r1][c1] = s
            board[r][c] = symboll
            print(board)
            return board
        else:
            print("Cantt Move")
            return board
    elif(s=='R'):
        if(r1,c1) in Rr_Moves(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
            return board
        else:
            print("Cant Move")
            return board
    elif(s=='N'):
        if (r1,c1) in Knight_Can_Move(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
            return board
        else: 
            print("Cant Move")
            return board
    elif (s=='B'):
        if (r1,c1) in Bishop_CanMove(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
            return board
        else:
            print("Cant Movee")
            return board
    elif (s=='Q'):
        if(r1,c1) in Queen_CanMove(board,r,c):
            board[r1][c1] = s
            board[r][c] = symboll
        else:
            print("Cant Move")
            return board
    elif (s=='K'):
        if(r1,c1) in get_valid_moves_king(board,r,c):
            board[r1][c1] = s
            board[r][c]= symboll
        else:
            print("Cant Move")
            return board
    else:
        print("Invalidd")
    return board
def returnScoreB(C_Bord):
        C_Scoree=0 #This whole function is to evaluate the board and give a score to the board
        varP='p'
        pVa='p'
        for loopi in range(8): #It is checking the score
            for loopj in range(8):
                if C_Bord[loopi][loopj]=="P":
                    C_Scoree+=1
                elif C_Bord[loopi][loopj]=="p":
                    C_Scoree-=1
                elif C_Bord[loopi][loopj]=="R":
                    C_Scoree+=5
                elif C_Bord[loopi][loopj]=="r":
                    C_Scoree-=5
                elif C_Bord[loopi][loopj]=="N":
                    C_Scoree+=3
                elif C_Bord[loopi][loopj]=="n":
                    C_Scoree-=3
        print()
        for loopi in range(8):
            for loopj in range(8):
                if C_Bord[loopi][loopj]=="B":
                    C_Scoree+=3
                elif C_Bord[loopi][loopj]=="b":
                    C_Scoree-=3
                elif C_Bord[loopi][loopj]=="Q":
                    C_Scoree+=9
                elif C_Bord[loopi][loopj]=="q":
                    C_Scoree-=9
                elif C_Bord[loopi][loopj]=="K":
                    C_Scoree+=100
                elif C_Bord[loopi][loopj]=="k":
                    C_Scoree-=100
        return C_Scoree
def minimax(ChBrd, Dcheck, AlpMax,BetMin,Play):
    if Dcheck == 0:
        return -returnScoreB(ChBrd)
    if Play:
        maxEval = -float('inf')
        for Checkmovess in Can_Move_S(ChBrd):
            evaluation = minimax(Checkmovess, Dcheck - 1, AlpMax, BetMin, False)
            maxEval = max(maxEval, evaluation)
            AlpMax = max(AlpMax, evaluation)
            if BetMin <= AlpMax:
                break
        return maxEval
    else:
        minEval = float('inf')
        for Checkmovess in Can_Move_All(ChBrd):
            evaluation = minimax(Checkmovess, Dcheck - 1, AlpMax, BetMin, True)
            minEval = min(minEval, evaluation)
            BetMin = min(BetMin, evaluation)
            if BetMin <= AlpMax:
                break
        return minEval
print(BoadInitializate())
PrintingBoard(BOcHEss)
print("hereee")
Can_Move_S(BOcHEss)
print()
print()
print()
print("Black possible moves")
Can_Move_All(BOcHEss)
print(Bishop_CanMove(BOcHEss,4,4))
#print(get_valid_moves_king(BOcHEss,3,3))
#print(Queen_CanMove(BOcHEss,4,4))
print("queen")
print(Queen_CanMove(BOcHEss,4,4))
print(Rr_Moves(BOcHEss,7,7))
boardd = movement(BOcHEss,6,0,3,0)
print("here")
PrintingBoard(boardd)
#print(Chess_Stateof_B(BOcHEss))
user = None
board = Chess_Stateof_B(BOcHEss)
playerC= 'q'
while user not in ['q', 'Q']:
    user = input("Choose your option feom q or Q: ")
while True:
    if( playerC == 'q'):
        spos = int(input("Enter the position off piecee you want to move i.e row: "))
        epos = int(input("Enter the position off piecee you want to move i.e col: "))
        nspos =int( input("Enter the position where you want to movee i.e row: "))
        nepos = int(input("Enter the position where you want to movee i.e col: "))

        BOcHEss= movement(BOcHEss,spos,epos,nspos,nepos)
        PrintingBoard(BOcHEss)
        playerC = 'Q'
        
    if(playerC == 'Q'):
        
        spos = int(input("Enter the position off piecee you want to move i.e row: "))
        epos = int(input("Enter the position off piecee you want to move i.e col: "))
        nspos =int( input("Enter the position where you want to movee i.e row: "))
        nepos = int(input("Enter the position where you want to movee i.e col: "))
        BOcHEss= movementt(BOcHEss,spos,epos,nspos,nepos)
        #PrintingBoard(BOcHEss)
        '''moveB= None
        value= -99999
        for m in Can_Move_S(BOcHEss):
            #sR, sC,R,C = m
            mvall= 0#minimax(movement(BOcHEss,sR,sC,R,C),4,-200000,20000,True)
            if mvall > value:
                moveB = m
                value = mvall
                print(moveB)
        BOcHEss = movementt(BOcHEss,moveB[0],moveB[1],moveB[1],moveB[0])
        PrintingBoard(BOcHEss) '''           
        playerC = 'q'


    