import unittest
from metro.station.station_class import *
from metro.helpers.file_helper import *

# correr python3 -m unittest discover 

input = read_json_input('metro/inputs/input_1.json')

class TestStation(unittest.TestCase):
  test_stations = create_stations(input["stations"])
  
  def test_create_station(self):
        '''
        testeamos que a partir del input se cree un diccionario, donde
        el valor de cada llave(nombre de la estación) sea una 
        instancia de la clase Station.
        '''
        message = "given object is not instance of Station."
        
        for key, value in self.test_stations.items():
          self.assertIsInstance(value, Station, message)
          
  def test_link_stations(self):
      '''
      testeamos que para cada nodo, exista una lista de vecinos
      que sean una instancia de la clase Station.
      '''
      link_stations(self.test_stations, input["stations"])
      for station in self.test_stations.values():
        message = "station's neighbor is not instance of Station."
        for neighbor in station.neighbors:
          self.assertIsInstance(neighbor, Station, message)



if __name__ == '__main__':
  unittest.main()