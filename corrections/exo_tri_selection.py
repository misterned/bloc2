# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=tri_selection
def tri_selection(list):
    '''la liste list est triée à l'aide de la méthode du tri par sélection'''
    for i in range(len(list)):
        mini = i
        for j in range(i, len(list)):
            if list[j] < list[mini]:
                mini = j
        list[i], list[mini] = list[mini], list[i]
    return list
# @END@



inputs_tri_selection = [
    Args([1, 10, 3, 5]),
    Args([10, 2, 8, 1, 0]),
    Args([5, 1, 3]),
    Args([15, 10, 14, 12, 8, 21]),
    
]



exo_tri_selection = ExerciseFunction(
    tri_selection, inputs_tri_selection)
