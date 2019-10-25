#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:29:57 2019

@author: skuarch
"""

file = 'Poblacion_Subordinada_Nivel_Ingresos.csv'
man = 'Hombre'
woman = 'Mujer'
selected_state = 'Jalisco'
selected_level = ''
selected_genred = ''
total_num_people = 0
selected_year = 2018

total_people_by_state_and_age_range = 0
total_people_by_state_and_level = 0
total_man_by_state_and_level = 0
total_woman_by_state_and_level = 0
total_people_state = 0
total_man_state = 0
total_woman_state = 0


genres = [
    man,
    woman
]

aguascalientes = 'Aguascalientes'
bajaCalifornia = 'Baja California'
bajaCaliforniaSur = 'Baja California Sur'
campeche = 'Campeche'
chiapas = 'Chiapas'
chihuahua = 'Chihuahua'
ciudadDeMexico = 'Ciudad de Mxico'
coahuila = 'Coahuila'
colima = 'Colima'
durango = 'Durango'
estadoDeMexico = 'Estado de M�xico'
guanajuato = 'Guanajuato'
guerrero = 'Guerrero'
hidalgo = 'Hidalgo'
jalisco = 'Jalisco'
michoacan = 'Michoac�n'
morelos = 'Morelos'
nayarit = 'Nayarit'
nuevoLeon = 'Nuevo Le�n'
oaxaca = 'Oaxaca'
puebla = 'Puebla'
queretaro = 'Queretaro'
quintanaRoo = 'Quintana Roo'
sanLuisPotosi = 'San Luis Potos�'
sinaloa = 'Sinaloa'
sonora = 'Sonora'
tabasco = 'Tabasco'
tamaulipas = 'Tamaulipas'
tlaxcala = 'Tlaxcala'
veracruz = 'Veracruz'
yucatan = 'Yucat�n'
zacatecas = 'Zacatecas'
nacional = 'Nacional'

states = [
    aguascalientes,
    bajaCalifornia,
    bajaCaliforniaSur,
    campeche,
    chiapas,
    chihuahua,
    ciudadDeMexico,
    coahuila,
    colima,
    durango,
    estadoDeMexico,
    guanajuato,
    guerrero,
    hidalgo,
    jalisco,
    michoacan,
    morelos,
    nayarit,
    nuevoLeon,
    oaxaca,
    puebla,
    queretaro,
    quintanaRoo,
    sanLuisPotosi,
    sinaloa,
    sonora,
    tabasco,
    tamaulipas,
    tlaxcala,
    veracruz,
    yucatan,
    zacatecas,
    nacional
]

'''
states = {
    'Aguascalientes': 1,
    'Baja California': 2,
    'Baja California Sur': 3,
    'Campeche': 4,
    'Chiapas': 5,
    'Chihuahua': 6,
    'Ciudad de M�xico': 7,
    'Coahuila': 8,
    'Colima': 9,
    'Durango': 10,
    'Estado de M�xico': 11,
    'Guanajuato': 12,
    'Guerrero': 13,
    'Hidalgo': 14,
    'Jalisco': 15,
    'Michoac�n': 16,
    'Morelos': 17,
    'Nayarit': 18,
    'Nuevo Le�n': 19,
    'Oaxaca': 20,
    'Puebla': 21,
    'Queretaro': 22,
    'Quintana Roo': 23,
    'San Luis Potos�': 24,
    'Sinaloa': 25,
    'Sonora': 26,
    'Tabasco': 27,
    'Tamaulipas': 28,
    'Tlaxcala': 29,
    'Veracruz': 30,
    'Yucat�n': 31,
    'Zacatecas': 32,
    'Nacional': 33,
}
'''

less_than_minimum_salary = 'Menos de 1 s.m.'
one_minimum_salary = '1 salario m¡nimo'
more_than_2_until_3 = 'M s de 2 hasta 3 s.m.'
more_than_3_until_5 = 'M s de 3 hasta 5 s.m.'
more_than_5_until_10 = 'M s de 5 hasta 10 s.m.'
more_than_10 = 'M s de 10 s.m.'
no_incoming = 'No recibe ingresos'
not_specified = 'No especificado'

levels = [
    less_than_minimum_salary,
    one_minimum_salary,
    more_than_2_until_3,
    more_than_3_until_5,
    more_than_5_until_10,
    more_than_10,
    no_incoming,
    not_specified
]


'''
levels = {
    'Menos de 1 s.m.': 1,
    '1 salario m¡nimo': 2,
    'M s de 2 hasta 3 s.m.': 3,
    'M s de 3 hasta 5 s.m.': 4,
    'M s de 5 hasta 10 s.m.': 5,
    'M s de 10 s.m.': 6,
    'No recibe ingresos': 7,
    'No especificado': 8
}
'''

from_15_to_24 = '15 A 24 A¥OS'

age_range = {
    '15 A 24 A¥OS': 1,
    '25 A 44 A¥OS': 2,
    '45 A 64 A¥OS': 3,
    '65 A¥OS Y MAS': 4
}

years = [
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018
]
