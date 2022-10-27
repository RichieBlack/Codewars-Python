"""
@File    : Holiday VI - Shark Pontoon.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:26

I have been learning Python since August 2022.
"""


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    time_to_alive = pontoon_distance / you_speed
    time_to_die = shark_distance / shark_speed

    if time_to_alive < time_to_die:
        return "Alive!"
    elif dolphin == True and time_to_alive < (time_to_die * 2):
        return "Alive!"
    else:
        return "Shark Bait!"


"""Best practices
-----------------

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2
        
    shark_eat_time = shark_distance / shark_speed
    you_safe_time = pontoon_distance / you_speed
    
    return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"

-----------------

def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    # Using the boolean to be used as 1 or 0 when multiplying
    return "Alive!" if (pontoonDistance / youSpeed) < sharkDistance / (
                sharkSpeed - (sharkSpeed * 0.5 * dolphin)) else "Shark Bait!"
-----------------

def shark(d1, d2, v1, v2, x):
    return "Alive!" if d1 / v1 < d2 / v2 * (x + 1) else "Shark Bait!"

-----------------

shark = lambda s, h ,a ,r , k: ["Shark Bait!", "Alive!"][h / r * (k + 1) > s / a]

-----------------
"""

# https://www.codewars.com/kata/reviews/5e428170a7d80d0001d176a2/groups/63342c592684a20001f10338
