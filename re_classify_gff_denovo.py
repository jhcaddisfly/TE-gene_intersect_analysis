# This script takes the consensi.fa.classified output from repeatmodeler and the gff from RepeatMasker
# and populates a new gff with the annotations from the consensi.classified.fa file.
# Run it with "python re_classify_gff_denovo.py <consensi.fa.classified> <repeatmasker.gff>" and it
# will write a new gff that ends in "_renamed.gff"

import sys

consensi_filename = sys.argv[1]
infilename = sys.argv[2]
outfilename = infilename + "_renamed.gff3"

repeat_dict = {}

with open(consensi_filename) as consensi_file:
    for line in consensi_file:
        if line[0] == ">":
            new_line = line.split("#")
            repeat_dict[new_line[0][1:]] = new_line[1].split()[0]

print(repeat_dict)

with open(infilename) as infile:
    with open(outfilename, "w") as outfile:
        for line in infile:
            if line[:2] == "##":
                outfile.write(line)
            else:
                new_line = line.split("\t")
                classification = new_line[8].split("=")[1].split()[0]
                if "(" in classification:
                    outfile.write("\t".join(new_line[:2]) + "\t" + "simple_repeat" + "\t" + "\t".join(new_line[3:]))
                elif classification in repeat_dict:
                    outfile.write("\t".join(new_line[:2]) + "\t" + repeat_dict[classification] + "\t" + "\t".join(new_line[3:]))
                else:
                    outfile.write("\t".join(new_line[:2]) + "\t" + classification + "\t" + "\t".join(new_line[3:]))
