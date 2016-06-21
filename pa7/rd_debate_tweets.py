import sys
import csv
import os.path
import operator
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np


# Dictionary of the Candidate information (as described in assignment writeup)
CANDIDATE_NAMES = {"bush":      "Jeb Bush",
                   "carson":    "Ben Carson",
                   "christie":  "Chris Christie",
                   "cruz":      "Ted Cruz",
                   "fiorina":   "Carly Fiorina",
                   "gilmore":   "Jim Gilmore",
                   "graham":    "Lindsey Graham",
                   "huckabee":  "Mike Huckabee",
                   "jindal":    "Bobby Jindal",
                   "kasich":    "John Kasich", 
                   "pataki":    "George Pataki",
                   "paul":      "Rand Paul",
                   "perry":     "Rick Perry", 
                   "rubio":     "Marco Rubio", 
                   "santorum":  "Rick Santorum", 
                   "trump":     "Donald Trump", 
                   "walker":    "Scott Walker",
                   "chafee":    "Lincoln Chafee",
                   "clinton":   "Hillary Clinton",
                   "omalley":   "Martin O'Malley",
                   "sanders":   "Bernie Sanders",
                   "webb":      "Jim Webb"}

GOP_CANDIDATES = ['bush', 'carson', 'christie', 'cruz', 'fiorina', 'gilmore', 'graham', 'huckabee', 
                  'jindal', 'kasich', 'pataki', 'paul', 'perry', 'rubio', 'santorum', 'trump', 'walker']
#List of GOP candidates by "code" name

DEM_CANDIDATES = ['chafee', 'clinton', 'omalley', 'sanders', 'webb']
#List of DEM candidates by "code" name

ALL_CANDIDATES = GOP_CANDIDATES + DEM_CANDIDATES
#List of ALL candidates by "code" name. Combines the two lists


# Size of the figures (these are the values you should pass
# in parameter "figsize" of matplotlib's "figure" function)
# Note: For task 4, use FIGWIDTH*2
FIGWIDTH = 12
FIGHEIGHT = 8


# Start and end time (in seconds) of the debate
DEBATE_START = 86400
  #Time = 0 is 24 hours prior to start of the debate
DEBATE_END = 97200
# Maximum time (in seconds) of the dataset
MAX_TIME = 183600
  #Total time that tweets were collected. Time 0 is 24 hours prior to 
  #start of the debate. MAX_TIME is total time, ending 24 hours
    #after the end of the debate (51 total hours)


# This function generates colors that can be passed to matplotlib functions
# that accept a list of colors. The function takes one parameter: the number
# of colors to generate. Using this function should result in the same colors
# shown in the assignment writeup.
def get_nice_colors(n_colors):
    return cm.Accent( [1 - (i/n_colors) for i in range(n_colors)] )


################################################
#
# Your functions go here
#
# Call your functions from the __main__ block
#



def read_csv(filename):
    '''
    Returns a list of dictionaries for all the rows/tweeets in a csv file.
    Keys are the desriptors (seconds, candidates, etc)
    Values are those specific value for each row/tweet
    
    Inputs: 
        String: file name

    Returns:
        List of dictionaries
    '''

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        tweets = []

        for row in reader:
            tweets.append(row)

        return tweets

    # will only get here if the open failed.
    return None


def count_num_mentions(tweets):

    #total_tweets = len(tweets) 

    num_mentions = {}

    for tweet in tweets:
        candidate_mentions = tweet['candidates'] #candidate_mentions is a string
        all_mentions = candidate_mentions.split('|')
        num_candidates = len(all_mentions)

        if num_candidates not in num_mentions:
            num_mentions[num_candidates] = 1
        else:
            num_mentions[num_candidates] += 1

    return num_mentions


def plot_num_mentions(num_mentions, save_to = None):

    x_numbers = list(num_mentions.keys())
    y_totals = list(num_mentions.values())
    N = len(x_numbers)

    bar_width = 0.5
    pos = np.arange(N)

    fig, ax = plt.subplots(figsize = (FIGWIDTH, FIGHEIGHT))

    bars = ax.bar(pos, y_totals, bar_width, color='b')

    ax.set_yscale('log', nonposy = 'clip')
    ax.set_ylabel('Number of Tweets')
    ax.set_xlabel('Number of Mentions')
    ax.set_title('Number of Candidate Mentions per Tweet')
    ax.set_xticks(pos + (bar_width/2))
    ax.set_xticklabels(x_numbers)

    axes = plt.gca()
    axes.set_xlim(0, N)
    #StackOverflow: http://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib

    if save_to is None:
        plt.show()
    else:
        fig.savefig(save_to) #directory and filename

def get_pair_mentions(tweets, top_mentions):
    '''
    Inputs:
        List of dictionaries
        top_metnions is an integer to mean the top number of mentions
            you want to look at
    '''
    pairs = {}
    for tweet in tweets:
        candidate_mentions = tweet['candidates'] #candidate_mentions is a string
        all_mentions = candidate_mentions.split('|') #list
        num_candidates = len(all_mentions)
        if num_candidates == 2:
            pair = (str(CANDIDATE_NAMES[all_mentions[0]]) + '\n' +
                str(CANDIDATE_NAMES[all_mentions[1]]))
            if pair not in pairs:
                pairs[pair] = 1
            else:
                pairs[pair] += 1
        elif num_candidates > 2:
            remaining_candidates = all_mentions[:]
            for base_candidate in all_mentions:
                for candidate in remaining_candidates:
                    if candidate != base_candidate and base_candidate in remaining_candidates: 
                        pair = (str(CANDIDATE_NAMES[base_candidate]) + '\n' +
                            str(CANDIDATE_NAMES[candidate]))
                        if pair not in pairs:
                            pairs[pair] = 1
                        else:
                            pairs[pair] += 1
                remaining_candidates.remove(base_candidate)

    top_ten = {}
    num_mentions = list(pairs.values())
    num_mentions.sort(reverse = True)
    top_ten_mentions = num_mentions[0:top_mentions]
    #pairs is a dictionary with keys as strings of candidate pairs and values
        #as the number of mentions
    for candidate_pair in pairs:
        current_num_mentions = pairs[candidate_pair]
        if current_num_mentions in top_ten_mentions:
            top_ten[candidate_pair] = current_num_mentions

    return top_ten

def plot_pair_mentions(top_ten, save_to = None):
    '''
    Inputs:
        Dictionary with keys as pairs, values as number of mentions
    '''
    x_labels = list(top_ten.keys())
    y_totals = list(top_ten.values())
    N = len(x_labels)

    bar_width = 0.5
    pos = np.arange(N)

    fig, ax = plt.subplots(figsize = (FIGWIDTH, FIGHEIGHT))

    bars = ax.bar(pos, y_totals, bar_width, color='b')

    ax.set_ylabel('Number of Tweets')
    ax.set_title('Pairs of Candidates Most Frequenty Mentioned Together')
    ax.set_xticks(pos + (bar_width/2))
    plt.xticks(fontsize = 8)
    ax.set_xticklabels(x_labels, rotation = 60)

    axes = plt.gca()
    axes.set_xlim(0, N)
    #StackOverflow: http://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib

    if save_to is None:
        plt.show()
    else:
        fig.savefig(save_to) #directory and filename


def get_percent_mentions(tweets, candidate_list, percent_threshold):
    '''
    Inputs:
        tweets: List of dictionaries
        candidates: list of candidates to work with
        percent: top percent to include
    '''

    total_mentions = 0
    mentions = {}
    for tweet in tweets:
        candidate_mentions = tweet['candidates'] #candidate_mentions is a string
        all_mentions = candidate_mentions.split('|')
            #generates a list with each candidate mentioned as an element
        for candidate in all_mentions:
            if candidate in candidate_list:
                total_mentions += 1
                mentions[candidate] = mentions.get(candidate, 0) + 1

    mentions_percent = {}
    for current_candidate in mentions:
        percent = ((mentions[current_candidate])/total_mentions)*100
        if percent < percent_threshold:
            mentions_percent["Other"] = mentions_percent.get("Other", 0) + percent
        else:
            name = CANDIDATE_NAMES[current_candidate]
            mentions_percent[name] = percent

    return mentions_percent

def get_colormap(N):
    '''
    http://stackoverflow.com/questions/14720331/how-to-generate-random-colors-in-matplotlib
    Returns a function that maps each index in 0, 1, ... N-1 to a distinct 
    RGB color.
    '''

    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cm.ScalarMappable(norm=color_norm, cmap='jet') 

    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)

    return map_index_to_rgb_color

def pie_plot_percent_mentions(mentions_percent, save_to = None):
    '''
    Inputs:
        Dictionary with keys as pairs, values as percent of mentions
    '''

    other = mentions_percent.pop("Other")
    swapped = {v:k for k, v in mentions_percent.items()}

    sizes = sorted(swapped)
    sizes.reverse()
    labels = [swapped[current_percent] for current_percent in sizes]

    sizes.append(other)
    labels.append("Other")
    N = len(labels)

    color_map = get_colormap(N-1)
    colors = []
    for i in range(N-1):
        col = color_map(i)
        colors.append(col)
    colors.append("white")
    print(colors)

    plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    fig = plt.figure()
    ax = fig.gca()

    plt.show()


def get_num_mentions_per_time(tweets, relative_start_time, relative_end_time, 
    per_time, top_names = None, percent = False):

    total_time = relative_end_time - relative_start_time 

    time_increments = []
    for i in range(0, total_time + per_time, per_time):
        #total_time + per_time to account for candidates being mentioned at 
        #exactly time 0 and at exactly the end time
        time_in_mins = i/60
        time_increments.append(time_in_mins)

    print("time_increments", time_increments)

    total_mentions = {}
    mentions = {}
    for tweet in tweets:
        candidate_mentions = tweet['candidates']
        all_mentions = candidate_mentions.split('|')
        time_seconds = float(tweet['seconds'])
        time_seconds_normalized = time_seconds - relative_start_time
            #relative time is either the absolute start time or the debate start time
        current_time_bin = int(time_seconds_normalized/per_time)
        time_mentioned = time_increments[current_time_bin]

        for candidate in all_mentions:
            name = CANDIDATE_NAMES[candidate]
            if top_names:
                if name in top_names:
                    total_mentions[time_mentioned] = total_mentions.get(time_mentioned, 0) + 1
                    if name not in mentions:
                        mentions[name] = {time_mentioned:1}
                    else:
                        if time_mentioned not in mentions[name]:
                            mentions[name][time_mentioned] = 1
                        else:
                            mentions[name][time_mentioned] += 1
            else:
                total_mentions[time_mentioned] = total_mentions.get(time_mentioned, 0) + 1
                if name not in mentions:
                    mentions[name] = {time_mentioned:1}
                else:
                    if time_mentioned not in mentions[name]:
                        mentions[name][time_mentioned] = 1
                    else:
                        mentions[name][time_mentioned] += 1

    if percent:
        mentions_percent = {}
        for current_candidate in mentions:
            times_mentioned = mentions[current_candidate]
            mentions_percent[current_candidate] = {}
            for time in times_mentioned:
                total_num_mentions = total_mentions[time]
                candidate_num_mentions = times_mentioned[time]
                percent = (candidate_num_mentions/total_num_mentions)*100
                mentions_percent[current_candidate][time] = percent
        return mentions_percent
    
    else:
        return mentions



def plot_mentions_per_time(mentions, title):

    
    x_labels_raw = list(mentions.values())
    N = len(x_labels_raw)

    for candidate in mentions:
        times = mentions[candidate]
        xs = sorted(times)
        ys = []
        for x in xs:
            y = times[x]
            ys.append(y)

        line = plt.plot(xs, ys, label = candidate)

    plt.xlabel("Time (mins)")
    plt.ylabel("Number of Mentions")
    plt.title(title)
    


    plt.legend()
    plt.show()


def stackplot_percent_mentions_per_time(mentions_percent, candidate_list, title):

    num_candidates = len(candidate_list)
    all_ys = [0]*num_candidates
    
    for i, candidate in enumerate(candidate_list):
        times = mentions_percent[candidate]
        xs = sorted(times)
        ys = []
        for x in xs:
            y = times[x]
            ys.append(y)
        all_ys[(num_candidates - 1) - i] = ys
            #num_candidates - 1 to account for lists starting at index = 0

    stacked_ys = np.row_stack(tuple(all_ys))

    color_map = get_colormap(num_candidates-1)
    colors = []
    for i in range(num_candidates-1):
        col = color_map(i)
        colors.append(col)
    colors.append("white")
    print(colors)
    legend_colors = [mpatches.Patch(edgecolor = 'black', facecolor = color) for color in colors[::-1]]

    params = {'legend.fontsize': 8,'legend.linewidth': 2}
    plt.rcParams.update(params)
    fig, ax = plt.subplots()
    ax.stackplot(xs, stacked_ys, colors = colors)
    #ax.set_xticks(pos + (bar_width/2))
    plt.xticks(fontsize = 8)
    ax.set_xticklabels(x_labels, rotation = 60)
    plt.legend(legend_colors, candidate_list)
    plt.xlabel("Time (mins)")
    plt.ylabel("Percent of Tweets")
    plt.title(title)
    plt.show()





################################################


#Donald Trump, Carly Fiorina, Jeb Bush, Ben Carson, Ted Cruz, Rand Paul, and Marco Rubio