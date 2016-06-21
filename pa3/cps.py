# CS121 A'15: Current Population Survey (CPS) 
#
# Functions for mining CPS data 
#
# Kristen Witte

from pa3_helpers import read_csv, plot_histogram
import statistics

# Constants 
HID = "h_id" 
AGE = "age"
GENDER = "gender" 
RACE = "race" 
ETHNIC = "ethnicity" 
STATUS = "employment_status"
HRWKE = "hours_worked_per_week" 
EARNWKE = "earnings_per_week" 

FULLTIME_MIN_WORKHRS = 35

COLUMN_WIDTH = 18
COLUMN_SEP = "|"

MEAN_INDEX = 0
MEDIAN_INDEX = 1
MIN_INDEX = 2
MAX_INDEX = 3

def make_input_dict(filename):
    '''
    Builds an input dictionary that contains the input Morg data 
    and the code files

    Inputs:
        filename: csv file
            the morg_data file name

        An example of input_dict is shown below: 
        {'morg':'data/morg_d14_mini.csv',
         'gender_codes':'data/gender_code.csv',
         'race_codes':'data/race_code.csv',
         'ethnic_codes':'data/ethnic_code.csv',
         'employment_codes':'data/employment_status_code.csv'}


    Returns:
        morg_input_dict 
    '''
    morg_input_dict = {'morg': ' ',
         'gender_codes':'data/gender_code.csv',
         'race_codes':'data/race_code.csv',
         'ethnic_codes':'data/ethnic_code.csv',
         'employment_codes':'data/employment_status_code.csv'}

    morg_input_dict['morg'] = filename

    return morg_input_dict


def build_morg_dict(input_dict):
    '''
    Build a dictionary that holds a set of CPS data 

    Inputs:
        input_dict: dict

        An example of input_dict is shown below: 
        {'morg':'data/morg_d14_mini.csv',
         'gender_codes':'data/gender_code.csv',
         'race_codes':'data/race_code.csv',
         'ethnic_codes':'data/ethnic_code.csv',
         'employment_codes':'data/employment_status_code.csv'}


    Returns:
        ID_dict: dictionary with HIDs as keys and values as a dictionary
        of their information, with keys as general terms and values as 
        the individuals information
    '''

    HID = "h_id" 
    AGE = "age"
    GENDER = "gender" 
    RACE = "race" 
    ETHNIC = "ethnicity" 
    STATUS = "employment_status"
    HRWKE = "hours_worked_per_week" 
    EARNWKE = "earnings_per_week" 

    sub_dict = make_subdict[input_dict]

    inds = sub_dict['data']

    categories = [HID, AGE, GENDER, RACE, ETHNIC, STATUS,
        HRWKE, EARNWKE]

    l = len(categories)
    ID_dict = {} 
    for i in inds:
        hid = i[0]
        info = {}
        for c in range(1,l):
            info[categories[c]] = i[c]

        descriptions = list(info.keys())
    
        for desc in descriptions:
            code = info[desc]
            if desc == STATUS or desc == ETHNIC or desc == RACE or desc == GENDER:
                curr_search = sub_dict[desc] 
                if code == '':
                    code = '0'
                for elem in curr_search:
                    cd = elem[0]
                    if code == cd:
                        str_code = elem[1]
                        info[desc] = str_code

            elif desc == AGE or desc == HRWKE:
                if code != '':
                    str_to_int = int(code)
                    info[desc] = str_to_int 

            elif desc == EARNWKE:
                if code != '':
                    earn = float(code)
                    info[desc] = earn
                else:
                    info[desc] = code

        ID_dict[hid] = info
 
    return ID_dict

def create_histogram(morg_dict, var_of_interest, num_buckets, 
                     min_val, max_val):
    '''
    Create a histogram using a list 

    Inputs:
        morg_dict: a MORG dictionary 
        var_of_interest: string (e.g., HRWKE or EARNWKE)
        num_buckets: number of buckets in the histogram
        min_val: the minimal value (lower bound) of the histogram
        max_val: the maximal value (upper bound) of the histogram 

    Returns:
        freq: list that represents a histogram 
    '''

    freq = [0]*num_buckets
    if num_buckets == 0:
        return freq
    else:
        diff = max_val - min_val
        step_size = diff/num_buckets

        step_dict = {}
        step_list = []

        top = min_val
        for s in range(num_buckets):
            r = []
            bottom = top
            top = top + step_size
            r.append(bottom)
            r.append(top)
            step_list.append(r)

        l = len(step_list)
        for i, step in enumerate(step_list):
            bot_r = step[0]
            top_r = step[1]
            for hid in morg_dict:
                info = morg_dict[hid]
                work = info[STATUS]
                if work == "Working":
                    ft = info[HRWKE]
                    if ft >= 35:
                        value = info[var_of_interest]
                        if i < l-1:
                            if value >= bot_r and value < top_r:
                                freq[i] = freq[i] + 1
                        elif i == l-1:
                            if value >= top_r:
                                freq[i] = freq[i] + 1

    return freq 

def make_subdict(input_dict):
    '''
    Builds a dictionary that contains the input Morg data 
    and the code files as values with keys of the provided Constants
    for each attribute (GENDER, RACE, etc)

    Inputs:
        input_dict: dict

        An example of input_dict is shown below: 
        {'morg':'data/morg_d14_mini.csv',
         'gender_codes':'data/gender_code.csv',
         'race_codes':'data/race_code.csv',
         'ethnic_codes':'data/ethnic_code.csv',
         'employment_codes':'data/employment_status_code.csv'}


    Returns:
        sub_dict: dict 
    '''

    data_csv = input_dict['morg']
    gen_csv = input_dict['gender_codes']
    rc_csv = input_dict['race_codes']
    ec_csv = input_dict['ethnic_codes']
    emc_csv = input_dict['employment_codes']

    csvs = [data_csv, gen_csv, rc_csv, ec_csv, emc_csv]
    names = ['data', GENDER, RACE, ETHNIC, STATUS]

    n = len(csvs)

    sub_dict = {}

    for n in range(n):
        f = csvs[n]
        read = read_csv(f, False)
        sub_dict[names[n]] = read

    return sub_dict

def calculate_unemployment_rates(filename_list, age_range, var_of_interest):
    '''
    Output a nicely formatted table for the unemployment rates 
    for the specified age_rage, 
    further broken down by different categories in var_of_interest
    for the data specified in each file in filename_list 

    Inputs:
        filename_list: a list of MORG dataset file names
        age_rage: a tuple consisted of two integers
        var_of_interest: string (e.g., AGE, RACE or ETHNIC)

    Returns:
        list 
    '''

    year_brkdn = make_year_brkdn(filename_list, age_range, var_of_interest)
    chart_l = make_chart_list(year_brkdn)
    chart = make_chart(chart_l)

    return chart

def make_year_brkdn(filename_list, age_range, var_of_interest):
    '''
    Builds a dictionary with the years for each file in filename_list
    as keys and values as a list of unemployment rates for each sub 
    group that satsifies age_range and var_of_interest. The values 
    in the list correspond to an alphabetized list of each sub group.
        Ex: value = [0.0, 0.4] corresponds to the unemployment rates for 
        "Female" and "Male" if the var_of_interest is GENDER

    Inputs:
        filename_list: a list of MORG dataset file names
        age_rage: a tuple consisted of two integers
        var_of_interest: string (e.g., AGE, RACE or ETHNIC)

    Returns:
        year_brkdn: dict 
    '''

    ages = list(age_range)
    low_bound = ages[0]
    up_bound = ages[1]

    data = {}
    input_dict = {}
    
    for f in filename_list:
        input_dict = make_input_dict('data/' + f)
        morg_dict = build_morg_dict(input_dict)
        year = f[6:8]

        data[year] = morg_dict

    sub_dict = make_subdict(input_dict)

    years = list(data.keys())

    hids_for_year = {}
    num_persons = 0
    for year in data:
        hids_of_int = []
        all_info = data[year]
        for hid in all_info:
            info = all_info[hid]
            status = info[STATUS]
            curr_age = info[AGE]
            if (status == "Working" or status == "Looking" or 
                status == "Layoff"):
                if curr_age >= low_bound and curr_age <= up_bound:
                    hids_of_int.append(hid)
                    num_persons += 1
        for yr in years:
            if yr == year:
                hids_for_year[yr] = hids_of_int

    codes = sub_dict[var_of_interest]
    total_variants = []
    for code in codes:
        description = code[1]
        total_variants.append(description)

    year_brkdn = {}
    for year in data:
        breakdown = {}
        curr_hids = hids_for_year[year]
        all_info = data[year]
        counts = {}
        for hid in curr_hids:
            info = all_info[hid]
            status = info[STATUS]
            if status == "Looking" or status == "Layoff":
                voi = info[var_of_interest]
                if voi not in counts:
                    counts[voi] = 1
                else:
                    counts[voi] = counts[voi] + 1

        for voi in counts:
            breakdown[voi] = (counts[voi])/num_persons

        curr_variants = list(breakdown.keys())

        diffs = []
        for var in total_variants:
            if var not in curr_variants:
                diffs.append(var)

        if len(diffs) > 0:
            for d in diffs:
                breakdown[d] = 0.0

        year_brkdn[year] = breakdown

    return year_brkdn 

def make_chart_list(year_brkdn):
    '''
    Builds a list of lists with each element in the list corresponding
    to what will be a row in the final chart. No processing of the 
    chart specifications (see make_chart)

    Inputs:
        year_brkdn: a dictionary containing the unemployment rates for
        each sub_group for each year_brkdn

    Returns:
        chart_l: list 
    '''

    yrs_l = list(year_brkdn.keys())
    yrs_l.sort()

    sorted_data = {}
    all_stats = {}
    all_cats = []
    for year in year_brkdn:
        data = []
        data_pairs = []
        all_stats = year_brkdn[year]
        all_cats = list(all_stats.keys())
        all_cats.sort()
        cats_values = list(all_stats.items())
        all_cats_values = [list(pair) for pair in cats_values]
        for cat in all_cats:
            for pair in all_cats_values:
                if cat == pair[0]:
                    data.append(pair[1])
                    data_pairs.append(pair)
        sorted_data[year] = data

    num_cats = len(all_cats)
    chart_l = []
    for i in range(num_cats):
        yr_cat_org = [all_cats[i]]
        for year in yrs_l:
            curr_data = sorted_data[year]
            data_point = curr_data[i]
            yr_cat_org.append(data_point)
        chart_l.append(yr_cat_org)

    yrs_l.insert(0, "Year")
    chart_l.insert(0, yrs_l)

    return chart_l

def make_chart(chart_l, COLUMN_SEP, COLUMN_WIDTH):
    '''
    Builds a list of lists with each element in the list corresponding
    to what will be a row in the final chart. Processes the strings
    to format the chart 

    Inputs:
        chart_l: list of lists 
        COLUMN_SEP: "|"
        COLUMN_WIDTH: 18

    Returns:
        chart: list of lists 
    '''

    COLUMN_WIDTH = 18
    COLUMN_SEP = "|"

    chart = []
    for i, row in enumerate(chart_l):
        sub_chart = [COLUMN_SEP]
        insert = []
        for inputs in row:
            print(inputs)
            inp = inputs
            t = type(inp)
            if t == float:
                inp = str(inp)
            curr_chars = len(inp)
            space = ['']
            diff = COLUMN_WIDTH - curr_chars)
            if diff < 0:
                num_chars = abs(diff)
                inp = inputs[:diff]
            else:
                while len(space) <= diff:
                    space.append(' ') 
            spaces = ''.join(space)
            insert.append(inp)
            insert.append(spaces)
            insert.append(COLUMN_SEP)
        insert.append('\n')
        insert_string = ''.join(insert)
        sub_chart.append(insert_string)
        row_insert = ''.join(sub_chart)
        chart.append(row_insert)

    for row in chart:
        print(row)

    return chart

def calculate_weekly_earnings_stats_for_fulltime_workers(morg_dict, gender, 
                                                         race, ethnicity):
    '''
    Returns a 4-element list of earnings statics (mean, median, min, and max) 
    for all fulltime workers who satisfy the given query criteria 

    Inputs:
        morg_dict: dict 
        gender: query criteria for gender 
        race: query criteria for race 
        ethnicity: query criteria for ethnicity 

    Returns:
        A 4-element list
    '''

    MEAN_INDEX = 0
    MEDIAN_INDEX = 1
    MIN_INDEX = 2
    MAX_INDEX = 3

    data_list = [0.0]*4
    given_stats = [gender, race, ethnicity]
    dex_of_all = [0]*3
    for i, s in enumerate(given_stats):
        if s == "All" or s == "ALL":
            dex_of_all[i] = True
        else:
            dex_of_all[i] = False 

    tot_persons = len(morg_dict)
    hids_of_int = []

    for hid in (morg_dict):
        add = [0]*3
        info = morg_dict[hid]
        work = info[STATUS]
        hours = info[HRWKE]
        print(work)
        if work == "Working" and hours >= 35:
            gen = info[GENDER]
            rc = info[RACE]
            en = info[ETHNIC]
            stats = [gen, rc, en]
            for i in range(3):
                if dex_of_all[i] == True:
                    add[i] = 1

                elif stats[i] == given_stats[i]:
                    add[i] = 1

                elif given_stats[i] == "Other":
                    if (stats[i] != "WhiteOnly" and stats[i] != "BlackOnly" and 
                    stats[i] != "AmericanIndian/AlaskanNativeOnly" and 
                    stats[i] != "AsianOnly" and stats[i] != "Hawaiian/PacificIslanderOnly"):
                        add[i] = 1
                
                else:
                    add[i] = 0

            total = sum(add)
            if total == 3:
                hids_of_int.append(hid)

    if len(hids_of_int) == 0:
        return data_list
    else:
        earnings = []
        for hid in hids_of_int:
            info = morg_dict[hid]
            earned = info[EARNWKE]
            earnings.append(earned)

        num_persons = len(hids_of_int)

        mean = float(sum(earnings)/num_persons)
        med = float(statistics.median(earnings))
        min_earned = float(min(earnings))
        max_earned = float(max(earnings))

        data_list[MEAN_INDEX] = mean
        data_list[MEDIAN_INDEX] = med
        data_list[MIN_INDEX] = min_earned
        data_list[MAX_INDEX] = max_earned
 
    return data_list 
