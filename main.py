#!/usr/bin/env python3
"""
Rock, Paper, Scissors Game Backend
A simple Flask backend for a Rock, Paper, Scissors game.
It serves the static HTML file and provides an API endpoint for gameplay.
"""

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    # Define winning combinations: rock beats scissors, scissors beats paper, paper beats rock
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if wins[player] == computer:
        return "You win!"
    else:
        return "You lose!"

@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

@app.route("/play", methods=["GET"])
def play():
    player_move = request.args.get("move", "").lower()
    if player_move not in ["rock", "paper", "scissors"]:
        return jsonify({"error": "Invalid move. Please choose rock, paper, or scissors."}), 400
    computer_move = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(player_move, computer_move)
    return jsonify({
        "player_move": player_move,
        "computer_move": computer_move,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
