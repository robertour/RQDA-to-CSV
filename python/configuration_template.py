# Configuration is a dictionary that contains all the permutations of the
# resulting data that you want to see
configurations = [{
# Possible values for codings
# -2 for filtered gephi (uses freecode_filtered)
# -1 for gephi
# 1 to 11 is going to find all the sets of codes in which n codes appear together
'codings': -2,

# Names of the file categories in RQDA that will be included in the query.
# You can select several with the following notation (notice each category is
# in between single quotes ''):
#   'file_catnames': "'FILE_CAT1','FILE_CAT2'"
# You can select all of them by setting
#   'file_catnames': None
'file_catnames': "'cat1'",

# Names of the coding categories in RQDA that will be included in the query.
# You can select several with the following notation (notice each category is
# in between single quotes ''):
#   'code_catnames': "'CODE_CAT1','CODE_CAT2'"
# You can select all of them by setting
#   'code_catnames': None
'code_catnames': "'cod_cat1'",

# Names of the coding in RQDA that will be included in the query. You can
# select several with the following notation (notice each name is in
# between single quotes ''):
#   'code_names': "'CODE1','CODE'",
# You can select all of them by setting
#   'code_names': None,
'code_names': "'code1','code2'",

# ONLY HONOURED BY codings = -2
# Names of the coding categories in RQDA that will be used to filter the query.
# A relation between any codecat_names will be present if, and only if, of of
# the filtering codes is also existant. The filtering codes won't appear in the
# final Gephi table. For example, CODE1 and CODE2 will appear just if FILTER1
# is present. You can select several with the following notation (notice
# each name is in between single quotes ''):
#   'code_filters': "'FILTER1','FILTER2'"
# You can select all of them by setting
#   'code_filters': None
'code_filters': "'filter1'"
},
# 2nd configuration
{
'codings': -2,
'file_catnames': "'cat2'",
'code_catnames': "'cod_cat2'",
'code_names': "'code1','code2'",
'code_filters': "'filter1'"
},
# 3rd configuration
{
'codings': 1,
'file_catnames': "'cat2'",
'code_catnames': "'cod_cat2'",
'code_names': "'code1','code2'",
'code_filters': None
}
# ...
]
