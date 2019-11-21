from state import *
from graph import * 
from utils_function import *
from queue import PriorityQueue

def a_star_search(graph, initial_state, goal):
  queue = PriorityQueue()
  queue.put([0, initial_state.station, initial_state])

  while(not queue.empty()):
    current_pair_state = queue.get()
    previous_cost = current_pair_state[0]
    current_state = current_pair_state[2]
    
    # Checking if the current state is the goal
    if current_state.final_state(goal):
      # Updating the cost in the goal
      current_state.update_total_cost(previous_cost) 

      # Getting the best way from the begin to the goal 
      graph.solution = [current_state]
      while current_state.dad:
        if (current_state == current_state.dad): 
          break

        graph.solution.insert(0, current_state.dad)
        current_state = current_state.dad
      break

    # Mark as visited
    graph.visited_states[current_state.station] = 1
    
    for state in graph.adj_list[current_state.station]:
      if graph.visited_states[state.station] == 0:
        cost = previous_cost + state.real_dist + state.heurist_dist

        if not current_state.same_line(state, graph):
          cost += 2

        state.dad = current_state
        state.update_color(current_state.color)
        state.update_total_cost(cost) 
        queue.put([cost, state.station, state])

def main():
  print('\n#################################')
  print('# Welcome to the Metro of Paris #')
  print('#################################', end='\n\n')

  print('Select the departure station: [1-14]: ', end='')
  begin = read_stations()
  print('Select the departure station: [1-14]: ', end='')
  goal = read_stations()

  print('\nTicket: From {} to {}'.format(begin, goal), end='\n\n')

  # Read the distances
  distances_list = read_files('files/distances.txt')

  '''
    Blue: 0
    Yellow: 1
    Green: 2
    Red: 3
  '''
  # Read the colors of the station
  colors_list = read_files('files/colors.txt')
  
  # Creating the Graph
  graph = Graph()
  graph.adj_list = graph.generate_graph(distances_list, colors_list, begin, goal)

  # Creating the initial state
  initial_state = State(int(begin), 0, 0, colors_list[begin - 1], begin)
  initial_state.dad = initial_state

  # Doing the A* search
  solution = a_star_search(graph, initial_state, goal)

  # Prining the best way
  print_best_way(graph.solution)

main()