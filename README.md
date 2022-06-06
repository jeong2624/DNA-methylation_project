# ChAMP_my_project

This is my project for DNA methylation analysis.

My project is differentially methylated analysis between control and bipolar group.

### Dataset information
* Infinium MethylationEPIC array chip (850K) platform
* Post-mortem hippocampus tissue
* the number of control group is 32 samples
* the number of bipolar group is 32 samples
* IDAT format. (GSE129428, Download from GEO database)

### We used ChAMP R package for analyzing DNA methylation.

we tried to do these step. (based on ChAMP R package tutorial code)
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
