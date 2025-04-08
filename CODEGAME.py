import time

def start_game():
    print("\nWelcome to the Escape Room!")
    print("You are trapped in a locked room. Solve the puzzles to escape!")
    room_one()

def room_one():
    print("\nRoom 1: The Locked Door")
    print("There is a keypad on the door. You need a 3-digit code to unlock it.")
    print("Hint: Ormonds Postcode Victoria")
    
    code = "3204"
    attempts = 3
    
    while attempts > 0:
        guess = input("Enter the 4-digit code: ")
        if guess == code:
            print("\nThe door unlocks! You move to the next room.")
            room_two()
            return
        else:
            attempts -= 1
            print(f"Incorrect code. {attempts} attempts remaining.")
    
    print("You have run out of attempts! Restarting the game...\n")
    start_game()

def room_two():
    print("\nRoom 2: The Riddle Room")
    print("A voice speaks: 'Solve this riddle to proceed.'")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
    
    answer = "echo"
    
    for _ in range(3):
        response = input("Your answer: ").strip().lower()
        if response == answer:
            print("\nCorrect! The door opens, leading to the final room.")
            room_three()
            return
        else:
            print("Incorrect. Try again.")
    
    print("You failed to answer the riddle. Restarting the game...\n")
    start_game()

def room_three():
    print("\nRoom 3: The Final Puzzle")
    print("There is a box with three colored buttons: Red, Blue, and Green.")
    print("A note says: 'Press them in the order of the rainbow.'")
    
    correct_order = ["red", "green", "blue"]
    attempt = []
    
    for _ in range(3):
        button = input("Press a button (Blue, Red, or Green): ").strip().lower()
        attempt.append(button)
    
    if attempt == correct_order:
        print("\nCongratulations! The final door unlocks, and you escape!")
    else:
        print("Incorrect order. Restarting the game...\n")
        restart_game()

def restart_game():
    print("\nYou have failed. Would you like to try again? (yes/no)")
    choice = input("> ").strip().lower()
    if choice == "yes":
        start_game()
    else:
        print("Thanks for playing! Goodbye.")
        exit()

if __name__ == "__main__":
    start_game()
