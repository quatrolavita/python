
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
    pass


#Написать функицию которая будет проверять победитетя

if __name__ == "__main__":

    index = None

    print("This is Tic Tac Toe, please choice index of box. First turn for  (\'X\')")
    bord = ['-']*9
    filling_field(bord)
    for i in range(9):

        while True:
            print(" \nEnter index your turn:", end='')
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
    print("\n")
