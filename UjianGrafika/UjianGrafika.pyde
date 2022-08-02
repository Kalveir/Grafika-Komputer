#Random
w = 200
h = 0

#motion
x = 0
y = 1
z = 0

def setup():
    size(800,500)
    
def mobil():
     # muatan
    fill(0,128,0)
    rect(10+x,320,150,100)
    #kendaraan
    fill(144,238,144)
    rect(160+x,360,50,60)
    #roda
    fill(0)
    circle(50+x,420,40)
    circle(150+x,420,40)
    #peleng
    fill(255)
    circle(50+x,420,20)
    circle(150+x,420,20)
    
def random_bola():
    global w,h
    fill(w,h,1)
    circle(w,h,60)
    w = random(width)
    h = random(height/2)
    
def jalan():
    fill(0,0,0)
    rect(0,300,800,250)
    stroke(255,255,255)
    for a in range(0,800,60):
        line(a,400,a+40,400)

def draw():
    global x,y,z
    background(z)
    jalan()
    random_bola()
    z = map(x,0,width,255,0)
    x+=y
    if x > width :
        x=-1
    mobil()
   
    
