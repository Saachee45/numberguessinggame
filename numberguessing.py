import random
print("NumberGuessingGame")
number=random.randint(1,9)

chances=0
print("GUESS A NUMBER(between 1 and 9)")
while chances<5:
    guess=int(input("ENTER YOUR GUESS"))

    if guess==number:
        print("CONGRATULATINS YOU WON!")
        break
    elif guess<number:
        print("YOUR GUESS WAS LOW .GUESS A HIGHER NUMBER",guess)
    else:
        print("GUESS WAS TO HIGH GUESS A LOWER NUMBER",guess)

    chances+=1
if not chances<5:
    print("YOU LOOSE,THE NUMBER IS",number)
