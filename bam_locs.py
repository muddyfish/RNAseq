import os, shutil
CCLE_DIR = "/lustre/scratch112/sanger/cgppipe/cttv-rnaseq-am26/ccle-fusions/"
DEST = "/lustre/scratch109/sanger/sb48/"

class Main(object):
    def __init__(self):
        samples = self.parse_nodups_txt())
        for i, sample in enumerate(samples):
            print i, len(samples)
            self.parse_sample(sample)

    def parse_nodups_txt(self):
        db_filename = os.path.join(CCLE_DIR, "tracking", "rna-tophat-nodup-bams.txt")
        db_file = open(db_filename)
        samples = []
        for line in db_file.readlines()[1:]:
            samples.append(line.rstrip().split("\t"))
        db_file.close()
        return samples
    
    def parse_sample(self, sample):
        src = sample[2]
        dest = os.path.join(DEST, sample[0]+".bam")
        shutil.copy2(src, dst)

def main():
    Main()

if __name__ == "__main__":
    main()
