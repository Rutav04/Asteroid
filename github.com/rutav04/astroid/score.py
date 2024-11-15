import time
import pygame
from constants import *

class Score:
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.last_time_check = time.time()

    def asteroid_destroyed(self):
        self.total_score += ASTEROID_KILL
    
    def time_up(self):
        self.total_score += SURVIVED

    def display_score(self):
        # You might want a method to display the score on-screen using pygame
        # Example:
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.total_score}", True, (255, 255, 255))
        return score_text
    
    def update(self):
        current_time = time.time()
        if current_time - self.last_time_check >= 10:
            self.time_up()
            self.last_time_check = current_time