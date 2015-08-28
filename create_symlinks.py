import os, glob

class Main(object):
    def __init__(self):
        self.exome_dir = "vcf_758_786"
        map(self.parse_sample, glob.glob(os.path.join(self.exome_dir, "*.vcf.gz*")))
    
    def parse_sample(self, src):
        sample_name = os.path.basename(src)
        dst_name = sample_name.split(".")[0]+"_RNA_TCGA."+".".join(sample_name.split(".")[1:])
        dst = os.path.join(self.exome_dir, dst_name)
        try:
            os.unlink(dst)
        except OSError: pass
        src = os.path.realpath(os.readlink(src))
        print src, dst
        os.symlink(src, dst)

def main(): Main()

if __name__ == "__main__":
    main()
