class Network(object):
    def __init__(self): 
        self.stations = [] 
        self.train_color = 'green'
        
    def add_station(self, station):
        if station not in self.stations:
          self.stations.append(station)
        return   

    def value(self, next_station):
        '''
        Retorna 1 o 0 para ser sumado al costo de una estación. 
        Depende si el tren realiza o no una parada en la 'next_station'
        '''
        if self.train_color == None: return 1
        if next_station.color in [self.train_color, None]:
          return 1  
        return 0  

def create_network(stations_dict, train_color):
    network = Network()
    for station in stations_dict.values():
        network.add_station(station)
    network.train_color = train_color if train_color != 'None' else None
    return network