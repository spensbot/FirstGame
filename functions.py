from parameters import *

def draw_obstacles(surface, obstacles):

    for i in range(len(obstacles)):
        from_left = obstacles[i][0]
        from_top = obstacles[i][1]
        surface.fill(obstacle_color, (from_left,from_top,obstacle_width,obstacle_height))

def draw_player(surface, pos):

    y_pos = height - player_height - pos
    x_pos = player_offset
    surface.fill(player_color, (x_pos, y_pos, player_width, player_height))

def draw_text(surface, font, list, color):
    for i in range(len(list)):
        text = font.render(list[i], 1, color)
        wth = text.get_width()
        hth = text.get_height()
        surface.blit(text, (width / 2 - wth / 2, 100 + hth*i))

