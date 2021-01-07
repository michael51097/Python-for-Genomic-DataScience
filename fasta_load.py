# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:02:54 2020

@author: Michael
"""


"""
This script loads a fasta file of sequences into a dictionary
and reports the number of sequences in the file, 
and sorts the sequences by lenght
"""

def fasta_load (filename):

    f = open(filename,'r')
    Seqs={}
    
    
    #LOADS THE FASTA FILE INTO A DICTIONARY WITH KEYS AND SEQUENCES
    for line in f:
        Line=line.rstrip()
    # remove trailing chars like space and /n from line
        if Line[0] == '>':
            words=line.split() # splits the header line on any space characters
            name=words[0][1:] #start at first entry then from the second character move onArithmeticError
            Seqs[name]='' # initialize a new dictionary entry	
        else: #sequence, not header
            Seqs[name] = Seqs[name] + Line # looks up the entry for name, then adds the current line to it
    
    
    count = 0
    for keys in Seqs.keys():
            count = count + 1
    
    """ QUESTION 1"""
    
    #PRINTS THE NUMBER OF SEQUENCES
    print("Here are the number of sequences: ")
    print(count)
    
    
    
    Seq_len={}
    #print the lengths first
    for keys in Seqs.keys():
        Seq_len[keys] = ''
        Seq_len[keys] = len(Seqs[keys])
    
    
    sorted_Seq_len = sorted(Seq_len.items(), key = lambda x: x[1])
    
    print("Here are the lengths of the sequences sorted from shortest to longest: ")
    for i in sorted_Seq_len:
        print(i[0],i[1])
    
    return Seqs

fasta_load("dna2.fasta")
