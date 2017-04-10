#!/usr/bin/python3
import CHIP_IO.GPIO as GPIO
import time
import math, sys, os
import subprocess
import socket
import random
#gpio.setmode(gpio.BCM)

#gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)

GPIO.setup("XIO-P0", GPIO.IN)

num = 0
prnt = 0
last = 0
number = 0 
def play(number):
        
        try:
               player.kill()
        except NameError:
               pass 
	
        #player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
	
while True:
        input_value = GPIO.input("XIO-P0")
        #try:
        #       player.kill()
        #except NameError:
        #       pass
        if (input_value == 1) and (input_value != last):
                last = 1
                prnt = 1
                num += 1
                time.sleep(0.05)
                continue

        if (input_value == 0) and (input_value != last):
                last = 0
                time.sleep(0.05)
                continue

        if (input_value == 0) and (input_value == last):
                if (prnt == 1):
                        if (num == 10):
                                num = 0
		
                        if (num == 0):
                                print("a")
                                #number = 10
                                #number = random.randrange(1,50)
                                #print("random number is",number) 
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
                        if (num == 1):
                                print("b") 
                                number = 1
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
              
                        if (num == 2):
                                print("c")
                                number = 2
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                        if (num == 3):
                                print("d")
                                number = 3
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                        if (num == 4):
                                print("e")
                                #number = 4
                                number = random.randrange(1,50)
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                        if (num == 5):
                                print("f")
                                number = 5
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                        if (num == 6):
                                print("g")
                                number = 6
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                        if (num == 7):
                                print("h")
                                number = 7
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                        if (num == 8):
                                print("i")
                                number = 8
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                        if (num == 9):
                                print("jklmnopqrstuvwxyz")
                                number = 9
                                play(number)
                                player = subprocess.Popen(["mpg123", "/media/" + str(number) + ".mp3", "-q"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)                

        num = 0
        prnt = 0
        last = 0
        continue

