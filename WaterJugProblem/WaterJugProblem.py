# Water Jug Problem - Breadth First Search Algorithm

jug1_capacity = 4
jug2_capacity = 3
initial_state = [0,0]
goal_state1, goal_state2 = [2,0] ,[0,2]

def solution(initial_state,jug1_capacity, jug2_capacity):
	path = []
	front = []
	front.append(initial_state)
	visited_nodes = []
 
	while(not (not front)):
		current_node = front.pop()
		x = current_node[0]
		y = current_node[1]
		path.append(current_node)
  
		if x == goal_state1[0] or y == goal_state2[1]:
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

if goal_state1[0] % checking(jug1_capacity,jug2_capacity) == 0:
	print(solution(initial_state,jug1_capacity, jug2_capacity))
else:
	print("Couln't find a sollution")