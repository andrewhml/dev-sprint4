#Exercise 10.1

def nested_sum(nestedList):
    newList = [0]

    def flatlist(nestedList):

        for i in range(len(nestedList)):
            if type(nestedList[i]) == int:
                newList.append(nestedList[i])
            else:
                flatlist(nestedList[i])
        return newList

    flatlist(nestedList)
    print sum(newList)


c = [1, 2, 3, [4, 5, [10, 5]]]

#nested_sum(c)

#Exercise 10.2

def capitalize_all(nestedList):
    result = []
    for s in nestedList:
        if type(s) == list:
            result.append(capitalize_all(s))
        else:
            result.append(s.capitalize())
    return result

a = ['a', 'b', 'c', ['d', 'e', 'f']]

#print capitalize_all(a)

#Exercise 10.3
def sum_list(numList):
    newList = [numList[0]]
    n = 0
    for s in range(len(numList)-1):
        a = numList[n] + numList[n+1]
        newList.append(a)
        n += 1
    return newList

d = [4, 5, 5, 20, 5]
#print sum_list(d)

d.index(5)

#Exercise 10.4
def middle(fullList):
    del fullList[0]
    del fullList[-1]
    return fullList

#print middle(d)

#Exercise 10.5
def chop(fullList):
    fullList.pop(0)
    fullList.pop(-1)
    return

#print chop(d)

#Exercise 10.7
def anagram(word1, word2):
    t1 = list(word1)
    t2 = list(word2)
    if len(t1) == len (t2):
        for s in t1:
            if t2.index(s) == ValueError:
                return 'Cannot be an anagram'
            else:
                return 'Boom anagram baby!'
    else:
        return 'Cannot be an anagram'

#print anagram('meat', 'team')

#Exercise 10.13
    

import time


def make_word_list1(filename):
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open(filename)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

#make_word_list1('words.txt')

start_time = time.time()
t = make_word_list1('words.txt')
elapsed_time = time.time() - start_time

#print len(t)
#print t[:10]
#print elapsed_time, 'seconds'

def interlockword(word1, word2):
    a = list(word1)
    b = list(word2)
    newword = []
    n = 0
    while (n < len(word1)):
        newword.append(a[n])
        newword.append(b[n])
        n += 1
    delimiter = ''
    newstring = delimiter.join(newword)
    return newstring

def interlock(filename):
    t = make_word_list1(filename)
    t1 = t[:500]
    t2 = ['shoe','bold', 'told', 'cold','schooled', 'bre', 'akd', 'barked']
    newList = []
    for w in t2:
        word1 = w
        for x in t2:
            word2 = x
            if len(word1) == len(word2):
                j = interlockword(word1, word2)
                if j in t2:
                    print word1, word2
                    print j

print interlock('words.txt')