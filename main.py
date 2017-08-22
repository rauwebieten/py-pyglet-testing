import pyglet

game_width = 800
game_height = 600

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

square = pyglet.resource.image("square.png")
game_window = pyglet.window.Window(
    width=game_width,
    height=game_height
)

fps_display = pyglet.clock.ClockDisplay(
    format='%(fps).1f',
    color=(0.5, 0.5, 0.5, 1)
)
sprite = pyglet.sprite.Sprite(square, x=100, y=100)

dx = 200
dy = 250


@game_window.event
def on_draw():
    game_window.clear()
    sprite.draw()
    fps_display.draw()


def update(dt):
    global dx, dy
    sprite.x += (dx * dt)
    sprite.y += (dy * dt)
    if sprite.x > game_width - 10:
        sprite.x = game_width - 10
        dx *= -1
    if sprite.x < 0:
        sprite.x = 0
        dx *= -1
    if sprite.y > game_height - 10:
        sprite.y = game_height - 10
        dy *= -1
    if sprite.y < 0:
        sprite.y = 0
        dy *= -1


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
