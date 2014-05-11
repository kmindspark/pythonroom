# author: kmindspark
import turtle

world=turtle.Screen()
world.bgcolor("red")
t1=turtle.Turtle()
t2=turtle.Turtle()


t1.hideturtle()
t2.hideturtle()

t1.color("blue")
t2.color("blue")




t1.left(75)
t2.left(105)
numbers = range (1,105)
angles = range (1, 2)
for i in numbers:
	t1.forward(2)
	t2.forward(2)
	for n in angles:
		t1.right(1+n)
		t2.left(1+n)

end = range (1,49)
for x in end:
	t1.forward(3)
	t2.forward(3)

t1.color("white")
t1.setpos (-45,-25)
t1.write("Happy Mother's Day!")
t1.setpos (-33,-45)
t1.write("Love, Kaushik")


