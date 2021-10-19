# -*- coding: utf-8 -*-

"""
Useful functions for the project.

@author: pavan
"""

class Status(object):
    """
    Class with code colors for write in system console.
    """
    none='\033[00m'
    error='\033[01;31m'
    success='\033[01;32m'
    info='\033[01;36m'
    
    
def cleaning_cnpj(cnpj):
    """
    Cleaning cnpj mask in string.
    
    Args:
        cnpj (string):    string of cnpj with mask
        
    Returns:
        string with cnpj without mask
    """
    
    cnpj = cnpj.replace('.','')
    cnpj = cnpj.replace('/','')
    cnpj = cnpj.replace('-','')    
    
    return cnpj


def only_numerics(seq):
    """
    Only numerics in string
    
    Args:
        seq (string):    string with numbers and characters.
    
    Returns:
        only integers of strings
    """
    
    number = filter(type(seq).isdigit, seq)
    
    if not number.isdigit():
        return 0
     
    return number
            