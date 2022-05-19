import sys
from metro.tests.test_station import *
from metro.network.network_class import *
from metro.station.station_class import *
from metro.helpers.file_helper import *
from metro.tests.test_station import *
from metro.const import *

def search_algorithm(graph, start_station):
    '''
    Este algoritmo consiste en una busqueda de la ruta mínima desde una estación de inicio a
    los demás nodos, inspirado en el algoritmo Dijkstra. Todos las estaciones comienzan
    con un costo inicial 'infinito', excepto la estación de inicio que inicia en valor 0.
    Luego, se visitan los vecinos de la estación inicial y se actualizan sus costos, que
    dependen si el tren para o no en dicha estación. Una vez visitados todos los vecinos y
    actualizados los valores, se procede a repetir el proceso con otra estación no visitada
    anteriormente.
    '''
    unvisited_stations = graph.stations
    # Diccionario donde se actualiza el costo de visitar cada estación
    shortest_path = {}
    # Diccionerio para llevar registro de la estación visitada justo antes
    previous_stations = {}
    #max_value = sys.maxsize
    for station in unvisited_stations:
        shortest_path[station] = MAX_VALUE
    shortest_path[start_station] = 0   
     
    # Se ejecuta el algoritmo hasta visitar todas las estaciones:
    while unvisited_stations:
        # Se actualiza la estación a analizar como la que tenga costo mínimo
        current_min_station = None
        for station in unvisited_stations:
            if current_min_station == None:
                current_min_station = station
            elif shortest_path[station] < shortest_path[current_min_station]:
                current_min_station = station
        # Se actualiza el costo minimo de los vecinos y su estación previa.
        neighbors = current_min_station.neighbors
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_station] + graph.value(neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_stations[neighbor] = current_min_station
 
        # Se marca la estación actual como visitada
        unvisited_stations.remove(current_min_station)
        
    return previous_stations, shortest_path
  
def run():
    
    input = read_json_input(sys.argv[-1])
    validate_input(input)
    
    stations = create_stations(input["stations"])
    link_stations(stations, input["stations"])
    network = create_network(stations, input["train color"])
    start_station = stations[input["start"]]
    target_station = stations[input["target"]]

    previous_stations, shortest_path = search_algorithm(network, start_station)

    print_result(network, previous_stations, shortest_path, start_station, target_station)
