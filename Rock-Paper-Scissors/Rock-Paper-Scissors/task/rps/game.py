# Write your code here
user_option = input()
comp_option = ""

if user_option == "rock":
    comp_option = "paper"
    print(f"Sorry, but the computer chose {comp_option}")
elif user_option == "paper":
    comp_option = "scissors"
    print(f"Sorry, but the computer chose {comp_option}")
elif user_option == "scissors":
    comp_option = "rock"
    print(f"Sorry, but the computer chose {comp_option}")
