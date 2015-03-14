""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
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

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
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