from state import *

class Graph:
  
  def __init__(self):
    self.adj_list = None
    self.visited_states = [0] * 11
    self.solution = []
    self.total_cost = 0
    
  def generate_graph(self, distances_list):
    graph = []
    graph.append([])
    input_adj_list = open('files/adj_list.txt', 'r')

    for i in range(10):
      adj_list = []
      for j in input_adj_list.readline().split():
        index = int(j) - 1
        
        state = State(int(j))
        adj_list.append(state)

      graph.append(adj_list)
    
    input_adj_list.close()
    return graph

  def check_hamiltonian_cycle(self, possible_solution, distances_list, begin):
    cost = 0

    for i in range(9):
      previous_state = possible_solution[i].city
      current_state = possible_solution[i + 1].city

      dist = distances_list[previous_state - 1][current_state - 1]
      if (dist == - 1):
        return 0
      else:
        cost += dist

    # Cost from the last to the begin

    cost += distances_list[current_state - 1][begin - 1]
    if (cost < self.total_cost):
      self.total_cost = cost
      self.solution.clear()
      self.solution.extend(possible_solution)
      return 1
    return 0

  def update_cost(self, distances_list, begin):
    cost = 0
    for i in range(9):
      previous_state = self.solution[i].city
      current_state = self.solution[i + 1].city
      cost += distances_list[previous_state - 1][current_state - 1]
    
    cost += distances_list[begin - 1][current_state - 1]
    self.total_cost = cost

  def print_graph(self):
    for i in range(11):
      city = str(i)
      print(city + " -> ", end="")
      for j in self.adj_list[i]:
        print(str(j.city), end=" -> ")
      print('//')

  def print_best_way(self, flag):
    if flag:
      print('Hamiltonian Cycle Initial State: cost: {}'.format(self.total_cost))  
    else:
      print('Hamiltonian Cycle: cost: {}'.format(self.total_cost))
    for i in self.solution:
      print(i.city, end=" -> ")
    print('//', end='\n')