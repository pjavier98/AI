from state import *

class Graph:
  
  def __init__(self):
    self.adj_list = None
    self.visited_states = [0] * 15
    self.solution = []
    
    
  def generate_graph(self, distances_list, colors_list, goal):
    graph = []
    graph.append([])
    input_adj_list = open('files/adj_list.txt', 'r')

    for i in range(14):
      adj_list = []
      for j in input_adj_list.readline().split():
        index = int(j) - 1
        
        real_dist = distances_list[i][index]
        # print('real distance: ' + str(real_dist))
        heurist_dist = distances_list[index][goal - 1]
        # print('heuristic distance: ' + str(heurist_dist))
        color = set(colors_list[index])
          
        state = State(int(j), real_dist, heurist_dist, color, i + 1)
        adj_list.append(state)

      graph.append(adj_list)
    
    input_adj_list.close()
    return graph

  def print_graph(self):
    for i in range(15):
      station = str(i)
      print(station + " -> ", end="")
      for j in self.adj_list[i]:
        print(str(j.station) + " ", end="")
      print()