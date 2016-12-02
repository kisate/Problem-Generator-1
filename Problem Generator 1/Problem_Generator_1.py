import geo
import random
llim = -10
rlim = 10
def ranPFR(a, b) :
    return geo.Point(random.randint(a, b), random.randint(a, b))
tasks = {}

def genParal() :
    A = ranPFR(llim + 1, rlim - 1)
    B = ranPFR(llim + 1, rlim - 1)
    AB = geo.Vector(A, B)
    DC = AB

    minx = llim - DC.x
    if llim > minx : 
        minx = llim
    maxx = rlim - DC.x
    if rlim < maxx : 
        maxx = rlim
    miny = llim - DC.y
    if llim > miny : 
        miny = llim
    maxy = rlim - DC.y
    if rlim < maxy : 
        maxy = rlim
    D = geo.Point(random.randint(minx, maxx), random.randint(miny, maxy))
    OC = geo.Vector(D.x, D.y) + DC
    C = geo.Point(OC.x, OC.y)    
    
    buf = ["A : " + str(A),"B : " + str(B),"C : " + str(C),"D : " + str(D)]
    tasks.update({"Paral" : buf})

def genRect() :
    k = random.randint(2,(rlim-llim-1) // 2)
    if random.randint(0, 1) == 1 :
        k *= - 1    
    x = random.randint(llim // abs(k), rlim // abs(k))
    y = random.randint(llim // abs(k), rlim // abs(k))    
    
    y2 = x * k  
    x2 = -y * k

    if random.randint(0 , 1) == 1 :
        AD = geo.Vector(x, y)
        BC = AD 
        AB = geo.Vector(x2, y2)
        DC = AB
    else :
        AB = geo.Vector(x, y)
        DC = AB 
        AD = geo.Vector(x2, y2)
        BC = AD
    minx = llim - AB.x
    if llim > minx : 
        minx = llim
    maxx = rlim - AB.x
    if rlim < maxx : 
        maxx = rlim
    miny = llim - AB.y
    if llim > miny : 
        miny = llim
    maxy = rlim - AB.y
    if rlim < maxy : 
        maxy = rlim
    A = geo.Point(random.randint(minx, maxx), random.randint(miny, maxy))
    OB = geo.Vector(A.x, A.y) + AB
    B = geo.Point(OB.x, OB.y)
    
    OC = OB + BC 
    OD = geo.Vector(A.x, A.y) + AD

    C = geo.Point(OC.x, OC.y)
    D = geo.Point(OD.x, OD.y)   
    
    if random.randint(0, 1) == 1 :
        AB = geo.Vector(x, y)
        DC = AB    
    buf = ["A : " + str(A),"B : " + str(B),"C : " + str(C),"D : " + str(D)]
    tasks.update({"Rectangle" : buf})

       
def genTrap() :
    k = random.randint(2, (rlim - llim) // 4)
    AB = geo.Vector(random.randint(-((rlim - llim) // k), (rlim - llim) // k), random.randint(-((rlim - llim) // k), (rlim - llim) // k))
    DC = AB * k
    minx = llim - AB.x
    if llim > minx : 
        minx = llim
    maxx = rlim - AB.x
    if rlim < maxx : 
        maxx = rlim
    miny = llim - AB.y
    if llim > miny : 
        miny = llim
    maxy = rlim - AB.y
    if rlim < maxy : 
        maxy = rlim
    A = geo.Point(random.randint(minx, maxx), random.randint(miny, maxy))
    OB = geo.Vector(A.x, A.y) + AB
    B = geo.Point(OB.x, OB.y)
    
    minx = llim - DC.x
    if llim > minx : 
        minx = llim
    maxx = rlim - DC.x
    if rlim < maxx : 
        maxx = rlim
    miny = llim - DC.y
    if llim > miny : 
        miny = llim
    maxy = rlim - DC.y
    if rlim < maxy : 
        maxy = rlim
    D = geo.Point(random.randint(minx, maxx), random.randint(miny, maxy))
    OC = geo.Vector(D.x, D.y) + DC
    C = geo.Point(OC.x, OC.y)    
   
    buf = ["A : " + str(A),"B : " + str(B),"C : " + str(C),"D : " + str(D)]
    tasks.update({"Trapeze" : buf})

def genSqr() :
     
    x = random.randint(llim // 2, rlim // 2)
    y = random.randint(llim // 2, rlim // 2)    
    
    if random.randint(0 , 1) == 1 :
        y2 = x 
        x2 = -y
    else :
        y2 = -x 
        x2 = y

    if random.randint(0 , 1) == 1 :
        AD = geo.Vector(x, y)
        BC = AD 
        AB = geo.Vector(x2, y2)
        DC = AB
    else :
        AB = geo.Vector(x, y)
        DC = AB 
        AD = geo.Vector(x2, y2)
        BC = AD
    minx = max(llim - AB.x, llim, llim - AD.x)
    maxx = min(rlim - AB.x, rlim, rlim - AD.x)
    miny = max(llim - AB.y, llim, llim - AD.y)
    maxy = min(rlim - AB.y, rlim, rlim - AD.y)
    A = geo.Point(random.randint(minx, maxx), random.randint(miny, maxy))
    OB = geo.Vector(A.x, A.y) + AB
    B = geo.Point(OB.x, OB.y)
    
    
    OC = OB + BC 
    OD = geo.Vector(A.x, A.y) + AD

    C = geo.Point(OC.x, OC.y)
    D = geo.Point(OD.x, OD.y)   
    
    buf = ["A : " + str(A),"B : " + str(B),"C : " + str(C),"D : " + str(D)]
    tasks.update({"Square" : buf})

def genDia() : 
    x = random.randint(llim // 2, rlim // 2)
    y = random.randint(llim // 2, rlim // 2)
    AB = geo.Vector(x, y)
    BC = geo.Vector(x, -y)
    AD = BC
    DC = AB

    minx = llim - AB.x
    if llim > minx : 
        minx = llim
    maxx = rlim - AB.x
    if rlim < maxx : 
        maxx = rlim
    miny = llim - AB.y
    if llim > miny : 
        miny = llim
    maxy = rlim - AB.y
    if rlim < maxy : 
        maxy = rlim
    A = geo.Point(random.randint(minx, maxx), random.randint(miny, maxy))
    OB = geo.Vector(A.x, A.y) + AB
    B = geo.Point(OB.x, OB.y)

    OC = OB + BC
    OD = geo.Vector(A.x, A.y) + AD

    C = geo.Point(OC.x, OC.y)
    D = geo.Point(OD.x, OD.y)

    buf = ["A : " + str(A),"B : " + str(B),"C : " + str(C),"D : " + str(D)]
    tasks.update({"Diamond" : buf})

def genCom() :
    x = random.randint(llim + 1, rlim - 1)
    y = random.randint(llim + 1, rlim - 1)
    
    x2 = random.randint(llim + 1, rlim - 1)
    y2 = random.randint(llim + 1, rlim - 1)
    
    while(x == x2) and (y == y2) :
        x2 = random.randint(llim + 1, rlim - 1)
        y2 = random.randint(llim + 1, rlim - 1)
    
    AB = geo.Vector(x, y)
    DC = geo.Vector(x2, y2)

    minx = llim - AB.x
    if llim > minx : 
        minx = llim
    maxx = rlim - AB.x
    if rlim < maxx : 
        maxx = rlim
    miny = llim - AB.y
    if llim > miny : 
        miny = llim
    maxy = rlim - AB.y
    if rlim < maxy : 
        maxy = rlim
    A = geo.Point(random.randint(minx, maxx), random.randint(miny, maxy))
    OB = geo.Vector(A.x, A.y) + AB
    B = geo.Point(OB.x, OB.y)

    x = random.randint(llim - A.x, rlim - A.x)
    y = random.randint(llim - A.y, rlim - A.y)
    
    x2 = random.randint(llim - B.x, rlim - B.x)
    y2 = random.randint(llim - B.y, rlim - B.y)
    
    while(x == x2) and (y == y2) :
        x2 = random.randint(llim - B.x, rlim - B.x)
        y2 = random.randint(llim - B.y, rlim - B.y)
    
    AD = geo.Vector(x, y)
    BC = geo.Vector(x2, y2)

    OC = OB + BC
    OD = geo.Vector(A.x, A.y) + AD

    C = geo.Point(OC.x, OC.y)
    D = geo.Point(OD.x, OD.y)

    buf = ["A : " + str(A),"B : " + str(B),"C : " + str(C),"D : " + str(D)]
    tasks.update({"Common" : buf})
    
        
    
    
    
genParal()
genRect()
genTrap()
genSqr()
genDia()
genCom()
keys =  list(tasks.keys())     
random.shuffle(keys)
for key in keys :
    print(key + " ")
for key in keys :
    print(tasks[key])
