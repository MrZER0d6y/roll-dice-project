from json_handling import *
import random

def roll_dice():
    return random.randint(1, 6)

def play_round():
    player_dice = roll_dice()
    computer_dice = roll_dice()

    winner = calculate_winner("Player", player_dice, computer_dice)
    
    return {
        "round": None,
        "player_dice": player_dice,
        "computer_dice": computer_dice,
        "winner": winner
    }

def number_of_rounds():
    valid_rounds = False
    while not valid_rounds:
        try:
            rounds = int(input("\nNumber of rounds (1-10): "))
        except ValueError:
            print("\nRounds must be integer.")
            continue
        if rounds < 1 or rounds > 10:
            print("\nMin rounds - 1, max rounds - 10.")
            continue
        valid_rounds = True
    return rounds

def get_player_name():
    valid_username = False
    while not valid_username:
        username = input("Player name: ")
        if not username:
            continue
        return username.capitalize()

def start_game():
    print("""
================================
           NEW GAME
================================
"""    )
    player = get_player_name()
    rounds = number_of_rounds()
    results = []

    for round_num in range(rounds):
        print(f"\n---------- ROUND {round_num} ----------")
        
        result = play_round()
        result["round"] = round_num
        
        if result["winner"] == "Player":
            result["winner"] = player
        
        print(f"\n{player + ":":<10}🎲 {result["player_dice"]}")
        print(f"{"Computer:":<10}🎲 {result["computer_dice"]}")
        
        if result["winner"] == "Draw":
            print("Draw!")
            continue
        
        print(f"\n{result["winner"]} wins this round!")
        results.append(result)

    player_score, computer_score = calculate_score(results)
    winner = calculate_winner(player, player_score, computer_score)

    game = {
    "player_name": player,
    "rounds": rounds,
    "player_score": player_score,
    "computer_score": computer_score,
    "winner": winner,
    "results": results
    }

    display_game_results(game)
    save_game(game)

    return True

def calculate_score(results):
    player_score = 0
    computer_score = 0

    for result in results:
        if result["winner"] == "Computer":
            computer_score += 1
        elif result["winner"] != "Draw":
            player_score += 1

    return player_score, computer_score

def calculate_winner(player, player_score, computer_score):
    if player_score > computer_score:
        return player
    elif player_score < computer_score:
        return "Computer"
    return "Draw"

def display_game_results(game):
    print("""
================================
           GAME OVER
================================
    """)

    print(f"{game["player_name"] + ":":<10}{game["player_score"]} points")
    print(f"{"Computer:":<10}{game["player_score"]} points")
    print(f"\nWINNER: {game["winner"]}!")
    return

def save_game(game):
    games = load_game_history()
    games.append(game)
    save_game_history(games)
    return

def display_game_history(history):
    if not history:
        print("No games gave been played yet.")
        return
        
    print("""
================================
          GAME HISTOYR
================================
    """)
    for number, game in enumerate(history, start=1):
        print(f"\n----- Game {number} -----")
        print(f"Player: {game["player_name"]} | Rounds: {game["rounds"]}"
        f" | Player Score: {game["player_score"]} | Computer Score: {game["computer_score"]}"
        f"\nWinner - {game["winner"]}")
    return

def display_statistics(history):
    if not history:
        print("No games have been played yet.")
        return
    
    print("""
================================
        GAME STATISTICS
================================
    """)
    print(f"Total Games: {len(history)}")

    player_wins = 0
    computer_wins = 0
    draws = 0
    for game in history:
        if game["winner"] == "Computer":
            computer_wins += 1
        elif game["winner"] == "Draw":
            draws += 1
        else:
            player_wins += 1
    
    print(f"Player Wins - {player_wins} | Computer Wins - {computer_wins} | Draws - {draws}")
    try:
        print(f"Players Win Rate: {player_wins / len(history):.2f}%")
    except ZeroDivisionError:
        print("Player Win Rate: 0%")
    return