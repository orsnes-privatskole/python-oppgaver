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

        # Object velocity (speed)
        self.vel_x = random.randint(-300, 300)
        self.vel_y = random.randint(-300, 300)

    def update(self, delta_time):
        if self.right() >= SCREEN_WIDTH and self.vel_x > 0:
            self.vel_x *= -1

        if self.left() <= 0 and self.vel_x < 0:
            self.vel_x *= -1

        if self.top() >= SCREEN_HEIGHT and self.vel_y > 0:
            self.vel_y *= -1

        if self.bottom() <= 0 and self.vel_y < 0:
            self.vel_y *= -1

        # Calculate new position based on velocity
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, arcade.color.LIGHT_CORAL)

    def right(self):
        return self.x + self.size

    def left(self):
        return self.x - self.size

    def top(self):
        return self.y + self.size

    def bottom(self):
        return self.y - self.size


class MyWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        # Create a shape object at 0 (left) x position and center of Y axis
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

            # Create a new shape
            shape = Shape(random_x, random_y)

            # Add the new shape to the list
            self.shapes.append(shape)


def main():
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_update_rate(1/60)
    arcade.run()


if __name__ == "__main__":
    main()