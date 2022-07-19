import random
##intro questions
print("Welcome to the weird ass calculator!")
print("Would you like to roll dice, flip a coin, or roll a custom dice?")
print("Dice [1]")
print("Coin [2]")
print("Custom Dice [3]")
response = int(input("Enter your choice:\n"))
if response ==  1:
    ##dice rolling
    n = int(input("How many times would you like to roll the dice?\n"))
    ##score
    evens = 0 
    odds = 0
    #large rolls get hidden
    if n >= 20:
        for x in range(n):
            y = random.randint(1, 6)
            if y % 2 == 0:
                evens += 1
            else:
                odds +=1
    ##small rolls get displayed
    elif n < 20:
        for x in range(n):
            print("Roll", x, ":")
            y=random.randint(1, 6)
            print(y)
            if y % 2 == 0:
                evens += 1
            else:
                odds += 1
    ##end screen
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You rolled", n, "times resulting in:")
    print("EVENS:", evens)
    print("ODDS:", odds)
#coin toss
elif response == 2:
    coin_num = int(input("How many times would you like to flip a coin?\n"))
    heads = 0
    tails = 0
    for tosses in range(coin_num):
        randcoin = random.randint(1,2)
        if randcoin % 2 == 0:
            heads += 1
        else:
            tails += 1
    ##end screen
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You flipped", coin_num, "times, resulting in:")
    print("HEADS:", heads)
    print("TAILS:", tails)
elif response == 3:
    dice_sides = int(input("How many sides will your dice have?\n"))
    dice_rolls = int(input("How many times will you roll the dice?\n"))
    even_custom = 0
    odd_custom = 0
    ##long rolls hidden
    if dice_rolls >= 20:
        highscore_custom = 0
        for dice_round in range(dice_rolls):
            dice_result = random.randint(1, dice_sides)
            dice_result2 = dice_result
            if dice_result % 2 == 0:
                even_custom += 1
            else:
                odd_custom += 1
            if dice_result2 > highscore_custom:
                highscore_custom = 0 + dice_result
            else:
                continue
    ##shorter rolls displayed
    else:
        highscore_custom = 0
        for dice_round in range(dice_rolls):
            dice_result = random.randint(0, dice_sides)
            dice_result2 = dice_result
            print("Round:", dice_round)
            print("Rolled:", dice_result)
            if dice_result % 2 == 0:
                even_custom += 1
            else:
                odd_custom += 1
            if dice_result2 > highscore_custom:
                highscore_custom = 0 + dice_result
            else:
                continue
    ##end screen
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You flipped a", dice_sides, "sided dice", dice_rolls, "times, resulting in")
    print("EVENS:", even_custom)
    print("ODDS:", odd_custom)
    print("Highest roll:", highscore_custom)
else:
    print("Not understood")