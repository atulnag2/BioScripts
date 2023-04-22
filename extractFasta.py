import sys
import re
import subprocess


if len(sys.argv) < 3:
	print("usage: python3 extractFasta.py <id list> <fasta db> <output>")
	sys.exit(1)

idFile = sys.argv[1]
fastaFile = sys.argv[2]
outFile = sys.argv[3]

fdb = {}
header = ''
seq = ''


idlist = []

with open(idFile) as IDS:
	for line in IDS:
		line = line.strip()
		idlist.append(line)

with open(fastaFile) as FASTA:
	for line in FASTA:
		if line.startswith(">"):
			if header != '' and seq != '':
				fdb[header] = seq
				seq = ''
				header = line
			else:
				header = line
		else:
			seq = seq + line
	fdb[header] = seq


with open(outFile,"w") as OUT:
	for id in idlist:
		for key in fdb.keys():
			if id in key:
				OUT.write(key+fdb[key])
