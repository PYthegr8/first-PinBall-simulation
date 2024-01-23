''' Papa Yaw Owusu Nti
    CS 152B
    Project 8
    November 7th 2023
    This program simulates physics objects.
    It defines a base class Thing with attributes and methods for common physics objects.
    Subclasses such as Ball, Block, Triangle, Pentagon, and BallonBlock implement specific shapes.
    
'''
import graphicsPlus as gr
import math

class Thing:
    """Base class for physics objects in the simulation."""
    def __init__(self, win, the_type):
        """
        Initialize a Triangle object with default attributes.
        """
        self.type = the_type
        self.elasticity =1
        self.color= (0,0,0)
        self.drawn =False
        self.mass = 1
        self.radius = 1
        self.position = [0,0]
        self.velocity = [0,0] 
        self.acceleration = [0,0]
        self.win = win
        self.scale = 10
        self.vis=[]
        
    def draw(self):
        """Draw the object in the graphics window."""
        for object in self.vis:
            object.draw(self.win)
        self.drawn = True

    def undraw(self):
        """Undraw the object from the graphics window."""
        for object in self.vis:
            object.undraw()
        self.drawn = False
        
    def getType(self):
        '''returns type of object'''
        return self.type

    def getMass(self):
        '''returns mass of object'''
        return self.mass
    
    def setMass(self, m):
        self.mass = m
        
    def getPosition(self):
        '''returns a 2-element list with the x, y position'''
        return self.position[:]
    
    def setPosition(self, px, py):
        """
        Takes arguments and Updates the position
        of the ball and its visual representation.
        """
        x_old = self.position[0]
        y_old = self.position[1]

        self.position[0] = px
        self.position[1] = py

        dx = (px - x_old) * (self.scale)
        dy = (py - y_old) * (-self.scale)

        for shape in self.vis:
            shape.move(dx, dy)
    
    def getVelocity(self):
        '''returns the Velocity of object'''
        return self.velocity[:]
    
    def setVelocity(self, vx, vy):
        """Takes arguments and Updates the velocity
        of the ball"""
        self.velocity = [vx, vy]

    def getAcceleration(self):
        '''returns the acceleration of object'''
        return self.acceleration[:]
    
    def setAcceleration(self, ax, ay):
        """Takes arguments and Updates the acceleration
        of the ball"""
        self.acceleration = [ax, ay]

    def getElasticity(self):
        """Get the elasticity of the object."""
        return self.elasticity

    def setElasticity(self,e):
        """Set the elasticity of the object."""
        self.elasticity = e

    def getScale(self):
        """Get the scale factor of the object."""
        return self.scale

    def getColor(self):
        """Get the color of the object."""
        return self.color

    def setColor(self, c):
        """
        Set the color of the object.
        """
        self.color = c
        if c is not None:
            for shape in self.vis:
                shape.setFill(gr.color_rgb(c[0], c[1], c[2]))

    def update(self, dt):
        """
        Update the object's position and velocity based on the current acceleration.
        """
        x_old = self.position[0]
        y_old = self.position[1]
        x_velocity = self.velocity[0]
        y_velocity = self.velocity[1]
        x_acceleration = self.acceleration[0]
        y_acceleration = self.acceleration[1]

        # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[0] = x_old + self.velocity[0] * dt + 0.5 * self.acceleration[0] * dt * dt
        self.position[1] = y_old + self.velocity[1] * dt + 0.5 * self.acceleration[1] * dt * dt

        # assign to dx the change in the x position times the scale factor (self.scale)
        # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        dx = (self.position[0] - x_old) * self.scale
        dy = (self.position[1] - y_old) * self.scale * (-1)

        # for each item in self.vis
        # call the move method of the graphics object with dx and dy as arguments
        for item in self.vis:
            item.move(dx, dy)

        # update the x velocity by adding the acceleration times dt to its old value
        # update the y velocity by adding the acceleration times dt to its old value
        x_velocity += x_acceleration * dt
        y_velocity += y_acceleration * dt
        self.setVelocity(x_velocity,y_velocity)

 

class Ball(Thing):
    """Class for representing a ball in the simulation."""
    def __init__(self, win, radius=1, x = 0, y = 0,  color=(0, 0, 0)):
        """Initialize a Ball object."""
        Thing.__init__(self, win, "ball")
        self.radius = radius
        self.position = [x, y]
        self.refresh()
        self.setColor(color)

    def refresh(self):
        """Update the visual representation of the ball."""
        drawn = self.drawn
        if drawn:
            self.undraw()
        self.vis = [
            gr.Circle(
                gr.Point(
                    self.position[0] * self.scale,
                    self.win.getHeight() - self.position[1] * self.scale,),
                self.radius * self.scale,)]
        if drawn:
            self.draw(self.win)

    def getRadius(self):
        '''returns the radius of the ball'''
        return self.radius

    def setRadius(self, r):
        '''sets the new radius of the ball'''
        self.radius = r
        self.refresh()
    

class Block(Thing):
    """Class for representing a block in the simulation."""
    def __init__(self, win, x = 0, y = 0, dx=1, dy=1, color=(0, 0, 0)):
        """Initialize a Block object."""
        Thing.__init__(self, win, "block")
        self.dx = dx
        self.dy = dy
        self.position = [x, y]
        self.refresh()
        self.setColor(color)

    def refresh(self):
        """Update the visual representation of the block."""
        drawn = self.drawn
        
        if drawn:
            self.undraw()
            
        self.point1 = gr.Point(
            self.position[0] * self.scale - (self.dx * self.scale / 2),
            self.win.getHeight() - (self.position[1] * self.scale - (self.dy * (self.scale) / 2)),)
        self.point2 = gr.Point(
            self.position[0] * self.scale + (self.dx * self.scale / 2),
            self.win.getHeight()- (self.position[1] * self.scale + (self.dy * (self.scale) / 2)),)
        self.vis = [gr.Rectangle(self.point1, self.point2)]
        
        if drawn:
            self.draw(self.win)

    def getWidth(self):
        """returns the width of the block"""
        return self.dx
    
    def setWidth(self, width):
        """
        Sets a new width for the block and updates its visuals
        """
        self.dx = width
        self.refresh()

    def getHeight(self):
        """returns the height of the block"""
        return self.dy
    
    def setHeight(self, Height):
        """
        Takes arguments and Updates the Height
        of the block and its visual representation.
        """
        self.dy = Height
        self.refresh()


class Triangle(Thing):
    """Class for representing a triangle in the simulation."""
    def __init__(self, win, x = 0, y = 0, side_length=1, color=(0, 0, 0)):
        """Initialize a Triangle object."""
        Thing.__init__(self, win, "triangle")
        self.side_length = side_length
        self.position = [x, y]
        self.radius = side_length/2
        self.setColor(color)
        self.refresh()
        
    def refresh(self):
        '''updates the visual representation of the triangle
        in the graphics window based on its current position'''
        p1 = gr.Point(self.position[0]*self.scale-(self.side_length*self.scale/2), self.win.getHeight()-(self.position[1]*self.scale - (((((self.side_length*self.scale)**2)-((self.side_length*self.scale/2)**2))**(1/2))/2)))
        p2 = gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]*self.scale + (((((self.side_length*self.scale)**2)+((self.side_length*self.scale/2)**2))**(1/2))/2)))
        p3 = gr.Point(self.position[0]*self.scale+(self.side_length*self.scale/2), self.win.getHeight()-(self.position[1]*self.scale - (((((self.side_length*self.scale)**2)-((self.side_length*self.scale/2)**2))**(1/2))/2)))
        self.vis = [gr.Polygon(p1,p2,p3)]

    def getRadius(self):
        return self.radius

    def setRadius(self, r):
        self.radius = r
        self.side_length= r*2
        self.refresh()



class Pentagon(Thing):
    """Class for representing a pentagon in the simulation."""
    def __init__(self, win, x=0, y=0, side_length=1, color=(0, 0, 0)):
        """Initialize a Pentagon object."""
        Thing.__init__(self, win, "pentagon")
        self.side_length = side_length
        self.position = [x, y]
        self.radius = side_length / (2 * (1 + (5 ** 0.5) / 2))  # Radius of the circumscribed circle
        self.setColor(color)
        self.refresh()

    def refresh(self):
        """Update the visual representation of the pentagon."""
        drawn = self.drawn

        if drawn:
            self.undraw()

        # Calculate pentagon vertices based on the center and side length
        angle = 360 / 5  # Angle between each vertex
        vertices = []
        for i in range(5):
            x = self.position[0] * self.scale + self.radius * self.scale * math.cos(math.radians(i * angle - 90))
            y = self.win.getHeight() - (self.position[1] * self.scale + self.radius * self.scale * math.sin(math.radians(i * angle - 90)))
            vertices.append(gr.Point(x, y))

        self.vis = [gr.Polygon(*vertices)]

        if drawn:
            self.draw()

    def getRadius(self):
        return self.side_length

    def setRadius(self, length):
        self.side_length = length
        self.radius = length / (2 * (1 + (5 ** 0.5) / 2))
        self.refresh()
        
    def setColor(self, c):
        self.color = c
        if c is not None:
            for shape in self.vis:
                shape.setFill(gr.color_rgb(c[0], c[1], c[2]))







class BallonBlock(Thing):
    """Class for representing a block with a circular balloon on top in the simulation."""
    def __init__(self, win, x=0, y=0, width=2, height=2.5, tip_height=1.5, color=(0, 0, 0)):
        """Initialize a BallonBlock object."""
        Thing.__init__(self, win, "customshape")
        self.width = width
        self.height = height
        self.tip_height = tip_height
        self.position = [x, y]
        self.refresh()
        self.setColor(color)

    def refresh(self):
        """Update the visual representation of the BallonBlock."""
        drawn = self.drawn
        if drawn:
            self.undraw()

        # Create a rectangle
        rect = gr.Rectangle(
            gr.Point(
                (self.position[0] - self.width / 2) * self.scale,
                self.win.getHeight() - (self.position[1] + self.height / 2) * self.scale,
            ),
            gr.Point(
                (self.position[0] + self.width / 2) * self.scale,
                self.win.getHeight() - (self.position[1] - self.height / 2) * self.scale,
            ),
        )

        # Create a circle centered on top of the block
        circle_radius = self.width / 2
        circle = gr.Circle(
            gr.Point(self.position[0] * self.scale, self.win.getHeight() - (self.position[1] + self.height / 2 + circle_radius) * self.scale),
            circle_radius * self.scale
        )

        self.vis = [rect, circle]

        if drawn:
            self.draw(self.win)

    def getRadius(self):
        # Use the Pythagorean theorem to find the diagonal distance of the bounding box
        diagonal_distance = ((self.width**2 + (self.height + self.tip_height)**2)**(1/2))
        # The radius of the bounding circle is half of the diagonal distance
        radius = diagonal_distance / 2
        return radius
