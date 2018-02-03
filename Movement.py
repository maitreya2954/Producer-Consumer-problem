import time
import random
import threading
import pygame, sys
from pygame.locals import *

#initialize the pygame
pygame.init()

#initialize the font in pygame
pygame.font.init()

smallfont = pygame.font.SysFont('comicsansms',40)   #Setting up font details of the text
mediumfont = pygame.font.SysFont('comicsansms',50)  #Setting up font details of the text
largefont = pygame.font.SysFont('comicsansms',80)   #Setting up font details of the text

ProImageR = "./Images/Producer/GoRight/cycle10" 	 #Setting path for animation sequence of Producer Right
ProImageL = "./Images/Producer/GoLeft/cycle10"  	 #Setting path for animation sequence of Producer Left
ProImageLF = "./Images/Producer/GoLeftFull/cycle10"  #Setting path for animation sequence of Producer Left
Back = "./Images/Back2.jpg"                    		 #Setting path background image

ConImageR = "./Images/Consumer/GoRight/Animated Walk and Skip Cycles-20"    #Setting up path for consumer animaiton sequence (Right)
ConImageL = "./Images/Consumer/GoLeft/consumer0"                            #Setting up path for consumer animaiton sequence (Left)
ConImageRE = "./Images/Consumer/GoRightEmpty/consumer0"    					#Setting up path for consumer animaiton sequence (Right)

#SysFont(FONT TYPE,SIZE)
#set font type and size of APPLE on fridge
myfont = pygame.font.SysFont('Comic', 50)

#set font type and size of Consumer_id
myfont2 = pygame.font.SysFont('Comic',35)

myfont3 = pygame.font.SysFont('Comic',35)

#display height and width
display_width = 1000
display_height = 562

Fridge_X_cord = display_width/3 + 50
Fridge_Y_cord = 3.5*display_height/7 - 50
Apple_text_X_Cord = Fridge_X_cord + 120
Apple_text_Y_Cord = Fridge_Y_cord - 30
Consumer_Left_Extreme = Fridge_X_cord + (display_width/7)
Consumer_Right_Extreme = display_width
Producer_Right_Extreme = Fridge_X_cord - (display_width/30)
Producer_Left_Extreme = -100
Capacity = 1
apple_count = 0
Consumer_text_offset_x = 60
Consumer_text_offset_Y = 100
Producer_text_offset_x = 110
Producer_text_offset_Y = -20

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PRODUCER-CONSUMER-SYNCHRONISATION_PROBLEM')

#set the Number of frames
PROD_FRAMES = 60
CON_FRAMES = 30
PROD_RATIO = 3
CON_RATIO = 3
PROD_SPEED = 4
CON_SPEED = 6

#set the black and white colors
black = (0,0,0)
white = (255,255,255)
green = (0,155,0)
red = (255,0,0)

clock = pygame.time.Clock()

#initial image of Lady
Lady_Image = pygame.image.load('./Images/Fridge1.png')

#initial image of Fridge
Fridge = pygame.image.load('./Images/Fridge1.png')
Background = pygame.image.load(Back)
Background = pygame.transform.scale(Background,(display_width,display_height))
Full = pygame.image.load('./Images/FULL.png')
#reduce the size of the fridge
Fridge = pygame.transform.scale(Fridge, (display_width/5,display_width/5))
Full = pygame.transform.scale(Full,(200,100))
Empty = pygame.image.load('./Images/EMPTY.png')
Empty = pygame.transform.scale(Empty,(200,100))

#This function defines the movement of the consumer walking to the right direction
def Consumer_Go_Right_Empty(X_cord,Y_cord,consumer_no, Lady_Image):
	image_id = 0
	go_right = True
	global apple_count
	while(go_right):
		image_id = (image_id + 1) % 31
		if(X_cord < Consumer_Right_Extreme):
			Lady_Image = pygame.image.load(ConImageRE + str(image_id).zfill(2) + ".png")         #Load image of walking sequence
			Lady_Image = pygame.transform.scale(Lady_Image,(368/CON_RATIO,720/CON_RATIO))       #Scale the Lady_Image
			X_cord = X_cord + CON_SPEED                                                         #Move the X coordinate for movement

		else:
			go_right = False
			#RENDER(TEXT,ANTI ALIASING,COLOR)
			Apple_text = myfont.render('Apples: '+ str(apple_count), True, (173, 0, 0))
			Consumer_Number = myfont2.render('C'+ str(consumer_no), True, (173, 0, 0))

			#BLIT(OBJECT(text,image....etc),POSITION)
			gameDisplay.fill(white)
			gameDisplay.blit(Background,(0,0))                                  #For drawing background
			gameDisplay.blit(Lady_Image, (X_cord,Y_cord))                       #For drawing lady image
			gameDisplay.blit(Empty,(X_cord + 100,Y_cord +50))
			gameDisplay.blit(Fridge,(Fridge_X_cord ,Fridge_Y_cord))             #For drawing fridge
			gameDisplay.blit(Apple_text,(Apple_text_X_Cord,Apple_text_Y_Cord))  #For drawing the text that displays apple count
			gameDisplay.blit(Consumer_Number,(X_cord + Consumer_text_offset_x,Y_cord + Consumer_text_offset_Y)) #For drawing the text of customer ID

			pygame.display.update() #Update the Frame

			#number of frames
			clock.tick(CON_FRAMES)
			if(go_right == False):
				break
   
   	return(Consumer_Right_Extreme)


#This function defines the movement of the consumer walking to the right direction
def Consumer_Go_Right(X_cord,Y_cord,consumer_no, Lady_Image):
	image_id = 0
	go_right = True
	global apple_count
	#go right till he reaches fridge
	while(go_right):
		image_id = (image_id + 1) % 31

		if(X_cord < Consumer_Right_Extreme):
			Lady_Image = pygame.image.load(ConImageR + str(image_id).zfill(2) + ".png")         #Load image of walking sequence
			Lady_Image = pygame.transform.scale(Lady_Image,(368/CON_RATIO,720/CON_RATIO))       #Scale the Lady_Image
			X_cord = X_cord + CON_SPEED                                                         #Move the X coordinate for movement

		else:
			go_right = False
			#RENDER(TEXT,ANTI ALIASING,COLOR)
			Apple_text = myfont.render('Apples: '+ str(apple_count), True, (173, 0, 0))
			Consumer_Number = myfont2.render('C'+ str(consumer_no), True, (173, 0, 0))

			#BLIT(OBJECT(text,image....etc),POSITION)
			gameDisplay.fill(white)
			gameDisplay.blit(Background,(0,0))                                  #For drawing background
			gameDisplay.blit(Lady_Image, (X_cord,Y_cord))                       #For drawing lady image
			gameDisplay.blit(Fridge,(Fridge_X_cord ,Fridge_Y_cord))             #For drawing fridge
			gameDisplay.blit(Apple_text,(Apple_text_X_Cord,Apple_text_Y_Cord))  #For drawing the text that displays apple count
			gameDisplay.blit(Consumer_Number,(X_cord + Consumer_text_offset_x,Y_cord + Consumer_text_offset_Y)) #For drawing the text of customer ID

			pygame.display.update() #Update the Frame

			#number of frames
			clock.tick(CON_FRAMES)
			if(go_right == False):
				break
	return(Consumer_Right_Extreme)

#This function defines the movement of the consumer walking to the left direction
def Consumer_Go_Left(X_cord,Y_cord,consumer_no, Lady_Image):
	global apple_count
	image_id = 0
	left = True
	apple_count = apple_count - 1  #Decreasing the number of apples in fridge
	while(left):
		image_id = (image_id + 1) % 31
		if(X_cord > Consumer_Left_Extreme):
			Lady_Image = pygame.image.load(ConImageL +str(image_id).zfill(2)+".png")
			Lady_Image = pygame.transform.scale(Lady_Image,(368/CON_RATIO,720/CON_RATIO))
			X_cord = X_cord - CON_SPEED
		else:
			return(Consumer_Left_Extreme)
		#RENDER(TEXT,ANTI ALIASING,COLOR)
		Apple_text = myfont.render('Apples: '+ str(apple_count), True, (173, 0, 0))
		Consumer_Number = myfont2.render('C'+ str(consumer_no), True, (173, 0, 0))
		gameDisplay.fill(white)
		#BLIT(OBJECT(text,image....etc),POSITION)
		gameDisplay.blit(Background,(0,0))
		gameDisplay.blit(Lady_Image, (X_cord,Y_cord))
		gameDisplay.blit(Fridge,(Fridge_X_cord ,Fridge_Y_cord))
		gameDisplay.blit(Apple_text,(Apple_text_X_Cord,Apple_text_Y_Cord))
		gameDisplay.blit(Consumer_Number,(X_cord + Consumer_text_offset_x,Y_cord + Consumer_text_offset_Y))

		pygame.display.update()

		#number of frames
		clock.tick(CON_FRAMES)
            

#This function defines the movement of the producer walking to the right direction
def Produce_Go_Right(X_cord,Y_cord,producer_no, Lady_Image):
	global apple_count
	image_id = 0
	go_right = True
	while(go_right):
		image_id = (image_id + 1) % 33
		if(X_cord < Producer_Right_Extreme):
			Lady_Image = pygame.image.load(ProImageR+str(image_id).zfill(2)+".png")
			Lady_Image = pygame.transform.scale(Lady_Image,(368/PROD_RATIO,720/PROD_RATIO))
			X_cord = X_cord + PROD_SPEED
		else:
			go_right = False
		# print(X_cord)
		#RENDER(TEXT,ANTI ALIASING,COLOR)
		Apple_text = myfont.render('Apples: '+ str(apple_count), True, (173, 0, 0)) #Text to display the count of apples
		Producer_Number = myfont3.render('P'+ str(producer_no), True, (173, 0, 0))
		gameDisplay.fill(white)

		#BLIT(OBJECT(text,image....etc),POSITION)
		gameDisplay.blit(Background,(0,0))
		gameDisplay.blit(Lady_Image, (X_cord,Y_cord))
		gameDisplay.blit(Fridge,(Fridge_X_cord,Fridge_Y_cord))
		gameDisplay.blit(Apple_text,(Apple_text_X_Cord,Apple_text_Y_Cord))
		gameDisplay.blit(Producer_Number,(X_cord + Producer_text_offset_x,Y_cord + Producer_text_offset_Y))
		pygame.display.update()

		#number of frames
		clock.tick(PROD_FRAMES)
		if(go_right == False):
			break
	apple_count = apple_count + 1 #Increases the apple count in the fridge
	return(X_cord,apple_count)


#This function defines the movement of the producer walking to the left direction
def Producer_Go_Left_Full(X_cord,Y_cord,producer_no, Lady_Image):
	global apple_co
	image_id = 0
	left = True

	while(left):
		image_id = (image_id + 1) % 33
		if(X_cord >= Producer_Left_Extreme):
			Lady_Image = pygame.image.load(ProImageLF+str(image_id).zfill(2)+".png")
			Lady_Image = pygame.transform.scale(Lady_Image,(368/PROD_RATIO,720/PROD_RATIO))
			X_cord = X_cord - PROD_SPEED
		else:
			return X_cord
		#RENDER(TEXT,ANTI ALIASING,COLOR)
		Apple_text = myfont.render('Apples: '+ str(apple_count), True, (173, 0, 0))
		Producer_Number = myfont3.render('P'+ str(producer_no), True, (173, 0, 0))
		gameDisplay.fill(white)
		#BLIT(OBJECT(text,image....etc),POSITION)
		gameDisplay.blit(Background,(0,0))
		gameDisplay.blit(Lady_Image, (X_cord,Y_cord))
		gameDisplay.blit(Full,(X_cord-100,Y_cord-70))
		gameDisplay.blit(Fridge,(Fridge_X_cord,Fridge_Y_cord))
		gameDisplay.blit(Apple_text,(Apple_text_X_Cord,Apple_text_Y_Cord))
		gameDisplay.blit(Producer_Number,(X_cord + Producer_text_offset_x,Y_cord + Producer_text_offset_Y))
		pygame.display.update()
		#number of frames
		clock.tick(PROD_FRAMES)


#This function defines the movement of the producer walking to the left direction
def Producer_Go_Left(X_cord,Y_cord,producer_no, Lady_Image):
	global apple_co
	image_id = 0
	left = True
	while(left):
		image_id = (image_id + 1) % 33
		if(X_cord >= Producer_Left_Extreme):
			Lady_Image = pygame.image.load(ProImageL+str(image_id).zfill(2)+".png")
			Lady_Image = pygame.transform.scale(Lady_Image,(368/PROD_RATIO,720/PROD_RATIO))
			X_cord = X_cord - PROD_SPEED
		else:
			return X_cord

		#RENDER(TEXT,ANTI ALIASING,COLOR)
		Apple_text = myfont.render('Apples: '+ str(apple_count), True, (173, 0, 0))
		Producer_Number = myfont3.render('P'+ str(producer_no), True, (173, 0, 0))
		gameDisplay.fill(white)
		#BLIT(OBJECT(text,image....etc),POSITION)
		gameDisplay.blit(Background,(0,0))
		gameDisplay.blit(Lady_Image, (X_cord,Y_cord))
		gameDisplay.blit(Fridge,(Fridge_X_cord,Fridge_Y_cord))
		gameDisplay.blit(Apple_text,(Apple_text_X_Cord,Apple_text_Y_Cord))
		pygame.display.update()
		#number of frames
		clock.tick(PROD_FRAMES)

def text_objects(msg,color,size):
    if size == 'small':
        textSurface = smallfont.render(msg,True,color)
        return textSurface, textSurface.get_rect()
    elif size == 'medium':
        textSurface = mediumfont.render(msg,True,color)
        return textSurface, textSurface.get_rect()
    elif size == 'large':
        textSurface = largefont.render(msg,True,color)
        return textSurface, textSurface.get_rect()


def message_to_screen(msg,color,x_displace = -50, y_displace = 0, size='small'):
    textSurf,textRect = text_objects(msg,color,size)
    # => get_rect().center returns a rectangle covering the surface, in this case it's the text ones
    textRect.center = (display_width/2) + x_displace , (display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

#This funtion used to display the start screen when ever called
def StartScreen():
    intro = True
    while intro:
        gameDisplay.fill(white)
        message_to_screen('Welcome!', green , y_displace= -150, size='medium')
        message_to_screen('To', green , y_displace= -50, size='medium')
        message_to_screen('Producer-Consumer-Synchronization-Problem', green , y_displace= 50, size='medium')
        message_to_screen('Press any Key to start!',red, y_displace = 250, size='small')
        message_to_screen('Press q to quit!',red, y_displace = 300, size='small')
        pygame.draw.circle(gameDisplay, red, [910, 550], 400, 10)
        pygame.display.update()
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                intro = False
            if event.type == KEYDOWN:
                if event.key == K_q:   #If key pressed is 'Q'
                    pygame.quit()
                    sys.exit()