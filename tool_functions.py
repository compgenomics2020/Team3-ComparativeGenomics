
#!/usr/bin/env python
import argparse
import subprocess
import re
import sys




def FastANI(filenames,??parameters,out):##any parameters for ??
	
	return




def StringMLST(filenames,??parameters,out):##any parameters for ??
	
	return




def ChewBBACA(filenames,??parameters,out):##any parameters for ??
	
	return




def kSNP():##only for 7210 project, cd to ComparativeGenomics directory

    subprocess.call(["conda", "activate", "T3env4"])
    
    subprocess.call(["kSNP3", "-in", "SNP/list_file.txt", "-outdir","output", "-k","19", "-ML","|", "tee","log.txt"])
   
    subprocess.call(["ete3", "view", "--text", "SNP/output/tree_tipAlleleCounts.ML.tre"])
    
    return




def Roary(filenames,??parameters,out):##any parameters for ??
	
	return




def BPGA(filenames,??parameters,out):##any parameters for ??
	
	return




def main():
    jobs = {"FastANI": FastANI, "StringMLST": StringMLST, "ChewBBACA": ChewBBACA, "kSNP": kSNP, "Roary": Roary, "BPGA": BPGA}
    choosenOption = sys.argv[1]
    jobs[choosenOption]()

if __name__ == "__main__":
    main()
