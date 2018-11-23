import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Shape:

    def __init__(self, x, y):
        # Object position
        self.x = x
        self.y = y
        self.size = random.randint(20, 50)

        # Object velocity (speed in pixels per second)
        self.vel_x = random.randint(-300, 300)
        self.vel_y = random.randint(-300, 300)

        # Find random color for this object
        red = random.randint(200, 255)
        green = random.randint(100, 200)
        blue = random.randint(100, 200)
        alpha = random.randint(100, 200)
        self.color = (red, green, blue, alpha)

    def right(self):
        return self.x + self.size

    def left(self):
        return self.x - self.size

    def top(self):
        return self.y + self.size

    def bottom(self):
        return self.y - self.size

    def update(self, delta_time):
        # Check if we hit the right wall and still moving right, then flip direction
        if self.right() >= SCREEN_WIDTH and self.vel_x > 0:
            self.vel_x *= -1
        # Check if we hit the left wall and still moving left, then flip direction
        elif self.left() <= 0 and self.vel_x < 0:
            self.vel_x *= -1

        # Check if we hit the window top and still are moving up, then flip direction
        if self.top() >= SCREEN_HEIGHT and self.vel_y > 0:
            self.vel_y *= -1
        # Check if we hit the window bottom, and still are moving down, then flip direction
        if self.bottom() <= 0 and self.vel_y < 0:
            self.vel_y *= -1

        # Calculate new position based on velocity
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)


class MyWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        # Create an empty list of shapes
        self.shapes = []

        arcade.set_background_color(arcade.color.BLACK_BEAN)

    def on_draw(self):
        arcade.start_render()

        for shape in self.shapes:
            shape.draw()

    def on_update(self, delta_time):
        for shape in self.shapes:
            shape.update(delta_time)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            # Create random start position
            random_x = random.randint(0, SCREEN_WIDTH)
            random_y = random.randint(0, SCREEN_HEIGHT)

            # Create new shape
            shape = Shape(random_x, random_y)

            # Add the new shape to the list
            self.shapes.append(shape)


def main():
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_update_rate(1/60)
    arcade.run()


if __name__ == "__main__":
    main()