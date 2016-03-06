# implementation of card game - Memory

import simplegui
import random
cards = []
exposed = [False] * 16
state = 0
turns = 0
card1 = 0
card2 = 0

# helper function to initialize globals
def new_game():
    global cards, exposed, state, turns, card1, card2
    cards = range(8) + range(8)
    random.shuffle(cards)
    exposed = [False] * 16
    state = 0
    card1 = 0
    card2 = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    global state, card1, card2, turns
    idx = pos[0] // 50

    if not exposed[idx]:
        exposed[idx] = True
        
        if state == 0:
            state = 1
            turns = 1
            card1 = idx
        elif state == 1:
            state = 2
            card2 = idx
        else:
            state = 1
            if not cards[card1] == cards[card2]:
                exposed[card1] = False
                exposed[card2] = False
            turns += 1
            card1 = idx
            card2 = 0
        
        label.set_text("Turns = " + str(turns))

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for idx in range(len(cards)):
        pos = 50 * idx
        if exposed[idx]:
            canvas.draw_text(str(cards[idx]), [pos+15, 60], 30, "White")
        else:
            canvas.draw_polygon([[pos, 0], [pos+50, 0], [pos+50, 100], [pos, 100]], 1, 'Black', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric