# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=somme_liste
def somme_liste(T, S):
    '''partant d’une liste T, on détermine si la somme des éléments de T
est ou non supérieure à une valeur entière donnée S.'''
    N = len(T)
    i , sss , sp = 0 , False , 0
    while not(i == N):
        sss = sss or (sp + T[i]>S)
        sp = sp + T[i]
        i += 1
    return sss
# @END@



inputs_somme_liste = [
    Args([10, 3, 5],20),
    Args([10, 13, 5],20),
    Args([10, 3, 5, 4],20),
    Args([10, 3, 5, 1, 0],23),
    
]



exo_somme_liste = ExerciseFunction(
    somme_liste, inputs_somme_liste)
