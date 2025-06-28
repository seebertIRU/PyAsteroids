import pygame
import constants
import circleshape
import player
def main():
	initresult=pygame.init()
	if initresult[1] != 0:
		raise Exception("Failed to initialize PyGame")
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	screen=pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	screen.fill(pygame.Color(0, 0, 0)) # black
	playerx=constants.SCREEN_WIDTH // 2
	playery=constants.SCREEN_HEIGHT // 2	
	plr=player.Player(playerx, playery)
	print(plr.rotation)
	pygame.display.flip()
	clk=pygame.time.Clock()
	dt=0
	while True:
		plr.draw(screen)
		plr.update(dt)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				return
			elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
				return
		dt+=clk.tick(constants.FPS) / 1000	

if __name__ == "__main__":
	main()
