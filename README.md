# TE-gene intersect analysis

We analyzed de novo genome assemblies of 17 caddisflies (Trichoptera) and find strong evidence that transposable element (TE) expansions are the primary drivers of large caddisfly genome sizes. Using an innovative method to examine TEs associated with BUSCO genes, we find that TE expansions have a major impact on protein-coding gene regions with TE-gene associations showing a linear relationship with increasing genome size. 
The following scripts are used as part of a pipeline to analyzed repeat dynamics of BUSCO genes, especially, to quantify shifts in associations between TEs (transposable elements) and genic regions across lineages with varying repeat abundance. 

The pipeline is described in detail in: Genome size evolution in the diverse insect order Trichoptera
Jacqueline Heckenhauer, Paul B. Frandsen, John S. Sproul, Zheng Li, Juraj Paule, Amanda M. Larracuente, Peter J. Maughan, Michael S. Barker, Julio V. Schneider, Russell J. Stewart, Steffen U. Pauls
doi: https://doi.org/10.1101/2021.05.10.443368

***Backgroud***
During the early exploration of our sequence data we noted that copy number profiles of some BUSCO genes showed regions of unexpected high copy number with the frequency of such genes varying widely across species. Following this observation we analyzed repeat dynamics of all BUSCO genes for all species to quantify the abundance of repetitive BUSCOs across samples and test two alternative hypotheses that could account for the observed patterns: (1.) inflated copy-number of BUSCO gene fragments occur at sequences of repetitive elements (e.g., TEs) inserted into genes; (2.) inflated regions are BUSCO gene fragments that have proliferated throughout the genome (e.g., by hitch-hiking with TEs. This analysis also allowed us to quantify shifts in associations between TEs and genic regions across Trichoptera lineages with varying repeat abundance.

***Methods***
We identified and classified repetitive elements in the genome assemblies of each species using RepeatModeler2.0 [114]. We annotated repeats in the contamination filtered assemblies with RepeatMasker 4.1.0 (http://www.repeatmasker.org) using the custom repeat libraries generated from RepeatModeler2 for each respective assembly with the search engine set to “ncbi” and using the -xsmall option. 
We converted the softmasked assembly resulting from the first RepeatMasker round into a hardmasked assembly using the lc2n.py script (https://github.com/PdomGenomeProject/repeat-masking). Finally, we re-ran RepeatMasker on the hard-masked genome with RepeatMasker’s internal arthropod repeat library using -species “Arthropoda”. We then merged RepeatMasker output tables from both runs by parsing them with a script (**RM_table_parser_families_mod4.py**) and then combined the resulting data columns for the two runs in Excel. 
We generated copy number profiles of all Endopterygota BUSCO genes (OrthoDB v.9) for all study species using RepeatProfiler [32]. We quantified the abundance of BUSCOs with repetitive fragments by identifying BUSCO genes with coverage peak that exceeded 20X average coverage for all BUSCO genes in that species. Average coverage was calculated by averaging coverage depth of all BUSCO genes after excluding the top and bottom 15% when sorted by max coverage which eliminated 0-coverage and unexpectedly high-coverage BUSCOs from the calculation. After producing a BLAST database from each genome assembly using the application makeblastdb in ncbi-blast 2.10.0 [33] applying the parameters -dbtype nucl, -parse_seqids_blastdb, -blastdb_version5, we quantify the genomic abundance of bases in repetitive BUSCOs by using each repetitive BUSCO as a query in a BLAST (blastn) search against the genome assembly with the following settings:  outfmt 6, -max_target_seqs 50000. We allowed 50K hits based on the maximum coverage of repetitive BUSCOS observed in profiles. We used the perl script rmOutToGFF3.pl from RepeatMasker to convert the Repeatmasker OUT files from each Repeatmasker run to version 3 to gff files containing the RepeatMasker hints. We reclassified the repeats in the gff3 files with custom scripts, concatenated the two RepeatMasker runs of each species and sorted the resulting file using bedtools.
We used custom scripts to parse BLAST output, collapse hits with overlapping coordinates and extract coordinates of filtered hits. For each unique BLAST hit, we then asked whether it mapped to masked or unmasked coordinates in the assembly by cross-referencing the coordinates of BLAST hits against a gff file containing RepeatMasker annotations using the ‘intersect’ function in BEDTools. We also used custom scripts to calculate the total number of bases in filtered BLAST after subtracting the number of bases at the locus belonging to all ‘complete’ BUSCO genes, and to categorize BUSCO repeats based on their annotation status and repeat classification. We plotted the number of BUSCO repeats belonging to repetitive element categories (i.e., classes and subclasses) alongside plots of the relative genomic abundance of each respective category.

An example for running the pipeline is given in ``` intersect_analysis_commands.txt ```

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
We annotated repeats in the contamination filtered assemblies with RepeatMasker 4.1.0 (http://www.repeatmasker.org) using the custom repeat libraries generated from RepeatModeler2 for each respective assembly with the search engine set to “ncbi” and using the -xsmall option. 
We used the perl script rmOutToGFF3.pl from RepeatMasker to convert the Repeatmasker OUT files  to version 3 to gff files containing the RepeatMasker hints. 

```Repeatmasker_hints_species_arthropoda_hard.zip```
Files: *gff3: Repeatmasker hints after first round of Repeatmasker
We used the perl script rmOutToGFF3.pl from RepeatMasker to convert the Repeatmasker OUT files  to version 3 to gff files containing the RepeatMasker hints. 
We converted the softmasked assembly resulting from the first RepeatMasker round into a hardmasked assembly using the lc2n.py script (https://github.com/PdomGenomeProject/repeat-masking). We re-ran RepeatMasker on the hard-masked genome with RepeatMasker’s internal arthropod repeat library using -species “Arthropoda”. We then merged RepeatMasker output tables from both runs by parsing them with a script (**RM_table_parser_families_mod4.py**).

```BLAST.zip```
Files: *out: Blast results


