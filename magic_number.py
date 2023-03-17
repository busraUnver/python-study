magic_no = 7


while True:
    play = input("would you like to play? (Y/n) ").lower()
    
    if play == "n":
        break
    
    user_no = int(input("guess a number:"))
    if user_no == magic_no:
        print("omg you guessed correctly!")
    elif abs(user_no - magic_no) == 1:
        print("you're off by 1")
    else:
        print("no, better luck next time...")

print("goodbye!")