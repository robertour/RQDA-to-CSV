RQDA-to-CSV: Overlapped RQDA Codes Finder (Version 1.0.0)
---------------------------------------------------------

This code take as an input an RQDA file generated with the RQDA Package (http://rqda.r-forge.r-project.org/) for Qualitative Data Analysis in R.

The code will search for tags that overlap in the text. Each time there is an overlap of n tags, a csv line is added to an external file, specifying the information of each tag. 

The script can also convert the RQDA database into a CSV Gephi friendly format (https://gephi.github.io/).

How to use it
-------------

For now you will need to manually modify the `generate_codings.py`. It has comments of what the parameters do. I will improve the input system soon, but basically it is a JSON format. 

You should also add a copy of your RQDA Database directly in the folder that contain this file and rename the RQDA file to `db.rqda`

Questions
---------

Please feel free to contact me if you have any questions. I am trying to organize the files.


How do I reference this code?
-----------------------------

If you want to reference this code p


ULLOA Roberto (2015). RQDA-to-CSV: Overlapping RQDA Codes Finder. Python Code Version 1.0.0. https://github.com/robertour/rqda-to-csv.



[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.16647.svg)](http://dx.doi.org/10.5281/zenodo.16647)

