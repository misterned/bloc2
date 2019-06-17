# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=longueur_chaine
def longueur_chaine(ch):
    '''ch est la chaine de caractères dont on cherche la longueur'''
    if not ch :
        return 0
    else :
        return 1+ longueur_chaine(ch[1:])
# @END@



inputs_longueur_chaine = [
    Args("Bonjour"),
    Args("Bonjour les collègues"),
    Args("anticonstitutionnellement"),
    Args("le chocolat c'est bon !"),
    
]



exo_longueur_chaine = ExerciseFunction(
    longueur_chaine, inputs_longueur_chaine)
