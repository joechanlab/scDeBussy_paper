import scanpy as sc
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

path = "/data1/chanj3/wangm10/CellAlignDTW_paper/HCA-BM/20492a4b-0def-457b-9574-60dfdde2a0f2/BM_standard_design.h5ad"
print("Loading adata from path:", path)
adata = sc.read_h5ad(path)

label_map = {
    'CD4+ naive T cells': 'CD4⁺ naive T',
    'CD8+ naive T cells': 'CD8⁺ naive T',
    'T helper cells': 'T helper',
    'Cytotoxic T cells': 'Cytotoxic T',
    'NK cells': 'NK',
    'Memory B cells': 'Mem B',
    'Naive B cells': 'Naive B',
    'Plasma cells': 'Plasma',
    'Pro-B cells': 'Pro-B',
    'Pre-B cells': 'Pre-B',
    'Megakaryocyte progenitors': 'Mega prog',
    'HSCs': 'HSCs',
    'Erythroid progenitors': 'Ery prog',
    'Erythroid cells': 'Ery cells',
    'ANK1-low erythroid cells': 'ANK1⁻ Ery',
    'MSCs': 'MSCs',
    'CD14+ monocytes': 'CD14⁺ Mono',
    'CD16+ monocytes': 'CD16⁺ Mono',
    'pDCs': 'pDCs',
    'cDCs': 'cDCs',
    'Neutrophil progenitors': 'Neut prog',
}

adata.obs['anno_short'] = adata.obs['anno'].replace(label_map)

sc.pl.umap(adata, color='anno_short', legend_loc='on data', title="", legend_fontsize=8, frameon=False, legend_fontoutline=True, add_outline=True, show=False)
plt.savefig("HCA.png", dpi=300, bbox_inches='tight')
plt.show()
