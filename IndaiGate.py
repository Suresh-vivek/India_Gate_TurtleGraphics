import turtle

t=turtle.Turtle()
t.screen.setup(1200,720)
#Functions used
def Rect(x,y,c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(2):
        t.forward(x)
        t.right(90)
        t.forward(y)
        t.right(90)
    t.end_fill()




def Air(x):
    t.penup()
    t.forward(x)
    t.pendown()

def lines(x,y,l):
    t.pensize(3)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(l)
    t.pensize(2)

def Rect1(x,y,c):
    t.fillcolor(c)
    t.begin_fill()
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
    t.forward(x)
    t.left(90)
    t.end_fill()

def trapezium(x,y,c):
    t.fillcolor(c)
    t.begin_fill()
    t.pensize(3)
    t.forward(x)
    t.right(60)
    t.forward(2*y)
    t.right(120)
    t.forward(x+ 2*y)
    t.right(120)
    t.forward(2*y)
    t.right(60)
    t.pensize(2)
    t.end_fill()

#Setting Pen Size
t.pensize(2)

t.right(90)
Air(340)
t.right(90)
Air(335)

turtle.colormode(255)
t.pencolor(128,103,72)

#Left_Pillar

t.right(90)
Rect(150,140,(237,176,102))
t.right(90)
t.forward(10)
t.left(90)
t.pencolor(122,82,43)
Rect(150,120,(244,192,145))
t.right(90)

t.pencolor(132,81,35)
t.forward(5)
t.left(90)
Rect(50,110,(234,152,83))

t.pencolor(82,44,21)
Air(50)
t.left(90)
t.pensize(3)
t.forward(18)
t.backward(146)
t.pensize(2)
Air(3)
t.right(90)
Air(100)
t.left(90)

t.pencolor(112,63,23)
trapezium(140,10,(235,152,84))



t.penup()
t.right(180)

lines(-335,-172,0)
t.left(90)
t.pencolor(108,99,75)
Rect(230,140,(238,175,101))
t.right(90)
Air(10)
t.left(90)
t.pencolor(123,82,45)
Rect(130,120,(243,192,144))


lines(-305,-160,0)
t.pencolor(134,73,21)
Rect(118,80,(235,152,84))
Air(118)
t.left(90)
t.pensize(3)
t.pencolor(44,8,1)
t.forward(35)
t.backward(150)
t.forward(5)
t.right(90)

lines(-225,10,0)
t.pensize(3)
t.pencolor(103,51,5)
t.fillcolor(223,151,92)
t.begin_fill()
t.circle(40)
t.end_fill()

lines(-235,10,0)
t.pensize(3)
t.pencolor(107,59,15)
t.fillcolor(219,175,114)
t.begin_fill()
t.circle(30)
t.end_fill()

lines(165,-340,0)

#Right_pillar
t.pencolor(128,103,72)

Rect(150,140,(237,176,102))
t.right(90)
t.forward(10)
t.left(90)
t.pencolor(122,82,43)
Rect(150,120,(244,192,145))
t.right(90)

t.pencolor(132,81,35)
t.forward(5)
t.left(90)
Rect(50,110,(234,152,83))


t.pencolor(82,44,21)
Air(50)
t.left(90)
t.pensize(3)
t.forward(18)
t.backward(146)
t.pensize(2)
Air(3)
t.right(90)
Air(100)
t.left(90)

t.pencolor(112,63,23)
trapezium(140,10,(235,152,84))

t.penup()
t.right(180)

lines(165,-172,0)
t.left(90)
t.pencolor(108,99,75)
Rect(230,140,(238,175,101))
t.right(90)
Air(10)
t.left(90)
t.pencolor(123,82,45)
Rect(130,120,(243,192,144))

lines(195,-160,0)
t.pencolor(134,73,21)
Rect(118,80,(235,152,84))

Air(118)
t.left(90)
t.pensize(3)
t.pencolor(44,8,1)
t.forward(35)
t.backward(150)
t.forward(5)
t.right(90)

lines(275,10,0)
t.pensize(3)
t.pencolor(103,51,5)
t.fillcolor(223,151,92)
t.begin_fill()
t.circle(40)
t.end_fill()

lines(265,10,0)
t.pensize(3)
t.pencolor(107,59,15)
t.fillcolor(219,175,114)
t.begin_fill()
t.circle(30)
t.end_fill()

#Middle_Portion
t.pensize(2)
lines(165,-340,0)
Air(220)
t.left(90)

t.fillcolor(234,152,82)
t.begin_fill()
t.pencolor(132,77,34)
t.forward(40)
t.left(90)

t.pencolor(57,37,25)
t.forward(220)
t.pensize(3)
t.right(90)
t.backward(40)
t.end_fill()


t.forward(360)
t.fillcolor(234,152,82)
t.begin_fill()
t.backward(42)
t.pensize(2)
t.right(90)
t.forward(220)
t.left(90)
t.forward(42)
t.end_fill()

lines(-195,-190,0)
t.pencolor(112,63,23)
trapezium(140,10,(235,152,84))

lines(305,-190,0)
t.pencolor(112,63,23)
trapezium(140,10,(235,152,84))

#Arch

lines(150,-120,0)
t.right(90)
t.pensize(3)
t.fillcolor(234,151,82)
t.begin_fill()
t.circle(164,180)
t.end_fill()

lines(125,-120,0)
t.right(180)
t.pensize(3)
t.pencolor(104,88,66)
t.fillcolor(255,255,255)
t.begin_fill()
t.circle(139,180)
t.end_fill()

lines(-195,44,0)
t.pensize(3)
t.left(90)
t.pencolor(130,85,45)
t.fillcolor(233,153,83)
t.begin_fill()
t.forward(358)
t.left(90)
t.forward(14)
t.left(90)
t.forward(358)
t.end_fill()

t.right(180)
lines(0,44,0)
t.pencolor(169,179,93)
t.fillcolor(243,192,145)
t.begin_fill()
t.forward(165)
t.right(90)
t.forward(164)
t.right(90)
t.forward(15)
t.right(90)
t.circle(164,90)
t.end_fill()

t.fillcolor(243,192,145)
t.begin_fill()
t.forward(180)
t.left(90)
t.forward(164)
t.left(90)
t.forward(15)
lines(-14,44,0)
t.left(180)
t.circle(164,90)
t.end_fill()
t.right(90)
#Upper_Portion
lines(305,60,0)
t.pensize(3)
t.pencolor(74,44,17)

trapezium(640,35,(235,153,80))

t.right(120)
t.forward(40.4)
t.left(120)
trapezium(680.4,15,(235,153,80))

lines(-335,60,0)
t.right(90)

t.pencolor(127,71,23)

for i in range(10):
    Rect1(35,30,(215,176,113))
    t.forward(30)
    t.left(90)


Rect(35,30,(215,176,113))

t.pencolor(138,89,51)
lines(-335,123,0)
Rect1(40,640,(238,176,103))

t.pencolor(154,102,52)
lines(-305,163,0)
t.left(90)
Rect1(30,590,(235,152,84))

t.left(90)
lines(-275,193,0)
t.pencolor(100,101,84)
Rect1(90,530,(238,175,102))

t.pencolor(89,36,4)
t.left(90)
lines(-135,238,0)
t.pensize(3)
t.fillcolor(235,152,84)
t.begin_fill()
t.circle(20)
t.end_fill()

lines(155,238,0)
t.pensize(3)
t.fillcolor(235,152,84)
t.begin_fill()
t.circle(20)
t.end_fill()

t.pencolor(134,81,33)
t.fillcolor(234,152,82)
t.begin_fill()
lines(-120,220,0)
t.pensize(3)
t.forward(40)
t.right(90)
t.forward(220)
t.right(90)
t.forward(40)
t.right(90)
t.forward(50)
t.left(90)
t.forward(10)
t.right(90)
t.forward(120)
t.right(90)
t.forward(10)
t.left(90)
t.forward(50)
t.right(90)
t.end_fill()

lines(-45,220,0)


t.pencolor(135,83,36) #color of letters
#For_Letter_I
t.pensize(2)
t.forward(30)

#for_letter_N
lines(-35,220,0)
t.pensize(2)
t.forward(30)
t.right(150)
t.forward(34.64)
t.left(150)
t.forward(30)

#For_Letter_D
lines(-7,220,0)
t.pensize(2)
Rect(30,12,(234,152,82))

#for_Letter_I
lines(15,220,0)
t.forward(30)

#For_Letter_A
lines(25,220,0)
t.forward(30)
t.right(90)
t.forward(12)
t.right(90)
t.forward(30)
t.backward(17)
t.right(90)
t.forward(12)

t.pencolor(150,99,57)
lines(-155,283,0)
t.right(90)
Rect(20,290,(233,153,85))

t.pencolor(77,99,97)
lines(-105,303,0)
Rect(20,200,(235,175,102))

t.pencolor(92,85,63)
lines(-65,323,0)
Rect(20,120,(234,152,84))



#lines
t.right(90)
t.pencolor(112,73,41)
lines(-305,-205,80)
t.pencolor(163,130,112)
lines(-305,-220,50)

t.pencolor(112,73,41)
lines(200,-205,80)
t.pencolor(163,130,112)
lines(230,-220,50)

t.left(90)
t.pencolor(153,94,48)
lines(-300,-90,40)
t.pencolor(145,73,15)
lines(-290,-110,30)

t.pencolor(153,94,48)
lines(270,-90,40)
t.pencolor(145,73,15)
lines(260,-110,30)

t.right(90)
t.pencolor(107,96,61)
lines(-185,10,25)
t.pencolor(108,72,43)
lines(-185,25,40)

t.pencolor(107,96,61)
lines(110,25,40)
t.pencolor(108,72,43)
lines(125,10,25)

t.pencolor(154,106,52)
lines(-325,50,30)
lines(265,50,30)

t.pencolor(145,99,47)
lines(-320,113,40)
t.pencolor(66,15,3)
lines(-320,106,25)
t.pencolor(145,99,47)
lines(-320,99,10)

t.pencolor(145,99,47)
lines(250,113,40)
t.pencolor(66,15,3)
lines(265,106,25)
t.pencolor(145,99,47)
lines(280,99,10)

t.pencolor(166,105,62)
lines(-290,153,30)
t.pencolor(158,97,53)
lines(-290,145,50)

t.pencolor(166,105,62)
lines(240,153,30)
t.pencolor(158,97,53)
lines(220,145,50)

t.pencolor(130,76,45)
lines(-145,275,40)

t.pencolor(127,75,34)
lines(-30,314,60)

t.pencolor(102,51,26)
lines(-185,54,335)

#Flag
lines(-50,-340,0)
t.left(90)
t.pencolor(112,112,112)
Rect(20,70,(210,211,205))
lines(-20,-320,0)
Rect(200,10,(210,211,205))
lines(-10,-130,0)
t.right(90)

t.pencolor(255,165,0)
Rect1(70,20,(255,165,0))

t.pencolor(255,255,255)
t.left(90)
Rect1(70,20,(255,255,255))

t.pencolor("Green")
t.left(90)
Rect1(70,20,("Green"))

t.pencolor("Blue")
t.pensize(1)
lines(25,-160,0)
t.left(90)
for i in range(24):

    t.forward(10)
    t.backward(10)
    t.left(15)

lines(35,-160,0)
t.left(90)
t.circle(10)

t.hideturtle()
