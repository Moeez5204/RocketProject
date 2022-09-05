from ursina import *



app = Ursina()

class Planets(Entity):
    def __init__(self,position,scale,rotation,collider,mass):
        super().__init__(
            model = "sphere",
            position = position,
            scale = scale,
            rotation = rotation,
            collider = 'mesh',
            mass = mass)

class moon(Entity):
    def __init__(self,position = (0,20,100)):
        super().__init__(
           model="sphere",
           color="#AFFF3C",
           scale=(100,100,100),
           collider="mesh",
           position=position,
           texture="white_cube")



Sun = Entity(model = 'sphere',  #making the first planet,
                position =(1,1,1),
                scale = 200000,
                rotation = (0,0,30),
                color = color.yellow,
                texture = 'sun_texture',
                collider = 'mesh',
                mesh = 'mesh',
                mass = 1000)



earth = Entity(model= 'sphere',
               scale = 50000,
               position = (0,0,0),
               rotation = (0,0,30),
               texture = 'earth_texture',
               collider = 'mesh',
               mass = 900
                )

venus = Entity(model ='sphere',
               scale = 47447,
               position = (0,0,0),
               rotation = (0,0,30),
               texture = 'venus_texture',
               collider= 'mesh',
               mass= 800)

mars = Entity(model = 'sphere',
              scale = 49000,
              position = (0,0,0),
              rotation = (0,0,30),
              texture = 'mars_texture',
              collider= 'mesh',
              mass = 700)

jupiter = Entity(model = 'sphere',
                 scale = 100000,
                 position = (0,0,0),
                 rotation = (0,0,30),
                 texture = 'jupiter_texture',
                 collider= 'mesh',
                 mass = 800)

saturn = Entity(model = 'sphere',
                 scale = 90000,
                 position = (0,0,0),
                 rotation = (0,0,30),
                 texture = 'saturn_texture',
                 collider= 'mesh',
                 mass = 800)


Uranus = Entity(model = 'sphere',
                 scale = 60000,
                 position = (0,0,0),
                 rotation = (0,0,30),
                 texture = 'uranus_texture',
                 collider= 'mesh',
                 mass = 800)


Neptune = Entity(model = 'sphere',
                 scale = 100000,
                 position = (0,0,0),
                 rotation = (0,0,30),
                 texture = 'neptune_texture',
                 collider= 'mesh',
                 mass = 800)





planetsList = [Sun,earth,mars,venus]
