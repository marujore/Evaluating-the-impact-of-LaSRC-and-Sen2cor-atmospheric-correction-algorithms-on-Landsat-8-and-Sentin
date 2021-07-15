# Evaluating the impact of LaSRC and Sen2cor atmospheric correction algorithms on Landsat-8 and Sentinel-2A/2B over AERONET stations in Brazilian territory

This repository contains the scripts used to process and compare surface reflectance derived from The article: "Evaluating the impact of LaSRC and Sen2cor atmospheric correction algorithms on Landsat-8 and Sentinel-2A/2B over AERONET stations in Brazilian territory"

Input images: Lansat-8/OLI and Sentinel-2/MSI. Source: http://earthexplorer.usgs.gov/ and https://scihub.copernicus.eu/dhus/#/home.

Ground Truth Data: AERONET Stations: Alta Floresta, Cuiabá-Miranda, Manaus-EMBRAPA, Itajubá and Rio Branco. Source: https://aeronet.gsfc.nasa.gov/

Authors: Rennan de Freitas Bezerra Marujo (https://orcid.org/0000-0002-0082-9498), José Guilherme Fronza (https://orcid.org/0000-0002-0830-8101), Anderson Soares (https://orcid.org/0000-0001-6513-2192), Gilberto R. Queiroz (https://orcid.org/0000-0001-7534-0219) and Karine R. Ferreira (https://orcid.org/0000-0003-2656-5504)

# Summary

[01_AERONET_data](https://github.com/marujore/Evaluating-the-impact-of-LaSRC-and-Sen2cor-atmospheric-correction-algorithms-on-Landsat-8-and-Sentin/tree/main/aeronet_data)

[02_Image Selection](https://github.com/marujore/Evaluating-the-impact-of-LaSRC-and-Sen2cor-atmospheric-correction-algorithms-on-Landsat-8-and-Sentin/blob/main/scripts/Image_selection.ipynb)

[03_SceneIds](https://github.com/marujore/Evaluating-the-impact-of-LaSRC-and-Sen2cor-atmospheric-correction-algorithms-on-Landsat-8-and-Sentin/tree/main/sceneids)

[04_Process_ARCSI](https://github.com/marujore/Evaluating-the-impact-of-LaSRC-and-Sen2cor-atmospheric-correction-algorithms-on-Landsat-8-and-Sentin/blob/main/scripts/process_ARCSI_calls.ipynb)

[05_LaSRC_FMASK](https://github.com/marujore/LaSRC-LEDAPS-Fmask)

[06_Sen2cor_FMASK](https://github.com/marujore/sen2cor-Fmask)

[07_Validation_Comparison](https://github.com/marujore/Evaluating-the-impact-of-LaSRC-and-Sen2cor-atmospheric-correction-algorithms-on-Landsat-8-and-Sentin/blob/main/scripts/validation.py)

[08_Scatter_Plots](https://github.com/marujore/Evaluating-the-impact-of-LaSRC-and-Sen2cor-atmospheric-correction-algorithms-on-Landsat-8-and-Sentin/tree/main/scatter_plots)

[09_Article](https://github.com/marujore/Evaluating-the-impact-of-LaSRC-and-Sen2cor-atmospheric-correction-algorithms-on-Landsat-8-and-Sentin/tree/main/scatter_plots)

# Citation
## Formated citation
R. F. B. Marujo, J. G. Fronza, A. R. Soares, G. R. Queiroz, K. R. Ferreira, Evaluating the impact of LaSRC and Sen2cor atmospheric correction algorithms on Landsat-8/OLI and Sentinel-2/MSI data over AERONET Stations in Brazilian territory, ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences V-3-2021 (2021) 271–277.doi:10.5194/isprs-annals-v-3-2021-271-2021.URL https://doi.org/10.5194/isprs-annals-v-3-2021-271-2021
## Bibtex

@article{Marujo2021,
  doi = {10.5194/isprs-annals-v-3-2021-271-2021},
  url = {https://doi.org/10.5194/isprs-annals-v-3-2021-271-2021},
  year = {2021},
  month = jun,
  publisher = {Copernicus {GmbH}},
  volume = {V-3-2021},
  pages = {271--277},
  author = {R. F. B. Marujo and J. G. Fronza and A. R. Soares and G. R. Queiroz and K. R. Ferreira},
  title = {Evaluating the impact of LaSRC and Sen2cor atmospheric correction algorithms on Landsat-8/OLI and Sentinel-2/MSI data over AERONET Stations in Brazilian territory},
  journal = {{ISPRS} Annals of the Photogrammetry,  Remote Sensing and Spatial Information Sciences}
}