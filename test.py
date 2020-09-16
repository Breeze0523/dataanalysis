from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
import sys
print("output #1: I'm excited to learn Oython.")
x = 4;
y = 8;
z = x * y;
print(z);
print("{0:4f}".format(exp(3))) 
print("{0:4f}".format(log(3))) 
print("{0:4f}".format(sqrt(3))) 


string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)",re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))

today = datetime.today()              
print("Output: {0!s}".format(today))
print(date.today())

#read words in file
#input_file = sys.argv[1]
#filereader = open(input_file,'r')
#for row in filereader:
 #   print(row.strip())
#filereader.close()