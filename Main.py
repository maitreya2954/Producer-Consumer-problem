import time
import random
import threading
import pygame, sys
from pygame.locals import *
from Movement import *

#SETTING UP THE PATHS FOR SOUNDS
FullHouse = './Sounds/full-house-Final.mp3'
Nil = './Sounds/Empty-final.mp3'
BGM = './Sounds/BGM.mp3'
# Empty = pygame.image.load('./Images/EMPTY.png')
# gameDisplay = pygame.display.set_mode((display_width,display_height))
# gameDisplay.blit(Empty, (0,0))
# pygame.display.update()
#LOADING THE BACKGROUND
pygame.mixer.music.load(BGM)
pygame.mixer.music.play()
f = open('Event.txt','a')

pygame.init()
##Producer thread
class Producer(threading.Thread):

    def __init__(self, integers, condition,producer_no):
        #
        threading.Thread.__init__(self)
        self.integers = integers                    #Taking list of apples as a argument
        self.condition = condition                  #Taking lock as a arguments
        self.daemon = True                          #Set to True to make threads as a background threads
        self.Y_cord =  3.5*display_height/7         #Setting Y Coordinate for producer
        self.X_cord = -100                          #Setting X Coordinate for Producer
        self.producer_no = producer_no

    
    def run(self):
    	global apple_count                     #To create apple_count(Global Variable) in local context
        while True:
            integer = random.randint(0, 40)     #Generate randomly a number to assign number to apple
            
            # print 'condition acquired by %s' % self.name
            if len(self.integers) == Capacity:  #When the Fridge has reached its capacity i.e the buffer is full
            	# pygame.mixer.music.load(FullHouse)
            	# pygame.mixer.music.play()
            	pygame.mixer.Channel(0).play(pygame.mixer.Sound(BGM))
            	# pygame.mixer.Channe0(1).play(pygame.mixer.Sound(FullHouse))
                (self.X_cord,apple_count) = Produce_Go_Right(self.X_cord,self.Y_cord,self.producer_no, Lady_Image) #Producer going right with an apple animation sequence
                self.condition.acquire()            #Acquiring lock on the Fridge
            	self.X_cord = Producer_Go_Left_Full(self.X_cord,self.Y_cord,self.producer_no, Lady_Image) #HAVE TO GO BACK WITH AN APPLE IN HAND
                self.condition.wait()  #Waits for Notify Signal
                self.condition.release()  #Releasing the lock on Fridge
                print ("Full.House..")
                f.write('Producer: Full\n')
            else:                       #if fridge is not full yet
                self.integers.append(integer)  #Append the apple number in fridge
                self.condition.acquire()
                (self.X_cord,apple_count) = Produce_Go_Right(self.X_cord,self.Y_cord,self.producer_no, Lady_Image) #producer goes right with an apple
                            #Acquiring lock on the Fridge
                # apple_count = apple_count + 1 #Increases the apple count in the fridge
                self.condition.notify() #notifies other waiting threads
                self.condition.release()    #Releases lock on the Fridge
                print('%d appended to list by %s' % (integer, self.name))
                f.write('Producer: Apple %d is added into the fridge\n' % (integer))
                print(str(self.X_cord) + " " + str(apple_count)) 
                self.X_cord = Producer_Go_Left(self.X_cord,self.Y_cord,self.producer_no, Lady_Image)  #producer puts apple in refrigerator and returns empty handed
                

            

            
            time.sleep(random.randint(0, 1))

class Consumer(threading.Thread):

    def __init__(self, integers, condition,consumer_no):

        threading.Thread.__init__(self)
        self.daemon = True                          #Set to True to make threads as a background threads
        self.integers = integers                    #Taking list of apples as a argument
        self.condition = condition                  #Taking lock as a arguments        
        self.Y_cord =  4*display_height/7 - 70      #Setting Y Coordinate for Consumer                
        self.X_cord = display_width                 #Setting X Coordinate for Consumer        
        self.consumer_no = consumer_no              #Consumer ID
    
    def run(self):
    	global apple_count         #To create apple_count(Global Variable) in local context
        while True:
            
            # print 'condition acquired by %s' % self.name
            while True:
                if len(self.integers) == 0:  #If fridge is empty i.e no apples
                    # pygame.mixer.music.load(Nil)
                    # pygame.mixer.music.play()
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(BGM))
                    self.X_cord = Consumer_Go_Left(self.X_cord,self.Y_cord,self.consumer_no, Lady_Image) #Consumer comes from left 
                    # pygame.mixer.Channel(1).play(pygame.mixer.Sound(Nil))
                    self.condition.acquire()        #Acquiring lock on the fridge
                    self.X_cord = Consumer_Go_Right_Empty(self.X_cord,self.Y_cord,self.consumer_no, Lady_Image) #CONSUMER HAS TO GO BACK EMPTY HANDED\
                    self.condition.wait()  #Waits for Notify Signal
                    self.condition.release()  #Releasing the lock on Fridge
                    print 'Empty ...'
                    f.write('Empty\n')
                
                if self.integers:
                    integer = self.integers.pop()
                    self.X_cord = Consumer_Go_Left(self.X_cord,self.Y_cord,self.consumer_no, Lady_Image)  #Consumer comes from left 
                    print('%d removed from list by consumer(%s)' % (integer, self.name))
                    f.write('Consumer %s: Apple %d is removed from fridge\n' % (self.name,integer))
                    self.condition.acquire()        #Acquiring lock on the Fridge
                    apple_count = apple_count - 1  #Decreasing the number of apples in fridge
                    # print(str(self.X_cord) + " " + str(apple_count))
                    self.condition.wait()  #Waits for Notify Signal
                    self.condition.release()  #Releasing the lock on Fridge
                    self.X_cord = Consumer_Go_Right(self.X_cord,self.Y_cord,self.consumer_no, Lady_Image) #Consumer goes to right with an apple
                    
                    break
            time.sleep(random.randint(0, 4));


#**************************** MAIN ****************************
# StartScreen()                           #Displays start screen defined in Movement module
apple_count = 0                         #Count of number of Apples
integers = []                           #List of apples append
condition = threading.Condition()       #Locking Mechanism

# #Creating 1 Producer and 3 Consumers
t1 = Producer(integers, condition,1)
# t2 = Producer(integers, condition,2)
# t3 = Producer(integers, condition,3)
t4 = Consumer(integers, condition,1)
t5 = Consumer(integers, condition,2)
t6 = Consumer(integers,condition,3)

#Starting Threads
time.sleep(random.randint(0, 4));
t1.start()
# t2.start()
# t3.start()
time.sleep(random.randint(0, 4));
t4.start()
# time.sleep(random.randint(0, 4));
# t5.start()
# time.sleep(random.randint(0, 4));
# t6.start()

while True:
    time.sleep(1)