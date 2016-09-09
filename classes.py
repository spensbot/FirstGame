from parameters import *
from functions import *
import pygame
import random


class SceneBase:
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)


class GameScene(SceneBase):

    frame = 0
    obstacles = [[width, 200]]  # x_position , y_position
    state = [x_0, v_0]  # position , velocity
    spawn_chance = initial_spawn_chance
    score = 0
    max_score = 0

    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state[1] = jump_vel

    def Update(self):
        self.state[0] += self.state[1]/FPS
        self.state[1] -= gravity/FPS
        if self.state[0] < 0:
            self.state[0] = 0
            self.state[1] = 0
        elif self.state[0] > height-player_height:
            self.state[0] = height-player_height
            self.state[1] = 0

        if random.random() < self.spawn_chance:
            self.obstacles.append([300, random.randint(0, height-obstacle_height)])
        for i in range(len(self.obstacles)):
            self.obstacles[i][0] -= speed/FPS

        for i in range(len(self.obstacles)):
            if player_offset - obstacle_width < self.obstacles[i][0] < player_offset + player_width:
                if self.state[0] < height - self.obstacles[i][1] < self.state[0] + player_height + obstacle_height:
                    self.SwitchToScene(DeathScene())

        self.score += 1

    def Render(self, screen):
        font = pygame.font.SysFont("Courier", 40)
        screen.fill(gamescene_color)
        draw_player(screen, self.state[0])
        draw_obstacles(screen, self.obstacles)
        draw_text(screen, font, ["Score: " + repr(self.score)], gamefont_color)

class TitleScene(SceneBase):

    text = ["Blocky Block!", "Play: [space]"]

    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.SwitchToScene(GameScene())

    def Update(self):
        pass

    def Render(self, screen):
        font = pygame.font.SysFont("Courier", 40)
        screen.fill(titlescene_color)
        draw_text(screen, font, self.text, titlefont_color)


class DeathScene(SceneBase):

    text = ["You Loose :D", "looser", "High Score: " + repr(GameScene.max_score), "Replay: [space]"]

    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.SwitchToScene(GameScene())

    def Update(self):
        GameScene.obstacles = [[width, 200]]  # x_position , y_position
        GameScene.state = [x_0, v_0]  # position , velocity
        GameScene.spawn_chance = initial_spawn_chance
        if GameScene.score > GameScene.max_score:
            GameScene.max_score = GameScene.score
        GameScene.score = 0


    def Render(self, screen):
        font = pygame.font.SysFont("Courier", 40)
        screen.fill(deathscene_color)
        draw_text(screen, font, self.text, titlefont_color)


