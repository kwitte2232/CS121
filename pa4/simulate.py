import json
import math
import os
import random
import sys
import time

#import Queue



import random
import queue
import heapq

class Voter_Queue(object):

    def __init__(self, num_voters):
        self.voter_q = queue.PriorityQueue()
        self._num_voters = num_voters
        self._max_capacity = self.maximum_voters() 
        #self.length = self.length()

    @property
    def num_voters(self):
        return self._num_voters   

    @property
    def max_capacity(self):
        return self._max_capacity 

    def length(self):
        return len(self.voter_q.queue)

    def maximum_voters(self):
        return self._num_voters

    def is_empty(self):
        return len(self.voter_q.queue) == 0

    def voter_sample(self):
        return sorted(self.voter_q.queue)

    def __repr__(self):
        return "queue: {}, ".format(self.voter_q.queue)



class Voter(object):
    VOTER_ID = 0

    def __init__(self, arrival, time_to_vote):
        Voter.VOTER_ID += 1
        self.ID = Voter.VOTER_ID
        self._arrival = arrival
        self._time_to_vote = time_to_vote
        self.enter_time = None

    @property
    def arrival(self):
        return self._arrival

    @property
    def time_to_vote(self):
        return self._time_to_vote

    def wait_time(self):
        if self.enter_time is None:
            return 0
        else:
            return self.enter_time - self._arrival

    def departure(self):
        if self.enter_time is None:
            return None
        else:
            return self.enter_time + self._time_to_vote + self.wait_time()

    def __repr__(self):
        return "ID: {}, arrival: {}, time_to_vote: {}, enter_time: {}".format(self.ID,
            self._arrival, self._time_to_vote, self.enter_time)


class Precinct(object):

    def __init__(self, num_booths):
        self.pQ = queue.PriorityQueue(maxsize = num_booths)
        self.num_booths = num_booths
        self.voters = []

    def add_voter(self, item):
        assert not self.pQ.full()
        self.pQ.put(item)
        self.voters += [item]

    def rem_voter(self):
        assert not self.pQ.empty()
        voter = self.pQ.get()
        self.pQ.task_done()
        self.voters.remove(voter)

    def is_empty(self):
        return len(self.pQ.queue) == 0

    def occupants(self):
        return sorted(self.pQ.queue)

    def next_departure(self):
        (x, y) = sorted(self.voters)[0]
        return (x, y)

    def full(self):
        return self.pQ.full()

    def __repr__(self):
        return str(self.voters)


def generate_voter_sample(minutes_open, num_voters, voting_mean):
    
    #minutes_open = hours_open*60
    lambd = (num_voters)/(minutes_open)
        #lambd is the arrival rate

    time = 0

    all_voters = Voter_Queue(num_voters)
    while time < minutes_open:
        if all_voters.length() < num_voters:
            random_time_generator = random.expovariate(lambd)
            arrival_time = random_time_generator + time
            if arrival_time >= minutes_open:
                break
            else:
                #print(arrival_time) 
                time_to_vote = random.expovariate(1/voting_mean)
                curr_voter = Voter(arrival_time, time_to_vote)
                voter_data = (curr_voter.arrival, curr_voter)
                all_voters.voter_q._put(voter_data)
                #print(all_voters.length())
                time = curr_voter.arrival
        else:
            break

    return all_voters

def simulate_election_day(params):
    '''
    Simulate a single election day.

    Input:
        params: configuration to simulate

    Output:
        True if the specified configruation was suffient to meet the
        threshold for one simulated election day, false otherwise.
   
    '''
    # Creating voter queue
    minutes_open = params["hours_open"] * 60  # will be params["hours_open"]
    num_voters = params["num_voters"] # will be params["num_voters"]
    voting_mean = params["voting_mean"] # will be params["voting_mean"]
    num_booths = params["number_of_booths"]
    threshold = params["threshold"]
    target_waiting_time = params["target_waiting_time"]

    all_voters = generate_voter_sample(minutes_open, num_voters, voting_mean)
    #initial_voter = [list(voter) for voter in all_voters.voter_sample())]
    #print(all_voters)
    total_voters = all_voters.length()
    print(total_voters)
    time = 0
    initial_voter = all_voters.voter_q.queue[0]
    print("initial voter", initial_voter)
    start_time = initial_voter[0]
    print("start_time", start_time)
        # not sure if this is the best way to do this
    time = time + start_time

    precinct = Precinct(num_booths)
    # Our return values: the list of customers that have been
    # served, and the list of customers that haven't been served
    #voted = []
    #did_not_vote = []
    #wait_list = []
    #print("time")
    wait = 0
    #while time <= minutes_open:
    while all_voters.length() > 0:
        #print('time', time)

        if all_voters.is_empty() is True and precinct.is_empty() is True:
            break
        
        elif precinct.is_empty() is True:
            #print('precinct is empty')
            get_voter = all_voters.voter_q._get()
            voter_info = get_voter[1]
            voter_info.enter_time = time
            voter_to_add = (voter_info.departure(), voter_info)
            precinct.add_voter(voter_to_add)
            #next_departure = precinct.pQ.queue[0][1].departure()
            next_departure = precinct.pQ.queue[0][0]
            #print("Next departure", next_departure)
            if all_voters.is_empty() is True:
                time = next_departure
            else:
                next_arrival = all_voters.voter_q.queue[0][1].arrival
                
                if next_departure < next_arrival:
                    precinct.rem_voter()
                time = next_arrival

        elif (precinct.is_empty() is not True and 
                precinct.full() is not True and 
                all_voters.is_empty() is not True):
            #print("entered")
            next_depart = 0
            while precinct.is_empty() is not True:
                #next_departure = precinct.pQ.queue[0][1].departure()
                next_depart = precinct.pQ.queue[0][0]
                next_arrival = all_voters.voter_q.queue[0][1].arrival
                if next_depart < next_arrival:
                    precinct.rem_voter()
                else:
                    time = next_arrival
                    break
            get_voter = all_voters.voter_q._get()
            voter_info = get_voter[1]
            #print(voter_info)
            voter_info.enter_time = next_depart
            #print(voter_info.wait_time())
            if voter_info.wait_time() > target_waiting_time:
                wait = wait + 1
                #print(wait)
            voter_to_add = (voter_info.departure(), voter_info)
            precinct.add_voter(voter_to_add)

        elif (all_voters.is_empty() is True and 
                precinct.is_empty() is not True):
            while precinct.is_empty() is not True:
                precinct.rem_voter()
            break

        elif precinct.full() is True:
            #print("precinct is full")
            next_departure = precinct.pQ.queue[0][0]
            #get_voter = all_voters.voter_q._get()
            #voter_info = get_voter[1]
            #voter_info.enter_time = next_departure
            precinct.rem_voter()
            time = next_departure
            #print(time)
            #print("length of voter queue", all_voters.length())

        #if time > minutes_open:
            #print("done with while loop")
      
    percent_waited = (wait/total_voters)*100
    #print(percent_waited)
    #print(threshold)
    if percent_waited > threshold:
        return False
    else:
        return True
        #if precinct.pQ.full() is True:


    #print(precinct)




def run_trials(params):
    '''
    #Run trials on the configuration specified by the parameters file.

    #Inputs: 
        #params: simulation parameters
    
    #Result:
        #Likelihood that the given number of machines is sufficient for
        #the specified configuration.
    #'''
    count = 0.0
    for t in range(params["num_trials"]):
        if simulate_election_day(params):
            count = count + 1.0
    
    return count/params["num_trials"]


def setup_params(params_filename, num_booths):
    '''
    #Set up the paramaters data structure and set the
    #seed for the random number generator

    #Inputs:
        #params_filename: name of the simulation parameters file
        #num_booths: the number of booths to simulate
    '''
    if not os.path.isfile(params_filename):
        print("Error: cannot open parameters file " + params_filename)
        sys.exit(0)

    if num_booths <= 0:
        print("Error: the number of voting booths must be positive")
        sys.exit(0)

    params = json.load(open(params_filename))
    params["number_of_booths"] = num_booths

    if "seed" in params:
        seed = params["seed"]
    else:
        seed = int(time.time())
        params["seed"] = seed

    random.seed(seed)

    return params


if __name__ == "__main__":
    usage_str = "usage: python {0} [parameters filename] [number of voting booths]".format(sys.argv[0])
    # process arguments
    num_booths = 1
    params_filename = "params.json"
    if len(sys.argv) == 2:
        params_filename = sys.argv[1]
    elif len(sys.argv) == 3:
        params_filename = sys.argv[1]
        num_booths = int(sys.argv[2])
    elif len(sys.argv) > 3:
        print(usage_str)
        sys.exit(0)

    params = setup_params(params_filename, num_booths)
    rv = run_trials(params)

    # print the parameters and the result
    for key in sorted(params):
        print(key + ": " + str(params[key]))
    print()
    print("result: " + str(rv))



        



            
            
            

    
