from game_logic import *

def main():
    exiting = False

    while not exiting:
        print("""
================================
           ROLL DICE
================================

1. Start New Game
2. View Game History
3. View Statistics
4. Exit
    """)

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("\nOption must be integer.")
        if choice < 1 or choice > 4:
            print("\nOption must be between 1 to 4.")

        if choice == 1:
            start_game()
        elif choice == 2:
            display_game_history(load_game_history())
        elif choice == 3:
            display_statistics(load_game_history())
        elif choice == 4:
            print("\nExiting...")
            exiting = True
    
    return 0

if __name__ == "__main__":
    main()