# import import_01  # import from current dir
# import import_01 as imp
from import_01 import find_index as fi, test
# from import_01 import *  # unaware from where from

import sys
# sys.path.append('dir path to PYTHONPATH')  # append before every other dir
# able to set PYTHONPATH in dot_bash file

# abel to import standard libraries
import math
import random
import os  # provides big functionality w/ os

courses = ['hist', 'math', 'logics']

index = fi(courses, 'Math')
# print(index)

print(sys.path)  # displays python search for modules
print(os.getcwd())
print(os.__file__)
