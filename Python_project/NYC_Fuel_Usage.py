# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:18:59 2019
Title: This program visualizes Fuel Oil Usage in different Boroughs in NYC and the strength of Community Boards in different Boroughs
"""

import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv("C:/Users/aakan/Desktop/Stevens/Semester 2/Self_Study/Python/Pandas/NYC Fuel_Usage/Python_project\DCAS_Managed_Building_Fuel_Usage.csv")
#print(file)

total_for_Borough=file.groupby(['Borough']).agg({'Fuel Oil Usage (MMBTU)':'mean'}).plot(kind='bar',title='Borough wise Average Fuel Oil Usage of NYC buildings',figsize=(8,3),color='brown')
total_for_Borough.set_ylabel('Fuel Oil Usage')

a=file.groupby(['Borough']).agg({'Community Board':'sum'}).plot(kind='pie',subplots=True,legend=False,figsize=(20,10),title='Strength of Community Boards in different Boroughs')


