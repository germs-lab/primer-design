import screed, sys

start = int(sys.argv[2])
end = int(sys.argv[3])

for record in screed.open(sys.argv[1]):
    name = record.name
    sequence = record.sequence
    #print sequence.find("CGTCACTTATTCGATGCCCTTAC")
    #print sequence.find("CGTCACTTATTCGATGCCCTTAC")
    print sequence[start:end+1]
