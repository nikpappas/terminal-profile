#!/usr/bin/python3

import sys
import os
import random

 
file_path = os.path.join(os.getcwd(),sys.argv[1])
with open(file_path,"r") as f:
  lines = f.readlines()
  random.shuffle(lines)
  for l in lines:
    print(l.strip())


