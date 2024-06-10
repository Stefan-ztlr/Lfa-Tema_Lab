import fileinput
import sys

from validation import createDict
from validation import validate
from validation import checkString
from DFAconvert import convert_nfa_to_dfa_from_dict

dict = createDict(fileinput.input(sys.argv[1]))

convert_nfa_to_dfa_from_dict(dict, sys.argv[2])