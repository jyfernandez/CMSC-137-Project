import pygame
WHITE = (255, 255, 255)
 
class Car(pygame.sprite.Sprite):
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

    # def eat():

    def levelUp(self):
        self.level += 1
        self.image = pygame.image.load("fish{}.png".format(self.level)).convert_alpha()
        if self.direction == "Left":
            self.changeDirection("Left")
        
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
