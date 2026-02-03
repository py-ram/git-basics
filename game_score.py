Player = input("Enter Name: ")
GamesPlayed = input("Enter number of games played:")
Games_played = int(GamesPlayed)
print("="*45)
Score_in_the_game1= int(input(f"Enter score in the game1: "))
Score_in_the_game2= int(input(f"Enter score in the game2: "))
Score_in_the_game3= int(input(f"Enter score in the game3: "))
print("="*45)
Total_score = Score_in_the_game1 + Score_in_the_game2 + Score_in_the_game3
print(f"Total_score: {Total_score}")
print("="*45)
Average_score = Total_score / Games_played
print(f"Average_score: {Average_score}")
