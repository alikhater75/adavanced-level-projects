

from ps1_partition import get_partitions
import time


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    transported=[]
    cows_copy=cows.copy()
    while sum(list(cows_copy.values())) !=0 :
     copy=sorted(list(cows_copy.values()),reverse=True)   
     trip=[] 
     total=0
     for w in copy :
        if total+w<=limit:
            trip.append(list(cows_copy.keys())[list(cows_copy.values()).index(w)])
            total+=w
            cows_copy.pop(list(cows_copy.keys())[list(cows_copy.values()).index(w)])
     transported.append(trip)    
    return transported   
    


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    solution=[]
    fitted,first=False,True
    for i in (get_partitions(cows)) :

         for j in i :
            if sum(cows[a] for a in j) > limit :
                fitted=False
                break  
            else:
             fitted=True
         if fitted :    
          if len(i)<len(solution) or first :
            solution=i
            first=False
    return  solution   
##


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    greedyStart = time.time()
    print(greedy_cow_transport(cows, limit))
    greedyStop = time.time()

    bruteStart = time.time()
    print(brute_force_cow_transport(cows, limit))
    bruteStop = time.time()

    print((greedyStop - greedyStart), (bruteStop - bruteStart))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#cows={'Milkshake': 40, 'Miss Bella': 25, 'MooMoo': 50, 'Boo': 20, 'Lotus': 40, 'Horns': 25}
#limit=100
#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))


compare_cow_transport_algorithms()