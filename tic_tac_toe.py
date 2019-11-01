theBoard={'top-L':' ','top-M':' ','top-R':' ',
          'mid-L':' ','mid-M':' ','mid-R':' ',
          'low-L':' ','low-M':' ','low-R':' '}
def winCheck(board):
    winPos=[['top-L','top-M','top-R'],
            ['top-L','mid-M','low-R'],
            ['top-L','mid-L','low-L'],
            ['mid-L','mid-M','mid-R'],
            ['low-L','low-M','low-R'],
            ['top-M','mid-M','low-M'],
            ['top-R','mid-R','low-R'],
            ['low-L','mid-M','top-R']]
    for i in winPos:
        if board[i[0]] == board[i[1]] and board[i[1]]==board[i[2]] and board[i[0]]!=' ':
            print(board[i[0]],"wins")
            return 1
    return 0
        
            
            

def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
    
turn='X'
for i in range(9):
    printBoard(theBoard)
    print('turn for ' + turn + '. ' + 'Move to which space?')
    move=input()
    theBoard[move]=turn
    check=winCheck(theBoard)
    if check==1:
        break
    if turn == 'X':
        turn='O'
    else:
        turn='X'



printBoard(theBoard)
