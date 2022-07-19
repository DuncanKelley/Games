import random

#1 for rock, 2 for paper, 3 for scissors

score = 0
scorecpu = 0

print("Rock paper scissors: How many rounds will you play?")
rounds = int(input(""))

for x in range(rounds):
    rng = random.randint(1,3)
    print("")
    answer = input("Select your move:\n")
    if rng == 1:
        print("CPU chooses rock")
    elif rng == 2:
        print("CPU chooses paper")
    else:
        print("CPU chooses scissors")
    if answer.lower() == "rock" and rng == 1:
        print("Tie")
    elif answer.lower() == "rock" and rng == 2:
        print("CPU wins")
        scorecpu += 1
    elif answer.lower() == "rock" and rng == 3:
        print("You win")
        score += 1
    elif answer.lower() == "paper" and rng == 1:
        print("You win")
        score += 1
    elif answer.lower() == "paper" and rng == 2:
        print("Tie")
    elif answer.lower() == "paper" and rng == 3:
        print("CPU wins")
        scorecpu += 1
    elif answer.lower() == "scissors" and rng == 1:
        print("CPU wins")
        scorecpu += 1
    elif answer.lower() == "scissors" and rng == 2:
        print("You win")
        score += 1
    elif answer.lower() == "scissors" and rng == 3:
        print("Tie")
print("")
print("CPU:", scorecpu)
print("Your score:", score)
if scorecpu > score:
    print("You lose!")
elif scorecpu == score:
    print("Tie game!")
else:
    print("You win!")