import glob, os, re, csv, subprocess

def reglob(exp, path="."):
    """
    Returns all files and directories on PATH that conform to the
    regular expression EXP
    """
    m = re.compile(exp)
    res = [f for f in os.listdir(path) if m.search(f)]
    res = map(lambda x: "%s/%s" % ( path, x, ), res)
    return res

def copy_sample(project_id, sample, sample_path, file_type):
    """
    Try to merge the sample SAMPLE in PROJECT_ID with matching exome samples.
    """
    if file_type.lstrip() == "bam" and len(project_id) != 3: # Only merge bam files in projects 1085,1088,1156
        sample_type = tsv_path.split("_")[0]
        #Get the correct path on RNASEQ
        rnaseq_path = glob.glob("%s_%sout/output/%s_%s_*_%s.tsv"%(project_id,sample_type, project_id, sample, sample_type))
        #Sometimes it doesn't exist
        if rnaseq_path:
            for exome_path in reglob("\A\d{3}_%sout"%sample_type):
                #For each path on the samples 758 and 788
                exome_id = exome_path.split("_")[0][2:]
                #Get the path to the exome data
                exome_full = glob.glob("%s/output/%s_%s_*_%s.tsv"%(exome_path, exome_id, sample, sample_type))
                #If it exists:
                if exome_full:
                    rnaseq_path = rnaseq_path[0]
                    exome_full = exome_full[0]
                    hdr_id = {"snp": 57, "indel": 47} #Header lengths for snp and indel files are different
                    #Generate the command to merge samples
                    cmd = "perl merge2files.pl -f1 %s -f2 %s -c1 3,4 -c2 3,4 -hdr %d"%(rnaseq_path, exome_full, hdr_id[sample_type])
                    print cmd
                    subprocess.call(cmd, shell=True)


paths = reglob(r"^\d{4}")

tsv_paths = ["indel_paths.tsv", "snp_paths.tsv"]
for tsv_path in tsv_paths:
    with open(tsv_path) as tsv_in:
        #TSV files are really csv files
        for row in list(csv.reader(tsv_in, delimiter='\t'))[1:]:
            project_id, sample, sample_path, file_type = [i for i in row if i.rstrip()!=""]
            #Remove _RNA_TCGA because some samples don't have it
            sample = sample.replace("_RNA_TCGA", "")
            if len(project_id) == 3: #indel_paths lists samples 758 and 786.
                for project_id in ["1085","1088","1156"]:
                    copy_sample(project_id, sample, sample_path, file_type)
            else:
                copy_sample(project_id, sample, sample_path, file_type)
