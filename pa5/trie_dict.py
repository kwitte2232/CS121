# CS121: Auto-completing keyboard using Tries
#
# usage: python trie_dict.py <dictionary filename>
#
# Kristen Witte

import os
import sys
from sys import exit
import tty
import termios
import fcntl
import string

import trie_shell

def create_trie_node():
    '''
    Create an emptry trie or trie node

    Inputs:
        None

    Returns:
        Empty dict
    '''
    return {}

def add_word(word, trie):
    '''
    Add word to the trie

    Inputs:
        word: the string (word) to add_word
        trie: the trie (see create_trie_node)

    Returns:
        The trie with the added word
    '''

    word_length = len(word)

    if word_length == 1:
        curr_node = create_trie_node()
        curr_node["final"] = True
        curr_node["count"] = 1
        trie[word] = curr_node
        return trie 
    else:
        if word[0] not in trie:
            curr_node = create_trie_node()
            trie[word[0]] = curr_node 
            curr_node["count"] = 1
            curr_node["final"] = False
        else:
            trie[word[0]]["count"] = trie[word[0]]["count"] + 1
        next_trie_step = word[1:]
        sub_tree = add_word(next_trie_step, trie[word[0]])
        trie[word[0]] = sub_tree
        return trie


def is_word(word, trie):
    '''
    Determine if word is in trie

    Inputs:
        word: the string (word) 
        trie: the trie (see create_trie_node)

    Returns:
        Boolean. True if word is in trie. False if not.
    '''

    word_length = len(word)

    if word_length == 1:
        if word in trie:
            status = trie[word]["final"]
            return status == True
        else:
            return False
    else:
        next_trie_step = word[1:]
        return(is_word(next_trie_step, trie[word[0]]))


def num_completions(word, trie):
    '''
    Detmine number of completed words that start with prefix (word)

    Inputs:
        word: the prefix
        trie: the trie (see create_trie_node)

    Returns:
        Integer. Number of completions that start with that prefix,
            including the prefix itself if it is a word
    '''

    word_length = len(word)

    num_full_words = 0

    if word_length == 1:
        curr_trie = trie[word]
        if curr_trie["final"] == True:
            num_full_words = 1
        
        for st in curr_trie:         
            if st != "final" and st != "count":
                sub_trie = curr_trie[st]
                if len(list(sub_trie.keys())) == 2:
                    num_full_words += 1
                else:
                    full_words = num_completions(st, curr_trie)
                    num_full_words = num_full_words + full_words
        return num_full_words

    else: 
        next_trie_step = word[1:]
        sub_prefix_trie = trie[word[0]]
        if next_trie_step[0] not in sub_prefix_trie.keys():
            return "Prefix not in dictionary"
        return(num_completions(next_trie_step, sub_prefix_trie))

    return num_full_words

def get_completions(word, trie):

    '''
    Get the word completions for the prefix

    Inputs:
        word: the prefix
        trie: the trie (see create_trie_node)

    Returns:
        List: all of the completions for the prefix
    '''
    word_length = len(word)

    rv = [" "]

    if word_length == 1:
        curr_trie = trie[word]
        for st in curr_trie:
            if st != "final" and st != "count":
                sub_trie = curr_trie[st]
                if len(list(sub_trie.keys())) == 2:
                    rv.append(st)
                else:
                    completions = get_completions(st, curr_trie)
                    string = ''
                    for completes in completions:
                        string = st + completes
                        rv.append(string)
        return rv      
    
    else:
        next_trie_step = word[1:]
        sub_prefix_trie = trie[word[0]]
        if (len(next_trie_step) == 1 and 
            next_trie_step not in sub_prefix_trie.keys()):
            return []
        return(get_completions(next_trie_step, sub_prefix_trie))

    return rv


if __name__ == "__main__":
    trie_shell.go("trie_dict")

