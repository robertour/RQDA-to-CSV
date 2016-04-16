RQDA-to-CSV: Overlapped RQDA Codes Finder (Version 1.0.0)
---------------------------------------------------------

This code take as an input an RQDA file generated with the RQDA Package (http://rqda.r-forge.r-project.org/) for Qualitative Data Analysis in R.

The code will search for tags that overlap in the text. Each time there is an overlap of n tags, a csv line is added to an external file, specifying the information of each tag. 

The script can also convert the RQDA database into a CSV Gephi friendly format (https://gephi.github.io/).

How to use it
-------------

Python Code
===========

The Python code is in the folder `python`. For now you will need to manually modify the `generate_codings.py`. It has comments of what the parameters do. A configuration example is provided in the `example.py` file.

You should also add a copy of your RQDA Database directly in the python folder and rename the RQDA file to `db.rqda`

R Code 
======

The R code is being added to `R scripts` folder. It is partially configuration, and it should serve as an example of how we process the tags in our project.


Questions
---------

Please feel free to contact me if you have any questions. I am trying to organize the files.


How do I reference this code?
-----------------------------

If you want to reference this code p


Ulloa, R. (2015). RQDA-to-CSV: First Release. Zenodo. 10.5281/zenodo.16647


[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.16647.svg)](http://dx.doi.org/10.5281/zenodo.16647)

