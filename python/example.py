# This file is an example of how we configure this file in order to get
# the overlapping codes in our research. Please check the generate_codings.py
# for a detailed documentation of the parameters.

# You can check at the end all our existing codes, code categories and filenames

import csv
import CSVGenerator

configurations = [
{
    'codings': 1,
    'file_catnames': "'Skill_open'",
    'code_catnames': "'Goals','Emotion','Effect','Imagery','Time'",
    'code_names': None,
    'code_filters': None },
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
    'codings': 1,
    'file_catnames': "'Skill_closed'",
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
    'codings': 1,
    'file_catnames': "'Skill_open','Skill_closed'",
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
    elif codings >= 1 and codings <= 11:
        generator.codings(codings)
    else:
        generator.codings_gephi()

for conf in configurations:
    generator = CSVGenerator.CSVGenerator(conf['codings'], conf['file_catnames'],
        conf['code_catnames'], conf['code_names'], conf['code_filters'])
    call_generator(generator, conf['codings'])




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

