# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Paul Krusell

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    # TODO: implement this
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this
    complement = []
    for x in dna:
        complement.append(get_complement(x))
    return ''.join(complement)

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
     """
    # TODO: implement this
    # index = dna.find('TGA',3)
    # if index != -1:
    #     return dna[:index]
    # index = dna.find('TAG',3)
    # if index != -1:
    #     return dna[:index]
    # index = dna.find('TAA',3)
    # if index != -1:
    #     return dna[:index]

    for i in range(0,len(dna),3):
        codon = dna[i:i+3]
        if len(codon) < 3:
            break
        elif aa_table[codon] == '|':
            return dna[0:i]
    return dna



def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("ATGCATGAATGTA")
    ['ATGCATGAATGTA']
    """
    # TODO: implement this

    all_codons = []
    i = 0 
    while i < len(dna):
            # print len(dna)
            codon = dna[i:i+3]
            if len(codon) < 3:
                break
            elif aa_table[codon] == 'M':
                all_codons.append(dna[i:i+len(rest_of_ORF(dna[i:]))])
                # print len(rest_of_ORF(dna)),i
                i += len(rest_of_ORF(dna))
            else:
                i +=3

    return all_codons   
        

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    # TODO: implement this
    allORFS = find_all_ORFs_oneframe(dna)
    allORFS.extend(find_all_ORFs_oneframe(dna[1:]))
    allORFS.extend(find_all_ORFs_oneframe(dna[2:]))
    # print "find_all_ORfs", allORFS
    return allORFS



def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this

    orf_list_1 = find_all_ORFs(get_reverse_complement(dna))
    # print "orf_list_1", orf_list_1
    orf_list_2 = find_all_ORFs(dna)
    # print "orf_list_2", orf_list_2
    orf_list_1.extend(orf_list_2)
    # print "ORFS both strands", orf_list_1
    return orf_list_1



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    list_of_orfs = find_all_ORFs_both_strands(dna)
    # print "Longest ORF", list_of_orfs
    return max(list_of_orfs, key = len)

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this

    empty_list = []
    for i in range(num_trials):
        new_dna = shuffle_string(dna)
        empty_list.append(longest_ORF(new_dna))
    return len(max(empty_list, key = len))

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    # print 'run'
    amino_acid_list = []
    for i in range(0,len(dna),3):
        # print i
        codon = dna[i:i+3]
        if len(codon) == 3:
            amino_acid = aa_table[codon]
            # print amino_acid
            amino_acid_list.append(amino_acid)
            # print 'endloop'
        else:
            break
    return ''.join(amino_acid_list)

# print coding_strand_to_AA("ATGCGA")


def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    threshold = longest_ORF_noncoding(dna,1500)
    if len(dna) > threshold:
        all_ORFS = find_all_ORFs_both_strands(dna)
        filtered_ORFS = [coding_strand_to_AA(orf) for orf in all_ORFS if len(orf) >= threshold]
    return filtered_ORFS

from load import load_seq
dna = load_seq("./data/X73525.fa")
# print find_all_ORFs_both_strands(dna)
print gene_finder(dna)



# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()