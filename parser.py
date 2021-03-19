from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguments (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
               then multiply the transform matrix by the translation matrix -
               takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, 'r')
    line = file.readline().rstrip('\n')

    while line != "":
        if line == "ident":
            ident(transform)
        elif line == "apply":
            matrix_mult(transform, points)
        elif line == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif line == "quit":
            break
        else:
            arg = file.readline().rstrip('\n')
            arg = arg.split(" ")

            if line == "rotate":
                arg[1] = int(arg[1])
                if arg[0] == "x":
                    matrix_mult(make_rotX(arg[1]), transform)
                elif arg[0] == "y":
                    matrix_mult(make_rotY(arg[1]), transform)
                elif arg[0] == "z":
                    matrix_mult(make_rotZ(arg[1]), transform)
            elif line == "save":
                clear_screen(screen)
                draw_lines(points, screen, color)
                save_extension(screen, arg[0])
            else:
                for i in range(len(arg)):
                    arg[i] = float(arg[i])
                if line == "line":
                    add_edge(points, arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
                elif line == "scale":
                    matrix_mult(make_scale(arg[0], arg[1], arg[2]), transform)
                elif line == "move":
                    matrix_mult(make_translate(arg[0], arg[1], arg[2]), transform)

        line = file.readline().rstrip('\n')

    file.close()
