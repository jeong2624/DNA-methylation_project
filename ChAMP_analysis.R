"
Created on Sat Jun 4 2022

@author: Jeong-Woon, Park

"

### https://bioconductor.org/packages/release/bioc/vignettes/ChAMP/inst/doc/ChAMP.html

### Load the package related to DNA methylation analysis.
library(ChAMP)

### Load the EPIC Chip dataset & Filtering
myLoad = champ.load(directory = ".", arraytype = "EPIC")

### Assign sample_name into myLoad rownames or colnames.
rownames(myLoad$pd) = myLoad$pd$Sample_name
colnames(myLoad$intensity) = myLoad$pd$Sample_name
colnames(myLoad$beta) = myLoad$pd$Sample_name

### Check the distribution CpG sites on chromosome, CpG islands, TSS regions.
CpG.GUI(arraytype = "EPIC")

### Quality control
champ.QC()

QC.GUI(arraytype = "EPIC") # Alternatively code.

### Normalization
myNorm = champ.norm(arraytype = "EPIC", cores = 5, plotBMIQ = TRUE)

### Quality control after normalization
champ.QC(beta = myNorm,
         pheno = myLoad$pd$Sample_Group,
         resultsDir = "./CHAMP_norm_QCimages/")

QC.GUI(beta = myNorm,
       pheno = myLoad$pd$Sample_Group,
       arraytype = "EPIC")

### SVD analysis for batch effect
myLoad$pd$Slide = as.factor(myLoad$pd$Slide)
myLoad$pd$Sample_Group = as.factor(myLoad$pd$Sample_Group)

champ.SVD(beta = as.data.frame(myNorm), pd = myLoad$pd)

### Batch Effect Correction
### Slide, Sex, Array, Age is highly significant correlation.
myCombat = champ.runCombat(beta = myNorm, pd = myLoad$pd,
                           batchname = c("Slide", "Sex", "Array", "Age")) 

### Differentially methylated position
myDMP = champ.DMP(beta = myCombat, arraytype = "EPIC")

DMP.GUI()

### Differentially methylated region
myDMR = champ.DMR(beta = myCombat, arraytype = "EPIC")

DMR.GUI(arraytype = "EPIC")

### Gene Set Enrichment Analysis
myGSEA = champ.GSEA(arraytype = "EPIC")

### Copy Number Variation
myCombat_CNA = champ.runCombat(beta = myLoad$intensity, pd = myLoad$pd, logitTrans = FALSE,
                               batchname = c("Slide"))

myCNA = champ.CNA(intensity = myCombat_CNA, pheno = myLoad$pd$Sample_Group, arraytype = "EPIC",
          controlGroup = "Control", groupFreqPlots = TRUE, sampleCNA = FALSE, control = TRUE)
