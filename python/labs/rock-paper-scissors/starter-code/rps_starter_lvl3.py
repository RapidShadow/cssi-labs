#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
ties = 0
computerWins = 0
personWins = 0

def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    person = raw_input("Please Enter r for rock, p for paper and s for Scissors ")

    if person.lower() == "r":
        return "ROCK"
    elif person.lower() == "p":
        return "PAPER"
    else:
        return "SCISSORS"

def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    computer = random.randint(1,3)
    if computer == 1:
        return "ROCK"
    elif computer == 2:
        return "PAPER"
    else:
        return "SCISSORS"
def determine_winner():
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    PersonMove = get_player_move()
    ComputerMove = get_computer_move()
    if PersonMove == ComputerMove :
        ties = (ties + 1)
        print("You tie")
        return "TIE"
    elif PersonMove == "PAPER" and ComputerMove == "SCISSORS":
        computerWins = (computerWins + 1)
        print("You lose")
        return "WIN"
    elif PersonMove == "PAPER" and ComputerMove == "ROCK":
        personWins = (personWins + 1)
        print("You win")
        return "LOSE"
    elif PersonMove == "SCISSORS" and ComputerMove == "PAPER":
        personWins = (personWins + 1)
        print("You win")
        return "LOSE"
    elif PersonMove == "SCISSORS" and ComputerMove == "ROCK":
        computerWins = (computerWins + 1)
        print("You lose")
        return "WIN"
    elif PersonMove == "ROCK" and ComputerMove == "PAPER":
        computerWins = (computerWins + 1)
        print("You lose")
        return "WIN"
    else:
        personWins = (personWins + 1)
        print("You win")
        return "LOSE"
determine_winner()
# def print_scoreboard(player_wins, comp_wins, ties):
#     """Prints out the scoreboard neatly.  Returns nothing."""
# def get_move_name(short_move):
#     """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
#     'Scissors' respectively. Use this to neatly print move choices"""
#
#     # TODO
# print(get_player_move())
#
# # Write your code below - make RPS happen using the functions above!
