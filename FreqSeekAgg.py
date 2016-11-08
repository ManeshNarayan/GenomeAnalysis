import xlsxwriter

row=0

workbook = xlsxwriter.Workbook("Check.xlsx")
worksheet = workbook.add_worksheet()
motifs = ["tgtcaa","tgtcac","tgtcag","tgtcat","tgtcca","tgtccc","tgtccg","tgtcct","tgtcga","tgtcgc","tgtcgg","tgtcgt","tgtcta","tgtctc","tgtctg","tgtctt"]

worksheet.write(row, 0, "Motif")	
worksheet.write(row, 1, "A")
worksheet.write(row, 2, "T")
worksheet.write(row, 3, "G")
worksheet.write(row, 4, "C")


for motif1 in motifs:
	for motif2 in motifs:
		Files = [open("gen.txt","w")]*30
		row+=1
		CntA = 0
		CntT = 0
		CntG = 0
		CntC = 0
		for i in range(1,31):
			Files[i-1] = open(motif1+"-"+motif2+"/"+"spacer"+str(i)+".txt","r")
			for String in Files[i-1].readlines():
				CntA+=String.count("a")
				CntT+=String.count("t")
				CntG+=String.count("g")
				CntC+=String.count("c") 
			Files[i-1].close()
		worksheet.write(row, 0, motif1+"-"+motif2)	
		worksheet.write(row, 1, CntA)
		worksheet.write(row, 2, CntT)
		worksheet.write(row, 3, CntG)
		worksheet.write(row, 4, CntC)
workbook.close()
		


