import math


def GravityForce(planet,mass1, mass2, distance):
    global force
    G = 6.67 * 10 ** -11                  #gravity calculator
    temp = mass1 * mass2 * G
    force = temp / (planet.radius + distance) ** 2


def timeneeded(U, A, S):
    TempaA = math.sqrt((U ** 2) - 4 * A * S)
    TEMPT1 = (-U + TempaA)
    T1 = TEMPT1 / (2 * A)
    TEMPT2 = (-U - TempaA)   # time calcultor
    T2 = TEMPT2 / (2 * A)

    if T1 > 0 and T2 <= 0:
        Time = T1
    elif T2 > 0 and T1 <= 0:
        Time = T2
    elif T2 > 0 and T1 > 0:
        if T2 > T1:
            Time = T2
        else:
            Time = T1
    print(Time)


def pythagerous(A,B):
    temp = A**2 + B**2
    ans = math.sqrt(temp)
    return ans

def Trajectory(objectA,objectB):

    global distance
    global angle

    X1,X2  = objectA.x,objectB.x
    Y1,Y2 = objectA.y,objectB.y
    Z1,Z2 = objectA.z,objectB.z

    Xdifferacne = X2 -X1
    Ydifferance = Y2-Y1
    Zdifferncae = Z2 -Z1

    AC = pythagerous(Xdifferacne,Zdifferncae)  #3d pythagerous to find the distacne betweeen two objects
    GC = Ydifferance
    AG = pythagerous(AC,GC)

    Distance= AG
    angle = math.atan(GC/AC) # find the 3d angle betwen two objects
    return angle,Distance


#def force_finder(angle,Distance,):

def attraction(mass1, mass2, force):
    global acceleration
    global bigger_mass
    if mass1 > mass2:
        bigger_mass = mass1               #accelearion decider
    else:
        bigger_mass = mass2

    acceleration = force / bigger_mass
    print(acceleration)


def movement(Force,object1,object2):
      attraction(object1.mass,object2.mass,Force)    # moving all the objects
      speed = acceleration / 10
      return speed
