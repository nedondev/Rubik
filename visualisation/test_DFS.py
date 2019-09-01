from ascii_template import *

# Initialise pieces
corners = [Corner(0, 0, 'ryb'), Corner(1, 0, 'rgy'), Corner(2, 0, 'rwg'), Corner(3, 0, 'rbw'), Corner(4, 0, 'owb'), Corner(5, 0, 'ogw'), Corner(6, 0, 'oyg'), Corner(7, 0, 'oby')]
edges = [Edge(0, 0, 'ry'), Edge(1, 0, 'rg'), Edge(2, 0, 'rw'), Edge(3, 0, 'rb'), Edge(4, 0, 'yb'), Edge(5, 0, 'wb'), Edge(6, 0, 'wg'), Edge(7, 0, 'yg'), Edge(8, 0, 'ow'), Edge(9, 0, 'og'), Edge(10, 0, 'oy'), Edge(11, 0, 'ob')]
centers = [Center(0, 'r'), Center(1, 'b'), Center(2, 'w'), Center(3, 'g'), Center(4, 'y'), Center(5, 'o')]
current_state = State()
for corner in corners:
    current_state.append_corner(corner)
for edge in edges:
    current_state.append_edge(edge)
for center in centers:
    current_state.append_center(center)

goal_corners = [Corner(0, 0, 'ryb'), Corner(1, 0, 'rgy'), Corner(2, 0, 'rwg'), Corner(3, 0, 'rbw'), Corner(4, 0, 'owb'), Corner(5, 0, 'ogw'), Corner(6, 0, 'oyg'), Corner(7, 0, 'oby')]
goal_edges = [Edge(0, 0, 'ry'), Edge(1, 0, 'rg'), Edge(2, 0, 'rw'), Edge(3, 0, 'rb'), Edge(4, 0, 'yb'), Edge(5, 0, 'wb'), Edge(6, 0, 'wg'), Edge(7, 0, 'yg'), Edge(8, 0, 'ow'), Edge(9, 0, 'og'), Edge(10, 0, 'oy'), Edge(11, 0, 'ob')]
goal_centers = [Center(0, 'r'), Center(1, 'b'), Center(2, 'w'), Center(3, 'g'), Center(4, 'y'), Center(5, 'o')]

# Program control
if len(sys.argv) == 1:
    try:
        s = open('scramble.txt', 'r').read()
    except:
        print("No scramble")
        s = ""
else:
    s = sys.argv[1]

current_state.scramble(s)
current_state.print_cube()

#check position and orientation
#for i,j in enumerate(corners):
    #print(str(i)+":"+str(j.p) +":"+str(j.o))

#check goal
#if (all(i.p== j.p for i,j in zip(goal_centers,centers)) and all(i.p == j.p and i.o == j.o  for i,j in zip(goal_corners,corners)) and all(i.p == j.p and i.o == j.o for i,j in zip(goal_edges,edges))):
    #print("Reach Goal")
