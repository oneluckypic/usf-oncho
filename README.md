
# Research

This project is based on a paper by Jacob, et al. "Validation of a Remote Sensing Model to Identify Simulium damnosum s.l. Breeding Sites in Sub-Saharan Africa." July, 2013.

### Notes from the paper
* A common characteristic of all of the members of the S. damnosum s.l. species complex is that the immature stages require fast flowing well oxygenated water for development [14].
* Simulium damnosum s.l. generally travels no further than 12 km from its river source in search of a blood meal [15].
* QuickBird sub-meter satellite data obtained from Digital Globe Inc., (Longmont, CO, USA) were used for this study.
* The satellite image and data of the study site were acquired on July 15, 2010, roughly at the mid-point of the rainy season.
* The satellite data contained 25 square km of the land area in the study site.
* The QuickBird image data were delivered as pan-sharpened composite products in infrared colors.
* (Algorithm One)[algorithm-one] The QuickBird imagery was classified using the Iterative Self-Organizing Data Analysis Technique (ISODATA) unsupervised routine in ERDAS Imagine v.8.7 (ERDAS, Inc., Atlanta, Georgia), as previously described [19].
* (Algorithm Two)[algorithm-two] To develop the BRR model, individual pixel (0.6 m2 per pixel) spectral reflectance estimates in the QuickBird images were extracted from georeferenced validated S. damnosum s.l. aquatic habitats using a Li-Strahler geometric-optical model, as previously described [20]. This procedure allowed for the creation of a spectral signature of a unit of habitat. The model used three scene components: sunlit canopy (C), sunlit background (G) and shadow (T) generated from the QuickBird image, to determine the subpixel endmember spectra associated with the known habitats. The C, G and T component classes were estimated using the ENVI software package (Exelis Visual Information Solutions, Boulder, CO) which employs an object-based classification algorithm [21].

### Questions about paper
* Were the images color corrected/balanced when the various algorithms were run?

# Algorithms needed in Python

# Algorithm One

ISODATA

# Algorithm Two

## Durbin-Watson Statistic

[video](https://www.youtube.com/watch?v=UFvDSX3jsYg)

## Eigenvector Spatial Filtering (ESF)

[video](https://www.youtube.com/watch?v=6wXoUxjFIcM)
[code](https://github.com/bchastain/esf)
[slides](http://bchastain.github.io/scipy2015/#/)

# References
[14] Crosskey RW (1990) The Natural History of Blackflies. Chichester: John Wiley and Sons.
[15] Thompson BH (1976) Studies on the flight range and dispersal of Simulium damnosum (Diptera: Simuliidae) in the rain-forest of Cameroon. Annals of Tropical Medicine and Parasitology 70: 343–354.
[19] Jacob BG, Novak RJ, Toe L, Sanfo MS, Afriyie A, et al. (2012) Quasi-likelihood techniques in a logistic regression equation for identifying Simulium damnosum s.l. larval habitats intra-cluster covariates in Togo. Geospatial Information Science 15: 1–17.
[20] Jacob BG, Novak RJ (2011) A taxonomy of unmixing algorithms using Li-Strahler geometric-optical model and other spectral endmember extraction techniques for decomposing QuickBird visible and near infra-red pixels of an Anopheles arabiensis habitat. Open Remote Sensing 4: 1–25.
[21] Jacob BG, Griffith DA, Mwangangi JM, Gathings DG, Mbogo CB, et al. (2011) A cartographic analyses using spatial filter logistic model specifications for implementing mosquito control in Kenya. Urban Geography 32: 363–377.
