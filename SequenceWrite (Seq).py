

import os,sys


motifs = ["tgtcaa"]#,"tgtcac","tgtcag","tgtcat","tgtcca","tgtccc","tgtccg","tgtcct","tgtcga","tgtcgc","tgtcgg","tgtcgt","tgtcta","tgtctc","tgtctg","tgtctt"]
for motif1 in motifs:
	for motif2 in motifs:
		os.mkdir(motif1+"-"+motif2+"/")
		Files = [open("gen.txt","w")]*25
		for i in range(1,26):
			Files[i-1] = open(motif1+"-"+motif2+"/"+"spacer"+str(i)+".txt","a+")



		file=open("PromoterSeq.txt","r+")
		fileread=file.read();

		diff=0

		for i in range(0,len(fileread)-10):
		    string=fileread[i]+fileread[i+1]+fileread[i+2]+fileread[i+3]+fileread[i+4]+fileread[i+5]
		    if string==motif1:
			i=i+6
			stringnew=""
			for k in range(i,i+26):
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
		for i in range(1,26):
			Files[i-1].close()
        
