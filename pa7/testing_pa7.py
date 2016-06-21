##testing for pa7

import rd_debate_tweets as debate

f = 'data/during.csv'
tweets = debate.read_csv(f)

##Task1
#num_mentions = debate.count_num_mentions(tweets)

#debate.plot_num_mentions(num_mentions, 
    #save_to = 'output/bar_num_mentions.png')

top_names = ['Donald Trump',
 'Carly Fiorina',
 'Jeb Bush',
 'Ben Carson',
 'Ted Cruz',
 'Rand Paul',
 'Marco Rubio']

x = debate.get_num_mentions_per_time(tweets, debate.DEBATE_START, debate.DEBATE_END, 
    600, top_names, percent = True)
