import os, glob

class Main(object):
    def __main__(self):
        self.bam_dir = "1085_out"
        print glob.glob(os.path.join(self.bam_dir, "*.bam"))
        print os.path.join(self.bam_dir, "*.bam")

def main(): Main()

if __name__ == "__main__": main()
