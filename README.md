# Rock, Paper, Scissors Game

A simple web-based Rock, Paper, Scissors game with a Python Flask backend and HTML/JavaScript frontend.

## Description

This project implements the classic Rock, Paper, Scissors game where players compete against the computer. The application consists of:

- A Flask backend that handles game logic and serves the web interface
- A responsive HTML/CSS frontend styled with Bootstrap
- JavaScript for interactive gameplay without page reloads

## Features

- Clean, modern user interface
- Real-time game results
- Displays both player and computer moves
- Responsive design that works on desktop and mobile devices

## Installation

### Prerequisites

- Python 3.6 or higher
- Flask

### Setup

1. Clone this repository or download the files:

```bash
git clone https://github.com/yourusername/rock-paper-scissors.git
cd rock-paper-scissors
```

2. Install required dependencies:

```bash
pip install flask
```

## Usage

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Click on one of the three buttons (Rock, Paper, or Scissors) to make your move.

## How to Play

- Select your move by clicking one of the buttons: Rock, Paper, or Scissors
- The computer will randomly select its move
- The result will be displayed on the screen
- Game rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
  - Same moves result in a tie

## Project Structure

```
rock-paper-scissors/
├── app.py          # Flask backend application
├── index.html      # Frontend HTML file
└── README.md       # This file
```

## Customization

You can customize the game by:

- Modifying the styles in the `<style>` section of `index.html`
- Adding new features to the Flask backend in `app.py`
- Extending the game logic in the `determine_winner` function

## Development

To run the application in development mode:

```bash
flask run --debug
```

This enables hot reloading so changes to the code will be reflected immediately.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

