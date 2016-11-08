import itertools
import os,sys
import xlsxwriter
from multiprocessing import Pool

def spacerCountWrite(motif1,motif2):
	Files = [open("gen.txt","w")]*30
	workbook = xlsxwriter.Workbook(motif1+"-"+motif2+"/"+motif1+"-"+motif2+".xlsx")
	worksheet = workbook.add_worksheet()
	worksheet.write(0, 1, "A")
	worksheet.write(0, 2, "T")
	worksheet.write(0, 3, "G")
	worksheet.write(0, 4, "C")
	for i in range(1,31):
		CntA = 0
		CntT = 0
		CntG = 0
		CntC = 0
		Files[i-1] = open(motif1+"-"+motif2+"/"+"spacer"+str(i)+".txt","r")
		for String in Files[i-1].readlines():
			CntA+=String.count("a")
			CntT+=String.count("t")
			CntG+=String.count("g")
			CntC+=String.count("c") 
		worksheet.write(i, 1, CntA)
		worksheet.write(i, 2, CntT)
		worksheet.write(i, 3, CntG)
		worksheet.write(i, 4, CntC)
		Files[i-1].close()
	workbook.close()










def func_star(a_b):
    """Convert `f([1,2])` to `f(1,2)` call."""
    return spacerCountWrite(*a_b)



pool = Pool(8)
#motifs = ["tgtcaa","tgtcac","tgtcag","tgtcat","tgtcca","tgtccc","tgtccg","tgtcct","tgtcga","tgtcgc","tgtcgg","tgtcgt","tgtcta","tgtctc","tgtctg","tgtctt"]
motifs1 = ["tgtcaa"]*16+["tgtcac"]*16+["tgtcag"]*16+["tgtcat"]*16+["tgtcca"]*16+["tgtccc"]*16+["tgtccg"]*16+["tgtcct"]*16+["tgtcga"]*16+["tgtcgc"]*16+["tgtcgg"]*16+["tgtcgt"]*16+["tgtcta"]*16+["tgtctc"]*16+["tgtctg"]*16+["tgtctt"]*16
motifs2 = ["tgtcaa","tgtcac","tgtcag","tgtcat","tgtcca","tgtccc","tgtccg","tgtcct","tgtcga","tgtcgc","tgtcgg","tgtcgt","tgtcta","tgtctc","tgtctg","tgtctt"]*16

pool.map(func_star, itertools.izip(motifs1, motifs2))

        



