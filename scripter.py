from random import randint

for i in range(30):
    '''
    //BODY
push
move 250 250 0
rotate y'''+ str(randint(-180, 180))+'''
rotate z -50
rotate x -30
box -100 125 50 200 250 100
//HEAD
push
move 0 175 0
rotate y -10
rotate x 90
sphere 0 0 0 50
pop
//LEFT ARM
push
move -100 125 0
rotate x -35
rotate y 0
rotate z -80
box -40 0 40 40 100 80
//LEFT LOWER ARM
push
move -20 -100 0
rotate y 30
rotate z 10
box -10 0 10 20 125 20
pop
pop
//RIGHT ARM
push
move 100 125 0
rotate x -45
rotate y -20
rotate z 30
box 0 0 40 40 100 80
//RIGHT LOWER ARM
push
move 20 -100 0
rotate x -20
rotate y 0
rotate z 45
box -10 0 10 20 125 20
pop
pop
//LEFT LEG
push
move -100 -125 0
rotate x -20
rotate z -70
box 0 0 40 50 120 80
pop
//RIGHT LEG
push
move 100 -125 0
rotate x -90
rotate z 50
box -50 0 40 50 120 80
//display
save robot03.png
)
