from random import choice
from typing import Any


class UniqueId:
    alphabet : Any

    def __init__(self) :
        self.alphabet = [ chr(i) for i in range(48,123) if i <= 57 or (i >= 65 and i <=90) or (i >= 97) ]
    
    def generate_id_formated(self):
        id = ''
        for i in range(4):
            if id != '':
                id += '-'
            for j in range(5):
                id += choice( self.alphabet )
                
        return id





