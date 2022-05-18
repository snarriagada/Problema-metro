import json
import unittest
import sys
from metro.station.station_class import *
from metro.network.network_class import *
from metro.helpers.file_helper import *
from metro.const import *
from metro.main import *


# correr python3 -m unittest discover 

input = read_json_input('metro/inputs/input_1.json')

class TestNetwork(unittest.TestCase):
  
  stations = create_stations(input["stations"])
  link_stations(stations, input["stations"])
  network = create_network(stations, input["train color"])
  start_station = stations[input["start"]]
  train_colors = [None, GREEN, RED]
  
  def test_search_algorithm(self):
    '''
    testeamos que el algoritmo de búsqueda retorne diccionarios válidos,
    incluyendo las instancias de las estaciones con sus respectivas
    estaciones previas.
    '''
    previous_stations, shortest_path = search_algorithm(self.network, self.start_station)    
    message_station_instace = "given object is not instance of Station."
    message_cost = "invalid path cost"

    for key, value in previous_stations.items():
      self.assertIsInstance(key, Station, message_station_instace)
      self.assertIsInstance(value, Station, message_station_instace)
    for key, value in shortest_path.items():
      self.assertIsInstance(key, Station, message_station_instace)
      self.assertTrue(0 <= value <= sys.maxsize, message_cost) # para comprobar que es int

if __name__ == '__main__':
  unittest.main()