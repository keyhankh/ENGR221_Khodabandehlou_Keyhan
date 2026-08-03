"""
Author: Keyhan Khodabandehlou
Last updated: July 30 2026
Description:
Opens the FIFA World Cup player dataset and prints all
column names so they can be used correctly in the project.
"""

import csv


# Name of the CSV dataset file
FILE_NAME = "fifa_world_cup_2026_player_performance.csv"


# Open the CSV file and read its first row
with open(FILE_NAME, "r", encoding="utf-8-sig") as csv_file:
    reader = csv.reader(csv_file)

    # The first row contains the column headings
    column_names = next(reader)


# Display each column name on a separate line
print("CSV columns:")

for column in column_names:
    print(column)