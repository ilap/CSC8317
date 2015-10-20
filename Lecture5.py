__author__ = 'ilap'


#### Set nad dictionaries are unordered and Set cannot have duplicated values...



from Bio import SeqIO

from Bio.Seq import *
from Bio.SeqRecord import *


seq = Seq ("ACTGCTATA")

print seq [:4]


print seq+seq

seq2 = Seq ("MNGTEGPNFYVPFSNATGVVRSPFEYPQYY")

print seq + seq2

dna_seq = Seq ("ACTGCTATA",IUPAC.unambiguous_dna)
prot_seq = Seq ("MNGTEGPNFYVPFSNATGVVRSPFEYPQYY",IUPAC.protein)

seq_record = SeqRecord (prot_seq, id="YP_025292.1", name="HokC", description="toxic membrane protein")

print (seq_record)
#print dna_seq+prot_seq


orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.gbk", "genbank"))

print orchid_dict.keys()

ind_rec = orchid_dict ['Z78484.1']
print ind_rec
#ind_rec.description




