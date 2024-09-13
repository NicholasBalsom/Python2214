# pip install geopy

import math
import geopy.distance

ranges = []
angles_vertical = []
def max_range(projectile_velocity):
    for number in range(45, 85):
        projectile_velocity_vertical = projectile_velocity * math.sin(math.radians(number))
        time = ((-projectile_velocity_vertical) - (projectile_velocity_vertical )) / (-9.81)
        horizontal_velocity = round(math.cos(math.radians(number)) * projectile_velocity, 2)
        horizontal_distance = round(horizontal_velocity* time, 2)
        ranges.append(horizontal_distance)
        angles_vertical.append(math.radians(number))
    return max(ranges)
       
def workings(ranges, distance, angles_vertical):
    for x in ranges:
        if x == distance:
            print("EHHEHEHE")

def distance_ab(coords_1, coords_2):
        # work in progress
    coords_1 = (48.956895, -57.918473)
    coords_2 = (48.956675, -57.918593)
    distance = geopy.distance.geodesic(coords_1, coords_2).m
    print(round(geopy.distance.geodesic(coords_1, coords_2).m))
    return distance

def earth_radius_get(alt1,alt2):
    geopy.distance.EARTH_RADIUS(((alt1+alt2)/2)/1000 + 6,378.137)
  
if __name__ == "__main__":
    projectile_velocity = int(input("Enter the velocity of projectile: "))
    coords_1 = float(input(": "))
    coords_2 = float(input(": "))
    distance_ab(coords_1, coords_2)
    
    max_range(projectile_velocity)
    print(max_range(ranges))
    # vertex_of_flight(projectile_velocity, ranges)