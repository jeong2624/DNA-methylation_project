# Project name : DNA methylation analysis for Bipolar

# Project time : 2019.09.07 - 2019.11.02
This is my project for DNA methylation analysis.

My project is differentially methylated analysis between control and bipolar group.

### Dataset information
* Infinium MethylationEPIC array chip (850K) platform
* Post-mortem hippocampus tissue
* the number of control group is 32 samples
* the number of bipolar group is 32 samples
* IDAT format. (GSE129428, Download from GEO database)

** It mainly deals with steps below. **
* Preprocessing step
* Quality control step (QC)
* Differentially methylated analysis
* Gene Set Enrichment analysis (GSEA)
* Copy number variation (CNA)

### We uploaded these files:
* ChAMP_analysis.R : DNA methylation analysis code using ChAMP R package.
* GSE129428_pd.csv : Metadata (Phenotype, Age, Smoke status, BMI and so on.)
* GSEA_result.csv : GSEA result
* CNA : CNA analysis result
* Normalization : QC results after normalization (MDS plot, Hirechical Cluster, Density plot)
* SVD_analysis : SVD analysis result (check batch effect)

### Important !!!
1. Metadata and IDAT files are in the same directory.
2. Check the Slide columns in Metadata. 
(ex) Slide : 202816900054, Basenames : GSM3712754_202816900054_R01C01
