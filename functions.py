#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:29:57 2019

@author: skuarch
"""

import variables

def calculate_rate(row):
    num_people = row['num_people']
    people_percentage = int(round((num_people / variables.total_num_people) * 100, 0))
    if people_percentage <= 10:
        return 1
    if people_percentage >= 11 and people_percentage <= 40:
        return 2
    if people_percentage >= 41 and people_percentage <= 80:
        return 3
    if people_percentage >= 81 and people_percentage <= 100:
        return 4


def save_image(df, image_name):
    df.plot().get_figure().savefig('website/img/' + image_name)

def save_image_bar(df, image_name):
    df.plot.bar().get_figure().savefig('website/img/' + image_name)
