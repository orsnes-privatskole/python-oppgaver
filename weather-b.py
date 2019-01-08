import arcade

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

        # If reached bottom, move back to top
        if self.y < 0:
            self.y = SCREEN_HEIGHT        

    def draw(self):
        arcade.draw_point(self.x, self.y, arcade.color.LIGHT_GRAY, 2)


class MyWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        background_color = (50, 50, 60)
        arcade.set_background_color(background_color)

        self.raindrop = RainDrop(SCREEN_WIDTH // 2, SCREEN_HEIGHT)

    def on_draw(self):
        arcade.start_render()
        self.raindrop.draw()

    def on_update(self, delta_time):
        self.raindrop.update(delta_time)

    def on_key_press(self, key, key_modifiers):
        pass


def main():
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()