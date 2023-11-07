#!/usr/bin/env python
## chmod +x /home/pjw/Pipe_code/Epigenomic_pipe/ChAMP/Annotation.py
## Running code : /home/pjw/Pipe_code/Epigenomic_pipe/ChAMP/Annotation.py /home/pjw/My_Project/Epigenomics/BP/myCNA.txt /home/pjw/Pipe_code/Epigenomic_pipe/ChAMP/Homo_sapiens.GRCh37.87.gtf

import os; import subprocess; import sys; import commands
import pandas as pd

data_path = sys.argv[1]; anno_path = sys.argv[2]

with open(data_path, "r") as data:
    lines = data.readlines()
    CNA_info = []
    for line in lines:
        line = line.strip().split("\t")
        chr_num = line[1]; start = line[2]; end = line[3]
        CNA_info.append([chr_num, start, end])

with open(anno_path, "r") as ano:
    ano_lines = ano.readlines()
    ano_gene = []
    for ano_line in ano_lines:
        if "#!" in ano_line:
            pass
        elif ano_line.split("\t")[2] == "gene":
            ano_gene.append(ano_line)

map_genelist = [[]*i for i in xrange(len(CNA_info)-1)]

for gene in ano_gene:
    for i in xrange(0,len(CNA_info)-1):
        if gene.split("\t")[0] == CNA_info[i+1][0]:
            if int(gene.split("\t")[3]) >= int(CNA_info[i+1][1]) and int(gene.split("\t")[4]) <= int(CNA_info[i+1][2]):
                gene_name = gene.split()
                num = gene_name.index("gene_name")
                result = gene_name[num+1].replace(";","")[1:-1]
                map_genelist[i].append(result)
            elif (int(gene.split("\t")[3]) <= int(CNA_info[i+1][1]) <= int(gene.split("\t")[4])) or (int(gene.split("\t")[3]) <= int(CNA_info[i+1][2]) <= int(gene.split("\t")[4])):
                gene_name = gene.split()
                num = gene_name.index("gene_name")
                result = gene_name[num+1].replace(";","")[1:-1]
                map_genelist[i].append(result)

rm_overlap_gene = []
for map_genelist in map_genelist:
    rm_overlap_gene_list = list(set(map_genelist))
    rm_overlap_gene.append(rm_overlap_gene_list)

output_path = data_path.replace("myCNA.txt","myCNA_gene.txt")

group = []; Chr_num = []; Start = []; End = []; Gene = []

for n in xrange(0,len(CNA_info)-1):
    result = lines[n+1].strip() + "\t" + ",".join(rm_overlap_gene[n])
    result = result.split("\t")
    group.append(result[0]); Chr_num.append(result[1])
    Start.append(result[2]); End.append(result[3])
    Gene.append(result[6])

table = pd.DataFrame({'Group':group,'Chr_num':Chr_num,'Start':Start,'End':End,'Gene':Gene},
                columns = ["Group", "Chr_num", "Start", "End", "Gene"])
print table

table.to_csv(output_path, index = False, sep = "\t")

