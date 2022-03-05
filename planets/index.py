import pygame
import math
pygame.init()
WIDTH, HEIGHT = 1300, 750
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KSP wannabe")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (65, 105, 225)
RED = (188, 39, 50)
GREY = (80, 78, 80)
font = pygame.font.SysFont("comicsans", 15)


class Planet:
    G = 6.674*10**-11
    au = 149.6e6 * 1000   # au km to meters
    grav = 6.67428e-11
    scale = 100/au  # 1 au is 100 px
    time_scale = 3600*100  # 2  min

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.sun = False
        self.dist_sun = 0
        self.orbit = []
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x*self.scale+WIDTH/2
        y = self.y*self.scale+HEIGHT/2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x*self.scale+WIDTH/2  # x coords to scale
                y = y*self.scale+HEIGHT/2  # y coords to scale
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)
        if not self.sun:
            dist_text = font.render(
                f"{round(self.dist_sun/1000,1)}km", 1, WHITE)
            win.blit(dist_text, (x-dist_text.get_width() /
                     2, y-dist_text.get_width()/2))

    def attraction(self, other):
        # F=G*(Mm)/(r**2) const val 6.674×10−11
        #   g=(G*M)/(r**2)  kappa ={\frac {8\pi G}{c^{2}}}\approx 1.866\times 10^{-26}\mathrm {\,m{\cdot }kg^{-1}} ein-tens
        # 6.674×10−11 * 1.98892*10**30 * 5.9742*10**24 / -1*Planet.au**2
        other_x, other_y = other.x, other.y
        dist_x = other_x-self.x
        dist_y = other_y-self.y
        dist = math.sqrt(dist_x**2 + dist_y**2)

        if other.sun:
            self.dist_sun = dist

        force = self.G * self.mass * other.mass / dist ** 2
        theta = math.atan2(dist_y, dist_x)
        x_force = math.cos(theta) * force
        y_force = math.sin(theta) * force
        return x_force, y_force

    def updater(self, planets):
        tot_fx = tot_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            tot_fx += fx
            tot_fy += fy

        self.x_vel += tot_fx / self.mass * self.time_scale
        self.y_vel += tot_fy / self.mass * self.time_scale

        self.x += self.x_vel*self.time_scale
        self.y += self.y_vel*self.time_scale
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892*10**30)  # kg
    sun.sun = True
    # distsun x,y color, mass
    earth = Planet(-1*Planet.au, 0, 16, BLUE, 5.9742*10**24)
    earth.y_vel = 29.783*1000
    mars = Planet(-1.5424*Planet.au, 0, 12, RED, 6.39*10**23)
    mars.y_vel = 24.077*1000
    mercury = Planet(0.387*Planet.au, 0, 8, GREY, 0.30*10**24)
    mercury.y_vel = -47.4*1000

    venus = Planet(0.700*Planet.au, 0, 14, WHITE, 4.8685*10**24)
    venus.y_vel = -35.02 * 1000
    saturn=Planet(-2.723*Planet.au,0,18,BLUE,8.8685*10**24 )
    saturn.y_vel=30.345*1000
    jupiter=Planet(-3.723*Planet.au,0,22,WHITE,10.8685*10**24 )
    jupiter.y_vel=32.55*1000

    planets = [sun, earth, mars, mercury, venus,
    # jupiter ,
    # saturn
    ]

    while run:
        clock.tick(60)
        win.fill((0, 0, 0))
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.updater(planets)
            planet.draw(win)
        pygame.display.update()

    pygame.quit()


main()
