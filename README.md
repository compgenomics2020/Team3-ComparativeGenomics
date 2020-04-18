## Team3-ComparativeGenomics 
We use tools from different levels to compare Listeria Monocytogenes isolates.
## Usage
This pipeline is specific for BIOL7210 group project. We have 6 tool avaliable which are listed below. Run on command line by choosing a tool. e.g., <./tool_functions FastANI> will only run FastANI, and output ANI scores.

## FastANI
Average Nucleotide Level, input fasta file, output ANI score.
## StringMLST
7-gene-mlst, input fastq file, output mlst allele matrix.
## ChewBBACA
Phylogeny level-cgMLST, input fasta file, output allele matrix, Genome Quality plot, results_statistics.tsv, results_contigsinfo.tsv.
## kSNP
Phylogeny level-SNP-based, input is a txt file with a list of paths to fasta files, output tipAlleleCounts maximum likelihood phylogentics tree.
## Roary
Pan-genome analysis
## BPGA
Pan-genome analysis
## Installation and Setup
The tools FastANI, StringMLST, ChewBBACA, kSNP, Roary, BPGA are installed using mini conda environment and manual installations in the server.
## environment setup
Miniconda environment for Linux 64-bit is set up in the server, with Python version 3.7. The tools installed in the T3env4 are :
FastANI v1.3
Roary v3.13.0
Ete3 v3.1.1
r 3.6.0
ggplot2 v3.1.1
gnuplot v5.2.7
The T3env has the tool kSNP v3.1
## dendogram.py
*This script uses -w flag with input for working directory where respective files with annotations are stored. -f flag is 1 if the files are just genes list from CARD and VFDB annotations, and is 0 when using merged GFF files are present in working directory. 

