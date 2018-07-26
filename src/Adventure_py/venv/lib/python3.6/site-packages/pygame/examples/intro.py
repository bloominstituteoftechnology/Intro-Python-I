intro.py


import random, math, pygame
from pygame.locals import *

#constants
WINSIZE = [640, 480]
# WINSIZE = [2448/2, 2448/2]
WINSIZE = [1920, 1080]
WINSIZE = [2048, 1280]

WINCENTER = [320, 240]
NUMSTARS = 150



def load_letters():
    letter_path = os.path.join('design', 'letters')
    fnames = glob.glob(os.path.join(letter_path, '*.png'))
    print(fnames)

    # images = [pg.image.load(f) for f in fnames]


    # In [1]: scaled = [pg.transform.smoothscale(s, (2448, 2448)) if s
    #    ...:    ...: .get_size() != (2448, 2448) else s for s in images]




def init_star():
    "creates new star values"
    dir = random.randrange(100000)
    velmult = random.random()*.6+.4
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    return vel, WINCENTER[:]


def initialize_stars():
    "creates a new starfield"
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        vel, pos = star
        steps = random.randint(0, WINCENTER[0])
        pos[0] = pos[0] + (vel[0] * steps)
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * .09)
        vel[1] = vel[1] * (steps * .09)
        stars.append(star)
    move_stars(stars)
    return stars


def draw_stars(surface, stars, color):
    "used to draw (and clear) the stars"
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)


def move_stars(stars):
    "animate the star values"
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            vel[:], pos[:] = init_star()
        else:
            vel[0] = vel[0] * 1.05
            vel[1] = vel[1] * 1.05


def main():
    "This is the starfield code"
    #create our starfield
    random.seed()
    stars = initialize_stars()
    clock = pygame.time.Clock()
    #initialize and prepare screen
    pygame.init()
    # screen = pygame.display.set_mode(WINSIZE, FULLSCREEN)
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('pygame Stars Example')
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)

    #main game loop
    done = 0
    while not done:
        draw_stars(screen, stars, black)
        move_stars(stars)
        draw_stars(screen, stars, white)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1
                break
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                WINCENTER[:] = list(e.pos)
        clock.tick(30)


# if python says run, then we should run
if __name__ == '__main__':

    load_letters()
    main()








