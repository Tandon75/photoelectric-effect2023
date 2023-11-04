import pygame
import math

#Initialize pygame

pygame.init()

#set up display

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

# making the plates + wire lengths
plate_width = 10
plate_height = 150
wire_width = 3
side_wire_length = 80
vertical_wire_length = 160
long_wire_length = 683

#plate locations
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

while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # make background of screen white
    screen.fill(white)
    # draw cathode
    pygame.draw.rect(screen, indigo, (left_plate_x, plate_y, plate_width, plate_height))
    #draw anode
    pygame.draw.rect(screen, lavender, (right_plate_x, plate_y, plate_width, plate_height))
    # side wires
    pygame.draw.rect(screen, silver, (left_side_wire_x, side_wire_y, side_wire_length, wire_width))
    pygame.draw.rect(screen, silver, (right_side_wire_x, side_wire_y, side_wire_length, wire_width))
    # vertical wires
    pygame.draw.rect(screen, silver, (left_vertical_wire_x, vertical_wire_y, wire_width, vertical_wire_length))
    pygame.draw.rect(screen, silver, (right_vertical_wire_x, vertical_wire_y, wire_width, vertical_wire_length))
    # long wire
    pygame.draw.rect(screen, silver, (long_wire_x, long_wire_y, long_wire_length, wire_width))
    #Update display
    pygame.display.flip()

#quit pygame
pygame.quit()