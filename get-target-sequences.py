import sys, screed

d = {}
for record in screed.open(sys.argv[1]):
    ncbi_id = record.name.split(' ')[0].rsplit('|',2)[1]
    seq = record.sequence
    d[ncbi_id] = seq

for line in open(sys.argv[2]):
    assay, ncbi, start, end = line.rstrip().split('\t')
    start = int(start)
    end = int(end)
    target = d[ncbi][start:end]
    new_dat = [assay, ncbi, str(start), str(end), target]
    print '\t'.join(new_dat)
