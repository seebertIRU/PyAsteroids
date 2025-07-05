import sys
import pygame
import constants
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
	initresult=pygame.init()
	if initresult[1] != 0:
		raise Exception("Failed to initialize PyGame")
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	screen=pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	screen.fill(pygame.Color(0, 0, 0)) # black
	clock=pygame.time.Clock()
	playerx=constants.SCREEN_WIDTH // 2
	playery=constants.SCREEN_HEIGHT // 2	
	updateable=pygame.sprite.Group()
	drawable=pygame.sprite.Group()
	asteroids=pygame.sprite.Group()
	shots=pygame.sprite.Group()

	Asteroid.containers=(asteroids, updateable, drawable)
	Shot.containers=(updateable, drawable, shots)
	AsteroidField.containers=updateable
	asteroid_field=AsteroidField()

	Player.containers=(updateable, drawable)
	plr=Player(playerx, playery)
	pygame.display.flip()
	dt=0
	while True:
		dt+=clock.tick(constants.FPS) / 1000	
		updateable.update(dt)
		for asteroid in asteroids:
			if asteroid.collide(plr):
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			killshots=False
			for shot in shots:	
				if asteroid.collide(shot):
					asteroid.split()
					killshots=True
			if killshots:
				for shot in shots:
					shot.kill()
						
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
