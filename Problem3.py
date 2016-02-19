# This file defines an event log of a particle collision in a Monte Carlo Radiation transport code.

# Important information tracked in this log includes, particle position, energy, scattering angle,scattering energy,pre-collision direction, pre-collision energy, type of reaction that occurred.

import math

particleID = 101
particle_position = [1,2,3]
collision_location = [0,0,0]

col_log = {}

def collisionlog(particleID,particle_position,collision_position):
   
    distance_prev = 0

    for i in range(0,len(collision_position)):
         dr = collision_position[i] - particle_position[i]
         
         distance_prev = distance_prev +  math.sqrt(dr[i]*dr[i])
    return dr, distance_prev 

dr = collisionlog(particleID,particle_position,collision_location)
print(dr)
    

