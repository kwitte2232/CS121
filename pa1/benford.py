# CS121 A'15: Benford's Law
#
# Functions for evaluating data using Benford's Law.
#
# Kristen Witte


import math

def extract_leading_digits_single(amount, num_digits):
    '''
    Given a positive floating point number and a number of digits,
    extract the specified number of leading digits

    Inputs:
        amount: float
        num_digits: the number of leading digits to extract from the
            amount.

    Returns:
        integer
    '''

    assert(num_digits > 0)
    assert(amount > 0)
    
    amount = float(amount)
    num_digits = float(num_digits)

    logamt = math.floor(math.log10(amount))
    exp = -logamt + num_digits - 1
    power = math.pow(10, exp)
    inside = power*amount

    lead = math.trunc(inside)
    return lead


def extract_leading_digits_from_list(dollar_amounts, num_digits):
    '''
    Extract the leading digit from a list of strings

    Inputs:
        dollar_amounts: list of strings
        num_digits: the number of leading digits to extract from
            the list

    Returns:
        list
    '''
    
    length = len(dollar_amounts)

    if length > 0:
        digits = []
        pos = 0
        for dollars in dollar_amounts:
            dollars = dollars.strip('$')
            amount = float(dollars)
            n = extract_leading_digits_single(amount, num_digits)
            digits.insert(pos, n)
            pos = pos + 1
    else:
        digits = []

    return digits


def compute_expected_benford_dist(num_digits):
    ''' 
    Returns the distribution of data values that start... 
       with x number of digits (num_digits)

    Inputs:
        num_digits: the number of leading digits to extract from
            the list

    Returns:
        list
    '''
    start = int((math.pow(10, num_digits))/10)
    end = int((math.pow(10, num_digits)))

    dist = []
    index = 0
    for i in range(start, end):
        prob = math.log10((1 + (1/i)))
        dist.insert(index, prob)
        index = index + 1

    return dist


def compute_benford_dist(dollar_amounts, num_digits):
    ''' 
    Compute the benford distribution given...
         the list dollar_amounts

    Inputs:
        dollar_amounts: list of strings
        num_digits: the number of leading digits to extract from
            the list

    Returns:
        list
    '''

    assert(num_digits > 0)
    assert(len(dollar_amounts)>0)
    n_digits = int((math.pow(10, num_digits))/10)
    end = (n_digits*10)

    length = 0

    for i in range(n_digits, end):
        length = length + 1

    counts = [0]*length
    freq = [0]*length
    lead_ex = extract_leading_digits_from_list(dollar_amounts, num_digits)
    
    for j in lead_ex:
        print(j)
        counts[j-10] = counts[j-10] + 1

    total = len(lead_ex)
    pos = 0
    for n in counts:
        pct = n/total
        freq[pos] = pct
        pos = pos + 1

    return freq


def compute_benford_MAD(dollar_amounts, num_digits):
    ''' 
    Extract the Mean Absolute Difference (MAD) between... 
        real data set and predicted distribution

    Inputs:
        dollar_amounts: list of strings
        num_digits: the number of leading digits to extract from
            the list

    Returns:
        float
    '''

    exp = compute_expected_benford_dist(num_digits)
    act = compute_benford_dist(dollar_amounts, num_digits)

    length = len(exp)
    av = []
    total = 0

    for i in range(length):
        x = exp[i]
        y = act[i]
        absval = abs(x-y)
        av.append(absval)

    for value in av:
        total = total + value

    mad = (1/length)*total

    return mad



