import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class RainDrop:

    def __init__(self, x, y):
        # Object position
        self.x = x
        self.y = y

        self.prev_x = x
        self.prev_y = y

        # Object velocity (speed)
        self.vel_x = 0
        self.vel_y = 0

        # Drop size
        self.size = random.randint(1, 2)

        # Color
        self.drop_color = (120, 120, 140, 230)
        self.trail_color = (100, 100, 120, 100)

    def update(self, delta_time, wind, speed):
        self.vel_x = wind
        self.vel_y = speed

        # Store previous position
        self.prev_x = self.x
        self.prev_y = self.y

        # Calculate new position based on velocity
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time

        # If reached bottom, reset position
        if self.y < 0:
            self.reset()

        # If drifted out of the screen because of wind, reset position
        if self.x > SCREEN_WIDTH or self.x < 0:
            self.reset()

    # Move to top of screen at random x position
    def reset(self):
        self.y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT + 50)
        self.x = random.randint(0, SCREEN_WIDTH)

        # If new position, also reset the previous position
        self.prev_x = self.x
        self.prev_y = self.y

        self.size = random.randint(1, 2)

    def draw(self):
        arcade.draw_line(self.x, self.y, self.prev_x, self.prev_y, self.trail_color)
        arcade.draw_point(self.x, self.y, self.drop_color, self.size)


class MyWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        background_color = (30, 30, 60)
        arcade.set_background_color(background_color)

        self.wind = 0
        self.speed = -100  # Speed towards ground

        self.raindrops = []

        self.add_raindrops(50)

    def add_raindrops(self, number_of_drops):
        for i in range(0, number_of_drops):
            raindrop = RainDrop(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            self.raindrops.append(raindrop)

    def remove_raindrops(self, number_of_drops):
        # Only remove if we still have enough drops
        if number_of_drops <= len(self.raindrops):
            for i in range(0, number_of_drops):
                self.raindrops.pop()

    def on_draw(self):
        arcade.start_render()
        for raindrop in self.raindrops:
            raindrop.draw()
        arcade.draw_text(f"Number of raindrops: {len(self.raindrops)}", 10, SCREEN_HEIGHT - 15, arcade.color.WHITE)
        arcade.draw_text(f"Wind: {self.wind}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE)

    def on_update(self, delta_time):
        for raindrop in self.raindrops:
            raindrop.update(delta_time, self.wind, self.speed)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.PLUS:
            self.add_raindrops(50)
        elif key == arcade.key.MINUS:
            self.remove_raindrops(50)
        elif key == arcade.key.LEFT:
            self.wind -= 50
        elif key == arcade.key.RIGHT:
            self.wind += 50
        elif key == arcade.key.UP:
            if self.speed < -50:
                self.speed += 50
        elif key == arcade.key.DOWN:
            self.speed -= 50


def main():
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
