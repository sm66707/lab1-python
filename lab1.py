from collections import Counter
import math
import sys

def fn1(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#x=fn1(1,2,3,4)
#print(x)

def fn2(mylist):
    return list(set(mylist))
#y=fn2([1,2,2,2,3,6,6])
#print(y)

def fn3(st1,st2):
    return st1[:math.ceil(len(st1)/2)]+st2[:math.ceil(len(st2)/2)] , st1[math.ceil(len(st1)/2):]+st2[math.ceil(len(st2)/2):]
#a=fn3("abcd","abcde")
#print(a)

def fn5(c):
     vowels = ('a', 'e', 'i', 'o', 'u')
     return ''.join([x for x in c if x not in vowels])
#x=fn5('mobile')
#print(x)

def fn4():
    f = open(sys.argv[len(sys.argv)-1], "r")
    my_str = f.read()
    f.close()
    words = Counter(my_str.split()).most_common(20)
    words = [word[0] for word in words]
    f = open("popular_words.txt", "w")
    f.write("\n". join(map(lambda word: str(word), words)))
    f.close()

fn4()
def fn6(st,ch):
    return [ i for i,x in  enumerate(st) if x==ch ]
#x=fn6('google','o')
#print(x)
