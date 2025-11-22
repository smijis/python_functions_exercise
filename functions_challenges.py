#############################################################################################################
# Challenge 1 -> A Function to get a float from the user

def get_float(prompt_string: str):
    """A function that gets a float from the user and returns it.

    Arguments:
        - prompt_string: A string that will be shown to the user when they are
          prompted to input the number.

    Returns:
        - A float converted from the user's input
    """
    num = input(prompt_string)
    return float(num)

# print (get_float("Enter a number: "))    
    


#############################################################################################################
# Challenge 2 -> A Function to convert miles to km
# NOTE: 1 mile is 1.60934km

def miles_to_km(distance_in_miles: float):
    """A function to convert distance from miles to km

    Arguments:
        - distance_in_miles: A float representing a distance in miles

    Returns
        - a float representing the distance in kilometers
    """
    distance_in_km = distance_in_miles * 1.60934
    return float(distance_in_km)

#print (miles_to_km (8))

# def miles_to_km(prompt_miles):
#     miles = float(input(prompt_miles))
#     km = miles * 1.60934
#     return float(km)
# print (miles_to_km ("Enter distance in miles: "))



#############################################################################################################
# Challenge 3 -> A function to calculate the total distance run in a relay

def relay_distance(distance_per_runner: float, number_of_runners: float):
    """A function to calculate the total distance run by a team of runners
    in a relay race.

    Arguments:
        - distance_per_runner: a float representing the amount each runner runs
            (in a relay race, all runners run the same distance!)
        - number_of_runners: a float representing the number of runners in a team

    Returns:
        - A float representing the total distance run.
    """
    total_distance = distance_per_runner * number_of_runners
    return total_distance

#print (relay_distance (5, 4))


#############################################################################################################
# Challenge 4 (extra tricky)
#
# See if you can write a single function that USES all three of the functions
# you wrote for the above challenges.
def relay_distance_input():
    """A function that asks for a user's inputs for the number of runners and the distance each runner
    will run in a relay race in miles, and then calculate and return the total distance (in km) ran by
    all the runners.

    Arguments: None
        
    Returns:
        - A float representing the total distance run.
    """
    
    distance_per_runner = get_float("Enter the distance each runner runs (in miles): ")
    number_of_runners = get_float("Enter the number of runners: ")
    total_distance = relay_distance(distance_per_runner, number_of_runners)
    total_distance_km = miles_to_km(total_distance)
    return float(total_distance_km)

print (relay_distance_input())
    