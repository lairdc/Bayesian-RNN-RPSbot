import pygame
import sys
from game import Game

class GUI:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Rock Paper Scissors Game")
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(None, 40)
        self.big_font = pygame.font.SysFont(None, 100)  # Bigger font for question mark
        self.running = True
        self.waiting_for_prediction = True  # Track if the bot is predicting

        self.user_pick = None  # Store the user's pick to display instead of the question mark
        self.question_mark = "?"  # Question mark symbol for when no pick is made

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)  # 30 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Allow the player to pick a move only after the bot has predicted
            if event.type == pygame.MOUSEBUTTONDOWN and not self.waiting_for_prediction:
                x, y = event.pos
                self.process_move_selection(x, y)

    def process_move_selection(self, x, y):
        """Process player's move based on where they clicked (Rock, Paper, or Scissors)."""
        if self.game.round_result is not None:
            return  # Ignore inputs until the round is reset

        if 25 <= x <= 125 and 400 <= y <= 500:  # Rock button position
            player_move = 0
        elif 150 <= x <= 250 and 400 <= y <= 500:  # Paper button position
            player_move = 1
        elif 275 <= x <= 375 and 400 <= y <= 500:  # Scissors button position
            player_move = 2
        else:
            return  # Invalid selection

        print("picked", player_move)
        sys.stdout.flush()

        # Play the round after a valid move is selected
        self.user_pick = ['Rock', 'Paper', 'Scissors'][player_move]  # Update user pick display
        self.game.play_round(player_move)
        self.waiting_for_prediction = True  # Block new input until next prediction

    def update(self):
        """Update the game state."""
        if self.waiting_for_prediction:
            self.game.bot_predict_move()  # Ensure bot makes a prediction
            self.waiting_for_prediction = False  # Allow player to pick a move after bot predicts
        elif self.game.round_result is not None:
            pygame.time.delay(1000)  # 1-second delay before resetting
            self.game.reset_round()  # Reset round and make the bot predict
            self.user_pick = None  # Reset user pick back to question mark

    def draw(self):
        """Draw the game state."""
        self.screen.fill((48, 150, 48))  # Background color

        # Display bot prediction, round result, and the score record
        if self.game.bot_move is not None:
            bot_move_text = self.big_font.render(f"{['Rock', 'Paper', 'Scissors'][self.game.bot_move]}", True, (0, 0, 0))
            self.screen.blit(bot_move_text, (650, 280))

        if self.game.round_result is not None:
            result_text = self.font.render(f"Result: {self.game.round_result}", True, (0, 0, 0))
            self.screen.blit(result_text, (50, 100))

        # Display the win/tie/loss record
        score_text = self.font.render(f"Bot W/T/L: {self.game.loss_count}/{self.game.tie_count}/{self.game.win_count}", True, (0, 0, 0))
        self.screen.blit(score_text, (50, 150))

        # Display move options for the player
        self.draw_move_options()

        vs_text = self.big_font.render(f'VS', True, (0,0,0))
        self.screen.blit(vs_text, (460, 280))

    def draw_move_options(self):
        """Draw the clickable options for Rock, Paper, Scissors."""
        # Display a big question mark (or the user's pick) above the options
        if self.user_pick:
            pick_text = self.big_font.render(self.user_pick, True, (0, 0, 0))  # Display user's pick
        else:
            pick_text = self.big_font.render(self.question_mark, True, (0, 0, 0))  # Display question mark

        self.screen.blit(pick_text, (100, 280))  # Center the text above the buttons

        # Draw buttons for Rock, Paper, and Scissors on the left and moved down a bit
        pygame.draw.rect(self.screen, (200, 0, 0), (25, 400, 100, 100))  # Rock button
        rock_text = self.font.render("Rock", True, (255, 255, 255))
        self.screen.blit(rock_text, (40, 435))

        pygame.draw.rect(self.screen, (0, 200, 0), (150, 400, 100, 100))  # Paper button
        paper_text = self.font.render("Paper", True, (255, 255, 255))
        self.screen.blit(paper_text, (160, 435))

        pygame.draw.rect(self.screen, (0, 0, 200), (275, 400, 100, 100))  # Scissors button
        scissors_text = self.font.render("Scissor", True, (255, 255, 255))
        self.screen.blit(scissors_text, (275, 435))
