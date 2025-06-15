class Settings:
    def __init__(self):
        # Game constants
        self.GAME_WIDTH = 1000 # Width of the game window, in pixels
        self.GAME_HEIGHT = 700 # Height of the game window, in pixels
        self.SPEED = 75 # Initial game speed (higher = slower, lower = faster)
        self.SPACE_SIZE = 25 # Size of all game components as rendered in the game window (lower = smaller, higher = larger)
        self.BODY_PARTS = 3 # Number of initial snake body parts
        self.SNAKE_COLOR = "#00FF00" # Snake body color
        self.FOOD_COLOR = "#FF0000" # Snake food color
        self.BACKGROUND_COLOR = "#000000" # Color of the game background
        # Game variables