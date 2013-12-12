#Exercise 11.1
def findword(check, filename):
	d = {}
	fin = open(filename)
	for line in fin:
		word = line.strip()
		d[word] = 1
	if check in d:
		return 'Nice you have a real word'
	else:
		return 'Try again my friend'

#print findword('balloon', 'words.txt')

#Exercise 11.2
def histogramshort(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0)
		d[c] += 1
	return d

#print histogramshort('hello')

#Exercise 11.3
def print_hist(h):
	d = histogramshort(h)
	dk = d.keys()
	dk.sort()
	return dk


#print print_hist('hello')

#Exercise 11.4

def reverse_lookup(d, v):
    looklist = []
    for k in d:
        if d[k] == v:
            looklist.append(k)
    return looklist

blammo = {'a':1, 'b':1, 'c':0, 'd':0}

#print reverse_lookup(blammo, 2)

#Exercise 11.9

def has_duplicates(s):
    d = histogramshort(s)
    for k in d:
        if d[k] > 1:
            return "has dupes"
    return "no dupes"

#print has_duplicates('andy')

#Exercise 11.10

def create_dict(filename):
    d = {}
    fin = open(filename)
    for line in fin:
        word = line.strip()
        s = list(word)
        s.sort()
        d[word] = s
    return d

def rotate_words(word, filename):
    d = create_dict(filename)
    v = list(word)
    v.sort()
    for key in d:
        if d[key] == v:
            return "you have a rotated word"
    return "there is no rotation"        

print rotate_words('care', 'shortwords.txt')



    

        