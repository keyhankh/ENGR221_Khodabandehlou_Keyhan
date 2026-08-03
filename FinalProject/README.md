# FIFA World Cup Player Performance System

## Author

Keyhan Khodabandehlou

## Description

This project is a Python program that manages and analyzes FIFA World Cup 2026 player performance data.

The program reads player information from a CSV file and stores each unique player in a Python dictionary. The dictionary works as a hash table, where the player ID is the key and the `Player` object is the value.

The program allows the user to search for players, add players, delete players, display player records, search by team or position, and view the highest-rated players.


## Runtime Analysis

Search by player ID: O(1) average case
Insert player: O(1) average case
Delete player: O(1) average case
Display all players: O(n)
Search by team: O(n)
Search by position: O(n)
Find top-rated player: O(n)
Sort and display top players: O(nlogn)


## Dataset

The program uses the following dataset:

`fifa_world_cup_2026_player_performance.csv`

The dataset contains information such as:

- Player ID
- Player name
- National team
- Position
- Age
- Goals
- Assists
- Tournament rating


## Data Structure

The main data structure used in this project is a hash table, implemented with a Python dictionary.

Each player ID is used as a key:

```python
self.players[player.player_id] = player



## How to Use the Program

When the program starts, it loads the player data from the CSV file and displays a menu.

Enter the number for the option you want to use, each correlating with an action. 


Choose option 1, Enter the player ID:

Choose option 2, then enter the new player’s information.

Choose option 3, then enter the player ID you want to remove.

Choose option 4 to display every player stored in the system.

Choose option 5, then enter a national team.

Choose option 6, then enter one of the following positions: Goalkeeper, Defender, Midfielder, Forward

Choose option 7 to display the player with the highest tournament rating.

Choose option 8 to display the ten players with the highest tournament ratings.

Choose option 9 to close the program.