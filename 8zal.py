import turtle
laki=turtle.Turtle()
laki.shape('turtle')
laki.color('#00A6FF')
laki.turtlesize()
laki.width(8)
laki.speed(5)
for i in range(16):
	for j in range(8):
		laki.forward(100)
		laki.left(45)
		laki.clone()
	laki.left(22)