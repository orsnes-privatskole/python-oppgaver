import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class RainDrop:

    def __init__(self, x, y):
        # Object position
        self.x = x
        self.y = y

        # Object velocity (speed)
        self.vel_x = 0
        self.vel_y = -100

    def update(self, delta_time):
        # Calculate new position based on velocity
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time

        # If reached bottom, move back to top at random X
        if self.y < 0:
            self.y = SCREEN_HEIGHT
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self):
        arcade.draw_point(self.x, self.y, arcade.color.LIGHT_GRAY, 2)


class MyWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        background_color = (50, 50, 60)
        arcade.set_background_color(background_color)

        self.raindrops = []

        for i in range(0, 49):
            raindrop = RainDrop(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            self.raindrops.append(raindrop)

    def on_draw(self):
        arcade.start_render()
        for raindrop in self.raindrops:
            raindrop.draw()

    def on_update(self, delta_time):
        for raindrop in self.raindrops:
            raindrop.update(delta_time)

    def on_key_press(self, key, key_modifiers):
        pass


def main():
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
