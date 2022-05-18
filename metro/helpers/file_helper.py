import sys
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
        if graph.train_color == None or station.color in [graph.train_color, None]: # hace parada en estacion sin color o del mismo que el tren
            path.append(str(station))
        station = previous_stations[station]
 
    # Add the start station manually
    path.append(str(start_station))
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_station]))
    print(" -> ".join(reversed(path)))


def validate_input(input):
    attributes = ['train color', 'start', 'target', 'stations']
    train_color = input['train color']
    start = input['start']
    target = input['target']
    stations = input['stations']
    
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
        

