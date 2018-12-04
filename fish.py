import pygame
WHITE = (255, 255, 255)
 
class Fish(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.direction = "Left"
        self.toFlip = False
        self.level = 1
        # Draw the car (a rectangle!)
        # pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Instead we could load a proper pciture of a car...
        self.image = pygame.image.load("fish{}.png".format(self.level)).convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveHorizontal(self, pixels):
        self.rect.x += pixels

    def moveVertical(self, pixels):
        self.rect.y += pixels

    def changeDirection(self, direction):
        # print(self.toFlip)
        if(self.direction != direction):
            if self.toFlip == False:
                self.toFlip = True
            else:
                self.toFlip = False

            self.direction = direction
            print(self.direction)
            self.image = pygame.transform.flip(self.image, self.toFlip, False)
            self.toFlip = False

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.rect.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.rect.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.rect.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.rect.x -= dist # move left

    def levelUp(self):
        self.level += 1
        # self.image = pygame.image.load("fish{}.png".format(self.level)).convert_alpha()
        # print("Direction: " + self.direction)
        if self.direction == "Left":
            self.image = pygame.image.load("fish{}_flip.png".format(self.level)).convert_alpha()
        else:
            self.image = pygame.image.load("fish{}.png".format(self.level)).convert_alpha()
        
    def repaint(self, color):
        self.color = color
        surface.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
