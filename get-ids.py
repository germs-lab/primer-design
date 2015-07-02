import sys

d = {}
for n, line in enumerate(open(sys.argv[1], 'rU')):
    if n > 0:
        dat = line.rstrip().split('\t')
        try: 
            ncbi_id = dat[0].rsplit('|',2)[1]
            assay = dat[1]
            start=int(dat[5])-1
            end=int(dat[6])-1
            if d.has_key(assay):
                continue
            else:
                d[assay]=[ncbi_id,str(start),str(end)]
        except:
            continue

l = []
for line in open(sys.argv[2]):
    l.append(line.rstrip())

for x in l:
    print x, '\t', '\t'.join(d[x])


