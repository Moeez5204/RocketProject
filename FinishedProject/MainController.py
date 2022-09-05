from ursina  import  *
from Planets import *



class ThirdPersonController(Entity):
    def __init__(self,model,position,scale,rotation):  #creats the object
        super().__init__(
            model=model,  # the shape of the user
            position=position,  #the geographic posistion of the users object
            scale=scale ,       # the scale of the users object
            rotation=rotation,
            collider = 'mesh',
            texture ='rocket_texture.png'
        )

    def controller(self):
        if held_keys['left arrow']: # creates basic movement for the object
           self.rotation_z += -1
           camera.rotation_y+= -1 #left
        if held_keys['right arrow']:
            camera.rotation_y  += 1 #right
            self.rotation_z += 1

        if held_keys['up arrow']:
           camera.rotation_x += -1 #up
           self.rotation_x += -1


        if held_keys['down arrow']:
            camera.rotation_x += 1 #down

        if held_keys['x']:
          camera.rotation_z += 1.5  #turn left
          self.rotation_z += -3
        if held_keys['z']:
          camera.rotation_z += -1.5 #turn right
          self.rotation_z += 3



        if held_keys['w']: # forward movment
            self.z += 5
            camera.z += 2.5
        if held_keys['s']: #backward movement
            self.z += -5
            camera.z += -2.5

        if held_keys['a']: #left movment
            self.x += -5
            camera.x += -2.5

        if held_keys['d']:
            self.x += 5
            camera.x += 2.5

        if held_keys['space']:
            self.y += 5
            camera.y += 5

        if held_keys['shift']:
            self.y += -5
            camera.y += -2.5

        if held_keys['f']:
            camera.fov += 1

        if held_keys['g']:
            camera.fov -= 1


def teleport(self):
        if held_keys['1']:
            self.position = (earth.x,earth.y+25000,earth.z)
        if held_keys['2']:
            self.position = (Sun.x,Sun.x +100000,Sun.z)
        if held_keys['3']:
            self.position = (venus.x,venus.y +23723.5,venus.z)
        if held_keys['4']:
            self.position = (mars.x,mars.y +9563,mars.z)
        if held_keys['5']:
            self.position = (jupiter.x,jupiter.y +50000,jupiter.z)
        if held_keys['6']:
            self.position = (saturn.x, saturn.y + 45000, saturn.z)
        if held_keys['7']:
            self.position = (Uranus.x,Uranus.y +30000,Uranus.z)
        if held_keys['8']:
            self.position = (Neptune.x, Neptune.y + 50000, Neptune.z)



















