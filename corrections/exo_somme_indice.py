# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=somme_indice
def somme_indice(T, S):
    '''partant d’une liste T, on détermine si la somme des éléments de T
est ou non supérieure à une valeur entière donnée S.'''
    N = len(T)
    i , sp = 0 , 0
    while not((i == N)or (sp + T[i]>S)):
        sp = sp + T[i]
        i += 1
    sss = not(i == N)
    return sss, i
# @END@



inputs_somme_indice = [
    Args([10, 3, 5],20),
    Args([10, 13, 5],20),
    Args([10, 3, 5, 4],20),
    Args([10, 3, 5, 1, 0],23),
    Args([10, 3, 5, 1, 0],12),
    
]



exo_somme_indice = ExerciseFunction(
    somme_indice, inputs_somme_indice)
