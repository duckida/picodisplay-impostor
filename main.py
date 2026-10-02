from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
from pimoroni import Button, RGBLED

# screen setup
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)

display.set_backlight(0.8)
display.set_font("bitmap6")

WIDTH, HEIGHT = display.get_bounds()

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
TEAL = display.create_pen(53, 222, 232)
RED = display.create_pen(252, 21, 0)
YELLOW = display.create_pen(252, 223, 2)
GREEN = display.create_pen(62, 188, 98)

def clear(color):
    display.set_pen(color)
    display.clear()
    display.update()

# led & button setup
led = RGBLED(6, 7, 8)
led.set_rgb(0, 0, 0)

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

# the code starts here...

clear(TEAL)

display.set_pen(WHITE)
display.text("OUT OF THE LOOP", 10, 10, 200, 4)

display.text("start", WIDTH-100, HEIGHT-35, 200, 3)

display.update()
