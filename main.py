import pyglet
from pyglet import shapes

window = pyglet.window.Window(800, 600, caption="maya")

batch = pyglet.graphics.Batch()

circle = shapes.Circle(400, 300, 20)

@window.event
def on_draw():
    window.clear()
    circle.draw()

def update(delta_time):
    print("frame", delta_time)

pyglet.clock.schedule(update)

pyglet.app.run()
