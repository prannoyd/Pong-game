
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[HEIGHT/2,WIDTH/2]
ball_vel=[-40.0/60.0,25.0/60.0]
paddle1_pos=[0,PAD_HEIGHT]
paddle2_pos=[WIDTH,HEIGHT-PAD_HEIGHT]
paddle1_vel=[4,4]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    #spawn_ball()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, 0],[WIDTH - HALF_PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[0]<=BALL_RADIUS:
        ball_vel[0]=-ball_vel[0]
    if ball_pos[0]>=WIDTH-BALL_RADIUS:
        ball_vel[0]=-ball_vel[0]
    if ball_pos[1]>=HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    if ball_pos[1]<=BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"Red","White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_line([0,PAD_WIDTH],paddle1_pos, 10, "White")
    #canvas.draw_line([WIDTH-PAD_WIDTH,0],[WIDTH-PAD_WIDTH,PAD_HEIGHT], 10, "White")
    canvas.draw_line([WIDTH,WIDTH-PAD_WIDTH],paddle2_pos, 10, "White")
    # determine whether paddle and ball collide    
    if ball_pos[0]<=BALL_RADIUS:
        spawn_ball(LEFT)
    if ball_pos[0]>=WIDTH-BALL_RADIUS:
        spawn_ball(RIGHT)
    # draw scores
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle1_pos[0]+=paddle1_vel[0]
        paddle1_pos[1]+=paddle1_vel[1]
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
