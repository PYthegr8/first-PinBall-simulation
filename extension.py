'''
    Papa Yaw Owusu Nti
    CS 152B
    Project 8
    November 21st 2023
This program extends the pinball game by integrating sound effects using the Pygame library.
It adds goal and hit sound effects triggered by specific events,
The graphical window displays a neon-themed background image with neon-themed obstacles
'''

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import time
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the goal sound effect
goal_sound = pygame.mixer.Sound("D:\Schoolwork\CS152 PROJECTS\project 8\mixkit-winning-a-coin-video-game-2069.wav")  # Replace with the actual path to your sound file
hit_sound = pygame.mixer.Sound("D:\Schoolwork\CS152 PROJECTS\project 8\mixkit-basketball-ball-hard-hit-2093.wav") 



def buildObstacles(win):

    # create  lower obstacle balls
    left_ball = pho.Ball(win, radius=1.7, x=10, y=20, color=(205,179,139))
    left_ball.setElasticity(0.7)
    right_ball = pho.Ball(win, radius=1.7, x=30, y=20, color=(139,102, 139))
    
    # create  upper obstacle balls
    left_ball_upper = pho.Ball(win, radius=1.7, x=10, y=50, color=(205,179,139))
    left_ball.setElasticity(1.7)
    right_ball_upper = pho.Ball(win, radius=1.7, x=30, y=50, color=(139,102, 139))
    
    #create middle blocks
    middleblock_1 = pho.Block(win, dx=11, dy=2, color=[0, 0, 128], x=4, y=30)
    middleblock_2 = pho.Block(win, dx=11, dy=2, color=[0, 0, 128], x=36, y=30)
    middleblock_small_right = pho.Block(win, dx=8, dy=2, color=[255, 246 ,143], x=4, y=33)
    middleblock_small_left = pho.Block(win, dx=8, dy=2, color=[255, 246 ,143], x=36, y=33)
    
    # Create blocks with different characteristics
    block_1 = pho.Block(win, dx=14, dy=2, color=[0, 0, 128], x=7, y=6)
    block_2 = pho.Block(win, dx=14, dy=2, color=[0, 0, 128], x=33, y=6)
    block_3 = pho.Block(win, dx=2, dy=60, color=[255,255,255], x=0, y=30)
    block_4 = pho.Block(win, dx=2, dy=60, color=[255,255,255], x=40, y=30)
    block_5 = pho.Block(win, dx=40, dy=2, color=[255,255,255], x=20, y=60)

    # Neon Shapes
    middle_triangle_1 = pho.Triangle(win, side_length=5, color=[0, 0, 0], x=19.75, y=34.1)
    middlesquare = pho.Block(win, dx=5.7, dy=5.7, color=[70, 41, 106], x=19.7, y=24.1)
    middle_ball = pho.Ball(win, radius=3, x=19.7, y=13.7,color=(115, 35, 48))

    # Combine all obstacles into a list
    obstacles = [left_ball, right_ball,middle_ball, middleblock_1, middleblock_2,middleblock_small_left,middlesquare,
                left_ball_upper,right_ball_upper, middleblock_small_right,block_1, block_2, block_3,
                block_4, block_5,middle_triangle_1,]

    return obstacles

def main():
    win = gr.GraphWin("Pinball Game", 400, 600)
    
    # Extension 1 - background image
    image_path = "D:\\Schoolwork\\CS152 PROJECTS\\project 8\\neon play.gif"
    # image_path = "D:\\Schoolwork\\CS152 PROJECTS\\project 8\\neon pinball resize.gif"
    center_point = gr.Point(win.getWidth() / 2, win.getHeight() / 2)
    background_image = gr.Image(center_point, image_path)
    background_image.draw(win)

    

    shapes = buildObstacles(win)

    #balls = []
    # loop over the shapes list and have each Thing call its draw method
    for shape in shapes:
        shape.draw()

    # assign to dt the value 0.02
    dt = 0.02
    # assign to frame the value 0
    frame = 0
    count = 0
    textbox = gr.Text( gr.Point( 200, 50 ), f"NUMBER OF GOALS: {count}" )
    textbox.draw(win)
    textbox.setTextColor("yellow")
    # create a ball, give it an initial velocity and acceleration, and draw it

    ball = pho.Ball(win, color=(255, 255, 0))
    #win.getMouse()
    ball.draw()
    ball.setPosition(20, 30)
    ball.setVelocity(10, 10)
    ball.setAcceleration(0, -0.5)
    #balls.append(ball)
    
    userblock_left = pho.Block(win, dx=11, dy=2, color=[0, 0, 128], x=4, y=30)
    userblock_right = pho.Block(win, dx=11, dy=2, color=[0, 0, 128], x=36, y=30)
    
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
            count += 1
            textbox.setText(f"NUMBER OF GOALS: {count}")
            goal_sound.play()
            ball.setPosition(20, 30)
            ball.setVelocity(random.randint(-10, 10), random.randint(-10, 10))
            
        # assign to collided the value False
        collided = False
        for shape in shapes:
            # if the result of calling the collision function with the ball and the item is True
            #for ball in balls:
            if coll.collision(ball, shape, dt):
                # set collided to True
                collided = True
                hit_sound.play()
         # if collided is equal to False
        if not collided:
            # call the update method of the ball with dt as the time step
            #for ball in balls:
            ball.update(dt) 
        # increment frame
        frame += 1

    # close the window
    win.close()
if __name__ == "__main__":
    main()




