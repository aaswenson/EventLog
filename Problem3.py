import math
import numpy

col_log = {}       #initialize collision log dictionary
dr = []  	   #initialize dr vector to fill later
direction = []     # initialize direction unit vector to fill later
collision_location = [1,2,3]
particle_position = [2,4,5]
ID = 43
energy = 2.1

# this function calculates distance to particle collision
# inputs: collision_location, particle_position
# outputs: distance to collision, unit vector of particle direction
def collision(ID,collision_location,particle_position,energy):
    distance_prev = 0
    for i in range(0,len(collision_location)):
        dr.append( collision_location[i] - particle_position[i])
        distance_prev = distance_prev +  math.sqrt(dr[i]*dr[i])
        direction = numpy.divide(dr,distance_prev)
        
    energy = energy*1000000
    Event_Log = {"distance to collision": distance_prev,"particle direction":direction,"energy":energy}
    return Event_Log
Event_Log = collision(ID,collision_location,particle_position,energy)
print(Event_Log)

col_log.update({ID:Event_Log})
print(col_log)


# A dictionary is the best container for storing information about an event. I considered using a tuple, but the nature of event tracking lends itself well to dictionary use. The key in a dictionary is immutable, but the values can be changed. This ability to change values is of little consequence in event tracking however. As soon as you track an event, you will move on to the next event, and the "immutability" of the key will protect the values of previous events from alteration. The dictionary provides a convienient way to store the information and tag the information with an event number (key). 




