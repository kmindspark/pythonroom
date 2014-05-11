# author: kmindspark
import turtle

t = turtle.Turtle()
legs = int (input ("How many legs do you want the sprite to have?"))
print legs

t.shape ("circle")

for i in range (legs):
	t.forward (100)
	t.stamp()
	t.backward (100)
	t.right ((360/(legs)))