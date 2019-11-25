class State:
  
    def __init__(self, city):
        self.city = city
        self.depth = 0
        self.dad = None

    def __str__(self):
      # childrens_id = str_children()
      return ('city: {}\ndepth: {}\ndad: {}\n'
            .format(self.city, self.depth, self.dad.city
      ))

    def create_state():
      return State(city, depth, dad)

    def update_depth(self, depth):
      self.depth = depth

    def final_state(self, begin):
      return self.station == begin