# Nim Game

This Python script implements the game of Nim, where two players take turns removing objects from piles. The game is designed to be played against a Q-learning AI, which learns and improves its strategy through self-play.

## Example Usage

```bash
python nim.py
```

This example demonstrates training the AI with 10,000 games and then allowing a human player to play against the trained AI.

### Nim Class (`nim.py`)

- **Initialization**: The `Nim` class initializes the game board with a list of piles and tracks the current player and the winner.

- **Available Actions**: The `available_actions` method generates all possible actions for a given state.

- **Other Player**: The `other_player` method returns the player opposite to the given player.

- **Switch Player**: The `switch_player` method switches the current player.

- **Move**: The `move` method executes a move for the current player, updating the game state and checking for a winner.

### NimAI Class (`nim.py`)

- **Initialization**: The `NimAI` class initializes the Q-learning AI with a Q-value dictionary, a learning rate (`alpha`), and an exploration rate (`epsilon`).

- **Update**: The `update` method updates the Q-values based on the old state, action taken, new state, and the reward received.

- **Q-value Methods**: `get_q_value` retrieves the Q-value for a given state-action pair, and `update_q_value` updates the Q-value using the Q-learning formula.

- **Best Future Reward**: The `best_future_reward` method returns the maximum Q-value for a given state. It can also return the corresponding action.

- **Choose Action**: The `choose_action` method selects an action for the current state, considering exploration with probability `epsilon`.

### Training Function (`train`)

- The `train` function trains the Q-learning AI by playing a specified number of games against itself.

### Play Function (`play`)

- The `play` function allows a human player to play against the trained AI. The human player can choose to move first or second.

### Running the Code

To use the code, an AI is trained using the `train` function (e.g., `ai = train(10000)`), and then a human player can play against the trained AI using the `play` function (e.g., `play(ai)`). The game state is displayed after each move, and the winner is determined at the end of the game. The AI learns and improves its strategy during training.

