# FIFA World Cup Player Performance System

## Author

Keyhan Khodabandehlou

## Description

This project is a Python program that manages and analyzes FIFA World Cup 2026 player performance data.

The program reads player information from a CSV file and stores each unique player in a Python dictionary. The dictionary works as a hash table, where the player ID is the key and the `Player` object is the value.

The program allows the user to search for players, add players, delete players, display player records, search by team or position, and view the highest-rated players.

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