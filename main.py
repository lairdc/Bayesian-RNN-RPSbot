import pygame
from game import Game
from gui import GUI

def main():
    pygame.init()
    game = Game()
    gui = GUI(game)
    gui.run()

if __name__ == "__main__":
    main()
