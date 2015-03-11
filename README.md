# PYTHON PROGRAMMING LANGUAGE - BIOPHYSICS LABORATORY

These functions are part of the term paper for the Biophysics laboratory exam. In this paper I analyzed the k-core structure of graphs, that were obtained from a set of proteins.
In particular I analyzed the set of disordered proteins (Dis Prot) taken from http://www.disprot.org, the Protein Disorder Database. The original data format is FASTA. Where each protein is a sequence of letters, the amino acids.

- The data set:

disprot_4.5_fastaA.txt -> The set of disordered proteins in FASTA format.

- From the protein to the graph:
	
prot4.py -> The method I used to transform a protein into a graph is based on a threshold mechanism. I considered the hydrophobicity value of the amino acids, according two different scales (Kyle-Doolittle and GES), and I put a link between two amino acids if the absolute difference of their hydrophobicity value is below or equal to a certain threshold (SOGLIA).
