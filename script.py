import mdl
from copy import deepcopy
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    tmp = []
    step = 0.1

    t = new_matrix()
    ident(t)
    systems = [ t ]
    
    #ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save', 'circle', 'bezier', 'hermite', 'box', 'sphere', 'torus' ]
    for comm in commands:
        if comm[0] == 'push':
            systems.append(deepcopy(systems[-1]))

        elif comm[0] == 'pop':
            systems.pop()

        elif comm[0] == 'box':
            #print 'BOX\t' + str(args)
            add_box(tmp,
                    float(comm[1]), float(comm[2]), float(comm[3]),
                    float(comm[4]), float(comm[5]), float(comm[6]))
            matrix_mult( systems[-1], tmp )
            draw_polygons(tmp, screen, color)
            tmp = []

        elif comm[0] == 'torus':
            #print 'TORUS\t' + str(args)
            add_torus(tmp,
                      float(comm[1]), float(comm[2]), float(comm[3]),
                      float(comm[4]), float(comm[5]), step)
            matrix_mult( systems[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []

        elif comm[0] == 'line':
            add_edge( tmp,
                      float(comm[1]), float(comm[2]), float(comm[3]),
                      float(comm[4]), float(comm[5]), float(comm[6]) )

        elif comm[0] == 'hermite' or comm[0] == 'bezier':
            add_curve(tmp,
                      float(comm[1]), float(comm[2]),
                      float(comm[3]), float(comm[4]),
                      float(comm[5]), float(comm[6]),
                      float(comm[7]), float(comm[8]),
                      step, line)                      
                           
        elif comm[0] == 'sphere':
            add_sphere(tmp,
                       float(comm[1]), float(comm[2]), float(comm[3]),
                       float(comm[4]), step)
            matrix_mult(systems[-1], tmp)
            draw_polygons(tmp, screen, color)
            tmp = []

        elif comm[0] == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(comm[2]) * (math.pi / 180)
            
            if comm[1] == 'x':
                t = make_rotX(theta)
            elif comm[1] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult( systems[-1], t )
            systems[-1] = [ x[:] for x in t]

        elif comm[0] == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(comm[1]), float(comm[2]), float(comm[3]))
            matrix_mult( systems[-1], t )
            systems[-1] = [ x[:] for x in t]

        elif comm[0] =='scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(comm[1]), float(comm[2]), float(comm[3]))
            matrix_mult( systems[-1], t )
            systems[-1] = [ x[:] for x in t]

        elif comm[0] == 'color':
            print 'COLOR CHANGE'
            color = [int(comm[1]), int(comm[2]), int(comm[3])]

        elif comm[0] == 'display':
            display(screen)
        print comm
