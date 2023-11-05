import pygame
import math

# Initialize pygame
pygame.init()

# Variables
number_of_photon = 1*10**14
number_of_electrons = number_of_photon
plank_constant = 6.63*10**-34
frequency = 1.5 * 10**15
work_function_sodium = 3.648*10**-19
mass_electron= 9.11 * 10**-31

#velocity_________________________________________________________________________________________________________


# Equation for the velocity of the particle

total_energy = plank_constant*frequency
kinetic_energy = total_energy - work_function_sodium
velocity = math.sqrt((2*kinetic_energy)/mass_electron)


#set up display_____________________________________________________________________________________________________

width, height = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Photoelectric Effect")

#distance between two plates
plate_distance = 250

# colors
white = (255,255,255)
black = (0,0,0)
silver = (192,192,192)
indigo = (102,118,255)
lavender = (164,102,255)
LIGHT_COLOR = (255, 255, 0)
BALL_COLOR = (255, 0, 0)


# making the plates + wire lengths
plate_width = 10
plate_height = 150
wire_width = 3
side_wire_length = 80
vertical_wire_length = 160
long_wire_length = 683

#plate locations ()
left_plate_x = width//2 - plate_width - plate_distance
right_plate_x = width//2 + plate_distance
plate_y = height//2 - plate_height//4

# side wire locations
left_side_wire_x = left_plate_x - side_wire_length
right_side_wire_x = right_plate_x + plate_width
side_wire_y = plate_y +  plate_height//2

# vertical wire locations
left_vertical_wire_x = left_side_wire_x
right_vertical_wire_x = right_side_wire_x + side_wire_length
vertical_wire_y = side_wire_y

#long wire locations
long_wire_x = left_vertical_wire_x
long_wire_y = vertical_wire_y + vertical_wire_length

#run the visuals
running = True





# electron movement_________________________________________________________________________________________________


# ball properties
ball_radius = 10
ball_color = (255, 0, 0)  # red color for the ball
ball_x = left_plate_x + plate_width // 2  # center of the left plate
ball_y = plate_y + plate_height // 2  # center of the left plate
speed = velocity/10000000 # adjust the speed of the ball



# Light properties and Light incident ray___________________________________________________________________
LIGHT_ANGLE = 210  # in degrees
LIGHT_LENGTH = 577


light_start_x = right_plate_x
light_start_y = plate_y - plate_height //0.58
light_end_x = light_start_x + LIGHT_LENGTH * math.cos(math.radians(LIGHT_ANGLE))
light_end_y = light_start_y - LIGHT_LENGTH * math.sin(math.radians(LIGHT_ANGLE))


# run the visuals
running = True
move_ball = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if move_ball:
        if ball_x < right_plate_x:
            ball_x += speed
        else:
            ball_x = left_plate_x  # reset the ball's position to the left plate
            move_ball = True  # set move_ball to True to keep the animation continuous

    # make background of screen white
    screen.fill(white)
    # draw cathode
    pygame.draw.rect(screen, indigo, (left_plate_x, plate_y, plate_width, plate_height))
    # draw anode
    pygame.draw.rect(screen, lavender, (right_plate_x, plate_y, plate_width, plate_height))
    # side wires
    pygame.draw.rect(screen, silver, (left_side_wire_x, side_wire_y, side_wire_length, wire_width))
    pygame.draw.rect(screen, silver, (right_side_wire_x, side_wire_y, side_wire_length, wire_width))
    # vertical wires
    pygame.draw.rect(screen, silver, (left_vertical_wire_x, vertical_wire_y, wire_width, vertical_wire_length))
    pygame.draw.rect(screen, silver, (right_vertical_wire_x, vertical_wire_y, wire_width, vertical_wire_length))
    # long wire
    pygame.draw.rect(screen, silver, (long_wire_x, long_wire_y, long_wire_length, wire_width))


    
    # draw light ray
    pygame.draw.line(screen, LIGHT_COLOR, (light_start_x, light_start_y), (light_end_x, light_end_y), 2)

    # draw ball at the left plate
    pygame.draw.circle(screen, ball_color, (int(ball_x), ball_y), ball_radius)

    # Update display
    pygame.display.flip()



    #frequency variable_________________________________________________________________________________________________


#kinetic energy display

    # Render the kinetic energy text
    font = pygame.font.Font(None, 36)
    text = font.render(f"Kinetic Energy: {kinetic_energy:.2e} J", True, black)
    screen.blit(text, (10, 10))

x = float(input("string:"))

#python docs and geeks for geeks 