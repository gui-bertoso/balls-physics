import pyglet
from pyglet import shapes

update_delay = 0.1
particles_amount = 10

instances_count = 0

window = pyglet.window.Window(800, 600, caption="maya")

particles_batch = pyglet.graphics.Batch()



label = pyglet.text.Label(
    "MAYA",
    font_name="Arial",
    font_size=24,
    x=400, y=20,
    anchor_x="center", anchor_y="center"
)

@window.event
def on_draw():
    window.clear()
    label.draw()
    particles_batch.draw()

def update(delta_time):
    print_log(delta_time)

def start(delta_time):
    spawn_particles()

def print_log(delta_time):
    print(f"\r[deltaTime: {delta_time}] - [instancesCount: {instances_count}]", end="", flush=True)

def spawn_particles():
    for i in range(particles_amount):
        new_particle = shapes.Circle(400, 300, 20, batch=particles_batch)

pyglet.clock.schedule(update)
pyglet.clock.schedule_once(start, 0)

pyglet.app.run()
