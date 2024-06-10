from validation import createDict
from validation import validate
import fileinput

dict = createDict(fileinput.input())
print(validate(dict))
