from BlastHit import BlastHit
from DiffExp import DiffExp
from Blast import Blast
from Matrix import Matrix

def tuple_to_string(tup):
    '''
    A function that will accept a tuple and return it as a tab-separated string
    Args:
        tup: a tuple
    Returns:
        A tab-separated string
    '''
    return '\t'.join(tup)

FP1 = open(<'BLAST file'>, 'r')
FP2 = open(<'trinity assembly matrix'>, 'r')

blast = []
for line in FP1:
    temp = line.strip().split()
    trID = temp[0].split('|')[0]
    SPID = temp[1].split('|')[3].split('.')[0]
    Idy = float(temp[2])
    msm = temp[4]
    #print(SPID)
    bh = BlastHit(trID, SPID, Idy, msm)
    blast.append(bh)
FP1.close

expressions = []
FP2.readline()
for line in FP2:
    temp = line.strip().split()
    trID = temp[0]
    dShift = temp[1]
    hShock = temp[2]
    loggrowth = temp[3]
    pphase = temp[4]
    dxp = DiffExp(trID, dShift, hShock, loggrowth, pphase)
    expressions.append(dxp)
FP2.close

objblast = Blast(blast)
objmatrix = Matrix(expressions)

'''
Load the BlastHit objects that are good matches into a dictionary
'''
goodblasthits = {}
for item in objblast:
    if item.good_match():
        goodblasthits[item.TranscriptID] = item.SwissProtID

'''
create an output file
'''
FP3 = open("Output.txt", 'w')
FP3.write('{}\t{}\t{}\t{}\t{}\n'.format('','Sp_ds','Sp_hs', 'Sp_log', 'Sp_plat'))

'''
Perform a transcript-to-protein lookup for each DiffExp object
'''
for item in objmatrix:
    if item.transcript in goodblasthits:
        FP3.write(goodblasthits[item.transcript] + '\t' + tuple_to_string(item.return_attribs())+'\n')
    else:
        FP3.write(item.transcript + '\t' + tuple_to_string(item.return_attribs())+'\n')
FP3.close()
