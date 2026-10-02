from re import L

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

# game class
class OutOfTheLoopGame:
    WORDS = {"food":
      # food words
        [# Mains
        "Pizza", "Sushi", "Lasagna", "Curry", "Kebab", "Pho", "Ramen", "Paella", "Spaghetti",
        "Fondue", "Falafel", "Grilled cheese",
        "Quesadilla", "Calzone", "Shawarma", "Stir-fry",

        # Breakfast
        "Pancakes", "Oatmeal", "Cereal", "Bagel", "Omelette", "Croissant",

        # Snacks
        "Popcorn", "Pretzel", "Chips", "Nachos", "Trail mix", "Granola bar",
        "Crackers", "Hummus", "Guacamole",

        # Desserts
        "Cheesecake", "Brownie", "Sundae", "Tiramisu", "Donut", "Cupcake",
        "Pudding", "Apple pie", "Macaron", "Cotton candy"],

      # household objects
      "household": [
          # Kitchen
          "Plate", "Bowl", "Mug", "Fork", "Spoon", "Knife", "Frying pan",
          "Saucepan", "Kettle", "Toaster", "Blender", "Whisk", "Spatula",
          "Cutting board", "Colander", "Tupperware", "Rolling pin", "Oven mitt",
          "Dish towel", "Grater", "Peeler", "Can opener", "Corkscrew", "Tongs",
          "Mixing bowl",

          # Living room
          "Sofa", "Armchair", "Bookshelf", "Television",
          "Remote control", "Lamp", "Rug", "Cushion",
          "Picture frame", "Candle", "Clock", "Coaster",

          # Bedroom
          "Bed", "Pillow", "Duvet", "Mattress", "Nightstand", "Wardrobe",
          "Dresser", "Mirror", "Alarm clock", "Hanger", "Hairbrush",

          # Bathroom
          "Toothbrush", "Toothpaste", "Towel", "Soap", "Shampoo", "Conditioner",
          "Hair dryer", "Sink", "Bathtub", "Shower curtain",

          # Cleaning
          "Vacuum cleaner", "Broom", "Mop", "Dustpan", "Bucket", "Sponge",
          "Trash can", "Iron", "Ironing board", "Spray bottle",

          # Tools
          "Hammer", "Screwdriver", "Nail", "Screw", "Tape measure", "Flashlight",
          "Batteries", "Extension cord", "Ladder", "Toolbox", "Wrench",
          "Duct tape", "Scissors", "Glue", "Stapler",

          # Electronics
          "Laptop", "Charger", "Headphones", "Speaker",
          "Keyboard", "Mouse", "Printer",
      ]
    }

    def __init__(self, players: int, theme: str):
        self.players = players
        self.theme = str




clear(TEAL)

display.set_pen(WHITE)
display.text("OUT OF THE LOOP", 10, 10, 200, 4)

display.text("start", WIDTH-100, HEIGHT-35, 200, 3)

display.update()
