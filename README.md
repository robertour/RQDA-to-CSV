RQDA-to-CSV: Overlapped RQDA Codes Finder (Version 1.0.0)
---------------------------------------------------------

This code take as an input an RQDA project file generated with the RQDA Package (http://rqda.r-forge.r-project.org/) for Qualitative Data Analysis in R.

The code will search for tags that overlap in the text. Each time there is an overlap of n tags, a csv line is added to an external file, specifying the information of each tag. Let's take the following tagged file:

> Lorem ipsum **\<tagA\>** dolor sit amet, **\<tagB\>**consectetur adipiscing elit,**\</tagA\>**sed do 
> eiusmod tempor**\</tagB\>** incididunt ut labore et dolore magna aliqua.

In this case, tagA and tagB are overlapped, so a row is produced in the CSV file output, with the following format

    filename, file_categories ..., tagA, tagA_categories... , tagB, tagB_categories, tagA-tagB

A new row is created each time tagA and tagB appear together. Currently, the script is able to find up to 11 overlapping tags.

The script can also convert the RQDA database into a CSV Gephi friendly format (https://gephi.github.io/).

How to use it
-------------

Python Code
===========

1. Install Python
2. Place a copy of your RQDA database (project) file directly in the python foloder and rename the RQDA file `db.rqda`
3. Manually modify the `generate_codings.py` to configure the type of output you would like. The `generate_codings.py` has comments of what the parameters do.  Also, a configuration example is provided in the `example.py` file.
4. Finally, run the `generate_codings.py` file. Folders with the results will be created accoding to the configuration.

R Code 
======

The R code is being added to `R scripts` folder. It is partially configured, and it should serve as an example of how we process the tags in our project.


Questions
---------

Please feel free to contact me if you have any questions.


How do I reference this code?
-----------------------------

If you want to reference this code p


Ulloa, R. (2015). RQDA-to-CSV: First Release. Zenodo. 10.5281/zenodo.16647


[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.16647.svg)](http://dx.doi.org/10.5281/zenodo.16647)

