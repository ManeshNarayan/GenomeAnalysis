import xlsxwriter

file=open("PromoterSeq.txt","r+")

fileread=file.read();
workbook = xlsxwriter.Workbook('Exp.xlsx')
worksheet = workbook.add_worksheet()
col = 1
motifs = ["tgtcaa","tgtcac","tgtcag","tgtcat","tgtcca","tgtccc","tgtccg","tgtcct","tgtcga","tgtcgc","tgtcgg","tgtcgt","tgtcta","tgtctc","tgtctg","tgtctt"]
for motif1 in motifs:
	for motif2 in motifs:
		row=0
		diff=0
		count = [0] * 30


		for i in range(0,len(fileread)-10):
		    string=""+fileread[i]+fileread[i+1]+fileread[i+2]+fileread[i+3]+fileread[i+4]+fileread[i+5]
		    if string==motif1:
			i=i+6
			stringnew=""
			for k in range(i,i+26):
			    stringnew=fileread[k]+fileread[k+1]+fileread[k+2]+fileread[k+3]+fileread[k+4]+fileread[k+5]
			    if stringnew==motif2:
				diff=k-i
				count[diff]+=1 
				i=k
				break

		worksheet.write(row, col, motif1+"-"+motif2)
		row+=1
		for k in range(0,26):		
			worksheet.write(row, col, count[k])
			row+=1
		print(col)
		col+=1

file.close()

workbook.close()

        
