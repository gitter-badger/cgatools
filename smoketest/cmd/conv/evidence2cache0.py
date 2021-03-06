#! /usr/bin/env python

# Copyright 2010 Complete Genomics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License. You
# may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.


import os,sys
sys.path = [ os.path.dirname(os.path.dirname(sys.argv[0])) ] + sys.path
from tutil import tucore as tc

idir = sys.argv[1]
odir = sys.argv[2]
cgatools = sys.argv[3]
cgatoolsapitest = sys.argv[4]

#####################################################################
# END BOILERPLATE
#####################################################################

from os.path import join as pjoin
import shutil

ref9719767_9721767 = """
AATTCTGAGAAACTTCTTTGTGAGGGTTGGATTCATTTCACACATTTGAA
CATTTCTTTGATTGAAGATTTGGAAACAGTCTTTTTGTAAAATCTATAAA
GGGATAATTGTGAACCCTTTGAGGCCTAGGGTGAAGTAGGAAATATCTTC
ACATAAAAACTACACAGAAATTTTCTGAGAAACGTTTTAGTGATGCGTGC
ATTCATCTCACAGAGTTGAACCTTTCCTTTGCTAGAGCACTTTGGAAACA
GTCCTATTGTAGAATCCCCAAAGGAATACTTCTCAGCCGATTGAGGCCTT
TGGTGATATTGGAAATATCTTCACATAAAAGCTAGACAGAAACTTTCTGA
GAAACTTATTTTTAATGAGTGCTCTCATCTCAAAGAGTTAAGTGTTTCTT
TTGAATGAGCAGTTTGGAAACACTCTTTTTGCATAATCTGCAAATGGATA
ATTGGAGCGTTTTGAGGCCTATGGTGAAAAAGGAAATATCTTCACATAAA
AACTAAACAGAAGCTTTCTGAGAAACTACTTTGTAATGTGTGCATTCATC
TCACAGCGTTGAAAACTTCTTTTGATTGAGCAGTTTGTAAACAGTCTTTT
TTGTAGAATCTGCAAATGGGTATTTGGAGTGCTCTGAGTTCTATAGTGAA
AAAGGAAATATCTTCCAAAAAAAACTAGAAAGAAACATTCTGAGAAACTT
CTTTGTGATATGTACTTTCATCTCACAGAGTTGAACCTTTCTTTTCATTG
AGCAGTTTGGAAACAGACTTTTTATAGAATCTGGAAATGCATATTTGGAG
AGCTTTGAGGCCTATGGAGAAAAAGGAAATATCTTCAGATAAACACTAAA
CAGAAGCTTTCTGAGAAACTTCTTTGTGATGTCTGCATTCATATCACAGA
GCTGAAACTTTCTTTTGATTTAGCAGTTTGTAAACAGTCTTTTGGTAGAA
TCTGCAAATAGATACTTGGAGTGCTTTGAGGCCTATGTTGAAAAAGGAAA
TATCTTCACAAAAAATCTAGAAAGATACATTCTGAGAAACTTCTTTGTGA
TGTGTGTTTTCACCTCACAGAGTTGAAACTTTCTTTTCATTGAGCAACTT
GGAAACAGTCTTTTTGTGGAATCTGCAAATGGATATTTGGAGCGCTTTGA
GGCTTGTGGTGAAAAAGGAAATATCTCATGTAAACCCTAGACAGAAGTAT
TCTGAGAAACTTCTTTGTATTGTGTCCATTCATCTCACAGAGTTGAAACT
TTCTTTGGATTGAGCAGTTTGGAAATAGTCTTTTTGTAGAATCTGTGAAA
AATATTTTTGGGCCCTTTATGGCCCATGGTGAAACAGAAAATATCCTCAA
AGAAAAACTAGACATAAGCTTTCTGAGAAACTTCTTTGTGATGTGTACTT
TCAACACACGGAGTTGTAGCTTTCTTTTCATTGAGCAGTTTTGAAACAGT
CTTTTTGCGGAATCAGCAAATGGATGTTTGGAGTGCTTTGAGGCCTATGG
TGAAAAGGTGAATAACTTCACATAAAAAATAGACAGAAGCATTGTGAGAA
ACATCTCTGTGATGTGTGCATTCATCTCACAGAGTTGAACCTTTCTTTGA
TTGAGCAGTTTGGAAACAGTCCTTTTGTAGAATCTGCAAAGGGATATTTC
TGAGCCCATTGAAGCCTAGGGTGAAAAAGAAATGTCTTCCCATAAAAAGT
AGATAGAAGCATTCTGATAAACTTTTTTGTGGTGTGTCCATTCATCTCAC
AGAGTTGAAACTTCCCTTGGATTGAGCAGTTTGGAAACAGTCTTTTTGCA
GAATTTACAAAAAAATTTTGTGAGCCTTATACGGCCCATGGTGAAATAGG
AAATATCGTCACATAAAAAATAGACAGAAGCTTTCTGAGAGACTACTTTG
TGATGTTTGCTTCCGTGTCACAGGTTTGAACCTTTCTTTTGATTGAGCAG
TTTGGAAACACTCTTTTTGTAGAATCTACAAATGGGTATTTGGAGCGCTT

TGAGGCCTATGGTGAAAAAAGAAATATCTGCACATAAAAACTAGACAGAT
GCATTCTGCAAAACTTCTTTGTAATGTGTGCATTCATCTCACAGAGTTGA
ATCTTTCTTTGGATTCAGCAGTTTTCTAAACAGACCTTTTGTAAAATCTA
CAAAGTAATACTTCTGAGCCCATTGAGGCCTATGGTGAAAAAGGAAATAT
CTTCACACGAAATCTTAACAGAAGCATTCTGAGAAACTTCTTTGTGATGT
GTGCATTCATCTCACAGTGTTGAAACTTTCTTTTGATTGAGCAGTTTGGA
AACGGTCTTTTTGTACAATCTGCAAAGGGATATTTCTGAGCCATTTGAGG
CCTACTGTGAAAGAGAAATATCTTCATATAAAAACTAGCAAAAGCATTCT
GAGAAACTTCTTTGTAATGTGTGCATTCATCACACAGAGTTGAAACTTTC
TTTTGATTGAGCAGTTTGGGGACAGTCTTTTTGTATAATGTGCAAAAGGA
TATTTGTGAGCCCTTTCAGGACTGTGGTGAAATAGGGAATATCTTCACAA
AAAAACTAGACCGAAGCTTTTGGAGAAACTTCTTTGTGTTGTGTGCTTTC
ATCTCACAGAGTTGAACTTTTCTTTGATTGAGCAGTTTGTAAACATTCTT
TTTGTAGAATCTGAAGATGGATATTTGCAGCATTTCAGGCCTATGGTGAA
CAGGAAATTTCTTCACATAAAAACTAGACAGAAGCATTCTGAGAAACTTC
TTTGTGATGTGTGCATTCATGTCACAGAGTTAAAACTTTCTGTGGATTGA
GCAGTTTGGAAAGAATTCTTTTGCAGAATCTGCAAAGGGATGTTTGTGAG
CCCATTGGGGCCTATGGTGAAATAGGAAATGTCTTCACATAAAAACTAGG
CAGAAGCTTTTTGTAAAACTTCTTTGTACTGTGTGCTTTCACCACAAAGA
GTTGAACCTCTCTTTTGAGTGAGCAGTTTGGAAACACTCTTTTTGTAGAA
ATTGCAAATGGATATTTGGAGTGCTTTGAGGCCTATAGTGAAAAAGAAAA
TATCTGCATTTAAAAACTAGACAGAAACTTTCTGAGAAACTTCTTTGTGA
TGTGTGCTTTCATCTCACAGATTTGGACCTTGCTTTTCATTGAGAAGTTT
GGCAACAACTCGTTTTGTAGAATCTGCAAAGGGATATTTGTCAGCAGTTT
GAGGCCTATGGTGAAAAAGTAAATATCTTCATCTAAAACCTAGACAGAAG
CATTTTGAGAAAACTCTTTGTGATGTTTGCATTCATCTCACTGAGTTGAA
CCTTTCAGTTCATTGAGCAGTGTGGAAACATGCTTTTTGTGCAATCTGCA
AAGGAATATTTGTTTGCGGTTTGAGACCTATGGTGAAAAAGTAATAACTT
CAAATAAAAACTGGACAGAAACATTCTGATAAACTAATTTTGCATGTGTG
CATTGATCTCACAGAGTTGAACCTTTCTTTTGATGAAGCAGTTCGGAAAC
AGTTTTTTGTAGAATCTGAATAGGGATATTTGTGATCCCTTTGAGGCCTA
AGGAGAAATAGGAAATATCTTCACATAAAAACTAGACGGAAACTTTCTGA
GAAAGTTCTTTGTGACGTGGGCTTTCATCTCACAGATGTGAAACTTTATT
TTGATTGAGCAGTTTGGAAAGAGTCTTTTGTAGTATCTGCAGAGGGCTAT
TAGTGAGCGGACAGGCTTACAGTGAAAAAAGAAGTGGCTTCTCAAAAAAA
CTATACAGAAGAATTCTGAGAGACTTCTTTGTAATGTGTGCATTTATCTT
ACAGTGTTAAACCTTTCTTTTGATTGAGCTTTTTGGAAACACTCTTTTTG
TAGCATCTGCAAGAGTATACTTCTGAGCCCATTGAGACCTATTTTGAAAT
ATGAAATATCTTCACATAAAAACTAGATAGAAGGTTTCTAAGAAACACTT
CTGTGAAGTGTGCTTTCATCTCACAGAGTTGAACCTTTCTTTTCATTGAG
CAGTTTGAAAACACTCTTTTTGTAGAATCTGCAAGTGGATATTTGGAGTG
CTTTCAGGCCCATGGTGAAAAAGGAAATACCTTCACATAATAACCACACA
GAAGCATTCTGAGAAACTTCTTTGTGATGTGTGCATTCATCTCACAGTGT
TGAAACTTTATTTTGTTTGAGCAGTTTAGAAACAGTCTTTTCCTGCATTC
TGCAAAGGTGTATTTCTGAGCCATTTGAGGTCTATGTGAAAAAGAAATAT
CTTCATATTTAAACTAGACAGAAGCATTCTGAGGAACTTCTTTGTGATGT
CTCCATTCATCTGACAGATTTGAAGGTTTCTTTTAATTCACACTTTTGAA
ACCATATTTTTGTAGAATCTGCAAAGGGATATTTTTGAGACATTTGAAGC
TTATAGTGACATAGTAAATATCGTCACATAAAAACTAGACAGGAGAGTTC
TGAGAAACTTCATTCTCATGTGTGCATTCACCTCACAGAATTTAAGCTTT
CTTTTGATTGAGCAGTATGGAAATGGTTGTCTTTTAGAAACTGGAAAGGG
ATATTTCTTAGCCCTTTGAGGCCTATGGTGAAACTGGAAATATCTTCACA
TGAAAACTAGACCGAAGCTTTCTGAGAAAGTTCTTTGAGATGTGTGCTTT
CATCTCACAGAGTTAAAACTTTCTTTTGATTCAGCAGTTTGGAAACACTC
TTTTTGTGATATCTGTAAATGGATATTAGGAGTGCTTTGAGGTCAATGGT
GACAAAGGAAATATCCTCACATAAAAACTAAACAGAAATTTTCTGAGAAA
TTACTTTTTGATGTGTCCATTAATCTAACAGAGTTGAAACTTTCTTTTTA
TTGAGCAGTTTGGATACAGTCTTTTTGTAGAATCTGCAAAAAAATATTTG
TGAGCCCTTTATTGCCTATGGTGAAATAGGAATTTTCTTCACATATAAAC
TAGAAAGAAGCATTCTGAGAAACTTCTTTTTGATGTGTGCATTCATCTCA
CATAGTTGAAACTTTCTTTGGATTGAGCAGTTTGGAAACAGCCCTTTTGT
AGAATCTGCAAAGGAATATTTCTGAGCGCATTGAGTACTATGGTGCAATG
TGAAATATCTTCACATAAAAACTAGAAAGAAGCTTTCTAAGAAACTTCTT
TGTGATGTGTGCTTTCATCTCACAGAATTGAAACTTTCTTTTGATTGAGG
AGTTTGGAAACACTCTTTATCTAGAATCTGCAAATGGATATTTTGAGCGC
TATTGAGGCCCATGGTGAAAAACGCAATATCCTCACATAAAAACTAAACA
GAAGCTTTCTGAGAAACTTCCTTGTAATGTGTGCATTCATCTCACAGAGT
TGAACCTTTCTTTTTATTGAGCAGGTTAGAAAGAGGTTTATTGAACAATC
TGCAAAGGGATAATTCTGATCATTTTGAGACCTATGGTGAAAGAGAAATA
TCTTCACATAAAAACTAGACAGAATCATTCCAAGAAATTTCTTTGTGATG
TGTCCATTCATCTCACAGAGTTGAAACTTTCTTTTGATTGAGCAGTTTGG
AAACAGTCTTTTTGTAGAAGCTTCAAAGGGATATTTGTGAGCCCTTTATG
ACCTCAGGTAAAATAGAAAATATCTTCACATACAAACTAGAGAGAAGCTG
TCTGAGTAACTTTTTTGTGATGTGTGCTTTCATCTCACAGAGGTAAAAAT
TTGTTTTGATTGATTAGTTTGGAAGCAGTCTTTTTGTTGAATCTGCAAAT
GGATGTTTGGATTGCTTTGAGGCCTATGTTGAGAAAGGTAATATGTTCAC
TAAAAACAAGACAGAAGACTGGATTAAGAAAATGTGGCACATATACACCA
TGGAATACTATGCAGCTATAATAAATGATGAGTTCATGTACTTTGTAGGG
ACATAGATGAAATTGGAAATCACCATTCTCAGTAAACTATCGCAAGAACA
AAAAACCAAACACCGCATATTCTCACTCATGGGTGGGAATTGAACAATGA
"""


def fillReference(file, nCount, charsPerLine=50, value = 'N'):
    while nCount>0:
        if nCount <= charsPerLine:
            charsPerLine = nCount
        nCount = nCount-charsPerLine
        nStr = value * charsPerLine
        print >>file, nStr

def generateReference(file,name,nocallsBefore,sequence,nocallsAfter=0):
    if name:
        print >>refFa, '>'+name
    fillReference(refFa,nocallsBefore)
    print >>refFa, sequence
    fillReference(refFa,nocallsAfter)

refFileName = pjoin(odir, 'TestRef.fa')
refFa = open(refFileName,"w")
generateReference(refFa,'chr21', 9719767, ref9719767_9721767, 1000)
refFa.close()

expDirName = 'GS19240-180-36-21-ASM'
shutil.rmtree(pjoin(odir, expDirName), True)
tc.copytree(pjoin(idir, 'common', expDirName),pjoin(odir, expDirName))

inputDir = pjoin(idir, 'conv','evidence2cache0')
expRootDir = pjoin(odir, expDirName, 'GS00028-DNA_C01')

# the followin block is used to allow lane->library mapping
mapDir = pjoin(expRootDir,'MAP','GS10364-FS3-L01')
mapDir2 = pjoin(expRootDir,'MAP','GS10364-FS3-L04')
os.mkdir(mapDir2)
shutil.copyfile(pjoin(mapDir, 'mapping_GS10364-FS3-L01_001.tsv'),
                pjoin(mapDir2, 'mapping_GS10364-FS3-L04_005.tsv'))
shutil.copyfile(pjoin(mapDir, 'reads_GS10364-FS3-L01_001.tsv'),
                pjoin(mapDir2, 'reads_GS10364-FS3-L04_005.tsv'))

evidenceDir = pjoin(expRootDir,'ASM','EVIDENCE')
shutil.copyfile(pjoin(inputDir, 'evidenceIntervals-chr21-GS19240-180-36-21-ASM.tsv'),
                pjoin(evidenceDir, 'evidenceIntervals-chr21-GS19240-180-36-21-ASM.tsv'))
shutil.copyfile(pjoin(inputDir, 'evidenceDnbs-chr21-GS19240-180-36-21-ASM.tsv'),
                pjoin(evidenceDir, 'evidenceDnbs-chr21-GS19240-180-36-21-ASM.tsv'))

tc.runCommand([ cgatools, 'fasta2crr',
                '--input='+pjoin(odir, 'TestRef.fa'),
                '--output='+pjoin(odir, 'TestRef.crr') ])

tc.runCommand( [ cgatools, 'evidence2cache',
                 '--beta',
                 '--genome-root='+pjoin(idir, expRootDir),
                 '--output='+pjoin(odir, 'evidenceCache'),
                 '--extract-genomic-region=chr21',
                 '--reference='+pjoin(odir, 'TestRef.crr'),
                 ] )


tc.textCompare(pjoin(inputDir,'GS10364-FS3-L04_5.tsv'),
               pjoin(odir, 'evidenceCache','chr21','GS10364-FS3-L04_5.tsv'),
               [ '#GENERATED_AT\t', 
                 '#SOFTWARE_VERSION\t',
               ] )

