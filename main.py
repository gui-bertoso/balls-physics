import random

import pyglet
from pyglet import shapes

class App:
    def __init__(self):
        self.attraction_grid = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 0, 0, 0, 0, 0,
            0, 0, 0, 3, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 1, 2, 2, 1, 1, 0, 0, 0,
            0, 0, 0, 2, 2, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]

        self.update_delay = 0.1
        self.particles_amount = 20

        self.particles = []
        self.grid_points = []

        self.instances_count = 0
        self.particle_radius = 10

        self.grid_size = 10

        self.interference_radius = 50

        self.window_size_x = 800
        self.window_size_y = 600

        self.window = pyglet.window.Window(self.window_size_x, self.window_size_y, caption="maya", vsync=False)
        self.fps_label = pyglet.window.FPSDisplay(self.window)

        self.particles_batch = pyglet.graphics.Batch()
        self.grid_batch = pyglet.graphics.Batch()
        self.grid_points_batch = pyglet.graphics.Batch()

        self.spawn_particles()
        self.create_grid()

        self.window.push_handlers(on_draw=self.on_draw)

        pyglet.clock.schedule_interval(self.update, self.update_delay)

    def on_draw(self):
        self.window.clear()
        self.grid_batch.draw()
        self.grid_points_batch.draw()
        self.particles_batch.draw()

    def update(self, delta_time):
        self.print_log(delta_time)
        self.apply_interference_radius()
        self.apply_particles_repulsion()

    def apply_particles_repulsion(self):
        min_dist = 20
        min_dist_sq = min_dist * min_dist
        push_strength = 0.5

        for i in range(len(self.particles)):
            p1 = self.particles[i]

            for j in range(i + 1, len(self.particles)):
                p2 = self.particles[j]

                dx = p2.x - p1.x
                dy = p2.y - p1.y
                dist_sq = dx * dx + dy * dy

                if dist_sq == 0:
                    dx = 1
                    dy = 0
                    dist_sq = 1

                if dist_sq < min_dist_sq:
                    dist = dist_sq ** 0.5
                    nx = dx / dist
                    ny = dy / dist

                    overlap = min_dist - dist
                    push = overlap * push_strength * 0.5

                    p1.x -= nx * push
                    p1.y -= ny * push

                    p2.x += nx * push
                    p2.y += ny * push

    def apply_interference_radius(self):
        circles = []
        values = []
        for i in self.grid_points:
            circles.append(i[1])
            values.append(i[2])

        for i in range(len(self.grid_points)):
            circle = circles[i]
            cx, cy = circle.x, circle.y
            for particle in self.particles:
                px, py = particle.x, particle.y

                dx, dy = cx - px, cy - py

                dist_sq = dx * dx + dy * dy + 0.0001
                force = values[i] / dist_sq

                particle.x += dx * force * 100
                particle.y += dy * force * 100


    def print_log(self, delta_time):
        print(f"\r[deltaTime: {delta_time}] - [instancesCount: {self.get_instances_count()}] - [fps: {self.get_fps()}]", end="", flush=True)

    def get_instances_count(self):
        return len(self.particles) + len(self.grid_points)*2

    def get_fps(self):
        return self.fps_label.label.text

    def get_window_size(self):
        return self.window.size

    def spawn_particles(self):
        for i in range(self.particles_amount):
            new_particle = shapes.Circle(400, 300, self.particle_radius, batch=self.particles_batch)
            self.particles.append(new_particle)

    def create_grid(self):
        self.grid_points.clear()

        cell_width = self.window_size_x / self.grid_size
        cell_height = self.window_size_y / self.grid_size

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                pos_x = x * cell_width + cell_width / 2
                pos_y = (self.grid_size - 1 - y) * cell_height + cell_height / 2

                index = y * self.grid_size + x
                value = self.attraction_grid[index]

                new_point = shapes.Circle(
                    x=pos_x, y=pos_y,
                    radius=self.interference_radius*value,
                    batch=self.grid_points_batch,
                    color=(255, 255, 255, 50)
                )
                new_label = pyglet.text.Label(
                    str(value),
                    x=pos_x, y=pos_y,
                    anchor_x="center", anchor_y="center",
                    batch=self.grid_batch,
                    color=self.get_color_per_force(value)
                )
                self.grid_points.append((new_label, new_point, value))

    @staticmethod
    def get_color_per_force(force):
        match force:
            case 1:
                return 0, 255, 0
            case 2:
                return 255, 255, 0
            case 3:
                return 255, 0, 0
            case _:
                return 255, 255, 255



if __name__ == "__main__":
    app = App()
    pyglet.app.run()