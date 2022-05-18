class Station(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.neighbors = []
        self.station = None
    
    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
        if self not in neighbor.neighbors:
            neighbor.neighbors.append(self)
            
    def __str__(self):
        return self.name
      
def create_stations(stations_input):
    stations = {}
    for name, data in stations_input.items():
        station_color = data["color"] if data["color"] != 'None' else None
        station_instance = Station(name, station_color)
        stations[name] = station_instance
    return stations

def link_stations(stations_dict, stations_input):
    for instance in stations_dict.values():
        for neighbor in stations_input[instance.name]["neighbors"]:
            instance.add_neighbor(stations_dict[neighbor])
    return
