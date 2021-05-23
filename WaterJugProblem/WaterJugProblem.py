# Water Jug Problem - Breadth First Search Algorithm

# Water jug problem

# 2 Jugs --> 1 jug with 4 leter and other jug 3 leter
# We have keep 2 leters in 4 leter jug -- Goal state
# Have unlimieted water supply
# No measurements in both jugs

# Define the intial state and goal state 

# Initial state ==> (no water in 4 leter jug, no water in 3 leter jug)
# Goal state ==> (2 leters of water in 4 leter jug, no water in 3 leter jug )

# Define Operations (Rules)

# 1 --> Fill 4 leter jug --> (4,0)
# 2 --> Fill 3 leter jug --> (0,3)
# 3 --> Empty 4 leter jug --> (0,0)
# 4 --> Empty 3 leter jug --> (0,0)
# 5 --> Pour water from 3 leter jug to 4 leter jug --> (3,0)
# 6 --> Pour water from 4 leter jug to 3 leter jug --> (1,3)

jug1_capacity = 4
jug2_capacity = 3
initial_state = [0,0]
goal_states= [[2,0] ,[0,2]]
goal_state1, goal_state2 = [2,0] ,[0,2]
end = 2

def solution():
	path = []
	front = []
	front.append(initial_state)
	visited_nodes = []
 
	while(not (not front)):
		current_node = front.pop()
		x = current_node[0]
		y = current_node[1]
		path.append(current_node)

		if x == end or y == end:
			print("Found!")
			return path
   
		# Rule 1 :
		if current_node[0] < jug1_capacity and ([jug1_capacity, current_node[1]] not in visited_nodes):
			front.append([jug1_capacity, current_node[1]])
			visited_nodes.append([jug1_capacity, current_node[1]])

		# Rule 2 :
		if current_node[1] < jug2_capacity and ([current_node[0], jug2_capacity] not in visited_nodes):
			front.append([current_node[0], jug2_capacity])
			visited_nodes.append([current_node[0], jug2_capacity])

		# Rule 3 :
		if current_node[0] > jug1_capacity and ([0, current_node[1]] not in visited_nodes):
			front.append([0, current_node[1]])
			visited_nodes.append([0, current_node[1]])

		# Rule 4 :
		if current_node[1] > jug2_capacity and ([jug1_capacity, 0] not in visited_nodes):
			front.append([jug1_capacity, 0])
			visited_nodes.append([jug1_capacity, 0])

		# Rule 5 :
		if current_node[1] > 0 and ([min(x + y, jug1_capacity), max(0, x + y - jug1_capacity)] not in visited_nodes):
			front.append([min(x + y, jug1_capacity), max(0, x + y - jug1_capacity)])
			visited_nodes.append([min(x + y, jug1_capacity), max(0, x + y - jug1_capacity)])

		# Rule 6 :
		if current_node[0] > 0  and ([max(0, x + y - jug2_capacity), min(x + y, jug2_capacity)] not in visited_nodes):
			front.append([max(0, x + y - jug2_capacity), min(x + y, jug2_capacity)])
			visited_nodes.append([max(0, x + y - jug2_capacity), min(x + y, jug2_capacity)])

	return "Not found"

def checking(a, b):
	if a == 0:
		return b
	return checking(b%a, a)

# condition for getting a solution:
# the goal state should be a multiple of checking(a,b)


if end % checking(jug1_capacity,jug2_capacity) == 0 :
    print(solution())
else:
    print("Couln't find a sollution")