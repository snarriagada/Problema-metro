class Network(object):
    def __init__(self): 
        # self.stations saves the Stations instances
        self.stations = [] 
        self.train_color = 'green'
        
    def add_station(self, station):
        if station not in self.stations:
          self.stations.append(station)
        return   

    def value(self, next_station):
        "if next_station are the same color as the train or has not color"
        if self.train_color == None: return 1
        if next_station.color in [self.train_color, None]:
          return 1  
        else:  
          "if next_station has other color different that the train"
          return 0  


def create_network(stations_dict, train_color):
    network = Network()
    for station in stations_dict.values():
        network.add_station(station)
    network.train_color = train_color
    return network