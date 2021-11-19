# TE-gene intersect analysis

We analyzed de novo genome assemblies of 17 caddisflies (Trichoptera) and find strong evidence that transposable element (TE) expansions are the primary drivers of large caddisfly genome sizes. Using an innovative method to examine TEs associated with BUSCO genes, we find that TE expansions have a major impact on protein-coding gene regions with TE-gene associations showing a linear relationship with increasing genome size. 
The following scripts are used as part of a pipeline to analyzed repeat dynamics of BUSCO genes, especially, to quantify shifts in associations between TEs (transposable elements) and genic regions across lineages with varying repeat abundance. 

The pipeline is described in detail in: Genome size evolution in the diverse insect order Trichoptera
Jacqueline Heckenhauer, Paul B. Frandsen, John S. Sproul, Zheng Li, Juraj Paule, Amanda M. Larracuente, Peter J. Maughan, Michael S. Barker, Julio V. Schneider, Russell J. Stewart, Steffen U. Pauls
doi: https://doi.org/10.1101/2021.05.10.443368

The pipeline is described in detail in ``` intersect_analysis_commands.txt ```

``` re_classify_gff_denovo.py ``` 

This script takes the consensi.fa.classified output from repeatmodeler and the gff from RepeatMasker and populates a new gff with the annotations from the consensi.classified.fa file.
Run it with "python re_classify_gff_denovo.py <consensi.fa.classified> <repeatmasker.gff>" and it will write a new gff that ends in "_renamed.gff".
*This script was written by Paul B. Frandsen.*

``` re_classify_gff_denovo.py ``` 

This  script  takes  the  consensi.fa.classified  output  from repeatmodeler and the gfffrom the 1stround of RepeatMasker and populates a new gff with the annotations from the consensi.classified.fa file.
*This script was written by Paul B. Frandsen.*

``` reorder_blast_bed_sense.py ``` 


This script reorders the converted blast output.
*This script was written by Paul B. Frandsen.*

```  RM_table_parser_families_mod4.py ``` 

This script merges output of two repeatmasker runs. Parse the output tables from each of the two RM runs with this script.
*This script was written by John S. Sproul.*

***Input data***

```Custom made libraries from Repeatmodeler.zip```
Files: *consensi.fa.classified: Custom repeat libraries generated from RepeatModeler2 for each respective assembly
We identified and classified repetitive elements in the genome assemblies of each species using RepeatModeler2.0 [114]. 

```Repeatmasker_hints.zip```
Files: *gff3: Repeatmasker hints after first round of Repeatmasker
We annotated repeats in the contamination filtered assemblies with RepeatMasker 4.1.0 (http://www.repeatmasker.org) using the custom repeat libraries generated from RepeatModeler2 for each respective assembly with the search engine set to “ncbi” and using the -xsmall option. We used the perl script rmOutToGFF3.pl from RepeatMasker to convert the Repeatmasker OUT files from each Repeatmasker run to version 3 to gff files containing the RepeatMasker hints. 

```Repeatmasker_hints_species_arthropoda_hard.zip```
Files: *gff3: Repeatmasker hints after first round of Repeatmasker
We used the perl script rmOutToGFF3.pl from RepeatMasker to convert the Repeatmasker OUT files  to version 3 to gff files containing the RepeatMasker hints. 
We converted the softmasked assembly resulting from the first RepeatMasker round into a hardmasked assembly using the lc2n.py script (https://github.com/PdomGenomeProject/repeat-masking). We re-ran RepeatMasker on the hard-masked genome with RepeatMasker’s internal arthropod repeat library using -species “Arthropoda”. We used the perl script rmOutToGFF3.pl from RepeatMasker to convert the Repeatmasker OUT files from each Repeatmasker run to version 3 to gff files containing the RepeatMasker hints. 

```BLAST.zip```
Files: *out: Blast results


