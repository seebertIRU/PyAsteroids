import pygame
import constants

def main():
	initresult=pygame.init()
	if initresult[1] != 0:
		raise Exception("Failed to initialize PyGame")
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	screen=pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	screen.fill(pygame.Color(0, 0, 0)) # black
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				return


if __name__ == "__main__":
	main()
