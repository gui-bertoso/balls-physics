import pyglet
from pyglet import shapes

class App:
    def __init__(self):
        self.update_delay = 0.1
        self.particles_amount = 100000

        self.particles = []

        self.instances_count = 0

        self.window = pyglet.window.Window(800, 600, caption="maya", vsync=False)
        self.fps_label = pyglet.window.FPSDisplay(self.window)

        self.particles_batch = pyglet.graphics.Batch()

        self.label = pyglet.text.Label(
            "MAYA",
            font_name="Arial",
            font_size=24,
            x=400, y=20,
            anchor_x="center", anchor_y="center"
        )

        self.spawn_particles()

        self.window.push_handlers(on_draw=self.on_draw)

        pyglet.clock.schedule_interval(self.update, self.update_delay)

    def on_draw(self):
        self.window.clear()
        self.label.draw()
        self.particles_batch.draw()

    def update(self, delta_time):
        self.print_log(delta_time)

    def print_log(self, delta_time):
        print(f"\r[deltaTime: {delta_time}] - [instancesCount: {self.get_instances_count()}] - [fps: {self.get_fps()}]", end="", flush=True)

    def get_instances_count(self):
        return len(self.particles)

    def get_fps(self):
        return self.fps_label.label.text

    def spawn_particles(self):
        for i in range(self.particles_amount):
            new_particle = shapes.Circle(400, 300, 20, batch=self.particles_batch)
            self.particles.append(new_particle)


if __name__ == "__main__":
    app = App()
    pyglet.app.run()