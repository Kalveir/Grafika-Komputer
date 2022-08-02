def setup():
    size(500,350)

def pagi():
    background(124,254,240)
    #matahari
    stroke(0,0,0)
    fill(226,192,22)
    ellipse(250,75,50,50)
    # taman
    stroke(0,0,0)
    fill(42,96,65)
    quad(0,200,500,200,500,350,0,350)
    #gunung 
    stroke(0,0,0)
    fill(85,153,221)
    triangle(50,200,150,100,250,200)
    triangle(250,200,350,100,450,200)
    # jalan
    stroke(0,0,0)
    fill(0,0,0)
    triangle(250,200,150,350,350,350)
    #markah
    stroke(225,225,225)
    for a in range(200,350,20):
        line(250,a+15,250,a)

def malam():
    background(0,10,204)
    #bulan
    fill(226,192,22)
    stroke(225,225,225)
    arc(250,75,50,50,QUARTER_PI,PI+QUARTER_PI)
    # taman
    fill(62,126,154)
    stroke(225,225,225)
    quad(0,200,500,200,500,350,0,350)
    #gunung 
    stroke(225,225,225)
    fill(17,112,207)
    triangle(50,200,150,100,250,200)
    triangle(250,200,350,100,450,200)
    # jalan
    stroke(0,0,0)
    fill(0,0,0)
    triangle(250,200,150,350,350,350)
    #markah
    stroke(225,225,225)
    for a in range(200,350,20):
        line(250,a+15,250,a)
def burung1():
    for a in range(20,101,20):
        if a==60:
            continue
        else:
            line(a-10,20,a,10)
            
    for b in range(20,101,20):
        if b==60:
           continue
        else:
           line(b,10,b+10,20) 
def burung2():
    for i in range(20,101,20):
        if i==60:
           continue
        else:
           line(i,50,i+10,40)
           
    for j in range(40,121,20):
        if j==80:
           continue
        else:
           line(j-10,40,j,50)
def burung3():
    for k in range(400,481,20):
        if k==440:
          continue
        else:
          line(k,10,k-10,20)
    for o in range(400,481,20):
        if o==440:
           continue
        else:
          line(o+10,20,o,10)   
def burung4():
    for m in range(400,481,20):
        if m==440:
          continue
        else:
            line(m,50,m-10,40)
        
    for p in range(380,461,20):
        if p==420:
          continue
        else:
            line(p+10,40,p,50)
def draw():
    if mousePressed:
        malam()
        if keyPressed:
            stroke(7)
            stroke(255,255,255)
            if key == 's' or key == 'S':
                burung1()
                burung3()
            if key == 'w' or key == 'W':
                burung2()
                burung4()
            if key == 'a' or key == 'A':
                burung1()
                burung4()
            if key == 'd' or key == 'D':
                burung2()
                burung3()
            if key == 'z' or key == 'Z':
                burung1()
                burung2()
            if key == 'c' or key == 'C':
                burung3()
                burung4()
    else:
        pagi()
        if keyPressed:
            stroke(7)
            stroke(0,0,0)
            if key == 's' or key == 'S':
                burung1()
                burung3()
            if key == 'w' or key == 'W':
                burung2()
                burung4()
            if key == 'a' or key == 'A':
                burung1()
                burung4()
            if key == 'd' or key == 'D':
                burung2()
                burung3()
            if key == 'z' or key == 'Z':
                burung1()
                burung2()
            if key == 'c' or key == 'C':
                burung3()
                burung4()
