# Solar System Objects Classifier

Classifying solar system objects observed by the Sloan Digital Sky Survey (SDSS) Moving Object Catalog into Asteroids, Comets and Natural Satellites using KNN

--- Details of the data files ---

1. The dataset, all_trained.csv was created by taking the attributes from Solontoi and
2MASS in order to change the IDFlags (For a subset of the SDSS Data) as follows -

	a. IDFlag = 1 => Asteroid (Unchanged)
	b. IDFlag = 2 => Comets (New)
	c. IDFlag = 3 => Natural Satellites (New)

2. The dataset, sdss_differences.csv was created from the SDSS Catalogue by taking the
differences between the U-G, G-R, R-I, I-Z attributes for the objects IDFlag = 0.
