from random import randint
player = 50

while True:
    pred = int(input('coin prediction 1 or 2 : '))
    coin = randint(1,2) 

    if coin == pred:
        player = player + 9
        print("$", player, "정답입니다.")
    else:
        if player >= 10:
            player = player - 10
        else:
            player = 0
        print("$", player, "오답입니다")

    if player == 100:
        print('$100가 되어 게임종료.')
        break
    elif player == 0:
        print('$0으로 게임종료.')
        break

    