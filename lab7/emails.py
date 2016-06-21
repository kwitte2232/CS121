

import re


f = open('emails.txt', 'r')
text = f.read()
f.close

tuples = re.findall('(\w.+)@uchicago.edu', text)

emails = list(tuples)

#print(emails)

def find_functions(files):

    f = open(files, 'r')
    text = f.read()
    f.close

    fxn = re.findall('(?<!\s{4})def\s(\w+)', text)


    return fxn



def ultimate_function(file_list):

    all_fxns = []
    for f in file_list:
        x = find_functions(f)
        for fxn in x:
            t = (fxn, f)
            all_fxns.append(t)

    return all_fxns


def make_file_list(directory):

    string = ''
    for i in directory:
        strings = str(i)
        string.join(strings)

    file_list = re.findall( ,string)


