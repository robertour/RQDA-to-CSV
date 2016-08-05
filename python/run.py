import csv
from configuration import configurations
import CSVGenerator


def call_generator(generator, codings):
    if codings == -2:
        generator.filtered_codings_gephi()
    elif codings == -1:
        generator.codings_gephi()
    elif codings >= 1 and codings <= 11:
        generator.codings(codings)
    else:
        generator.codings_gephi()

for conf in configurations:
    generator = CSVGenerator.CSVGenerator(conf['codings'], conf['file_catnames'],
        conf['code_catnames'], conf['code_names'], conf['code_filters'])
    call_generator(generator, conf['codings'])

