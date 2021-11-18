import sys

infilename = sys.argv[1]
outfilename = infilename + "_renamed.gff"

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
                else:
                    outfile.write("\t".join(new_line[:2]) + "\t" + classification + "\t" + "\t".join(new_line[3:]))
