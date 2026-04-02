import random
import pyglet
from pyglet import shapes


class App:
    def __init__(self):
        self.grid_width = 30
        self.grid_height = 30

        self.attraction_grid = [
            # 0–5 (vazio)
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

            # olhos
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

            # vazio
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

            # boca
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

            # resto vazio até fechar 30 linhas
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]

        self.particles_amount = 60
        self.particles = []
        self.grid_points = []
        self.active_points = []

        self.particle_radius = 4
        self.grid_size = 30
        self.interference_radius = 8

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
        pyglet.clock.schedule(self.update)

    def on_draw(self):
        self.window.clear()
        self.grid_batch.draw()
        self.grid_points_batch.draw()
        self.particles_batch.draw()

    def update(self, dt):
        self.apply_interference_radius(dt)
        self.apply_particles_repulsion()
        self.apply_particles_physics(dt)

    def apply_particles_physics(self, dt):
        for particle in self.particles:
            particle.vx *= 0.82
            particle.vy *= 0.82

            particle.x += particle.vx * min(dt * 60.0, 2.0)
            particle.y += particle.vy * min(dt * 60.0, 2.0)

    def apply_particles_repulsion(self):
        min_dist = self.particle_radius * 2.2
        min_dist_sq = min_dist * min_dist
        push_strength = 0.25

        for i in range(len(self.particles)):
            p1 = self.particles[i]
            for j in range(i + 1, len(self.particles)):
                p2 = self.particles[j]

                dx = p2.x - p1.x
                dy = p2.y - p1.y
                dist_sq = dx * dx + dy * dy

                if dist_sq == 0:
                    dx = random.uniform(-1.0, 1.0)
                    dy = random.uniform(-1.0, 1.0)
                    dist_sq = dx * dx + dy * dy + 0.0001

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

    def apply_interference_radius(self, dt):
        # local attraction only: cells affect nearby particles
        for _, circle, value in self.active_points:
            cx, cy = circle.x, circle.y
            radius = circle.radius
            radius_sq = radius * radius

            for particle in self.particles:
                dx = cx - particle.x
                dy = cy - particle.y
                dist_sq = dx * dx + dy * dy

                if 0 < dist_sq <= radius_sq:
                    dist = dist_sq ** 0.5
                    falloff = 1.0 - (dist / radius)
                    force = falloff * value * 0.18

                    particle.vx += dx * force * dt * 60.0
                    particle.vy += dy * force * dt * 60.0

    def spawn_particles(self):
        for _ in range(self.particles_amount):
            x = 400 + random.uniform(-120, 120)
            y = 300 + random.uniform(-120, 120)
            particle = shapes.Circle(x, y, self.particle_radius, color=(255, 255, 255), batch=self.particles_batch)
            particle.vx = 0.0
            particle.vy = 0.0
            self.particles.append(particle)

    def create_grid(self):
        self.grid_points.clear()
        self.active_points.clear()

        cell_width = self.window_size_x / self.grid_size
        cell_height = self.window_size_y / self.grid_size

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                pos_x = x * cell_width + cell_width / 2
                pos_y = (self.grid_size - 1 - y) * cell_height + cell_height / 2

                index = y * self.grid_size + x
                value = self.attraction_grid[index]

                circle = shapes.Circle(
                    x=pos_x,
                    y=pos_y,
                    radius=max(1, self.interference_radius * value),
                    color=(255, 255, 255),
                    batch=self.grid_points_batch,
                )
                circle.opacity = 28 if value > 0 else 0

                label = pyglet.text.Label(
                    str(value),
                    x=pos_x,
                    y=pos_y,
                    anchor_x="center",
                    anchor_y="center",
                    batch=self.grid_batch,
                    color=self.get_color_per_force(value),
                )

                item = (label, circle, value)
                self.grid_points.append(item)
                if value > 0:
                    self.active_points.append(item)

    @staticmethod
    def get_color_per_force(force):
        match force:
            case 1:
                return 0, 255, 0, 255
            case 2:
                return 255, 255, 0, 255
            case 3:
                return 255, 80, 80, 255
            case _:
                return 255, 255, 255, 100


if __name__ == "__main__":
    app = App()
    pyglet.app.run()
