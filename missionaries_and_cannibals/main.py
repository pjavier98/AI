from node import *
from util import *

def generate_solution(queue, visited_states, util):
  initial_state = State(3, 0, 3, 0, 'left')
  
  visited_states = [initial_state]
  queue = [initial_state]

  for state in queue:
    if state.final_state():
      util.solution = [state]
      while state.dad:
        util.solution.insert(0, state.dad)
        state = state.dad
      break

    state.generate_children(visited_states)
    queue.extend(state.children)
  
def print_solution(solution):
  index = 1
  print('\n\t\tSolution: Missionaries and Cannibals\n')
  for state in solution:
    print(65 * '#')
    print('#\tState ' + str(index) + ': \t\t\t\t\t\t#\n' + str(state))
    print(65 * '#', end='\n\n')
    index += 1

def main():
  util = Util()
  generate_solution(util.queue, util.visited_states, util)
  print_solution(util.solution)

main()
  