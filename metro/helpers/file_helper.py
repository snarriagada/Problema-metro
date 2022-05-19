import json
from metro.const import *

def read_json_input(file_name):
    try:
        file = open(file_name, "r")
        input = file.read()
        js = json.loads(input)
        file.close()
        return js
    except:
      raise Exception("Invalid JSON format")


def print_result(graph, previous_stations, shortest_path, start_station, target_station):
    path = []
    station = target_station
    if graph.train_color != None and target_station.color not in [graph.train_color, None]:
        raise Exception("Please confirm that the train can stop in the target station")
        
    while station != start_station:
        # Tren hace parada en estacion sin color o de su mismo color
        if graph.train_color == None or station.color in [graph.train_color, None]: 
            path.append(str(station))
        try:
            station = previous_stations[station]
        except:
            raise Exception("There is a unlinked station in the given network")
    path.append(str(start_station))
    
    print("We found the following best path with {} stop(s).".format(shortest_path[target_station]))
    print(" -> ".join(reversed(path)))


def validate_input(input):
    attributes = ['train color', 'start', 'target', 'stations']
    train_color = input['train color']
    start = input['start']
    target = input['target']
    stations = input['stations']
    stations_names = list(map(str, stations.keys()))

    if set(attributes) != set(input.keys()):
        raise Exception("Sorry, there are invalid attributes in input")
    if train_color not in ["None", GREEN, RED]:
        raise Exception("Sorry, the train color is invalid")
    if not isinstance(start, str):
        raise Exception("The 'start' station must be a string in the input")
    if not isinstance(target, str):
        raise Exception("The 'target' station must be a string in the input")
    if not isinstance(stations, dict):
        raise Exception("Invalid 'stations' format in the input")
    if stations[start]['color'] != "None" and train_color != "None":
        if stations[start]['color'] != train_color:
            raise Exception("The train can`t start form the given 'start' station")
    if start not in stations_names:
        raise Exception("Invalid start station")
    if target not in stations_names:
        raise Exception("Invalid target station")
