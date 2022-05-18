import sys
import json

def read_json_input(file_name):
    file = open(file_name, "r")
    input = file.read()
    js = json.loads(input)
    file.close()
    return js

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
    
# validaciones

# validar estructura json con slguna libreria externa probablemente.

# chequear que se pueda llegar del nodo inicio al fin

# chequear que la estacion de inicio coincida con el color del tren (o sean None)


