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

# 1 --> Fill 4 leter jug --> (4,y)
# 2 --> Fill 3 leter jug --> (x,3)
# 3 --> Empty 4 leter jug --> (0,y)
# 4 --> Empty 3 leter jug --> (x,0)
# 5 --> Pour from 1st jug to 2nd jug until it's full --> (x-(3 -y) ,3)
# 6 --> Pour from 2nd jug to 1st jug until it's full --> (4, y - (4-x))
# 7 -->  Pour all water from 1st to 2nd  --> (0, x+y)
# 8 -->  Pour all water from 2nd to 1st --> (x+y, 0)

jug1_capacity = 4
jug2_capacity = 3
initial_state = [0,0]
full_capacity_state = [4, 2]
goal_state= [2,0]

def solution():
	path = []
	queue = []
	queue.append(initial_state)
	visited_nodes = []
 
	while(not (not queue)):
		print('queue', queue)
		current_node = queue.pop(0)
		x = current_node[0]
		y = current_node[1]
		path.append(current_node)
  
		# Base Case 
		if x == goal_state[0] and y == goal_state[1]:
			print("Found!")
			return path
		
		temp_node = current_node.copy()
   
		# Rule 1 
		if x < full_capacity_state[0] and ([full_capacity_state[0],y] not in visited_nodes):
			temp_node = [full_capacity_state[0],y]
			queue.append(temp_node)
			visited_nodes.append(temp_node)

		# Rule 2
		if y < full_capacity_state[1] and ([x, full_capacity_state[1]] not in visited_nodes):
			temp_node = [x, full_capacity_state[1]]
			queue.append(temp_node)
			visited_nodes.append(temp_node)

		# Rule 3 
		if x > 0 and ([0, y]):
			temp_node = [0, y]
			queue.append(temp_node)
			visited_nodes.append(temp_node)

		# Rule 4 
		if y > 0 and ([x, 0]):
			temp_node = [x, 0]
			queue.append(temp_node)
			visited_nodes.append(temp_node)

		# Rule 5
		if x > 0 and (x + y) >= full_capacity_state[1] and ([x - (full_capacity_state[1] - y), full_capacity_state[1] ]):
			temp_node = [x - (full_capacity_state[1] - y), full_capacity_state[1] ]
			queue.append(temp_node)
			visited_nodes.append(temp_node)
   
		# Rule 6 
		if y > 0 and (x + y) >= full_capacity_state[0]  and ([full_capacity_state[0], y - (full_capacity_state[0] - x)]):
			temp_node = [full_capacity_state[0], y - (full_capacity_state[0] - x)]
			queue.append(temp_node)
			visited_nodes.append(temp_node)
   
		# Rule 7
		if x > 0 and (x+y) <= full_capacity_state[1] and ([0, x+y]):
			temp_node = [0, x+y]
			queue.append(temp_node)
			visited_nodes.append(temp_node)

		# Rule 8 
		if y > 0 and (x+y) <= full_capacity_state[0]  and ([x+y, 0]):
			temp_node = [x+y, 0]
			queue.append(temp_node)
			visited_nodes.append(temp_node)
	return "Not found"


print(solution())
