## Team3-ComparativeGenomics 
We use tools from different levels to compare Listeria Monocytogenes isolates.
## Usage
This pipeline is specific for BIOL7210 group project. We have 6 tool avaliable which are listed below. Run on command line by choosing a tool. e.g., <./tool_functions FastANI> will only run FastANI, and output ANI scores.

## FastANI
Average Nucleotide Level, input fasta file, output ANI score.
## StringMLST
7-gene-mlst, input fasta file, output mlst allele matrix.
## ChewBBACA
Phylogeny level-cgMLST, input fastq file, output allele matrix, Genome Quality plot, results_statistics.tsv, results_contigsinfo.tsv.
## kSNP
Phylogeny level-SNP-based, input is a txt file with a list of paths to fasta files, output tipAlleleCounts maximum likelihood phylogentics tree.
## Roary
Pan-genome analysis
## BPGA
Pan-genome analysis

## Installation and Setup
## mini conda??
## environment setup??


## dendogram.py
*This script uses -w flag with input for working directory where respective files with annotations are stored. -f flag is 1 if the files are just genes list from CARD and VFDB annotations, and is 0 when using merged GFF files are present in working directory. 

