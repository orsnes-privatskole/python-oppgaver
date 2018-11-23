# We are using the arcade library. See http://arcade.academy/ for documentation
import arcade
import random  # We want to use random for a new art image each time

# Create a window with 640 pixels width and 400 pixels height
WIDTH = 800
HEIGHT = 400
arcade.open_window(WIDTH, HEIGHT, "My Random Art")

# Use white canvas, see possible colors here: http://arcade.academy/arcade.color.html
arcade.set_background_color(arcade.color.DARK_BLUE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Draw dots in a random position with a random color, inside the window
number_of_dots = 200
for i in range(0, number_of_dots):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    red = random.randint(50, 255)
    green = random.randint(50, 255)
    blue = random.randint(100, 255)
    alpha = random.randint(100, 255)

    color = (red, green, blue, alpha)

    dot_size = random.randint(15, 50)

    if i % 2 == 0:
        arcade.draw_point(x, y, color, dot_size)
    else:
        arcade.draw_circle_filled(x, y, dot_size, color)



arcade.finish_render()  # Need this to put the drawing to the screen

arcade.run()  # This keep the window open until closed by the user