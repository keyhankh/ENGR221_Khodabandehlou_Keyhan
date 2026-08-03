"""
Author: Keyhan Khodabandehlou
Last updated: July 30 2026
Description:
Reads the FIFA World Cup CSV file and displays every match 
record associated with one selected player ID
"""

import csv

# Name of the CSV dataset file
FILE_NAME = "fifa_world_cup_2026_player_performance.csv"

# Player ID to search for
PLAYER_ID = input("Enter a player ID: ").strip()

# Open the CSV file and read each row as a dictionary
with open(FILE_NAME, "r", encoding="utf-8-sig") as csv_file:
    reader = csv.DictReader(csv_file)


    # Traverses every row in the datasheet
    for row in reader:

        # Display the row only if its player ID matches the selected ID
        if row["player_id"] == PLAYER_ID:
            print(
                row["player_id"],
                row["player_name"],
                row["team"],
                row["position"],
                row["match_id"],
                row["player_rating"]
            )