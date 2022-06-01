# Marching Band Drill Simulator


import matplotlib.pyplot as plt
import os.path


''' Load Football Field Image with Matplotlib '''
# Get the directory and build filename
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'footballField.png')
img = plt.imread(filename)

# Put image on figure
fig, ax = plt.subplots(1, 1)
ax.imshow(img, interpolation='none')

# Turn off axes and add title
plt.axis('off')
plt.title('(front)')


''' Get drill information from user input '''
# Get user's number of sets
number_of_sets = int(raw_input('How many sets are in your drill? '))

# Initialize flag variable and coordinate lists
flag = 0
x_list = []
y_list = []

# Loop until number of sets is reached
while flag != number_of_sets:

    # Right to left
    print(" ")
    print(" ")
    print "SET", flag
    print("RIGHT - LEFT")

    side_of_field = raw_input('Side of field (L or R): ')
    side_of_field = side_of_field.capitalize()

    steps_rl = float(raw_input('Number of steps (0 = on yard line): '))

    inside_outside = raw_input('Inisde or outside yard line (I or O): ')
    inside_outside = inside_outside.capitalize()

    ydln = int(raw_input('Yard line: '))


    # Back to front
    print(" ")
    print("BACK - FRONT")

    steps_bf = float(raw_input('Number of steps (0 = on): '))

    behind_infrnt = raw_input('Behind or in front of (B or F): ')
    behind_infrnt = behind_infrnt.capitalize()

    sl_hash = raw_input('FRONT side line (a), FRONT hash (b) , BACK hash (c),\
    BACK side line (d): ')
    sl_hash = sl_hash.lower()



    ''' Make Coordinates'''
    # Find X-coordinate
    pixels_rl = 8.53 * steps_rl # 8.53 pixels = 1 step on the field

    ydlns_left = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    ydlns_right = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]

    index_of_ydln = 0
    x = 0

    if side_of_field == 'L':
        index_of_ydln = ydlns_left.index(ydln)
        x = (78.8 * (index_of_ydln)) + 163.5

    if side_of_field == 'R':
        index_of_ydln = ydlns_right.index(ydln)
        x = (78.8 * (index_of_ydln)) + 951.5


    if inside_outside == 'O' and side_of_field == 'L':
        x = x - pixels_rl

    if inside_outside == 'I' and side_of_field == 'R':
        x = x - pixels_rl

    if inside_outside == 'I' and side_of_field == 'L':
        x = x + pixels_rl

    if inside_outside == 'O' and side_of_field == 'R':
        x = x + pixels_rl


    # Find Y-coordinate
    pixels_bf = 10.32 * steps_bf

    y = 0

    if sl_hash == 'a':
        y = pixels_bf

    if sl_hash == 'b':
        if behind_infrnt == 'F':
            y = 317.5 - pixels_bf
        if behind_infrnt == 'B':
            y = 317.5 + pixels_bf

    if sl_hash == 'c':
        if behind_infrnt == 'F':
            y = 562 - pixels_bf
        if behind_infrnt == 'B':
            y = 562 + pixels_bf

    if sl_hash == 'd':
        y = 866.88 - pixels_bf


    # Add coordinates to lists
    x_list.append(x)
    y_list.append(y)


    # Increment flag
    flag += 1



''' Show Simulation'''
def show_dot_simulation():
    fig.show()
    i = 0
    while i != number_of_sets: # Plot each point with a pause in between
        plt.plot(x_list[0+i], y_list[0+i], 'ro')
        plt.pause(1.0)
        i += 1
