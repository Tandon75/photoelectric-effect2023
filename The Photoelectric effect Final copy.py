import pygame
import math

# Initialize pygame
pygame.init()

# Variables
intensity = 100 # must be a value 20,40,60,80,100
number_of_photon = 0  # define number_of_photon with a value
number_of_electrons = number_of_photon
plank_constant = 6.63 * 10**-34
work_function_sodium = 3.648 * 10**-19
mass_electron = 9.11 * 10**-31
frequency = 1.5 * 10**15 

# equations for velocity_____________________________________________________________________________________________

total_energy = plank_constant * frequency  # Update the total energy value
kinetic_energy = total_energy - work_function_sodium  # Update the kinetic energy value
velocity = math.sqrt((2 * kinetic_energy) / mass_electron)  # Update the velocity value


# Check the condition for intensity_________________________________________________________________________________
if intensity == 20:
    number_of_photon = 10
elif intensity == 40:
    number_of_photon = 15
elif intensity == 60:
    number_of_photon = 25
elif intensity == 80:
    number_of_photon = 35
elif intensity == 100:
    number_of_photon = 45
else:
    number_of_photon = intensity

# Set up display____________________________________________________________________________________________________
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Photoelectric Effect")

# Distance between two plates
plate_distance = 250

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
silver = (192, 192, 192)
indigo = (102, 118, 255)
lavender = (164, 102, 255)
LIGHT_COLOR = (255, 255, 0)
BALL_COLOR = (255, 0, 0)

# Making the plates + wire lengths
plate_width = 10
plate_height = 150
wire_width = 3
side_wire_length = 80
vertical_wire_length = 160
long_wire_length = 683

# Plate locations
left_plate_x = width // 2 - plate_width - plate_distance
right_plate_x = width // 2 + plate_distance
plate_y = height // 2 - plate_height // 4

# Side wire locations
left_side_wire_x = left_plate_x - side_wire_length
right_side_wire_x = right_plate_x + plate_width
side_wire_y = plate_y + plate_height // 2

# Vertical wire locations
left_vertical_wire_x = left_side_wire_x
right_vertical_wire_x = right_side_wire_x + side_wire_length
vertical_wire_y = side_wire_y

# Long wire locations
long_wire_x = left_vertical_wire_x
long_wire_y = vertical_wire_y + vertical_wire_length


# Line color
line_color = (0, 0, 0)  # Black color for the line





# Electron movement_________________________________________________________________________________________________

# Ball properties
ball_radius = 10
ball_color = (255, 0, 0)  # red color for the ball
ball_x = left_plate_x + plate_width // 2  # center of the left plate
ball_y = plate_y + plate_height // 2  # center of the left plate
speed = velocity / 10000000  # adjust the speed of the ball

# Ball1 properties
ball1_radius = 10
ball1_color = (192, 192, 192)  # silver color for the ball
ball1_x = left_plate_x + plate_width // 2  # center of the left plate
ball1_y = plate_y + plate_height // 7  # center of the left plate
speed = velocity / 10000000  # adjust the speed of the ball


# Ball 2 properties
ball2_radius = 10
ball2_color = (0, 0, 255)  # blue color for the ball
ball2_x = left_plate_x + plate_width // 2  # center of the left plate
ball2_y = plate_y + plate_height // 3.1  # center of the left plate
speed = velocity / 10000000  # adjust the speed of the ball


# Ball 3 properties
ball3_radius = 10
ball3_color = (0, 255, 0)  # green color for the ball
ball3_x = left_plate_x + plate_width // 2  # center of the left plate
ball3_y = plate_y + plate_height // 1.1 # center of the left plate
speed = velocity / 10000000  # adjust the speed of the ball


# Ball 4 properties
ball4_radius = 10
ball4_color = (255, 0, 255)  # magenta color for the ball
ball4_x = left_plate_x + plate_width // 2  # center of the left plate
ball4_y = plate_y + plate_height // 1.4  # center of the left plate
speed = velocity / 10000000  # adjust the speed of the ball





# Light properties and Light incident ray_________________________________________________________________________

LIGHT_ANGLE = 210  # in degrees
LIGHT_LENGTH = 577
light_start_x = right_plate_x
light_start_y = plate_y - plate_height // 0.58
light_end_x = light_start_x + LIGHT_LENGTH * math.cos(math.radians(LIGHT_ANGLE))
light_end_y = light_start_y - LIGHT_LENGTH * math.sin(math.radians(LIGHT_ANGLE))

# Main loop for frequency input_____________________________________________________________________________________
running = True
input_text = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Frequency entered:", input_text)
                frequency = float(input_text)  # Update the frequency value
                total_energy = plank_constant * frequency  # Update the total energy value
                kinetic_energy = total_energy - work_function_sodium  # Update the kinetic energy value
                velocity = math.sqrt((2 * kinetic_energy) / mass_electron)  # Update the velocity value
                speed = velocity / 10000000  # Update the speed value
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode




    if ball_x < right_plate_x:
        ball_x += speed
    else:
        ball_x = left_plate_x  # reset the ball's position to the left plate


    if ball1_x < right_plate_x:
        ball1_x += speed
    else:
        ball1_x = left_plate_x  # reset the ball's position to the left plate


    if ball2_x < right_plate_x:
        ball2_x += speed
    else:
        ball2_x = left_plate_x  # reset the ball's position to the left plate


    if ball3_x < right_plate_x:
        ball3_x += speed
    else:
        ball3_x = left_plate_x  # reset the ball's position to the left plate


    if ball4_x < right_plate_x:
        ball4_x += speed
    else:
        ball4_x = left_plate_x  # reset the ball's position to the left plate


# drawing_____________________________________________________________________________________________________________

    # Make background of screen white
    screen.fill(white)
    # Draw cathode
    pygame.draw.rect(screen, indigo, (left_plate_x, plate_y, plate_width, plate_height))
    # Draw anode
    pygame.draw.rect(screen, lavender, (right_plate_x, plate_y, plate_width, plate_height))
    # Side wires
    pygame.draw.rect(screen, silver, (left_side_wire_x, side_wire_y, side_wire_length, wire_width))
    pygame.draw.rect(screen, silver, (right_side_wire_x, side_wire_y, side_wire_length, wire_width))
    # Vertical wires
    pygame.draw.rect(screen, silver, (left_vertical_wire_x, vertical_wire_y, wire_width, vertical_wire_length))
    pygame.draw.rect(screen, silver, (right_vertical_wire_x, vertical_wire_y, wire_width, vertical_wire_length))
    # Long wire
    pygame.draw.rect(screen, silver, (long_wire_x, long_wire_y, long_wire_length, wire_width))

    # Draw light ray
    pygame.draw.line(screen, LIGHT_COLOR, (light_start_x, light_start_y), (light_end_x, light_end_y), 2)

    # Draw ball at the left plate
    pygame.draw.circle(screen, ball_color, (int(ball_x), ball_y), ball_radius)





        # Draw ball 1 at the left plate

    if number_of_photon>=11:
        pygame.draw.circle(screen, ball1_color, (int(ball1_x), ball1_y), ball1_radius)


         # Draw ball 2 at the left plate

    if number_of_photon>=21:
        pygame.draw.circle(screen, ball2_color, (int(ball2_x), ball2_y), ball2_radius)


         # Draw ball 3 at the left plate

    if number_of_photon>=31:
        pygame.draw.circle(screen, ball3_color, (int(ball3_x), ball3_y), ball3_radius)


         # Draw ball 4 at the left plate

    if number_of_photon>=41:
        pygame.draw.circle(screen, ball4_color, (int(ball4_x), ball4_y), ball4_radius)



    # Render the kinetic energy text
    font = pygame.font.Font(None, 36)
    text = font.render(f"Kinetic Energy: {kinetic_energy:.2e} J", True, black)
    screen.blit(text, (10, 10)) 

    # Display the frequency input function 
    input_prompt_text = font.render("Enter Frequency (threshold is 10e14): " + input_text, True, (0, 0, 0))
    screen.blit(input_prompt_text, (10, 50))

    pygame.display.flip()



