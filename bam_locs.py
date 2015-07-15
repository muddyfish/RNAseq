import os, shutil, subprocess
CCLE_DIR = "/lustre/scratch112/sanger/cgppipe/cttv-rnaseq-am26/ccle-fusions/"
TMP_DIR = "/lustre/scratch109/sanger/sb48/"

class Main(object):
    def __init__(self):
        self.samples = dict(map(lambda x: (x[0], x[2]), self.parse_nodups_txt()))
        #for i, sample in enumerate(samples):
        #    print i, len(samples)
        #    self.parse_sample(sample)
        self.parse_sample("HCC1187")

    def parse_nodups_txt(self):
        db_filename = os.path.join(CCLE_DIR, "tracking", "rna-tophat-nodup-bams.txt")
        db_file = open(db_filename)
        samples = []
        for line in db_file.readlines()[1:]:
            samples.append(line.rstrip().split("\t"))
        db_file.close()
        return samples
    
    def parse_sample(self, sample):
        #self.copy_bam(sample)
        self.add_bai(sample)
        self.run_loci(sample)
    
    def copy_bam(self, sample):
        src = self.samples[sample]
        dest = os.path.join(TMP_DIR, sample+".bam")
        shutil.copy2(src, dest)
        print "Sample copied to %s"%(dest)

    def add_bai(self, sample):
        print "Created BAM index file"
    
    def run_loci(self, sample):
        dest = os.path.join(TMP_DIR, sample+".bam")
        tmp_tsv = os.path.join(TMP_DIR, sample)
        cmd = "/software/CGP/projects/wholegenomepipeline/perl/scripts/utilities/multiSampleLoci.pl -f -l %s -b %s -o %s"%(sample+".txt",dest,tmp_tsv)
        sub = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        for i in sub.communicate(): print i
        

def main():
    Main()

if __name__ == "__main__":
    main()
