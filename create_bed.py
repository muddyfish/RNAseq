TSV = "/nfs/cancer_translation/Sequenom_and_STR_analysis_of_cell_lines/Data_for_CORE_Cell_lines/Lines_Data/Variants/Cell_Line_Data/RNA-seq/COSMIC_Variants/CosmicCLP_MutantExport.tsv"

class CreateBed(object):
    def __init__(self):
        #Open the tsv file
        tsv_f = open(TSV)
        line_id = 0
        for line in tsv_f.readlines()[1:]:
            parts = line.split("\t")
            #Does the line have an extra field?
            fiddle = not bool(parts[18].find(":")+1)
            chromosome_id, pos = parts[18+fiddle].split(":")
            pos = map(int, pos.split("-"))
            rep = parts[13+fiddle]
            cosmic_id = parts[28+fiddle]
            if rep[-2] != ">": continue
            rep = rep[-3], rep[-1]
            #print parts
            print "\t".join(map(str, (chromosome_id, pos[0], rep[0], rep[1])))
            if line_id == -1:
                exit()
            line_id+=1
        tsv_f.close()

def main(): CreateBed()

if __name__ == "__main__": main()
