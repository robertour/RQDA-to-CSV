import csv
import CSVGenerator



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
]

# FILE CATEGORIES: Skill_open, Skill_closed, Person_HC, Person_LC, Sex_Male,
# Sex_Female, Job_LC, Job_HL, Age_under25, Age_over25


# CODE CATEGORIES: Emotion, Goals, Imagery, Time, CL_high, CL_low

# CODE NAMES: effect_helpful, effect_unhelpful, emotion_aggression_adrenaline,
# emotion_calm_even, emotion_doubt, emotion_excitement, emotion_fear_nerves,
# emotion_focus_concentrated, emotion_focus_distracted, emotion_frustration,
# emotion_insecurity, emotion_mood_bad, emotion_mood_good, emotion_motivated,
# emotion_pain, emotion_pressure, emotion_pride, emotion_satisfaction,
# emotion_support_recognition, goal_CL1, goal_CL2, goal_CL3, goal_automated,
# goal_behavior, goal_comparison_others, goal_do_best,
# goal_experience_improvement, goal_fun, goal_health_fitness, goal_none,
# goal_outcome, goal_placement_win, goal_psychology, goal_qualifying,
# goal_self_defense, goal_social_team, goal_timedistance, imagery_abstract,
# imagery_body_awareness, imagery_concrete, imagery_distant_future,
# imagery_do_best, imagery_external, imagery_internal, imagery_near_now,
# imagery_negative, imagery_none, imagery_positive, imagery_selftalk,
# imagery_tactics, imagery_technique, time_before_competition,
# time_competition_after_action, time_competition_before_action,
# time_competition_in_action, time_outside_competition, time_practice
configurations = [
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_before_competition'"},
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_before_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_in_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_practice'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_before_competition'"},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_before_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_in_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Imagery','CL_imagery','Effect'",
    'code_names': None,
    'code_filters': "'time_practice'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_before_competition'"},
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_before_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_in_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_practice'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_before_competition'"},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_before_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_competition_in_action'"
},
{
    'codings': -2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','CL_goal','Effect'",
    'code_names': None,
    'code_filters': "'time_practice'"
},
]

configurations = [
{
    'codings': 2,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 3,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 4,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 5,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 6,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 7,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 8,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 9,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 10,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 11,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
    {
    'codings': 2,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 3,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 4,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 5,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 6,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 7,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 8,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 9,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 10,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 11,
    'file_catnames': "'Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 2,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 3,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 4,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 5,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 6,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 7,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 8,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 9,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 10,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
{
    'codings': 11,
    'file_catnames': "'Skill_open','Skill_closed'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
]


def call_generator(generator, codings):
    if codings == -2:
        generator.filtered_codings_gephi()
    elif codings == -1:
        generator.codings_gephi()
    elif codings == 1:
        generator.codings1()
    elif codings == 2:
        generator.codings2()
    elif codings == 3:
        generator.codings3()
    elif codings == 4:
        generator.codings4()
    elif codings == 5:
        generator.codings5()
    elif codings == 6:
        generator.codings6()
    elif codings == 7:
        generator.codings7()
    elif codings == 8:
        generator.codings8()
    elif codings == 9:
        generator.codings9()
    elif codings == 10:
        generator.codings10()
    elif codings == 11:
        generator.codings11()
    else:
        generator.codings_gephi()

for conf in configurations:
    generator = CSVGenerator.CSVGenerator(conf['codings'], conf['file_catnames'],
        conf['code_catnames'], conf['code_names'], conf['code_filters'])
    call_generator(generator, conf['codings'])
