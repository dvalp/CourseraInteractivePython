# template for "Stopwatch: The Game"
import simplegui
# define global variables
counter = 0
tries = 0
score = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    b = (t // 100) % 6
    c = (t // 10) % 10
    d = t % 10
    return str(a) + ':' + str(b) + str(c) + '.' + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    global tries
    global score
    
    if timer.is_running():
        tries += 1
        if (counter % 10) == 0:
            score += 1
        
    timer.stop()
    
def reset_handler():
    global counter
    global tries
    global score
    
    timer.stop()
    counter = 0
    score = 0
    tries = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), (65, 80), 30, 'White')
    canvas.draw_text(str(score) + ' / ' + str(tries), (150, 20), 20, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 200, 150)
frame.set_draw_handler(draw_handler)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
start_button = frame.add_button('Start', start_handler, 100)
stop_button = frame.add_button('Stop', stop_handler, 100)
reset_button = frame.add_button('Reset', reset_handler, 100)

# start frame
frame.start()


# Please remember to review the grading rubric
