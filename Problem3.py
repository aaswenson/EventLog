import math

collision_location = [1,2,3]
particle_position = [2,4,5]
dr=[]
def collision(collision_location,particle_position):
    distance_prev = 0
    for i in range(0,len(collision_location)):
        dr.append( collision_location[i] - particle_position[i])
        distance_prev = distance_prev +  math.sqrt(dr[i]*dr[i])
    return distance_prev


dr  = collision(collision_location,particle_position)
print(dr)
#print(distance)
