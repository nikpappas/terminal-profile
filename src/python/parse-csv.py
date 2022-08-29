#!/usr/bin/python3

import sys
from utils.readFile import readFile



import argparse

parser = argparse.ArgumentParser(description='Parse csv and output the given columns.')

parser.add_argument('file', type=str, 
		help='the file to parse')
parser.add_argument('-c', '--columns', default="*",
                    help='The integer idices of the columns to keep, comma separated')
parser.add_argument('-d', '--delimiter', default='\t',
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print('column', args.columns)
print('file', args.file)
print('delimiter', args.delimiter)


lines = readFile(args.file)


for l in lines:
  tokens =l.split(args.delimiter)
  print(tokens)
  lineOut = ""
  for t in args.columns.split(','):
    i = int(t)
    lineOut += tokens[i].strip() +'\t'
  print(lineOut.strip())
