from classes import *

# Create earth
earth = NotSatellite("Earth", 0)

# Create satellites
sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)
sat3 = Satellite("Sat3", 300)
sat4 = Satellite("Sat4", 400)
sat5 = Satellite("Sat5", 500)
sat6 = Satellite("Sat6", 600)

space_entity_list = [earth, sat1, sat2, sat3, sat4, sat5, sat6]




wrapping_packet("Hello from sat1", sat1, sat4, space_entity_list, b"P")
