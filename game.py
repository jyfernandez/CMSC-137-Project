# import the pygame module, so you can use it
import pygame
import random
import socket
from fish import Fish

pygame.init()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
bright_blue = (255,0,0)

screen = pygame.display.set_mode((800,521))
logo = pygame.image.load("resistance.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Fish Eat Fish")

display_width = 800
display_height = 521

clock = pygame.time.Clock()
 
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def button(msg,x,y,width,height,inactColor,actColor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, actColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, inactColor,(x,y,width,height))

    smallText = pygame.font.Font('./Fonts/GRUNJA__.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def how_to_play():
	print("How to play")

def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		
		image = pygame.image.load("menu_bg.jpg")  #changes the bg of the menu
		screen.blit(image, (0,0)) #places the image in the position(0,0)
		largeText = pygame.font.Font('./Fonts/CHOPS___.ttf',115) #using font chops size 115
		TextSurf, TextRect = text_objects("Fish eat Fish", largeText) # create a rectangle with the text "Fish eat Fish" written in chops font inside
		TextRect.center = ((display_width/2),(display_height/2)-100) # place the rectangle in the center
		screen.blit(TextSurf, TextRect) #show the rectangle

		#parameter: (where to place, color, (x,y,width, height))
		mouse = pygame.mouse.get_pos()
		
		button("START",(display_width/2)-50,(display_height/2)+50,100,50,blue,bright_blue,main)
		button("How to Play",(display_width/2)-100,(display_height/2)+110,200,50,blue,bright_blue,how_to_play)
		button("QUIT",(display_width/2)-50,(display_height/2)+170,100,50,blue,bright_blue,quit)

		pygame.display.update()
		clock.tick(15)


def random_fish_spawn():
	print("Fish spawn")

def getFishPoints(player, score):
	if(score == 7):
		player.levelUp()
		score += 1
	elif (score == 14):
		player.levelUp()
		score += 1

# define a main function
def main():
	UDP_IP_ADDRESS = "127.0.0.1"
	UDP_PORT_NO = 6789
	print("GOT IT")

	serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    # initialize the pygame module
   
    # create a surface on screen that has the size of 240 x 180
	image = pygame.image.load("underwaterbg.jpg")
	image3 = pygame.image.load("fish1.png")
    # blit image to screen
    
    # define a variable to control the main loop
	running = True
	x_change = 0 #change in the x position of player1
	x_change2 = 0 #change in the x position of player2
	y_change = 0 #change in the y position of player1
	y_change2 = 0 #change in the y position of player2
	
	size = 1 #sample size of the fish

	all_sprites_list = pygame.sprite.Group() #creates a list of sprites
	block_list = pygame.sprite.Group()
 
	# playerFish = Fish(bright_blue, 45, 45) #parameters: (color of the rect, width, height)
	# playerFish.rect.x = 50 # initial x pos
	# playerFish.rect.y = 50 # initial y pos
	playerCar2 = Fish(bright_blue, 45, 45)
	playerCar2.rect.x = 100
	playerCar2.rect.y = 50
	 
	# Add the car to the list of objects
	all_sprites_list.add(playerFish)
	all_sprites_list.add(playerCar2)
	block_list.add(playerCar2)

	for i in range(50):
	    # This represents a block
	    block = Fish(black, 20, 15)
	 
	    # Set a random location for the block
	    block.rect.x = random.randrange(800)
	    block.rect.y = random.randrange(521)
	 
	    # Add the block to the list of objects
	    block_list.add(block)
	    all_sprites_list.add(block)

	score = 0

    # main loop
	while running:
		# only do something if the event is of type QUIT
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
		# change the value to False, to exit the main loop
			running = False
			quit()

		playerFish.handle_keys()
		playerCar2.handle_keys()
		# data, addr = serverSock.recvfrom(1024)
		# print("Message: " + data.decode())

		all_sprites_list.update() #updates the list with all the changes made.
		blocks_hit_list = pygame.sprite.spritecollide(playerFish, block_list, True)
		for block in blocks_hit_list:
		    score +=1
		    getFishPoints(playerFish, score)
		    print(score)

		# updates the background with the starting index in the window: (0,0)
		screen.blit(image, (0,0))
		all_sprites_list.draw(screen) #draws all the sprites that are inside the list

		# update the screen to make the changes visible (fullscreen update)
		pygame.display.update()
		# amount of time before the screen updates
		clock.tick(500)
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    game_intro()