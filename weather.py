import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SNOW_MAX_SIZE = 6
SNOW_MIN_SIZE = 3


class SnowFlake:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vel_x = 0
        self.vel_y = 0

        self.size = random.randint(SNOW_MIN_SIZE, SNOW_MAX_SIZE)

        self.color = (220, 220, 220, 200)

        # Wiggle component of sideways movement
        self.wiggle = 0

        # Counter for how long to apply the same "random" direction to simulate
        self.wiggle_reset_limit = 0
        self.wiggle_count = 0

        self.reset_wiggle()

    def reset_wiggle(self):
        self.wiggle_count = 0
        self.wiggle = random.randint(-50, 50)
        self.wiggle_reset_limit = random.randint(50, 70)

    def update(self, delta_time, wind, speed):
        # Apply wind force and the random wiggle direction for sideways movement
        self.vel_x = wind + self.wiggle
        # Apply gravity for movement down
        self.vel_y = speed

        # Reset the wiggle movement to make it random after a set n umber of frames
        self.wiggle_count += 1
        if self.wiggle_count > self.wiggle_reset_limit:
            self.reset_wiggle()

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
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(SCREEN_HEIGHT - 10, SCREEN_HEIGHT + 5)

        self.size = random.randint(SNOW_MIN_SIZE, SNOW_MAX_SIZE)

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)


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
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT + 50)

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

        # True if rain, False if snow
        self.rain = False

        self.raindrops = []
        self.snowflakes = []

        if self.rain:
            self.add_raindrops(50)
        else:
            self.add_snowflakes(50)

    def add_snowflakes(self, number_of_flakes):
        for i in range(0, number_of_flakes):
            snowflake = SnowFlake(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            self.snowflakes.append(snowflake)

    def remove_snowflakes(self, number_of_flakes):
        # Only remove if we still have enough drops
        if number_of_flakes <= len(self.snowflakes):
            for i in range(0, number_of_flakes):
                self.snowflakes.pop()

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
        arcade.draw_text(f"Wind: {self.wind}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE)
        if self.rain:
            for raindrop in self.raindrops:
                raindrop.draw()
            arcade.draw_text(f"Raindrops: {len(self.raindrops)}", 10, SCREEN_HEIGHT - 15, arcade.color.WHITE)
        else:
            for snowflake in self.snowflakes:
                snowflake.draw()
            arcade.draw_text(f"Snowflakes: {len(self.snowflakes)}", 10, SCREEN_HEIGHT - 15, arcade.color.WHITE)

    def on_update(self, delta_time):
        if self.rain:
            for raindrop in self.raindrops:
                raindrop.update(delta_time, self.wind, self.speed)
        else:
            for snowflake in self.snowflakes:
                snowflake.update(delta_time, self.wind, self.speed)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.PLUS:
            if self.rain:
                self.add_raindrops(50)
            else:
                self.add_snowflakes(50)
        elif key == arcade.key.MINUS:
            if self.rain:
                self.remove_raindrops(50)
            else:
                self.remove_snowflakes(50)
        elif key == arcade.key.LEFT:
            self.wind -= 50
        elif key == arcade.key.RIGHT:
            self.wind += 50
        elif key == arcade.key.UP:
            if self.speed < -50:
                self.speed += 50
        elif key == arcade.key.DOWN:
            self.speed -= 50
        elif key == arcade.key.SPACE:
            self.change_weather()

    def change_weather(self):
        # Its raining, change to snow
        if self.rain:
            # Delete all raindrops
            self.raindrops = []
            # Add snowflakes
            self.add_snowflakes(50)

        # Its snowing, change to rain
        else:
            # Delete all snowflakes
            self.snowflakes = []
            # Add rain
            self.add_raindrops(50)

        # Toggle weather flag
        self.rain = not self.rain


def main():
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
