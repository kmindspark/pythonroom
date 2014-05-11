# author: kmindspark
import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()
t=turtle.Turtle()

t.color(purple)




t1.left(75)
t2.left(105)
numbers = range (1,105)
angles = range (1, 2)
for i in numbers:
	t1.forward(1)
	t2.forward(1)
	for n in angles:
		t1.right(1+n)
		t2.left(1+n)
	
t1.forward(80)
t2.forward(80)
	