u = 0
s = 710
def setup():
    size(1000,500)
def author():
    fill(0)
    textSize(14)
    text("Nama : Syeh Abdi Yoga Krisna",540,120)
    text("NPM : 2055201001033",540,150)
    text("Kelas : Pagi",540,180)
def tanah():
    noStroke()
    fill(4,50,8)
    square(0,400,1000)
    fill(8,100,44)
    rect(0,400,1000,20)

def tank_kiri():
    stroke(1)
    #moncong tank
    fill(5,140,69)
    rect(265,263,10,40)
    rect(200,268,65,30)
    #kepala tank
    fill(23,188,101)
    rect(70,240,140,80,50,50,3,3)
    #badan tank
    fill(12,94,51)
    rect(45,310,190,30)
    #dasar tank
    fill(47,83,37)
    rect(20,340,240,60,20)
    # roda tank
    for l in range(53,225,50):
        fill(49,139,24)
        circle(l+10,370,50)
        fill(100,144,88)
        circle(l+10,370,30)

def tank_kanan():
    stroke(1)
    #moncong tank
    fill(146,164,0)
    rect(730,263,10,40)
    rect(740,268,65,30)
    #kepala tank
    fill(212,231,57)
    rect(804,240,140,80,50,50,3,3)
    #badan tank
    fill(178,204,0)
    rect(777,310,190,30)
    #dasar tank
    fill(138,158,0)
    rect(750,340,240,60,20)
    # roda tank
    for l in range(785,980,50):
        fill(230,242,125)
        circle(l+10,370,50)
        fill(112,118,58)
        circle(l+10,370,30)
def tembak():
    global u,s
    #kiri
    stroke(1)
    p =map(u,0,width,0,175)
    fill(255,p,0)
    u=u+20
    ellipse(295+u,283,40,20)
    if(u>580):
        circle(715,284,400)
        u=u-580
    #kanan
    s = s-20
    ellipse(s,283,40,20)
    if(s<200):
        circle(280,284,400)
        s = s+530

def smoke():
    noStroke()
    for a in range(500,width,40):
        fill(random(255))   
        circle(random(a),380,random(10,200))

def tiang():
    stroke(1)
    #kabel
    line(0,50,1000,50)
    line(0,80,1000,80)
    # tiang
    fill(174,104,31)
    for w in range(100,810,350):
        push()
        translate(w,50)
        rect(0,0,30,350)
        pop()
    for f in range(40,750,350):
        push()
        translate(f,80)
        rect(0,0,150,10)
        pop()

def draw():
    background(123,135,234)
    author()
    tiang()
    smoke()
    tank_kanan()
    tank_kiri()
    tembak()
    tanah()
