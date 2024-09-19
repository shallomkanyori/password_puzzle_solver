# Password Puzzle Solver
![Pasword Puzzle Solver start screen](https://github.com/shallomkanyori/password_puzzle_solver/blob/master/docs/images/feature1.png?raw=true)
Welcome to Password Puzzle Solver, a web-based game that challenges players to decrypt hidden passwords in a terminal-like interface. You can access the game here: [https://password-puzzle-solver.vercel.app/](https://password-puzzle-solver.vercel.app/).

This is my foundations portfolio project for the ALX software engineering program. Learn more about how I built this project [here](https://medium.com/@shallomkanyori/password-puzzle-solver-my-portfolio-project-journey-29ac9e744c45). You can also check out my [LinkedIn](https://www.linkedin.com/in/shallom-kanyori-613148254/).

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Contributing](#contributing)
- [License](#license)

## About the Project

Password Puzzle Solver is an engaging and educational game where players attempt to guess a hidden password by suggesting letters. The game features a hacker-themed terminal interface, a unique twist to the classic game Hangman.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (version 3.8+)
- MongoDB (version 4.3+)

### Installation

To install and run this app, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Ensure you have `mongod` running.
4. Install the required dependencies by running the command `pip install -r requirements.txt`.
5. If this is your first time, run `python populate_dp.py` to have some words to work with.
6. You can set the `MONGODB_URI` environment variable (default is `mongodb://localhost:27017`).
7. You can run the app using the command `python app.py`.
8. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the game.

Enjoy playing Password Puzzle Solver!

## How to Play

1. Open your web browser and navigate to [http://web-01.thayu.tech/password-puzzle](http://web-01.thayu.tech/password-puzzle).
2. Select your desired difficulty to start the game.
3. Guess letters to reveal the hidden password.
4. Try to beat your best score.
5. Enjoy the challenge and have fun!

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:
1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature-name.
3. Make your changes and commit them: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature/your-feature-name.
5. Create a pull request.

## License

This project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).
