from space_network_lib import *
from classes import Satellite, SpaceNetwork, transmission_attempt


sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)

message = Packet("Hi there...", sat1, sat2)

transmission_attempt(message)
