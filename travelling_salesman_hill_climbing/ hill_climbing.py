from utils_function import *
from graph import *
from state import *
from random import randint

flag = 1

def search_hamiltonian_cycle(graph, initial_state, begin, distances_list):
  global flag
  graph.visited_states[initial_state.city] = 1

  if ((initial_state.depth == 9) and (distances_list[initial_state.city - 1][begin - 1] != -1) and flag):
    graph.solution = [initial_state]
    while initial_state.dad:
      if (initial_state == initial_state.dad): 
        break

      graph.solution.insert(0, initial_state.dad)
      initial_state = initial_state.dad
    flag = 0
    graph.update_initial_cost(distances_list)
    return

  for state in graph.adj_list[initial_state.city]:
    if (not graph.visited_states[state.city]):
      state.update_depth(initial_state.depth + 1)
      state.dad = initial_state
      search_hamiltonian_cycle(graph, state, begin, distances_list)
      graph.visited_states[state.city] = 0

def hill_climbing(graph, begin, distances_list, amount_permutations):
  adj_list_begin = graph.adj_list[begin]

  solution = []
  solution.extend(graph.solution)

  new_solution = []
  for num in adj_list_begin:
    if (num.city != graph.solution[9]):
      for i in range(amount_permutations):
        x = randint(1, 8)
        y = randint(1, 8)

        new_solution = solution

        aux_state = new_solution[x]
        new_solution[x] = new_solution[y]
        new_solution[y] = aux_state
        
        if (graph.check_hamiltonian_cycle(new_solution, distances_list, begin)):
          graph.print_best_way(0)

      new_solution.clear()
      solution.clear()
      solution.extend(graph.solution)

      for i in range(10):
        state = solution[i]
        if (state.city == num.city):
          solution[i] = solution[9]
          solution[9] = state
          break
    

def main():
  print('Select the start city: [1-10]: ', end='')
  begin = read_input(0, 10)

  print('Select the numbers of permutations: [0-10e6]: ', end='')
  amount_permutations = read_input(0, 1000000)

  distances_list = read_files('files/distances.txt')

  graph = Graph()
  graph.adj_list = graph.generate_graph(distances_list)

  initial_state = State(int(begin), 0)
  initial_state.dad = initial_state

  search_hamiltonian_cycle(graph, initial_state, begin, distances_list)

  graph.print_best_way(1)
  hill_climbing(graph, begin, distances_list, amount_permutations)
main()