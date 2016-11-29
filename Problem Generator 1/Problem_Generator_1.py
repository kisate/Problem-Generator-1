import geo
import random
llim = -10
rlim = 10
def ranPFR(a, b) :
    return geo.Point(random.randint(a, b), random.randint(a, b))
tasks = []
A = geo.Point(0, 0)
B = geo.Point(0, 0)
AB = geo.Vector(A, B)

def genAB(maxl) : 
    global A
    global B 
    global AB 
    A = ranPFR(llim, rlim)
    B = ranPFR(llim, rlim)
    AB = geo.Vector(A, B)
    l = AB.length2()
    while(l > maxl**2) :
        B = ranPFR(llim, rlim)
        AB = geo.Vector(A, B)
        l = AB.length2()
    
def genParal() :
    genAB((abs(llim) + abs(rlim)) // 2)
    C = ranPFR(llim, rlim)
    BC = geo.Vector(B, C)
    l = BC.length2()
    while(l > (((abs(llim) + abs(rlim)) // 2) - 2)**2) :
        C = ranPFR(llim, rlim)
        BC = geo.Vector(B, C)
        l = BC.length2()
    OD = geo.Vector(A.x, A.y) + BC
    D = geo.Point(OD.x, OD.y)
    buf = [str(A), str(B), str(C), str(D)]
    tasks.append(buf)

def genRect() :
    genAB(abs(llim) + abs(rlim))
    BC = geo.Vector(0, 0)
    if (AB.x == 0) or (AB.y == 0) :
        if (AB.x == 0) : 
            y = 0
            x = random.randint(-abs(llim)-B.x, rlim - B.x)
            BC = geo.Vector(x, y)
        if (AB.y == 0) : 
            x = 0
            y = random.randint(-abs(llim)-B.y, rlim - B.y)
            BC = geo.Vector(x, y)
    elif AB.y % AB.x == 0 :
        k = AB.y // AB.x
        y =  random.randint(-(abs(llim) // abs(k)), rlim // abs(k))
        x = -k*y
        BC = geo.Vector(x, y)
    elif AB.x % AB.y == 0 :
        k = AB.x // AB.y
        x =  random.randint(-(abs(llim) // abs(k)), rlim // abs(k))
        y = -k*x
        BC = geo.Vector(x, y)
    else :  
        x = AB.y * random.randint(-(abs(llim) // abs(AB.y)), rlim // abs(AB.y))
        y = -AB.x*x//AB.y
        BC = geo.Vector(x, y)
    OC = geo.Vector(B.x, B.y) + BC
    C = geo.Point(OC.x, OC.y)
    OD = OC - AB
    D = geo.Point(OD.x, OD. y) 
    buf = [str(A), str(B), str(C), str(D)]
    tasks.append(buf)
       
def genTrap() :
    k = random.randint(2, (abs(llim) + abs(rlim)) // 4)
    A = ranPFR(llim, rlim)
    B = random.randint(llim ,rlim)
    
    
    
genParal()
genRect()
print(tasks)
