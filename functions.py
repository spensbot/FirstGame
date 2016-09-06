from parameters import *

def draw_window(surface):
    surface.fill(background_color)

def draw_obstacles(surface, obstacles):

    from_top = height-obstacle_height

    for i in range(len(obstacles)):
        from_left = obstacles[i]
        surface.fill(obstacle_color, (from_left,from_top,obstacle_width,obstacle_height))


def draw_player(surface, pos):

    from_top = height - player_height - pos
    from_left = 30
    surface.fill(player_color, (from_left, from_top, player_width, player_height))
