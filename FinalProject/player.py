"""
Author: Keyhan Khodabandehlou
Last updated: July 30 2026
Description:
Defines the Player class used to store information about
one FIFA World Cup player.
"""


class Player:
    """Represents one player and their performance data."""

    def __init__(
        self,
        player_id: str,
        player_name: str,
        team: str,
        position: str,
        age: int,
        goals: int,
        assists: int,
        player_rating: float
    ) -> None:
        # Store the player's identifying information
        self.player_id = player_id
        self.player_name = player_name
        self.team = team
        self.position = position
        self.age = age

        # Store the player's performance statistics
        self.goals = goals
        self.assists = assists
        self.player_rating = player_rating

    def __str__(self) -> str:
        """Returns the player's information in a readable format."""

        return (
            f"ID: {self.player_id}\n"
            f"Name: {self.player_name}\n"
            f"Team: {self.team}\n"
            f"Position: {self.position}\n"
            f"Age: {self.age}\n"
            f"Goals: {self.goals}\n"
            f"Assists: {self.assists}\n"
            f"Tournament rating: {self.player_rating}"
        )