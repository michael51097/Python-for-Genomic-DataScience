# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:32:13 2020

@author: Michael
"""
"""
Assignment: 
Given an input reading frame on the forward strand (1, 2, or 3) your program
 should be able to identify all ORFs present in each sequence of the FASTA 
 file, and answer the following questions: what is the length of the longest 
 ORF in the file? What is the identifier of the sequence containing the longest 
 ORF? For a given sequence identifier, what is the longest ORF contained in 
 the sequence represented by that identifier? What is the starting position 
 of the longest ORF in the sequence that contains it?
"""



#This Function splits a sequence into 'n' number of characters, and creates
# a member of a list for each split,
#In this case the function was used to identify every codon of a sequence

def N_splitter_ORF(n,testseq):
    #split the sequence by n  
    my_test_list1=[]
    my_test_list2=[]
    my_test_list3=[]
    x=0
    for NT in range(0,len(testseq)-(n-1)):
         
        if x%3 ==0:
            my_test_list1.append(testseq[NT:NT+n])
        if x%3 ==1:
            my_test_list2.append(testseq[NT:NT+n])
        if x%3 ==2:
            my_test_list3.append(testseq[NT:NT+n])
        x=x+1
    return(my_test_list1, my_test_list2, my_test_list3)


def ORFs_max(filename,search_term,n):
    
    f = open(filename,'r')
    
    Seqs={}
    
    #LOADS THE FASTA FILE INTO A DICTOINARY WITH KEYS AND SEQUENCES
    for line in f:
        Line=line.rstrip()
    # remove trailing chars like space and /n from line
        if Line[0] == '>':
            words=line.split() # splits the header line on any space characters
            name=words[0][1:] #start at first entry then from the second character move onArithmeticError
            Seqs[name]='' # initialize a new dictionary entry	
        else: #sequence, not header
            Seqs[name] = Seqs[name] + Line # looks up the entry for name, then adds the current line to it
    
    
    stats1={}
    stats2={}
    stats3={}
    
    for keys in Seqs:
        # this splits the sequence into three distint open reading frames
        x = N_splitter_ORF(n,Seqs[keys])
        
        
        
        ORF1 = []
        ORF2 = []
        ORF3 = []
        
        ORF1 = x[0] #x is the output from N_splitter, in this line loading the first reading frame of the sequence
        ORF2 = x[1]
        ORF3 = x[2]
        
        s_ORF1 =[]
        s_ORF2 =[]
        s_ORF3 =[]
    
        t_ORF1 =[]
        t_ORF2 =[]
        t_ORF3 =[]
    
        
        
        s_ORF1 = [i for i, x in enumerate(ORF1) if x =='ATG'] #Identifies the position of Start codon in first reading frame
        s_ORF2 = [i for i, x in enumerate(ORF2) if x =='ATG']
        s_ORF3 = [i for i, x in enumerate(ORF3) if x =='ATG']
    
        #t_ORF1 identifies the position of the stop codon of the first reading frame
        t_ORF1 = [i for i, x in enumerate(ORF1) if x =='TGA'] + [i for i, x in enumerate(ORF1) if x =='TAG'] + [i for i, x in enumerate(ORF1) if x =='TAA']
        t_ORF2 = [i for i, x in enumerate(ORF2) if x =='TGA'] + [i for i, x in enumerate(ORF2) if x =='TAG'] + [i for i, x in enumerate(ORF2) if x =='TAA']
        t_ORF3 = [i for i, x in enumerate(ORF3) if x =='TGA'] + [i for i, x in enumerate(ORF3) if x =='TAG'] + [i for i, x in enumerate(ORF3) if x =='TAA']
        
      
        #Compares the start and stop codon position in the first reading frame to determine 
        #the start position and the length of the open reading frame
        for x in s_ORF1:
            for y in t_ORF1:
                if x>y:
                    continue
                else:
                    # stop - the start starting at index 
                    stats1[keys+"@ Starts at Position "+ str(3*(x)+1)+ ", Whose length is -->"] =[(3*y+3) - (3*(x))]
                    
        for x in s_ORF2:
            for y in t_ORF2:
                if x>y:
                    continue
                else:
                    stats2[keys+"@ Starts at Position "+ str(3*(x)+1)+ ", Whose length is -->"] =[(3*y+3) - (3*(x))]
                    
        for x in s_ORF3:
            for y in t_ORF3:
                if x>y:
                    continue
                else:
                    stats3[keys+"@ Starts at Position "+ str(3*(x)+1)+ ", Whose length is -->"] =[(3*y+3) - (3*(x))]
                    
    
          
        
    
    print("ORF1:     ")
    print(sorted(stats1.items(), key=lambda z: z[1], reverse = True)[0])
    print("ORF2:     ")
    print(sorted(stats2.items(), key=lambda z: z[1], reverse = True)[0])
    print("ORF3:     ")
    print(sorted(stats3.items(), key=lambda z: z[1], reverse = True)[0])
    
    
    #search_term = "gi|142022655|gb|EQ086233.1|16"
    print("Searching for specific term: " + str(search_term))
    
    s_ORF={}
    
    stats1.update(stats2)
    stats1.update(stats3)
    
    ORFALL = stats1
    
    for keys in ORFALL:
        
        keys_split = keys.split('@')
        if keys_split[0] == search_term:
            s_ORF[keys]=ORFALL[keys]
        
    
    print(sorted(s_ORF.items(), key = lambda z: z[1], reverse = True)[0])

file ="dna2.fasta"
search_term = "gi|142022655|gb|EQ086233.1|16"
n = 3

ORFs_max(file,search_term,n)



    
