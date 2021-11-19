# TE-gene intersect analysis

These scripts are used as part of a pipeline to analyzed repeat dynamics of BUSCO genes, especially, to quantify shifts in associations between TEs (transposable elements) and genic regions across lineages with varying repeat abundance. 

The pipeline is described in detail in: Genome size evolution in the diverse insect order Trichoptera
Jacqueline Heckenhauer, Paul B. Frandsen, John S. Sproul, Zheng Li, Juraj Paule, Amanda M. Larracuente, Peter J. Maughan, Michael S. Barker, Julio V. Schneider, Russell J. Stewart, Steffen U. Pauls
doi: https://doi.org/10.1101/2021.05.10.443368

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

