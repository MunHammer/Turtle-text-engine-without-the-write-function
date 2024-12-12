#!/usr/bin/env python3
'''This Python program is to write letters using the turtle module.
This is also slightly incomplete with not all characters included'''

from turtle import *
from random import randint, choice
from os import system

def setup():
    system('clear')
    hideturtle()
    Screen().bgcolor('black')
    color('white')
    shape('turtle')
    speed(10)
    pensize(4)
    penup()

# draws an oval of a defined height and width
def oval(height,width):
	shape("circle")
	shapesize(height,width,1)
	fillcolor("white")
	shape("circle")
	shapesize(height - 1,width - 1,1)
	fillcolor("black")

# General function to draw a letter
def draw_letter(letter, x, y):
    letter_functions = {
        'A': lambda: draw_A(x, y),
        'B': lambda: draw_B(x, y),
        'C': lambda: draw_C(x, y),
        'D': lambda: draw_D(x, y),
        'E': lambda: draw_E(x, y),
        'F': lambda: draw_F(x, y),
        'G': lambda: draw_G(x, y),
        'H': lambda: draw_H(x, y),
        'I': lambda: draw_I(x, y),
        'J': lambda: draw_J(x, y),
        'K': lambda: draw_K(x, y),
        'L': lambda: draw_L(x, y),
        'M': lambda: draw_M(x, y),
        'N': lambda: draw_N(x, y),
        'O': lambda: draw_O(x, y),
        'P': lambda: draw_P(x, y),
        'Q': lambda: draw_Q(x, y),
        'R': lambda: draw_R(x, y),
        'S': lambda: draw_S(x, y),
        'T': lambda: draw_T(x, y),
        'U': lambda: draw_U(x, y),
        'V': lambda: draw_V(x, y),
        'W': lambda: draw_W(x, y),
        'X': lambda: draw_X(x, y),
        'Y': lambda: draw_Y(x, y),
        'Z': lambda: draw_Z(x, y),
        '1': lambda: draw_1(x, y),
        '2': lambda: draw_2(x, y),
        '3': lambda: draw_3(x, y),
        '4': lambda: draw_4(x, y),
        '5': lambda: draw_5(x, y),
        '6': lambda: draw_6(x, y),
        '7': lambda: draw_7(x, y),
        '8': lambda: draw_8(x, y),
        '9': lambda: draw_9(x, y),
        '0': lambda: draw_0(x, y),
        '!': lambda: draw_exclaim(x, y),
    }
    letter_functions.get(letter, lambda: None)()  # Draw the letter or do nothing

# Define letter drawing functions here (same as before, but without redundancy)
def draw_exclaim(x, y):
    penup()
    goto(x, y)
    pendown()
    goto(x, y + 1)
    penup()
    goto(x, y + 10)
    pendown()
    goto(x, y + 40)
    penup()

def draw_A(x, y):
    goto(x, y)
    pendown()
    goto(x + 10, y + 40)
    goto(x + 20, y)
    goto(x + 15, y + 10)
    goto(x + 5, y + 10)
    penup()

# Function to draw the letter B
def draw_B(x, y):
    penup()
    goto(x + 3, y + 40)
    pendown()
    goto(x + 13, y + 40)
    goto(x + 18, y + 35)
    goto(x + 18, y + 25)
    goto(x + 13, y + 20)
    goto(x, y + 20)
    goto(x + 15, y + 20)
    goto(x + 20, y + 15)
    goto(x + 20, y + 5)
    goto(x + 15, y)
    goto(x + 3, y)
    goto(x, y)
    goto(x,y + 37)
    goto(x + 3, y + 40)
    penup()

# Function to draw the letter C
def draw_C(x,y):
	penup()
	goto(x + 20, y + 40)
	pendown()
	goto(x + 3, y + 40)
	goto(x, y + 37)
	goto(x, y + 3)
	goto(x + 3, y)
	goto(x + 20, y)
	penup()

# Function to draw the letter D
def draw_D(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x,y + 40)
    goto(x,y)
    circle(20, 180)
    goto(x,y)
    penup()
    right(180)

# Function to draw the letter E
def draw_E(x, y):
    penup()
    goto(x + 20, y + 40)
    pendown()
    goto(x + 3, y + 40)
    goto(x, y + 37)
    goto(x, y + 20)
    goto(x + 20, y + 20)
    goto(x, y + 20)
    goto(x, y + 3)
    goto(x + 3, y)
    goto(x + 20, y)
    penup()

# Function to draw the letter F
def draw_F(x, y):
    penup()
    goto(x + 20, y + 40)
    pendown()
    goto(x + 3, y + 40)
    goto(x, y + 37)
    goto(x, y + 24)
    goto(x + 17, y + 24)
    goto(x, y + 24)
    goto(x, y)
    penup()

# Function to draw the letter G
def draw_G(x, y):
    penup()
    goto(x,y + 40)
    pendown()
    goto(x + 20,y + 40)
    goto(x, y + 40)
    goto(x,y + 20)
    goto(x + 20,y + 20)
    goto(x + 20,y + 40)
    goto(x + 20,y)
    goto(x,y)
    goto(x,y + 5)
    penup()

# Function to draw the letter H
def draw_H(x, y):
    goto(x, y)
    pendown()
    goto(x, y + 40)
    goto(x, y + 20)
    goto(x + 20, y + 20)
    goto(x + 20, y + 40)
    goto(x + 20, y)
    penup()

# Function to draw the letter I
def draw_I(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x + 20,y)
    goto(x + 10,y)
    goto(x + 10,y + 40)
    goto(x,y + 40)
    goto(x + 20,y + 40)
    penup()

# Function to draw the letter J
def draw_J(x, y):
    penup()
    goto(x,y + 40)
    pendown()
    goto(x + 20,y + 40)
    goto(x + 10,y + 40)
    goto(x + 10,y + 10)
    goto(x + 7,y + 7)
    goto(x + 5,y + 5)
    goto(x + 2,y + 2)
    goto(x,y)
    penup()

# Function to draw the letter K
def draw_K(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x,y + 40)
    goto(x,y + 20)
    goto(x + 20,y + 40)
    goto(x,y + 20)
    goto(x + 20,y)
    penup()

# Function to draw the letter L
def draw_L(x, y):
    penup()
    goto(x,y + 40)
    pendown()
    goto(x,y)
    goto(x + 20,y)
    penup()

# Function to draw the letter M
def draw_M(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x + 5,y + 40)
    goto(x + 10,y)
    goto(x + 15,y + 40)
    goto(x + 20,y)
    penup()

# Function to draw the letter N
def draw_N(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x,y + 40)
    goto(x + 20,y)
    goto(x + 20, y + 40)
    penup()

# Function to draw the letter O
def draw_O(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x,y + 40)
    goto(x + 20,y + 40)
    goto(x + 20,y)
    goto(x,y)
    penup()

# Function to draw the letter P
def draw_P(x, y):
    goto(x, y)
    pendown()
    goto(x, y + 40)
    goto(x + 20, y + 40)
    goto(x + 20, y + 30)
    goto(x, y + 30)
    penup()

# Function to draw the letter Q
def draw_Q(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x,y + 40)
    goto(x + 15,y + 40)
    goto(x + 15,y)
    goto(x,y)
    penup()
    goto(x + 7,y + 12)
    pendown()
    goto(x + 20,y)
    penup()

# Function to draw the letter R
def draw_R(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x,y + 40)
    goto(x + 20,y + 40)
    goto(x + 20,y + 30)
    goto(x,y + 30)
    goto(x + 20,y)
    penup()

# Function to draw the letter S
def draw_S(x, y):
    penup()
    goto(x + 20,y + 40)
    pendown()
    goto(x,y + 40)
    goto(x,y + 20)
    goto(x + 20,y + 20)
    goto(x + 20,y)
    goto(x,y)
    penup()

# Function to draw the letter T
def draw_T(x, y):
    penup()
    goto(x + 20,y + 40)
    pendown()
    goto(x,y + 40)
    goto(x + 10,y + 40)
    goto(x + 10,y)
    penup()

# Function to draw the letter U
def draw_U(x, y):
    penup()
    goto(x,y + 40)
    pendown()
    goto(x,y)
    goto(x + 10,y)
    goto(x + 20,y + 5)
    goto(x + 20,y + 40)
    goto(x + 20,y)
    penup()

# Function to draw the letter V
def draw_V(x, y):
    penup()
    goto(x,y + 40)
    pendown()
    goto(x + 10,y)
    goto(x + 20,y + 40)
    penup()

# Function to draw the letter W
def draw_W(x, y):
    penup()
    goto(x,y + 40)
    pendown()
    goto(x + 5,y)
    goto(x + 10,y + 40)
    goto(x + 15,y)
    goto(x + 20,y + 40)
    penup()

# Function to draw the letter X
def draw_X(x, y):
    penup()
    goto(x + 20,y + 40)
    pendown()
    goto(x,y)
    penup()
    goto(x + 20,y)
    pendown()
    goto(x,y + 40)
    penup()

# Function to draw the letter Y
def draw_Y(x, y):
    penup()
    goto(x, y + 40)
    pendown()
    goto(x + 10, y + 20)
    goto(x + 20, y + 40)
    goto(x + 10, y + 20)
    goto(x + 10, y)
    penup()

# Function to draw the letter Z
def draw_Z(x, y):
    penup()
    goto(x,y + 40)
    pendown()
    goto(x + 20,y + 40)
    goto(x,y)
    goto(x + 20,y)
    penup()

# Function to draw the number 1
def draw_1(x, y):
    penup()
    goto(x,y)
    pendown()
    goto(x + 20,y)
    goto(x + 10,y)
    goto(x + 10,y + 40)
    goto(x + 5,y + 35)
    penup()

# Function to draw the number 2
def draw_2(x, y):
	penup()
	goto(x + 20,y)
	pendown()
	goto(x, y)
	goto(x, y + 20)
	goto(x + 20, y + 20)
	goto(x + 20, y + 40)
	goto(x, y + 40)
	penup()
	
# Function to draw the number 3
def draw_3(x, y):
	penup()
	goto(x,y)
	pendown()
	goto(x + 17, y)
	goto(x + 20,y + 3)
	goto(x + 20, y + 17)
	goto(x + 17, y + 20)
	goto(x, y + 20)
	goto(x + 17, y + 20)
	goto(x + 20, y + 23)
	goto(x + 20, y + 37)
	goto(x + 17, y + 40)
	goto(x, y + 40)
	penup()
	
# Function to draw the number 4
def draw_4(x, y):
	penup()
	goto(x + 15,y)
	pendown()
	goto(x + 15, y + 40)
	goto(x, y + 10)
	goto(x + 20, y + 10)
	penup()

# Function to draw the number 5
def draw_5(x, y):
	penup()
	goto(x,y)
	pendown()
	goto(x + 20, y)
	goto(x + 20, y + 20)
	goto(x, y + 20)
	goto(x, y + 40)
	goto(x + 20, y + 40)
	penup()

# Function to draw the number 6
def draw_6(x, y):
	penup()
	goto(x + 20,y + 40)
	pendown()
	goto(x, y + 16)
	penup()
	goto(x + 10, y)
	pendown()
	circle(10)
	penup()
	
# Function to draw the number 7
def draw_7(x, y):
	penup()
	goto(x, y + 40)
	pendown()
	goto(x + 20, y + 40)
	goto(x, y)
	penup()

# Function to draw the number 8
def draw_8(x, y):
	penup()
	goto(x + 17, y + 40)
	pendown()
	goto(x + 3, y + 40)
	goto(x, y + 37)
	goto(x, y + 23)
	goto(x + 3, y + 20)
	goto(x + 17, y + 20)
	goto(x + 20, y + 17)
	goto(x + 20, y + 3)
	goto(x + 17, y)
	goto(x + 3, y)
	goto(x, y + 3)
	goto(x, y + 17)
	goto(x + 3, + y + 20)
	goto(x + 17, y + 20)
	goto(x + 20, y + 23)
	goto(x + 20, y + 37)
	goto(x + 17, y + 40)
	penup()

# Function to draw the number 9
def draw_9(x, y):
	penup()
	goto(x + 10, y + 20)
	pendown()
	circle(10)
	penup()
	goto(x + 20, y + 30)
	pendown()
	goto(x + 20, y)
	penup()

# Function to draw the number 0
def draw_0(x, y):
	penup()
	goto(x + 10, y + 20)
	pendown()
	shape("circle")
	shapesize(3,2,1)
	fillcolor("white")
	shape("circle")
	shapesize(2,1,4)
	fillcolor("black")
	stamp()
	penup()
	goto(x + 15, y + 30)
	pendown()
	goto(x + 5, y + 10)
	penup()
	setup()

def draw_words(x, y, word):
    words = word.upper()
    ex = 0
    for char in words:
        draw_letter(char, x + ex, y)
        ex += 30  # Move over for next letter

def randomwords():
	colors = ['white', 'lime', 'red', 'magenta', 'dark slate blue', 'rosy brown', 'yellow']
	DOOOM = randint(300, 1000)
	for _ in range(DOOOM):
		pensize(randint(1, 10))
		color(choice(colors))
		rando = choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9',])
		draw_words(randint(-600, 600), randint(-400, 400), rando)
	pendown()
	color('black')
	pensize(100)
	booom = 40
	while booom > 0:
		goto(randint(0,50),booom)
		booom -= 1
		goto(randint(50,100),booom)
		booom -= 1
	color('deep sky blue')
	pensize(4)
	draw_words(0,0, str(DOOOM))

# Setup
wut = input('What do you want to run?\nlettercheck\nrando\n').upper()
setup()

if wut == 'RANDO':
    randomwords()
elif wut == 'LETTERCHECK':
    draw_words(-500, 10, 'abcdefghijklmnopqrstuvwxyz!1234567890')
else:
    draw_words(-700, 350, 'You might have spelled wrong')

done()
