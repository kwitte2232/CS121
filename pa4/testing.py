

import simulate
#import priority_queue

#params = simulate.setup_params('data/params2.json', 8)
#Expects True

#params = simulate.setup_params('data/params2.json', 6)
#Expects False

#params = simulate.setup_params('data/params0.json', 1)
#Expects False

params = simulate.setup_params('data/params0.json', 2)
#Expects False

s = simulate.simulate_election_day(params)
print(s)