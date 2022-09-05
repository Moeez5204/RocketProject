from Planets import planetsList
from PhysicsEngine import *
from time import *

def move(player):
    for i in range(len(planetsList)):
        Thing = planetsList[i].mass


        angle, Distance = Trajectory(Thing, player)



        Force = GravityForce(Thing, Thing.mass, player.mass, Distance)
        ForceX, ForceY = Force * math.sin(angle), Force * math.cos(angle)

        Xspeed = movement(ForceX, player.mass, Thing.mass)
        Yspeed = movement(ForceY, player.mass, Thing.mass)

        player.x += Xspeed * time.dt
        player.y += Yspeed * time.dt




