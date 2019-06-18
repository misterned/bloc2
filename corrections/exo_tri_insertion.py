# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=tri_insertion
def tri_insertion(list):
    '''la liste list est triée à l'aide de la méthode du tri par insertion'''
    for k in range(1,len(list)):
        temp=list[k]
        j=k
        while j>0 and temp<list[j-1]:
            list[j]=list[j-1]
            j-=1
        list[j]=temp
    return list
# @END@



inputs_tri_insertion = [
    Args([1, 10, 3, 5]),
    Args([10, 2, 8, 1, 0]),
    Args([5, 1, 3]),
    Args([15, 10, 14, 12, 8, 21]),
    
]



exo_tri_insertion = ExerciseFunction(
    tri_insertion, inputs_tri_insertion)
