import itertools
import os,sys
from multiprocessing import Pool

def spacerCountWrite(motif1,motif2):
	os.mkdir(motif1+"-"+motif2+"/")
	Files = [open("gen.txt","w")]*30
	for i in range(1,31):
		Files[i-1] = open(motif1+"-"+motif2+"/"+"spacer"+str(i)+".txt","a+")



	file=open("PromoterSeq.txt","r+")
	fileread=file.read();

	diff=0

	for i in range(0,len(fileread)-10):
	    string=fileread[i]+fileread[i+1]+fileread[i+2]+fileread[i+3]+fileread[i+4]+fileread[i+5]
	    if string==motif1:
		i=i+6
		stringnew=""
		for k in range(i,i+31):
		    stringnew=fileread[k]+fileread[k+1]+fileread[k+2]+fileread[k+3]+fileread[k+4]+fileread[k+5]
		    if stringnew==motif2:
			diff=k-i
			if(diff!=0):	
				for count1 in range(i,k):
					Files[diff-1].write(fileread[count1])
				Files[diff-1].write("\n")                          

			i=k
			break

	file.close()
	for i in range(1,31):
		Files[i-1].close()

def func_star(a_b):
    """Convert `f([1,2])` to `f(1,2)` call."""
    return spacerCountWrite(*a_b)



pool = Pool(8)
#motifs = ["tgtcaa","tgtcac","tgtcag","tgtcat","tgtcca","tgtccc","tgtccg","tgtcct","tgtcga","tgtcgc","tgtcgg","tgtcgt","tgtcta","tgtctc","tgtctg","tgtctt"]
motifs1 = ["tgtcaa"]*16+["tgtcac"]*16+["tgtcag"]*16+["tgtcat"]*16+["tgtcca"]*16+["tgtccc"]*16+["tgtccg"]*16+["tgtcct"]*16+["tgtcga"]*16+["tgtcgc"]*16+["tgtcgg"]*16+["tgtcgt"]*16+["tgtcta"]*16+["tgtctc"]*16+["tgtctg"]*16+["tgtctt"]*16
motifs2 = ["tgtcaa","tgtcac","tgtcag","tgtcat","tgtcca","tgtccc","tgtccg","tgtcct","tgtcga","tgtcgc","tgtcgg","tgtcgt","tgtcta","tgtctc","tgtctg","tgtctt"]*16

pool.map(func_star, itertools.izip(motifs1, motifs2))

        



