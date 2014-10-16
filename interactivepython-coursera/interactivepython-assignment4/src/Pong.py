__author__ = 'andrucuna'

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
# Constants
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
MIN_INIT_BALL_VEL = 2
MAX_INIT_BALL_VEL = 3
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PAD_SPEED = 3.5
LEFT = -1.0
RIGHT = 1.0

# Global variables
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0.0, 0.0]
direction = RIGHT
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT / 2]
paddle1_vel = [0.0, 0.0]
paddle2_vel = [0.0, 0.0]
score = [0, 0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score # these are ints
    global direction
    direction = RIGHT
    spawn_ball(direction)
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT / 2]
    paddle1_vel = [0.0, 0.0]
    paddle2_vel = [0.0, 0.0]
    score = [0, 0]

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = (random.randrange(MIN_INIT_BALL_VEL, MAX_INIT_BALL_VEL) + random.random() ) * direction
    ball_vel[1] = -abs(ball_vel[0])


# define event handlers
def draw(canvas):
    global score, paddle1_pos, paddle2_pos, ball_pos, ball_vel, direction

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

    # check for collisions & reflections
    if (ball_pos[0] <= BALL_RADIUS+PAD_WIDTH):
        direction = -direction
        if (ball_pos[1] > paddle1_pos[1]-HALF_PAD_HEIGHT) and (ball_pos[1] < paddle1_pos[1]+HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1
        else:
            score[1] += 1
            spawn_ball(direction)
    elif (ball_pos[0] >= WIDTH-BALL_RADIUS-PAD_WIDTH):
        direction = -direction
        if (ball_pos[1] > paddle2_pos[1]-HALF_PAD_HEIGHT) and (ball_pos[1] < paddle2_pos[1]+HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1
        else:
            score[0] += 1
            spawn_ball(direction)
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT-BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos[1]+paddle1_vel[1]>=HALF_PAD_HEIGHT) and (paddle1_pos[1]+paddle1_vel[1]<=HEIGHT-HALF_PAD_HEIGHT):
        paddle1_pos[1] = paddle1_pos[1] + paddle1_vel[1]

    if (paddle2_pos[1]+paddle2_vel[1]>=HALF_PAD_HEIGHT) and (paddle2_pos[1]+paddle2_vel[1]<=HEIGHT-HALF_PAD_HEIGHT):
        paddle2_pos[1] = paddle2_pos[1] + paddle2_vel[1]

    # draw paddles
    canvas.draw_polygon([(paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT), (paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT), (paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT), (paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT)], 1, "Red", "White")
    canvas.draw_polygon([(paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT), (paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT), (paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT), (paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT)], 1, "Red", "White")

    # draw scores
    canvas.draw_text(str(score[0]), [WIDTH/2-70, 80], 50, "White")
    canvas.draw_text(str(score[1]), [WIDTH/2+50, 80], 50, "White")


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = PAD_SPEED
    elif (key==simplegui.KEY_MAP["up"]):
        paddle2_vel[1] = -PAD_SPEED
    if chr(key)=='W':
        paddle1_vel[1] = -PAD_SPEED
    elif chr(key)=='S':
        paddle1_vel[1] = PAD_SPEED

def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key==simplegui.KEY_MAP["down"]) or (key==simplegui.KEY_MAP["up"]):
        paddle2_vel[1] = 0.0
    if (chr(key)=='W') or (chr(key)=='S'):
        paddle1_vel[1] = 0.0


# create frame
frame = simplegui.create_frame("Pong!", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 120)


# start frame
new_game()
frame.start()
