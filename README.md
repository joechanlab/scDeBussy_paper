# scDeBussy paper
Code to reproduce the figures in the paper. 
The code repository of scDeBussy is [here](https://github.com/joechanlab/scDeBussy)

## B cell development
The source data of bone marrow B cell development came from [Human Cell Atlas](https://explore.data.humancellatlas.org/projects/cc95ff89-2e68-4a08-a234-480eca21ce79/get-curl-command). We downloaded the data in h5ad format and the relevant file is `20492a4b-0def-457b-9574-60dfdde2a0f2/BM_standard_design.h5ad`. We extracted three B cells subsets: Pre-B, Pro-B, and Naive B cells. 

The scripts that are used to extract and preprocess data are located in folder `b_cell_development`, as described in the following table. 

| Script            | Description                                               |
|-------------------|-----------------------------------------------------------|
| 1_extract_data.py | Extract the B cells and preprocess the source data        |
| 2_palantir.py     | Run palantir pseudotime on h5ad files                     |
| 3_align.py        | Align pseudotime across samples                           |


## Young/aged hematopoiesis from normal and MDS individuals
The source data came from [Ainciburu et al 2023](https://elifesciences.org/articles/79363). We downloaded the data in h5 format as well as the metadata from [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE180298). 

The scripts that are used to extract and preprocess data are located in folder `MDS`, as described in the following table. 


## Richter transformation

The source data of CLL to Richter transformation came from [Nadeu et al 2022 Nat Med](https://www.nature.com/articles/s41591-022-01927-8) and the seurat objects were downloaded from [Zenodo](https://zenodo.org/records/6631966) into the `data/` folder.

```{bash}
cd data/
wget https://zenodo.org/record/6631966/files/Nadeu2022_scRNAseq.zip
unzip Nadeu2022_scRNAseq.zip
cd Nadeu2022_scRNAseq
```

The scripts that are used to extract and preprocess data are located in folder `richter_transformation`, as described in the following table. 

| Script           | Description                                               |
|------------------|-----------------------------------------------------------|
| 1_extract_data.R | Extract count matrix and annotations from the source data |
| 2_preprocess.py  | Preprocess the expression matrix into h5ad file           |
| 3_palantir.py    | Run palantir pseudotime on h5ad files                     |
| 4_align.py       | Align pseudotime across samples                           |

