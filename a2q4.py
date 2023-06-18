###############################################################################
# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    15 June 2023
#
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Testing; relevant to Chapter 5, 6, 7
###############################################################################

# TODO: Fill in your information below
# Student Name-Harry Patel
# NSID-ozc189
# Student Number-11358887

# TODO: TEST DRIVEN DEVELOPMENT

def get_patient_people(community: list):
    """
    Get a list of all dictionaries where the value for "foes" is an empty list.

    Args:
        community (list): List of dictionaries to iterate through. Each dictionary
                          must contain the keys "name", "friends", and "foes".
                          The "name" values should be unique, and the "friends" and "foes"
                          values must be lists.

    Returns:
        list: List of dictionaries of those with no foes.
    """
    return [person for person in community if person["foes"] == []]