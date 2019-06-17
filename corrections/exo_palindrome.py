# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=palindrome
def palindrome(ch):
    '''on vérifie si la chaine ch est un palindrome'''
    if len( ch )==1:
        return True
    if ch [0]== ch [ -1]:
        return palindrome ( ch [1: len ( ch ) -1])
    return False
# @END@



inputs_palindrome = [
    Args('kayak'),
    Args('bonjour'),
    Args('laval'),
    Args('bref ici ferb'),
    
]



exo_palindrome = ExerciseFunction(
    palindrome, inputs_palindrome)
