#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        tup = (len(sentence), None)
        return 'None'
    else:
        tup = (len(sentence), sentence[0])
        return tup
