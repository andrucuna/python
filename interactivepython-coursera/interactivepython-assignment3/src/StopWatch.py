__author__ = 'andrucuna'

# template for "Stopwatch: The Game"
import simplegui


# define global variables
timeElapsed = 0
interval = 100
stops = 0
wins = 0
isRuning = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    decs = t%10
    secs = (t/10) % 60
    mins = (t/10) / 60
    result = str(secs)
    if len(result)<2:
        result = "0"+result
    result = str(mins)+":"+result+"."+str(decs)
    return result


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isRuning
    timer.start()
    isRuning = True

def stop():
    global stops
    global wins
    global isRuning
    timer.stop()
    if isRuning:
        stops += 1
        if (timeElapsed%10) == 0:
            wins += 1
    isRuning = False

def restart():
    global timeElapsed
    global stops
    global wins
    global isRuning
    timer.stop()
    isRuning = False
    timeElapsed = 0
    stops = 0
    wins = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global timeElapsed
    timeElapsed += 1


# define draw handler
def draw(canvas):
    canvas.draw_text(format(timeElapsed), [65, 80], 30, "White")
    canvas.draw_text(str(wins)+"/"+str(stops), [160, 25], 20, "Green")


# create frame
frame = simplegui.create_frame("Stopwatch: The Game!", 200, 140)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Restart", restart, 120)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()

# Please remember to review the grading rubric
