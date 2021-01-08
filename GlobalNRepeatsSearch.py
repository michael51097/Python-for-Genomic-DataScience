# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:20:05 2020

@author: Michael
"""



#Loads fasta file into a dictionary where keys are ids and values are sequences
def load_fasta(filename):
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

    return Seqs

Seqs = load_fasta("dna2.fasta")

#splits a sequence by a specified length
def N_splitter(n,testseq):
    #split the sequence by n  
    my_test_list=[]
    for NT in range(0,len(testseq)-(n-1)):      
            my_test_list.append(testseq[NT:NT+n])
    return(my_test_list)

def search_Repeats_global(my_test_list,testseq):
    x=0
    num=0
    repeats={}

    for search in my_test_list:
        x=0
        #find the first stop where this search term is found
        if testseq.find(search,x) >=0:
            x = testseq.find(search,x)+1
            #finds if there is a secound spot where the search term occurs
            if testseq.find(search,x) >=0:
                #If it happens again after the the first and secound search see if we 
                #have taken it into the repeats dicitonary yet
                #if we have then we can go to the next term
                if (search in repeats):
                    x=0                    
                    continue
                else:
                    #If we have not then we look through and count how many times this terms
                    #repeats and add it to our running list
                    x=0
                    
                    while testseq.find(search,x) >=0:
                        x = testseq.find(search,x)+1
                        num = num+1
                    repeats[search]=(num)
                    num=0
        continue
    return repeats         

#groups up all the sequences togther into a long string
#Seperated by @ character
def concat(diction):
    Mlist=""
    for terms in diction:
        Mlist= Mlist +"@"+ diction[terms]
        
    return Mlist

#This creates a master list of all the search terms that will be used
def search_list(Seqs,n):
    Labeled_repeats ={}
    testseq = ""
    all_searches =[]

       
    for keys in Seqs:
        test_seq = Seqs[keys]
        my_test_list = N_splitter(n,test_seq)
        all_searches = all_searches + my_test_list
        
    return all_searches


#n is the specified length of the repeats searching through
n=7
all_searches = search_list(Seqs,n)

output = search_Repeats_global(all_searches, concat(Seqs))

print("Sorted list of all repeats: ")
print(sorted(output.items(), key=lambda z: z[1], reverse = True))




 
