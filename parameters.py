#User Parameters
FPS = 60.0
speed = 100.0 #pixels/second
gravity = 1000.0 #pixels/(second^2)
jump_vel = 300.0 #velocity imparted to the player given a jump command
v_0 = 300.0 #initial velocity
x_0 = 300.0 #initial position
initial_spawn_chance = .1 #a higher number increases the odds of an obstacle spawning
spawn_chance_increment = 60 #the number of frames between increasing the spawn chance

#Generated Parameters
period = 1000/FPS #The time each frame will be displayed in milliseconds

#GUI Parameters
    #Colors
background_color = (0,0,0)
player_color = (255,100,100)
obstacle_color = (200,200,200)
deathscene_color = (200,100,100)
deathfont_color = (0,0,0)
gamescene_color = (0,0,0)
gamefont_color = (255,255,255)
titlescene_color = (50,50,50)
titlefont_color = (255,255,255)

player_offset = 30
player_width = 30
obstacle_width = 20
width = 640

player_height = 30
obstacle_height = 20
height = 480