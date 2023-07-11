
import re

def get_unique_letters(text: str, case_sensitive: bool=False, only_lowers:bool=True, only_uppers:bool=False) -> set:
    regex = r'[A-Za-z]' if case_sensitive else r'[a-z]' if only_lowers else r'[A-Z]'
    return set(re.findall(regex, text))

def get_letters(text: str, case_sensitive: bool=False, only_lowers:bool=True, only_uppers:bool=False) -> list:
    regex = r'[A-Za-z]' if case_sensitive else r'[a-z]' if only_lowers else r'[A-Z]'
    return list(re.findall(regex, text))