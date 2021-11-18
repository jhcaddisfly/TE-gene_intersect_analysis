import sys

inbed_filename = sys.argv[1]
outbed_filename = sys.argv[2]

with open(inbed_filename) as inbed_file:
    with open(outbed_filename, "w") as outbed_file:
        for count, line in enumerate(inbed_file):
            new_line = line.split("\t")
            if int(new_line[1]) > int(new_line[2]):
                outbed_file.write(new_line[0] + "\t" + str(int(new_line[2].strip()) - 1)
                 + "\t" + new_line[1] + "\t" + "." + "\t" + "100" + "\t" + "-" + "\n")
            else:
                outbed_file.write(new_line[0] + "\t" + str(int(new_line[1]) - 1) + "\t" 
                    + new_line[2].strip() + "\t" + "." + "\t" + "100" + "\t" + "+" + "\n")
