import unittest
from metro.station.station_class import *
from metro.network.network_class import *
from metro.helpers.file_helper import *
from metro.const import *

input = read_json_input('metro/inputs/input_1.json')
class TestNetwork(unittest.TestCase):
  
  stations = create_stations(input["stations"])
  network = create_network(stations, input["train color"])
  train_colors = [None, GREEN, RED]
  
  
  def test_create_network(self):
    '''
    testeamos que la creacion de la red de estaciones corresponda
    a una instancia de la clase Network
    '''
    message = "given object is not instance of Network."
    self.assertIsInstance(self.network, Network, message)
        
  def test_train_color(self):
    '''
    testeamos que se almacena correctamente el color del tren
    dentro de las opciones disponibles
    '''
    self.assertIn(self.network.train_color, self.train_colors)
          
if __name__ == '__main__':
  unittest.main()