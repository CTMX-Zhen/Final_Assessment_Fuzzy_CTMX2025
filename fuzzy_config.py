
"""
# Final Assessment: FUZZY LOGIC DEVELOPMENT
    In a dishwasher appliance, Fuzzy Logic control is proposed to be used to obtain a processing 
    time based on number of plates and level of dirtiness. The conventional method required the 
    human interruption to decide upon what should be the processing time for the different dish 
    conditions. In other words, analysis and decision-making ability have been incorporated to the 
    machine which makes the machine much more intelligent. 

The input and output details as follows: 

## Inputs (Antecedents): 
    1. Number of dishes 
        - Fuzzy set: LOW, AVERAGE, HIGH 
        - Scale: 0-50 plates 
    2. Level of dirtiness 
        - Fuzzy set: LIGHT, MEDIUM, HEAVY 
        - Scale: 0-100 percent 

## Output (Consequents): 
    1. Wash time  
        - Fuzzy set: SHORT, AVERAGE, LONG, MAXIMUM 
        - Scale: 0-60 minutes 

## Your task is to develop the Fuzzy Inference System (FIS) for the dishwasher with the following requirements: 
    1. Use MAMDANI FIS model. 
    2. Create a fuzzy membership function for all input and output. 
    3. Create TEN FUZZY RULES with the mixture of AND and OR operators. 
    4. Implementation must be in PYTHON. 

## Submission, upload to eLearning: 
    1. Report: 
        - Brief introduction to the proposed FIS. 
        - Membership functions design. 
        - Fuzzy rules list.
        - Complete screen short of source code and development steps. 
        - Complete screen short of simulated input and output produced by proposed FIS. 
        - Result analysis 
    2. Complete working source code. 

## Mark distributions: 
    1. Produce a report.    (25 marks) 
    2. Design the solution. (25 marks) 
    3. Develop FIS in Python.   (30 marks) 
    4. Evaluate and analyze the result.  (20 marks)      

NAME: Connie Tang Ming Xin
MATRIC NUMBER: MEC245051
"""

# Final Assessment:
    # 1. Project Overview:
    #     - Develop a Fuzzy Inference System (FIS)
    #     - Use Fuzzy Logic to know wash time based on number of dishes from 0 to 50 and dirtiness level from 0% to 100%
    #         - Input Variable:
    #             - Number of Dishes (range: 0 to 50)
    #             - Dirtiness Level (range: 0% to 100%)
    #         - Output Variable:
    #             - Predicted Wash Time (range: 0 to 60 minutes)

    # 2. Model to apply for FIS
    #     - Mamdani FIS
    #         - Mamdani FIS is a type of fuzzy logic model that introduced by Ebrahim Mamdani in 1975
    #         - Mamdani FIS is the one of the most commonly used in fuzzy systems

    # 3. Create fuzzy membership for all input and output

    # 4. Create at least 10 fuzzy rules with mix of AND and OR operators

    # 5. Platform: offline AI tools & code your own solution
    #     - Visual Studio Code
    #     - Jupyter Notebook
    #     - Python 3.12
    #     - scikit-fuzzy, matplotlib, scipy, networkx, seaborn

    # GitHub: https://github.com/CTMX-Zhen/Final_Assessment_Fuzzy_CTMX2025
    
"""
    STUDENT'S OUTCOMES
"""

# == IMPORT LIBRARIES ==
import numpy as np
import skfuzzy as fuzz

from skfuzzy.control import Rule
from skfuzzy import control as ctrl

# Define input value
dishes = ctrl.Antecedent(np.arange(0, 51, 1), 'dishes')  # 0 to 50, start form 1
dirtiness = ctrl.Antecedent(np.arange(0, 101, 1), 'dirtiness')  # 0% to 100%, start from 1%
wash_time = ctrl.Consequent(np.arange(0, 61, 1), 'wash_time')  # 0min to 60min, start from 1min

# Define membership function
""" Input 1: Number of dishes """
dishes['low'] = fuzz.trimf(dishes.universe, [0, 0, 20])
dishes['average'] = fuzz.trimf(dishes.universe, [10, 25, 40])
dishes['high'] = fuzz.trimf(dishes.universe, [30, 50, 50])

""" Input 2: Dirtiness level """
dirtiness['light'] = fuzz.trimf(dirtiness.universe, [0, 0, 40])
dirtiness['medium'] = fuzz.trimf(dirtiness.universe, [30, 50, 70])
dirtiness['heavy'] = fuzz.trimf(dirtiness.universe, [60, 100, 100])

""" Input 3: Wash Time """
wash_time['short'] = fuzz.trimf(wash_time.universe, [0, 10, 20])
wash_time['average'] = fuzz.trimf(wash_time.universe, [15, 30, 45])
wash_time['long'] = fuzz.trimf(wash_time.universe, [40, 50, 55])
wash_time['maximum'] = fuzz.trimf(wash_time.universe, [50, 60, 60])

# Create fuzzy rules
rules = [
    # AND Rules
    Rule(dishes['low'] & dirtiness['light'], wash_time['short']),
    Rule(dishes['low'] & dirtiness['medium'], wash_time['average']),
    Rule(dishes['low'] & dirtiness['heavy'], wash_time['long']),

    Rule(dishes['average'] & dirtiness['light'], wash_time['average']),
    Rule(dishes['average'] & dirtiness['medium'], wash_time['long']),
    Rule(dishes['average'] & dirtiness['heavy'], wash_time['maximum']),

    Rule(dishes['high'] & dirtiness['light'], wash_time['long']),
    Rule(dishes['high'] & dirtiness['medium'], wash_time['maximum']),
    Rule(dishes['high'] & dirtiness['heavy'], wash_time['maximum']),

    # OR Rule
    Rule(dishes['low'] | dirtiness['light'], wash_time['short']),
]


