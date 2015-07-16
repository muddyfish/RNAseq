TSV = "/nfs/cancer_translation/Sequenom_and_STR_analysis_of_cell_lines/Data_for_CORE_Cell_lines/Lines_Data/Variants/Cell_Line_Data/RNA-seq/COSMIC_Variants/CosmicCLP_MutantExport.tsv"

class CreateBed(object):
    def __init__(self):
        tsv_f = open(TSV)
        for line in tsv_f.readlines()[1:]:
            parts = line.split("\t")
            fiddle = not bool(parts[18].find(":")+1)
            chromosome_id, pos = parts[18+fiddle].split(":")
            pos = map(int, pos.split("-"))
            rep = parts[13+fiddle]
            cosmic_id = parts[12+fiddle]
            if rep[-2] != ">": continue
            rep = rep[-3], rep[-1]
            print chromosome_id, pos[0], rep[0], rep[1], cosmic_id
        tsv_f.close()

def main(): CreateBed()

if __name__ == "__main__": main()
