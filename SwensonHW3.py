import math
import numpy

col_log = {}		# initialize collision log

# run dictionary-filling function three times
for j in [1,2,3]:

    
    dr = []  	   #initialize dr vector to fill later
    direction = []     # initialize direction unit vector to fill later
    collision_location = [1,2,3]
    particle_position = [2,4,5]
    Event_number = j
    Particle_ID = 43
    energy = 2.1
    reaction_code = 102
    atomic_code = 102		# identify target atomicnumber0atomic mass

# this function calculates distance to particle collision
# inputs: collision_location, particle_position
# outputs: distance to collision, unit vector of particle direction

    def collision(Particle_ID,collision_location,particle_position,energy,reaction_code,atomic_code):
        distance_prev = 0

        for i in range(0,len(collision_location)):
            dr.append( collision_location[i] - particle_position[i])
            distance_prev = distance_prev +  math.sqrt(dr[i]*dr[i])
            direction = numpy.divide(dr,distance_prev)
        
        energy = energy*1000000
        Event_Log = {"Particle ID":Particle_ID,"Collision Location":collision_location,"distance to collision": distance_prev,"particle direction":direction,"energy":energy,"Reaction Code": reaction_code,"Target Atom Composition Code":atomic_code}
        return Event_Log

    Event_Log = collision(Particle_ID,collision_location,particle_position,energy,reaction_code,atomic_code)
    
    col_log.update({Event_number:Event_Log})

print(col_log)


# A dictionary is the best container for storing information about an event. I considered using a tuple, but the nature of event tracking lends itself well to dictionary use. The key in a dictionary is immutable, but the values can be changed. This ability to change values is of little consequence in event tracking however. As soon as you track an event, you will move on to the next event, and the "immutability" of the key will protect the values of previous events from alteration. The dictionary provides a convienient way to store the information and tag the information with an event number (key). 



# I used a dictionary to store the events as well, I liked the fact that every event will have a key attached to it. This makes pully data about specific events very easy. I also considered using a list here. I ulitimately settled on a dictionary in case particle histories were generated out of realistic order. A list will simply reflect the order the values were generated in. A dictionary will have no order however, will have a key attached to the value indicating the place in sequence where the event belongs.

## This code determines energy change between the 5th and 6th event

 
# event5 = col_log['5']
# event6 = col_log['6']

# energy5 = event5['energy']
# energy6 = event6['energy']

# dE = energy6 - energy5


## This code determines the distance between the 7th and 8th event

# event7 = col_log['7']
# event8 = col_log['8']

# position7 = event7['collision_location']
# position8 = event8['collision_location']

#    def distance(position1,position2):
#        for i in range(0,len(collision_location)):
#            dr.append(position2[i] - position1[i])
#            distance = distance + math.sqrt(dr[i]*dr[i])
#        return distance


## This example code determines which event is closer aligned to the z-axis

direction9 = [1,1,1]
valdirect9 = math.sqrt(numpy.sum(numpy.square(direction9)))
unit_direct9 = numpy.divide(direction9,valdirect9)

direction4 = [1,1,1]
valdirect4 = math.sqrt(numpy.sum(numpy.square(direction4)))
unit_direct4 = numpy.divide(direction4,valdirect4)

z_axis = [0,0,1]
def alignment(unitdirect1,unitdirect2):
    zdot1 = numpy.dot(z_axis,unitdirect1)
    zdot2 = numpy.dot(z_axis,unitdirect2)
    if zdot1 > zdot2:
         x = "The first argument is more aligned with the z-axis"
    elif zdot1 == zdot2:
         x = "The first and second arguments are equally aligned with the z-axis"
    else:
         x = "The second argument is more aligned with the z-axis"

    return x
x = alignment(unit_direct4,unit_direct9)

print(x)

