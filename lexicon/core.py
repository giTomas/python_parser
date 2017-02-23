#!/usr/bin/python

# from functools import partial

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

#words sets
directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
# str.isdigit()

def index_word(word):
    if word in directions:
        return ('direction', word)
    elif word in verbs:
        return ('verb', word)
    elif word in stop_words:
        return ('stop_word', word)
    elif word in nouns:
        return ('noun', word)
    elif word.isdigit():
        return ('number', int(word))
    else:
        return ('error', word)

# nezbehnu testy ak to nie je v komente!!!
# stuff = raw_input('> ')

def scan(input_str):
    list_to_be_mapped = input_str.lower().split()
    return map(index_word, list_to_be_mapped)
