#!/usr/bin/python3
def multiple_returns(sentence):
    
    tuple = (sentence)
    
    if(sentence == ""):
        return(len(tuple), None)
    else:
        return(len(tuple), tuple[0])