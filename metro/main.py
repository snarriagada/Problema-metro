import sys
import json
from metro.tests.test_station import *
from metro.network.network_class import *
from metro.station.station_class import *
from metro.helpers.file_helper import *
from metro.tests.test_station import *

def search_algorithm(graph, start_station):
    unvisited_stations = graph.stations
    # We'll use this dict to save the cost of visiting each station and update it as we move along the graph   
    shortest_path = {}
    # We'll use this dict to save the shortest known path to a station found so far
    previous_stations = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited stations   
    max_value = sys.maxsize
    for station in unvisited_stations:
        shortest_path[station] = max_value
    # However, we initialize the starting station's value with 0   
    shortest_path[start_station] = 0    
    # The algorithm executes until we visit all stations
    while unvisited_stations:
        # The code block below finds the station with the lowest score
        current_min_station = None
        for station in unvisited_stations:
            if current_min_station == None:
                current_min_station = station
            elif shortest_path[station] < shortest_path[current_min_station]:
                current_min_station = station      
        # The code block below retrieves the current station's neighbors and updates their distances
        neighbors = current_min_station.neighbors
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_station] + graph.value(neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current station
                previous_stations[neighbor] = current_min_station # podria ser almacenado en el Station
 
        # After visiting its neighbors, we mark the station as "visited"
        unvisited_stations.remove(current_min_station)
        
    return previous_stations, shortest_path
  
def run():
    # # stations, color, start, target = read_json_input()
    input = read_json_input(sys.argv[-1])
    stations = create_stations(input["stations"])
    link_stations(stations, input["stations"])
    network = create_network(stations, input["train color"])
        
    start_station = stations[input["start"]]
    target_station = stations[input["target"]]

    previous_stations, shortest_path = search_algorithm(network, start_station)

    print_result(network, previous_stations, shortest_path, start_station, target_station)
