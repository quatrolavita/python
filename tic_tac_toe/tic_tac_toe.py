
def filling_field(bord):
    print('|', end='')

    for i in range(len(bord)):

        if bord[i] == '-':
            print(f'{i}|', end='')
        else:
            print(f'{bord[i]}|', end='')

        if i == 2 or i == 5:
            print('', end='\n')
            print('|', end='')


def foll_check(index, bord):

    if index < 0 or index > 8:

        raise TypeError

    if bord[index] == 'X' or bord[index] == 'O':

        raise TypeError


def check_winner(bord):

    index = 0
    for i in range(1, 4):
        if (bord[index*i] == bord[index*i+1]) and (bord[index*i+1] == bord[index*i+2]):
            if bord[index*i] != '-':
                return {f'{bord[index*i]}': True}
    return {f'{bord[index*i]}': False}




if __name__ == "__main__":

    index = None

    print("This is Tic Tac Toe, please choice index of box. First turn for  (\'X\')")
    bord = ['-']*9
    filling_field(bord)
    for i in range(9):

        while True:
            print(" \nEnter index your turn,:", end='')
            try:
                index = int(input())
                foll_check(index, bord)

            except TypeError:
                print("Invalid action")
                continue

            if i % 2 == 0:
                bord[index] = 'X'
            else:
                bord[index] = 'O'
            break
        print('\n')
        filling_field(bord)
        if check_winner(bord).values() == True:
            print(f"Congratulations player {check_winner(bord).items()} become winner!!!")
            break

    print("\n")
