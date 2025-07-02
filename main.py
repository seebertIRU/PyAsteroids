import sys
import pygame
import constants
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField



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
	updateable=pygame.sprite.Group()
	drawable=pygame.sprite.Group()
	asteroids=pygame.sprite.Group()
	shots=pygame.sprite.Group()
	Shot.containers=(updateable, drawable, shots)
	Asteroid.containers=(updateable, drawable, asteroids)
	Player.containers=(updateable, drawable)
	AsteroidField.containers=(updateable,)
	plr=Player(playerx, playery)
	asteroid_field=AsteroidField()
	pygame.display.flip()
	clk=pygame.time.Clock()
	dt=0
	while True:
		dt+=clk.tick(constants.FPS) / 1000	
		updateable.update(dt)
		for asteroid in asteroids:
			if asteroid.collide(plr):
				print("Game over!")
				sys.exit()
		screen.fill(pygame.Color(0, 0, 0)) # black
		for drawableitem in drawable:
			drawableitem.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				return
			elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
				return


if __name__ == "__main__":
	main()
