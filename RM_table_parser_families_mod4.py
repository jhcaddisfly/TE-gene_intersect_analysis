import sys

table_filename = sys.argv[1]
outfilename = sys.argv[2]
tandem_repeats = [0, 0.0]
other_repeats = [0,0.0]
accession_key = {}

with open("accession_key_custom.txt") as key:
    for line in key:
        new_line = line.split()
        print(new_line)
        accession_key[new_line[1]] = new_line[0]

repeat_dict = {}
with open(table_filename) as table_file:
    for line in table_file:
        if "total length:" in line:
            new_line = line.split()
            total_bps = new_line[2]
            tot_length = int(total_bps)
        elif "bases masked:" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[2])
            bases_masked = [total_bps, percent]
        elif "file" in line:
            taxon_accession = line.split()[2]
            taxon = accession_key[taxon_accession]
        elif "LINEs:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            lines = [total_bps, percent]
        elif "SINEs:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            sines = [total_bps, percent]
        elif "LTR elements:" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[3])
            ltrs = [total_bps, percent]
        elif "DNA transposons" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[3])
            transposons = [total_bps, percent]
        elif "Satellites:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            satellites = [total_bps, percent]
            #tandem_repeats[0] += int(new_line[2])
            #tandem_repeats[1] += float(new_line[4])/100
        elif "Simple repeats:" in line:
            new_line = line.split()
            #percent = float(new_line[5])/100
            #total_bps = int(new_line[3])
            #simple_repeats = [total_bps, percent]
            other_repeats[0] += int(new_line[3])
            other_repeats[1] += float(new_line[5])/100
        elif "Low complexity:" in line:
            new_line = line.split()
            #percent = float(new_line[5])/100
            #total_bps = int(new_line[3])
            #low_complexity = [total_bps, percent]
            other_repeats[0] += int(new_line[3])
            other_repeats[1] += float(new_line[5])/100
        elif "Penelope" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            penelope = [total_bps, percent]
            #other_repeats[0] += int(new_line[2])
            #other_repeats[1] += float(new_line[4])/100
        elif "Rolling-circles" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            rolling_circles = [total_bps, percent]
            #other_repeats[0] += int(new_line[2])
            #other_repeats[1] += float(new_line[4])/100
        elif "Small RNA:" in line:
            new_line = line.split()
            other_repeats[0] += int(new_line[3])
            other_repeats[1] += float(new_line[5])/100
        elif "Unclassified:" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            unclassified = [total_bps, percent]
        elif "L2/CR1/Rex" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            l2_cr1_rex = [total_bps, percent]
        elif "R1/LOA/Jockey" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            r1_loa_jockey = [total_bps, percent]
        elif "R2/R4/NeSL" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            r2_r4_nesl = [total_bps, percent]
        elif "RTE/Bov-B" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            rte_bov_b = [total_bps, percent]
        elif "L1/CIN4" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            l1_cin4 = [total_bps, percent]
        elif "CRE/SLACS" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            cre_slacs = [total_bps, percent]
        elif "BEL/Pao" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            bel_pao = [total_bps, percent]
        elif "Ty1/Copia" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            ty1_copia = [total_bps, percent]
        elif "Gypsy/DIRS1" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            gypsy_dirs1 = [total_bps, percent]
        elif "hobo-Activator" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            hobo_activator = [total_bps, percent]
        elif "Tc1-IS630-Pogo" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            tc1_is630_pogo = [total_bps, percent]
        elif "En-Spm" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            en_spm = [total_bps, percent]
        elif "MuDR-IS905" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            mudr_is905 = [total_bps, percent]
        elif "PiggyBac" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            piggybac = [total_bps, percent]
        elif "Tourist/Harbinger" in line:
            new_line = line.split()
            percent = float(new_line[4])/100
            total_bps = int(new_line[2])
            tourist_harbinger = [total_bps, percent]
        elif "Other (Mirage," in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[2])
            mirage_p_element_transib = [total_bps, percent]
        #added to simplify calculation of total categorized repeats (which is different than total bases masked)
        elif "Total interspersed repeats" in line:
            new_line = line.split()
            percent = float(new_line[5])/100
            total_bps = int(new_line[3])
            total_interspersed = [total_bps, percent]

total_reps = other_repeats[0]+tandem_repeats[0]+sines[0]+lines[0]+ltrs[0]+transposons[0]+unclassified[0]
#print(total_reps)

#Total interspersed repeats + Rolling-circles + small RNA + Satellites + Simple repeats + Low complexity
#other = penelope, Rolling cir, small rnas
#tandem = satellites, simple, low-complexity
#add SINEs, LINEs, LTRs, DNA trans, unclassified

with open(outfilename, "a") as outfile:
    outfile.write(taxon + "\t" + str(lines[0]) + "\t" + str(lines[1]) + 
            "\tz_LINEs\n" +
        taxon + "\t" + str(sines[0]) + "\t" + str(sines[1]) + "\tx_SINEs\n" +
        taxon + "\t" + str(ltrs[0]) + "\t" + str(ltrs[1]) + "\ty_LTRs\n" +
        taxon + "\t" + str(transposons[0]) + "\t" + str(transposons[1]) + 
            "\tw_DNA_transposons\n" +
        taxon + "\t" + str(penelope[0]) + "\t" + str(penelope[1]) + 
            "\tv_penelope\n" +
        taxon + "\t" + str(rolling_circles[0]) + "\t" + str(rolling_circles[1]) + 
            "\tu_rolling_circles\n" +
        taxon + "\t" + str(satellites[0]) + "\t" + str(satellites[1]) + 
            "\tt_satellites\n" +
        taxon + "\t" + str(other_repeats[0]) + "\t" + str(other_repeats[1]) + 
            "\ts_Other_repeats\n" +
        taxon + "\t" + str(unclassified[0]) + "\t" + str(unclassified[1]) + 
            "\tr_Unclassified_repeats\n" +
        taxon + "\t" + str(tot_length - int(bases_masked[0])) + "\t" + 
            str((tot_length - int(bases_masked[0]))/float(tot_length)) + 
            "\tq_Unique_low_repeat\n")


#New block that leaves unique out and calculates a proportion of total repeats for each category and not the total bases in the whole assembly
with open("prop_repeat_families.txt", "a") as prop_outfile:
    prop_outfile.write(taxon + "\t" + str(lines[0]) + "\t" + str((lines[0])/(total_reps)) + 
            "\tLINEs\n" +
        taxon + "\t" + str(sines[0]) + "\t" + str((sines[0])/(total_reps)) + "\tSINEs\n" +
        taxon + "\t" + str(ltrs[0]) + "\t" + str((ltrs[0])/(total_reps)) + "\tLTRs\n" +
        taxon + "\t" + str(transposons[0]) + "\t" + str((transposons[0])/(total_reps)) + 
            "\tDNA_transposons\n" +
        taxon + "\t" + str(tandem_repeats[0]) + "\t" + str((tandem_repeats[0])/(total_reps)) + 
            "\ttandem_repeats\n" +
        taxon + "\t" + str(other_repeats[0]) + "\t" + str((other_repeats[0])/(total_reps)) + 
            "\tOther_repeats\n" +
        taxon + "\t" + str(unclassified[0]) + "\t" + str((unclassified[0])/(total_reps)) + 
            "\tUnclassified_repeats\n") #+
        #taxon + "\t" + str(tot_length - int(total_reps)) + "\t" + 
            #str((tot_length - int(bases_masked[0]))/float(tot_length)) + 
            #"\tUnique_low_repeat\n")


#JSS modified, rather than print genome proportion in third column, now prints proportion of LINEs (now it divides total bases for a given category by total LINEs)
with open("line_repeat_families.txt", "a") as line_outfile:
    line_outfile.write(taxon + "\t" + str(l2_cr1_rex[0]) + "\t" + 
        str((l2_cr1_rex[0])/(lines[0])) + "\tL2/Cr1/Rex\n")
    line_outfile.write(taxon + "\t" + str(l1_cin4[0]) + "\t" + str((l1_cin4[0])/(lines[0])) +
        "\tL1/CIN4\n")
    line_outfile.write(taxon + "\t" + str(r1_loa_jockey[0]) + "\t" + str((r1_loa_jockey[0])/(lines[0])) +
        "\tR1/LOA/Jockey\n")
    line_outfile.write(taxon + "\t" + str(r2_r4_nesl[0]) + "\t" + str((r2_r4_nesl[0])/(lines[0])) +
        "\tR2/R4/NeSL\n")
    line_outfile.write(taxon + "\t" + str(rte_bov_b[0]) + "\t" + str((rte_bov_b[0])/(lines[0])) +
        "\tRTE/Bov-B\n")
    line_outfile.write(taxon + "\t" + str(cre_slacs[0]) + "\t" + str((cre_slacs[0])/(lines[0])) +
        "\tCRE/SLACS\n")
    other_lines = [lines[0] - (l2_cr1_rex[0] + l1_cin4[0] + r1_loa_jockey[0] + 
        r2_r4_nesl[0] + rte_bov_b[0] + cre_slacs[0]), lines[1] - 
        (l2_cr1_rex[1] + l1_cin4[1] + r1_loa_jockey[1] + r2_r4_nesl[1] + 
            rte_bov_b[1] + cre_slacs[1])]
    line_outfile.write(taxon + "\t" + str(other_lines[0]) + "\t" + str((other_lines[0])/(lines[0])) +
        "\tOther_LINEs\n")

with open("ltr_repeat_families.txt", "a") as ltr_outfile:
    ltr_outfile.write(taxon + "\t" + str(gypsy_dirs1[0]) + "\t" + 
        str((gypsy_dirs1[0])/(ltrs[0])) + "\tGypsy/DIRS1\n")
    ltr_outfile.write(taxon + "\t" + str(ty1_copia[0]) + "\t" + str((ty1_copia[0])/(ltrs[0])) +
        "\tTy1/Copia\n")
    ltr_outfile.write(taxon + "\t" + str(bel_pao[0]) + "\t" + str((bel_pao[0])/(ltrs[0])) +
        "\tBEL/Pao\n")
    other_ltrs = [ltrs[0] - (gypsy_dirs1[0] + ty1_copia[0] + bel_pao[0]), 
        ltrs[1] - (gypsy_dirs1[1] + ty1_copia[1] + bel_pao[1])]
    ltr_outfile.write(taxon + "\t" + str(other_ltrs[0]) + "\t" + str((other_ltrs[0])/(ltrs[0])) +
        "\tOther_LTRs\n")

with open("dna_transposon_repeat_families.txt", "a") as dnat_outfile:
    dnat_outfile.write(taxon + "\t" + str(hobo_activator[0]) + "\t" + 
        str((hobo_activator[0])/(transposons[0])) + "\thobo-Activator\n")
    dnat_outfile.write(taxon + "\t" + str(tc1_is630_pogo[0]) + "\t" + str((tc1_is630_pogo[0])/(transposons[0])) +
        "\tTc1-IS630-Pogo\n")
    dnat_outfile.write(taxon + "\t" + str(en_spm[0]) + "\t" + str((en_spm[0])/(transposons[0])) +
        "\tEn-Spm\n")
    dnat_outfile.write(taxon + "\t" + str(mudr_is905[0]) + "\t" + str((mudr_is905[0])/(transposons[0])) +
        "\tMuDR-IS905\n")
    dnat_outfile.write(taxon + "\t" + str(piggybac[0]) + "\t" + str((piggybac[0])/(transposons[0])) +
        "\tPiggyBac\n")
    dnat_outfile.write(taxon + "\t" + str(tourist_harbinger[0]) + "\t" + str((tourist_harbinger[0])/(transposons[0])) +
        "\tTourist/Harbinger\n")
    dnat_outfile.write(taxon + "\t" + str(mirage_p_element_transib[0]) + "\t" + 
        str(mirage_p_element_transib[1]) + "\tMirage, P-element, Transib\n")
    other_dnats = [transposons[0] - (hobo_activator[0] + tc1_is630_pogo[0] + en_spm[0] + 
        mudr_is905[0] + piggybac[0] + tourist_harbinger[0] + mirage_p_element_transib[0]), 
        transposons[1] - (hobo_activator[1] + tc1_is630_pogo[1] + en_spm[1] + mudr_is905[1] + 
            piggybac[1] + tourist_harbinger[1] + mirage_p_element_transib[1])]
    dnat_outfile.write(taxon + "\t" + str(other_dnats[0]) + "\t" + str((other_dnats[0])/(transposons[0])) +
        "\tOther_DNA\n")
#there were two errors in previous block statement, called variable "lines" and "other_lines" instead of "transposons" and "other_dnats"
