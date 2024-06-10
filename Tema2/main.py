import fileinput
import sys

from validation import createDict
from validation import validate
from validation import checkString

dict = checkString(fileinput.input(sys.argv[1]), sys.argv[2])