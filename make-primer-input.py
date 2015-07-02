import sys

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    id = dat[0]
    seq = dat[4]
    fp = open(id.rstrip() + '.primer3', 'w')
    fp.write('SEQUENCE_ID=%s\n' % id)
    fp.write('SEQUENCE_TEMPLATE=%s\n' % seq)
    fp.write('PRIMER_TASK=pick_pcr_primers\nPRIMER_OPT_SIZE=27\nPRIMER_MIN_SIZE=22\nPRIMER_MAX_SIZE=30\nPRIMER_MIN_TM=55\nPRIMER_OPT_TM=59\nPRIMER_MAX_TM=100\nPRIMER_MIN_GC=15\nPRIMER_OPT_GC_PERCENT=47\nPRIMER_MAX_GC=80\nPRIMER_MAX_NS_ACCEPTED=0\nPRIMER_MAX_POLY_X=5\nPRIMER_PRODUCT_SIZE_RANGE=58-700\nP3_FILE_FLAG=1\nPRIMER_EXPLAIN_FLAG=1\n=')
