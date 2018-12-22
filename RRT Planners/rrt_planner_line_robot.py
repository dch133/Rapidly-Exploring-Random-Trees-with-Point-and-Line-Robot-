import time
import random
import drawSample
import math
import _tkinter as tk
import sys
import imageToRects

# display = drawSample.SelectRect(imfile=im2Small,keepcontrol=0,quitLabel="")

visualize = 1
prompt_before_next = 1  # ask before re-running since solved
SMALLSTEP = 10  # what our "local planner" can handle.
SMALLTHETA = 5

XMAX = 1800
YMAX = 1000
G = [[0], []]  # nodes, edges

s, obstacles = imageToRects.imageToRects(sys.argv[1])

XMAX = s[0]
YMAX = s[1]

# goal/target
tx = 800
ty = 150
theta = 0
# start
start_x = 100
start_y = 630
start_t = 0

vertices = [[start_x, start_y, start_t]]

sigmax_for_randgen = XMAX / 2.0
sigmay_for_randgen = YMAX / 2.0

nodes = 0
edges = 1
maxvertex = 0


def drawGraph(G):
    global vertices, nodes, edges
    if not visualize: return
    for i in G[edges]:
        if len(vertices) != 1:
            canvas.polyline([vertices[i[0]], vertices[i[1]]])


def genPoint():
    # Function to implement the sampling technique
    x = 0.0
    y = 0.0
    t = 0.0
    pt_samplefree = False

    while (not pt_samplefree):
        x =random.random() * XMAX
        y = random.random() * YMAX
        t = random.random() *360.0

        for rect in obstacles:
            if (inRect([x,y], rect, 0)):
                pt_samplefree = False
                break
            else:
                pt_samplefree = True
    return [x, y, t]


def genvertex():
    vertices.append(genPoint())
    return len(vertices) - 1


def pointToVertex(p):
    vertices.append(p)
    return len(vertices) - 1


def pickvertex():
    return random.choice(range(len(vertices)))


def lineFromPoints(p1, p2):
    line = []
    llsq = 0.0  # line length squared
    for i in range(2):  # each dimension #############EDITED (len(p1)
        h = p2[i] - p1[i]
        line.append(h)
        llsq += h * h
    ll = math.sqrt(llsq)  # length
    # normalize line
    if ll <= 0: return [0, 0]
    for i in range(2):  # each dimension #############EDITED (len(p1)
        line[i] = line[i] / ll
    return line


def pointPointDistance(p1, p2):
    """ Return the distance between a pair of points (L2 norm). """
    llsq = 0.0  # line length squared
    # faster, only for 2D
    h = p2[0] - p1[0]
    llsq = llsq + (h * h)
    h = p2[1] - p1[1]
    llsq = llsq + (h * h)
    return math.sqrt(llsq)

    for i in range(len(p1)):  # each dimension, general case
        h = p2[i] - p1[i]
        llsq = llsq + (h * h)
    return math.sqrt(llsq)


def closestPointToPoint(G, p2):
    dmin = 999999999
    for v in G[nodes]:
        p1 = vertices[v]
        d = pointPointDistance(p1, p2)
        if d <= dmin:
            dmin = d
            close = v
    return close


def returnParent(k):
    """ Return parent note for input node k. """
    for e in G[edges]:
        if e[1] == k:
            canvas.polyline([vertices[e[0]], vertices[e[1]]], style=3)
            return e[0]


def pickGvertex():
    try:
        edge = random.choice(G[edges])
    except:
        return pickvertex()
    v = random.choice(edge)
    return v


def redraw():
    canvas.events()
    return
    canvas.clear()
    canvas.markit(start_x, start_y, r=SMALLSTEP)
    canvas.markit(tx, ty, r=SMALLSTEP)
    drawGraph(G)
    for o in obstacles: canvas.showRect(o, outline='blue', fill='blue')
    canvas.delete("debug")


def ccw(A, B, C):
    """ Determine if three points are listed in a counterclockwise order.
    For three points A, B and C. If the slope of the line AB is less than 
    the slope of the line AC then the three points are in counterclockwise order.
    See:  http://compgeom.cs.uiuc.edu/~jeffe/teaching/373/notes/x06-sweepline.pdf
    """
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def intersect(A, B, C, D):
    """ do lines AB and CD intersect? """
    i = ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
    # if i:
    #    canvas.polyline(  [ A,B ], style=4  , tags = ("debug"))
    #    canvas.polyline(  [ C,D ], style=4  , tags = ("debug"))
    # else:
    #    canvas.polyline(  [ A,B ], style=1  , tags = ("debug")) # green
    #    canvas.polyline(  [ C,D ], style=1  , tags = ("debug"))
    return i


def lineHitsRect(p1, p2, r):
    rline = ((r[0], r[1]), (r[0], r[3]))
    if intersect(p1, p2, rline[0], rline[1]): return 1
    rline = ((r[0], r[1]), (r[2], r[1]))
    if intersect(p1, p2, rline[0], rline[1]): return 1
    rline = ((r[0], r[3]), (r[2], r[3]))
    if intersect(p1, p2, rline[0], rline[1]): return 1
    rline = ((r[2], r[1]), (r[2], r[3]))
    if intersect(p1, p2, rline[0], rline[1]): return 1

    return 0


def inRect(p, rect, dilation):
    """ Return 1 in p is inside rect, dilated by dilation (for edge cases). """
    if p[0] < rect[0] - dilation: return 0
    if p[1] < rect[1] - dilation: return 0
    if p[0] > rect[2] + dilation: return 0
    if p[1] > rect[3] + dilation: return 0
    return 1

global iteration_list
iteration_list = []
# Implementation of rrt_search algorithm in this function.
def rrt_search(G, tx, ty, theta, size):
    num_iterations = 0
    while(1):
        num_iterations +=1
        pt_random = genPoint() # call genPoint() to get samples from different distributions.
        index_nearest = closestPointToPoint(G, pt_random) #index of nearest point in G
        pt_nearest = vertices[index_nearest] # get the coord of nearest point
        #Steer

        line_to_pt_new = lineFromPoints(pt_nearest, pt_random)
        #robot_size = 3 # set the size of the line robot
        bigger_line_to_pt_new = [line_to_pt_new[0]*SMALLSTEP, line_to_pt_new[1]*SMALLSTEP]
        pt_new = [bigger_line_to_pt_new[0]+pt_nearest[0], bigger_line_to_pt_new[1]+pt_nearest[1], pt_nearest[2]] #get coord of new point

        #check the rotation angle for our new point is reachable
        shift = abs(pt_random[2] - pt_nearest[2]) # angular shift
        # if the angle shift > threshold angle, shift by the max possible
        if (shift > SMALLTHETA):
            if (pt_random[2] > pt_nearest[2]):
                pt_new[2] = (pt_new[2] + SMALLTHETA) % 360
            else:
                pt_new[2] = (pt_new[2] - SMALLTHETA) % 360
        # if the angle shift =< threshold angle, shift to the new angle
        if (shift <= SMALLTHETA):
            if (pt_random[2] > pt_nearest[2]):
                pt_new[2] = (pt_new[2] + shift) % 360
            else:
                pt_new[2] = (pt_new[2] - shift) % 360


        if (pt_new[0] > XMAX or pt_new[1] > YMAX or pt_new[0] < 0 or pt_new[1] < 0): #Make sure our graph doesn't go out of window
            continue
        #end steer
        #Check pt_new is obstacle free
        pt_contacts_obstacle = False
        #check if the whole robot doesn't hit obstacles
        # calculate edge pt of line-robot, generated by theta: [xcos(t) +x, ysin(t)] and check if that line hits obstacles
        pt_edge = [pt_new[0]+size*math.cos(pt_new[2]),pt_new[1]+size*math.sin(pt_new[2])]
        if (pt_edge[0] > XMAX or pt_edge[1] > YMAX or pt_edge[0] < 0 or pt_edge[1] < 0): #Make sure our graph doesn't go out of window
            continue
        for ob in obstacles: #check if new point is in some obstacle
            if (lineHitsRect(pt_nearest,pt_new,ob)==1):
                pt_contacts_obstacle = True
                break
            if (inRect(pt_new,ob,0)==1):
                pt_contacts_obstacle = True
                break
            if (lineHitsRect(pt_edge,pt_new,ob)==1):
                pt_contacts_obstacle = True
                break

        if (pt_contacts_obstacle): continue #Get another point from saple space if current hits/is in obstacle
        #end check obstacle_free

        #Update G and Vertices and Edges
        index_pt_new = pointToVertex(pt_new) #generate the index of the new node
        G[nodes].append(index_pt_new)#add new node to G
        G[edges].append((index_nearest, index_pt_new))#add new edge to G
        canvas.events()
        canvas.polyline([vertices[index_nearest],vertices[index_pt_new]])
        #When we reached the goal
        if (pointPointDistance([pt_new[0],pt_new[1]], [tx,ty]) <= SMALLSTEP):
            child_node = index_pt_new
            while(1):
                parent_node = returnParent(child_node)
                canvas.polyline([vertices[child_node], vertices[parent_node]])
                pt_parent = vertices[parent_node]
                pt_edge = [pt_parent[0] + size * math.cos(pt_parent[2]), pt_parent[1] + size * math.sin(pt_parent[2])]
                canvas.polyline([pt_parent, pt_edge], style=1)
                if (parent_node == 0):
                    break
                child_node = parent_node
            break

    return num_iterations, G

if visualize:
    canvas = drawSample.SelectRect(xmin=0, ymin=0, xmax=XMAX, ymax=YMAX, nrects=0,
                                   keepcontrol=0)  # , rescale=800/1800.)

if 0:  # line intersection testing
    obstacles.append([75, 60, 125, 500])  # tall vertical
    for o in obstacles: canvas.showRect(o, outline='red', fill='blue')
    lines = [
        ((70, 50), (150, 150)),
        ((50, 50), (150, 20)),
        ((20, 20), (200, 200)),
        ((300, 300), (20, 200)),
        ((300, 300), (280, 90)),
    ]
    for l in lines:
        for o in obstacles:
            lineHitsRect(l[0], l[1], o)
    canvas.mainloop()

if 0:
    # random obstacle field
    for nobst in range(0, 6000):
        wall_discretization = SMALLSTEP * 2  # walls are on a regular grid.
        wall_lengthmax = 10.  # fraction of total (1/lengthmax)
        x = wall_discretization * int(random.random() * XMAX / wall_discretization)
        y = wall_discretization * int(random.random() * YMAX / wall_discretization)
        # length = YMAX/wall_lengthmax
        length = SMALLSTEP * 2
        if random.choice([0, 1]) > 0:
            obstacles.append([x, y, x + SMALLSTEP, y + 10 + length])  # vertical
        else:
            obstacles.append([x, y, x + 10 + length, y + SMALLSTEP])  # horizontal
else:
    if 0:
        # hardcoded simple obstacles
        obstacles.append([300, 0, 400, 95])  # tall vertical
        # slightly hard
        obstacles.append([300, 805, 400, YMAX])  # tall vertical
        # obstacles.append( [ 300,400,1300,430 ] )
        # hard
        obstacles.append([820, 220, 900, 940])
        obstacles.append([300, 0, 400, 95])  # tall vertical
        obstacles.append([300, 100, 400, YMAX])  # tall vertical
        obstacles.append([200, 300, 800, 400])  # middle horizontal
        obstacles.append([380, 500, 700, 550])
        # very hard
        obstacles.append([705, 500, XMAX, 550])

if visualize:
    for o in obstacles: canvas.showRect(o, outline='red', fill='blue')

maxvertex += 1

while (1):
    # graph G
    G = [[0], []]  # nodes, edges
    vertices = [[10, 630, 0], [60, 630, 0]]
    redraw()

    G[edges].append((0,1))
    G[nodes].append(1)
    if visualize:
        canvas.markit(tx, ty, r=SMALLSTEP)
        drawGraph(G)
        rrt_search(G, tx, ty, theta, 40)
        canvas.events()
        #canvas.showRect(rect,fill='red')

    if visualize:
        canvas.mainloop()
