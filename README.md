# PYTHON PROGRAMMING LANGUAGE - BIOPHYSICS LABORATORY

These functions are part of the term paper for the Biophysics laboratory exam. In this paper I analyzed the k-core structure of graphs, that were obtained from a set of proteins. The aim of this work was to extract some information about the protein folding process, and structure in general, on the basis of the hydrophobicity values of the amino acids.
In particular I analyzed the set of disordered proteins (Dis Prot) downloaded from http://www.disprot.org, the Protein Disorder Database. The original data format is FASTA. Where each protein is a sequence of letters, the amino acids.

- The data set:

disprot_4.5_fastaA.txt -> The set of disordered proteins in FASTA format.

conta.py, lunghezze.py -> It extracts the distribution of the size of a set of proteins.

distribuzione.py, distribuzione>.py -> It extracts the distribution (and the cumulative distribution) of amino acids in a set of proteins.

- From the protein to the graph:
	
prot4.py -> The method I used to transform a protein into a graph is based on a threshold mechanism. I considered the hydrophobicity value of the amino acids, according two different scales (Kyle-Doolittle and GES), and I put a link between two amino acids if the absolute difference of their hydrophobicity value is below or equal to a certain threshold (SOGLIA). The result is an adjacency matrix, printed on file.

kyle-doolittle-scal.txt, ges-scale.txt -> Hydrophobicity values of amino acids.

- From the graph to the k-core decomposition:

divide_core.py -> Given the matrices (graphs) it evaluates the k-core decomposition of each matrix. The results are printed on file.

1core_matr.py, 1matrice.txt -> The divide_core.py scrip calls for each matrix this other script that performs the k-pruning algorithm on the graph.







