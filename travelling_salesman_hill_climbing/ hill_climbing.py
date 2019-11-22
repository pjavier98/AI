from utils_function import *
from graph import *
from state import *

flag = 1

def search_hamiltonian_cycle(graph, initial_state, begin, distances_list):
  global flag
  graph.visited_states[initial_state.city] = 1

  # print(str(initial_state))

  if ((initial_state.depth == 9) and (distances_list[initial_state.city - 1][begin - 1] != -1) and flag):
    print('entrou aqui')
    graph.solution = [initial_state]
    while initial_state.dad:
      if (initial_state == initial_state.dad): 
        break

      graph.solution.insert(0, initial_state.dad)
      initial_state = initial_state.dad
    flag = 0
    return

  for state in graph.adj_list[initial_state.city]:
    if (not graph.visited_states[state.city]):
      state.depth = initial_state.depth + 1
      state.dad = initial_state
      search_hamiltonian_cycle(graph, state, begin, distances_list)
      graph.visited_states[state.city] = 0

def main():
  print('Select the start city: [1-10]: ', end='')
  begin = read_city()

  distances_list = read_files('files/distances.txt')

  graph = Graph()
  graph.adj_list = graph.generate_graph(distances_list)
  # graph.print_graph()

  initial_state = State(int(begin), 0)
  initial_state.dad = initial_state

  search_hamiltonian_cycle(graph, initial_state, begin, distances_list)

  print_best_way(graph.solution)
main()