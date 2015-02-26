# from pattern.web import *
# fp = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
import string
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = 22.0

def dictionary_creation(filename):
	""" make a dictionary which maps the word with it's frequency"""
	fp = open(filename)
	d = dict()
	for line in fp:
		# print line
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			# print word
			if len(word) >5:
				if word not in d:
					# print 'in'
					d[word] = 1
				else:
					# print 'not in'
					d[word] += 1
	return d

	fp.close()



def most_common(filename,n):
	""" takes the nth most common words and puts them into a list """
	freq_dict = dictionary_creation(filename)
	t = []
	for key, value in freq_dict.items():
		t.append((value,key))
		t.sort(reverse=True)
	wordlist = []
	freqlist = []
	print n, 'most common words:'
	for freq,word in t[0:n]:
		print word,'\t', freq
		wordlist.append(word)
		freqlist.append(freq)
	return wordlist,freqlist


def plot_data(filename):
	""" takes data from most_common and plots it"""
	wordlist,freqlist = most_common(filename,10)
	plt.plot(freqlist)
	plt.ylabel('frequency of words')
	plt.xlabel(wordlist)
	plt.show()


def piechart(filename):
	""" a test pie chart that i'm gonna develop into the actual thing"""
	wordlist,freqlist = most_common(filename,10)
	labels = wordlist
	plt.pie(freqlist, explode=None, labels=labels,
    colors=('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','aqua','azure'),
    autopct=None, pctdistance=0.6, shadow=False,
    labeldistance=1.1, startangle=None, radius=None)

	plt.show()

piechart('oliver_twist')


