from time import *
from MainController import ThirdPersonController,teleport
from Planets import *
from Database import everyupdate,data,nextletter


t = 0

player = ThirdPersonController(model = 'rocketmodel.obj',  # making the player
                               position = (0,5000,0),
                               scale = 0.1,
                               rotation = (0,0,0),
                               )

Sky(texture = 'background')  # giving the background the space theme

camera.rotation_x = 0
camera.fov = 100

def orbits(object,dfs): # when trying to import there were alot of errors

    global t
    t += time.dt
    timecounter = t / 100


    X = dfs * math.sin(timecounter)
    Z = dfs  * math.cos(timecounter)
    object.position = Vec3(X,0,Z)


def update():
    if held_keys['q']:
        quit()  # easy way to quit the game

    camera.x = player.x -10
    camera.y = player.y + 30  # getting the camera to sit just above the rocket to allow
    camera.z = player.z - 20  # a facing down on the rocket so you can see the majority of it

    ThirdPersonController.controller(player)  # checking for new inputs every tick
    orbits(earth,60000)
    orbits(venus,30000)
    orbits(mars,5000)
    orbits(jupiter,100000)  #making all the planets orbit
    orbits(saturn,140000)
    orbits(Uranus,250000)
    orbits(Neptune,350000)

    everyupdate(player,data[0])

    teleport(player) #easy moving



app.run() #launching the application





