""" this is the file i'm gonna use to explore creating words in matplotlib
	to try to figure out how i'm gonna ever manage to creat a word cloud or
	tag cloud as they're known
	"""

import string
import matplotlib.pyplot as plt
import random
import numpy as np
import math as m


def dictionary_creation(filename):
	""" make a dictionary which maps the word with it's frequency"""
	fp = open(filename)
	d = dict()
	for line in fp:
		# print line
		for word in line.split():
			if "xe2" not in word:
				word = word.strip(string.punctuation + string.whitespace)
				# print word
				if len(word) >5:
					if word not in d:
						# print 'in'
						d[word] = 1
					else:
						# print 'not in'
						d[word] += 1
	fp.close()
	return d



def most_common(filename,n):
	""" takes the nth most common words and puts them into a list """
	freq_dict = dictionary_creation(filename)
	t = []
	for key, value in freq_dict.items():
		t.append((value,key))
		t.sort(reverse=True)
	wordlist = []
	freqlist = []
	# print n, 'most common words:'
	for freq,word in t[0:n]:
		# print word,'\t', freq
		wordlist.append(word)
		freqlist.append(freq)
	print len(freq_dict)
	return wordlist,freqlist

# wordlist,freqlist = most_common('alice',10)
# print most_common('alice',10)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval
    """
    # TODO: implement this

    input_interval_range = input_interval_end - input_interval_start
    output_interval_range = output_interval_end - output_interval_start
    new_val = float(val - input_interval_start)/float(input_interval_range)
    return output_interval_start + (new_val * output_interval_range)

def wordcloudplot(filename):
	wordlist,freqlist = most_common(filename,20)
	print wordlist
	x = 0.5
	y = 0.5
	a = np.matrix([x,y]).T
	input_max = max(freqlist)
	input_min = min(freqlist)
	angle = m.radians(36)
	i = 0
	angle2 = 0
	# print input_min
	rot = np.matrix( [ (m.cos(angle),-m.sin(angle)), (m.sin(angle), m.cos(angle)) ] )
	for word,freq in zip(wordlist,freqlist):
		if i < 10:
			scaled_value = remap_interval(freq,input_min,input_max,20,50)
			wally = plt.text(x,y,word,fontsize=scaled_value,color=random.choice(['r','deeppink','y','b','darkorange','aqua','teal','coral','cadetblue','forestgreen']))
			a = rot * a
			wally.set_rotation(angle2)
			wally.set_verticalalignment('top')
			angle2 = angle2 - 90
			# print "a", a,'word',word
			# print "newx", newx
			# print "newy", newy
			x = a[0,0]
			# print x
			y = a[1,0]
			# print y
			plt.xlim(-1,1)
			plt.ylim(-1,1)
			i = i + 1
		elif i >= 10:
			scaled_value = remap_interval(freq,input_min,input_max,20,70)
			wally = plt.text(x/2.1,y/2.1,word,fontsize=scaled_value, color=random.choice(['r','deeppink','y','b','darkorange','aqua','teal','coral','cadetblue','forestgreen']))
			wally.set_rotation(angle2)
			angle2 = angle2 + 90
			wally.set_verticalalignment('baseline')
			a = rot * a
			# print "a", a,'word',word
			# print "newx", newx
			# print "newy", newy
			x = a[0,0]
			# print x
			y = a[1,0]
			# print y
			plt.xlim(-1,1)
			plt.ylim(-1,1)
			i = i + 1

		# print wally.get_fontsize()
	
	
	# plt.text(0.5, 0.5,'matplotlib')

	plt.show()


wordcloudplot('muchado.txt')
