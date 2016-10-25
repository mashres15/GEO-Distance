# Maniz Shrestha, mashres15
# Lab 11-1 Update

import math as m

radius = 6372.795
def distanceBetweenPoints(lat1, lon1, lat2, lon2):
  # Compute the distance between two latitude, longitude pairs, 
  # Assume that the earth is a perfect sphere.
    
  # Convert latitude and longitude to spherical coordinates in radians.
  degrees_to_radians = m.pi / 180.0

  # phi = 90 - latitude
  phi1 = (90.0 - lat1) * degrees_to_radians
  phi2 = (90.0 - lat2) * degrees_to_radians

  # theta = longitude
  theta1 = lon1 * degrees_to_radians
  theta2 = lon2 * degrees_to_radians

  # Compute spherical distance from spherical coordinates. For two locations in 
  # spherical coordinates (1, theta, phi) and (1, theta', phi'): 
  #   cosine( arc length ) = sin phi sin phi' cos(theta-theta') + cos phi cos phi'
  #   distance = rho * arc length
  cos = (m.sin(phi1) * m.sin(phi2) * m.cos(theta1 - theta2) + m.cos(phi1) * m.cos(phi2))
  distance = m.acos(cos)

  # Multiply arc by the radius of the earth in the appropriate units to get normalized distance.
  return(distance*radius)

def  main():
    file = input('Enter File name: ')
    
    # input lat, lon pair
    while True:
        try:
            lat1, lon1 = eval(input('Enter lat, long pair separated by a comma (in decimals): '))
            if (lat1 <= 180.0 and lat1 >= -180.0):
                if(lon1 <= 90.0 and lon1 >= -90.0): break
                else: 
                    print ('The value you entered is incorrect, please enter again.')
                    continue
            else: 
                print ('The value you entered is incorrect, please enter again.')
                continue
        except ValueError:
            print ('The value you entered is incorrect, please enter again.')
        except TypeError:
            print ('The value you entered is incorrect, please enter again.')
            
    # input distance
    while True:
        try:
            KM = eval(input('Enter the distance in KM: '))
            if ((KM > 0.0) and (KM < .5 * (2 * m.pi * 6372.795))): break
            else: 
                print ('The value you entered is incorrect, please enter again.')
                continue

        except ValueError:
            print ('The value you entered is incorrect, please enter again.')

    handler = open(file,'r') 
    for line in handler: 
        line = line.strip()
        [lat2,lon2] = line.split(',')
        lat2,lon2 = float(lat2), float(lon2)
        distance = distanceBetweenPoints(lat1, lon1, lat2, lon2)
        if distance < KM: 
            print (lat1, ',', lon1, 'is', distance,'kilometre', 'from', lat2, ',', lon2)
    handler.close()

main()