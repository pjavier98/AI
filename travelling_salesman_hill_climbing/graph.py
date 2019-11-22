from state import *

class Graph:
  
  def __init__(self):
    self.adj_list = None
    self.visited_states = [0] * 11
    self.solution = []
    
    
  def generate_graph(self, distances_list):
    graph = []
    graph.append([])
    input_adj_list = open('files/adj_list.txt', 'r')

    for i in range(10):
      adj_list = []
      for j in input_adj_list.readline().split():
        index = int(j) - 1
        
        dist = distances_list[i][index]
        # print('distance: ' + str(dist))
        
        state = State(int(j), dist)
        adj_list.append(state)

      graph.append(adj_list)
    
    input_adj_list.close()
    return graph

  def print_graph(self):
    for i in range(11):
      city = str(i)
      print(city + " -> ", end="")
      for j in self.adj_list[i]:
        print("(" + str(j.city) + ", " + str(j.dist) + ")", end=" ")
      print()