class State:
  
    def __init__(self, station, heurist_dist, real_dist, color, dad):
        self.station = station
        self.heurist_dist = heurist_dist
        self.real_dist = real_dist
        self.total_cost = heurist_dist + real_dist
        self.color = color
        self.dad = None

    def __str__(self):
      # childrens_id = str_children()
      return ('station: {}\nheurist_dist: {}\nreal_dist: {}\ntotal_cost: {}\ncolor: {}\ndad: {}\n'
            .format(self.station, self.heurist_dist, self.real_dist, self.total_cost, self.color, self.dad.station
      ))

    def create_state():
      return State(station, heurist_dist, real_dist, color)
    
    def update_total_cost(self, total_cost):
      self.total_cost = total_cost
    
    def update_color(self, dad_color):
      self.color = dad_color

    def same_line(self, next_state, current_line):
      return set(self.color) & set(next_state.color)

    def final_state(self, goal):
      return self.station == goal