import os, glob

class Main(object):
    def __init__(self):
        self.bam_dir = "1085_out"
        self.exome_dir = "758_and_786_out"
        map(self.parse_sample, glob.glob(os.path.join(self.exome_dir, "*.vcf.gz*")))
    
    def parse_sample(self, src):
        sample_name = os.path.basename(src)
        dst = os.path.join(self.bam_dir, sample_name)
        print src, dst
        try:
            os.unlink(dst)
        except OSError: pass
        src = os.path.realpath(os.readlink(src))
        print src, dst
        os.symlink(src, dst)

def main(): Main()

if __name__ == "__main__":
    main()

"/software/CGP/projects/vcfCommons/perl/bin/mergeAndPileup.pl -i 1085_out/1085_VcfMergeConfig.ini -d 1085_out/ -a snp -s 1 -o 1085_vcfout  -f cave_java &"
