''' Papa Yaw Owusu Nti
    CS 152B
    Project 8
    November 20th 2023
    This  program creates a pinball game using the graphics library. 
    It defines obstacles :balls, blocks, triangles, and pentagons, 
    and animates a bouncing ball within the pinball window 
    The program includes collision detection and the graphical window displays a background image. 
    The game loop continues until the user presses 'q' to exit.
'''

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import time
import random



def buildObstacles(win):

    # create  lower obstacle balls
    left_ball = pho.Ball(win, radius=3, x=10, y=20, color=(205,179,139))
    left_ball.setElasticity(0.7)
    
    right_ball = pho.Ball(win, radius=3, x=30, y=20, color=(139,58,58 ))
    
    # create  upper obstacle balls
    upper_ball_left = pho.Ball(win, radius=2, x=35, y=50, color=(95, 100, 59))
    upper_ball_right = pho.Ball(win, radius=2, x=5, y=50, color=(95, 100, 59))
    
    #create middle blocks
    middleblock_1 = pho.Block(win, dx=14, dy=2, color=[0, 0, 128], x=7, y=30)
    middleblock_1.setElasticity(1.7)
    middleblock_2 = pho.Block(win, dx=14, dy=2, color=[0, 0, 128], x=33, y=30)
    middleblock_small_right = pho.Block(win, dx=8, dy=2, color=[255, 246 ,143], x=4, y=33)
    middleblock_small_left = pho.Block(win, dx=8, dy=2, color=[255, 246 ,143], x=36, y=33)
    
    # Create blocks with different characteristics
    block_1 = pho.Block(win, dx=14, dy=2, color=[0, 0, 128], x=7, y=6)
    block_2 = pho.Block(win, dx=14, dy=2, color=[0, 0, 128], x=33, y=6)
    block_3 = pho.Block(win, dx=2, dy=60, color=[0, 0, 128], x=0, y=30)
    block_3.setElasticity(1.5)
    block_4 = pho.Block(win, dx=2, dy=60, color=[0, 0, 128], x=40, y=30)
    block_5 = pho.Block(win, dx=40, dy=2, color=[0, 0, 128], x=20, y=60)

    # Create triangles 
    middle_triangle_1 = pho.Triangle(win, side_length=4, color=[0, 0, 0], x=20, y=10)

    # Create pentagons 
    pentagon_1 = pho.Pentagon(win, side_length=20, color=[0,0, 0], x=20, y=50)

    # Combine all obstacles into a list
    obstacles = [left_ball, right_ball,upper_ball_left,upper_ball_right, middleblock_1, middleblock_2,middleblock_small_left,
                 middleblock_small_right,block_1, block_2, block_3, block_4, block_5,middle_triangle_1,pentagon_1]

    return obstacles

def main():
    win = gr.GraphWin("Pinball Game", 400, 600)
    
    # Extension 1 - background image
    image_path = "D:\\Schoolwork\\CS152 PROJECTS\\project 8\\pinball_neon-removebg-preview.png"
    center_point = gr.Point(win.getWidth() / 2, win.getHeight() / 2)
    background_image = gr.Image(center_point, image_path)
    background_image.draw(win)

    

    shapes = buildObstacles(win)


    # loop over the shapes list and have each Thing call its draw method
    for shape in shapes:
        shape.draw()

    # assign to dt the value 0.02
    dt = 0.02

    # assign to frame the value 0
    frame = 0

    # create a ball, give it an initial velocity and acceleration, and draw it

    ball = pho.Ball(win, color=(255, 255, 0))
    #win.getMouse()
    ball.draw()
    ball.setPosition(20, 30)
    ball.setVelocity(10, 10)
    ball.setAcceleration(0, -0.5)

    
    
    
    while True:
        time.sleep(0.5 * dt)
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            # call win.update()
            win.update()
        key = win.checkKey()
        # using checkKey, if the user typed a 'q' then break
        if key == "q":
            break
        # if the ball is out of bounds, re-launch it
        if (
            (ball.getPosition()[0] * ball.scale) > 400
            or (ball.getPosition()[0] * ball.scale) < 0
            or (ball.getPosition()[1] * ball.scale) > 600
            or (ball.getPosition()[1] * ball.scale) < 0
        ):
            ball.setPosition(20, 30)
            ball.setVelocity(random.randint(-10, 10), random.randint(-10, 10))
        # assign to collided the value False
        collided = False
        for shape in shapes:
            # if the result of calling the collision function with the ball and the item is True
            if coll.collision(ball, shape, dt):
                # set collided to True
                collided = True
                # print ("collision")
         # if collided is equal to False
        if not collided:
            # call the update method of the ball with dt as the time step
            ball.update(dt) 
        # increment frame
        frame += 1

    # close the window
    win.close()
if __name__ == "__main__":
    main()


