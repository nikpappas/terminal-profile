import os
 
def readFile (relativeFilePath):
  file_path = os.path.join(os.getcwd(),relativeFilePath)
  with open(file_path,"r") as f:
    return f.readlines()

  
