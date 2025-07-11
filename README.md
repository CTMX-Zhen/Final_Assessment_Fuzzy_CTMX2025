---
# Final Assessment: FUZZY LOGIC DEVELOPMENT
- Name: Connie Tang Ming Xin
- Matric Number: MEC245051

---
# STUDENT OUTCOME:
## 1. Project Overview:
    - Develop a Fuzzy Inference System (FIS)
    - Use Fuzzy Logic to know wash time based on number of dishes from 0 to 50 and dirtiness level from 0% to 100%

## 2. Input:
    - Number of Dishes (0 - 50)
        - LOW: 0-20
            - 0 is the lowest
            - until 20 just right for maximum of LOW level
            - so more than 20 no longer is LOW level
        - AVERAGE: 10-40
            - 25 is the average
            - which from 10 start become "AVERAGE"
            - so more than 40 no longer is AVERAGE level
        - HIGH:30-50
            - 30 can be considered as "HIGH" at the beginning
            - 50 is the maximum number of dishes

    - Dirtiness Level (0% - 100%)
        - LIGHT: 0-40
            - the closer to 0, means that the more to sure that is LIGHT level
        - MEDIUM: 30-70
            - 50 is the MEDIUM dirty level
            - 30 to 70 is a fuzzy gap for multiple different sets at the same time (0min - 60min)
        - HEAVY: 60-100
            - The more close to 100, means that the more to sure that is HEAVY

## 3. Output:
    - Wash Time (0min - 60min)
        - SHORT: 0-20
            - LIGHT dirtiness + LOW number of dishes
            - the more close to 0 means that the dirtiness and number of dishes are more lighter and lower
            - after 20 no longer is "SHORT" level
        - AVERAGE:15-45
            - in this range consider as "noraml"
            - less than or long than this time range will no longer is AVERAGE level
        - LONG: 40-55
            - MEDIUM dirtiness + AVERAGE number of dishes
            - after 55 no longer is "LONG" level
        - MAXIMUM:50-60
            - HEAVY dirtiness + HIGH number of dishes
            - Maximum wash time

## 4. Create fuzzy membership for all input and output
- Membership_Dishes

![Membership_Dishes](data\\1.membership_dishes.png)

- Memebership_Dirtiness

![Memebership_Dirtiness](data\\1.membership_dishes.png)

- Membership_Wash Time

![Membership_Wash Time](data\\1.membership_dishes.png)

## 5. Create at least 10 fuzzy rules with mix of AND and OR operators
### TOTAL: 10 rules
- AND conditions:(9 rules)

| No. | Number of dishes | Dirtiness Level | Wash Time |
| --- | ---------------- | --------------- | --------- |
| 1. | LOW | LIGHT | SHORT |
| 2. | LOW | MEDIUM | AVERAGE |
| 3. | LOW | HEAVY | LONG |
| 4. | AVERAGE | LIGHT | AVERAGE |
| 5. | AVERAGE | MEDIUM | LONG |
| 6. | AVERAGE | HEAVY | MAXIMUM |
| 7. | HIGH | LIGHT | LONG |
| 8. | HIGH | MEDIUM | MAXIMUM |
| 9. | HIGH | HEAVY | MAXIMUM |

- OR condistions:(9 rules)

| No. | Number of dishes | Dirtiness Level | Wash Time |
| --- | ---------------- | --------------- | --------- |
| 1. | LOW | HEAVY | LONG |
| 2. | AVERAGE | HEAVY | MAXIMUM |
| 3. | HIGH | LIGHT | LONG |
| 4. | AVERAGE | LIGHT | AVERAGE |
| 5. | LOW | MEDIUM | AVERAGE |
| 6. | HIGH | MEDIUM | MAXIMUM |

| No. | Number of dishes | Number of dishes | Wash Time |
| --- | ---------------- | ---------------- | --------- |
| 1. | LOW | AVERAGE | AVERAGE |

| No. | Dirtiness Level | Dirtiness Level | Wash Time |
| --- | --------------- | --------------- | --------- |
| 2. | LIGHT | MEDIUM | AVERAGE |
| 3. | MEDIUM | HEAVY | LONG |

## 6. Model to apply for FIS
    - Mamdani FIS
        - Mamdani FIS is a type of fuzzy logic model that introduced by Ebrahim Mamdani in 1975
        - Mamdani FIS is the one of the most commonly used in fuzzy systems

## 7. Platform: offline AI tools & code your own solution
    - Visual Studio Code
    - Jupyter Notebook
    - Python 3.12
    - scikit-fuzzy, matplotlib, scipy, networkx, seaborn

# Result:
1. Wash Time vs Dirtiness.png

![Wash Time vs Dirtiness](data\\4.WashTimevsDirtiness.png)

2. Fuzzy Inference_Wash Time

![Fuzzy Inference_Wash Time](data\\7.FuzzyInference_WashTime.png)

3. 3D LinePlot_Wash vs Dirtiness.png

![3D LinePlot_Wash vs Dirtiness](data\\9.3DLinePlot_WashvsDirtiness.png)

*and more can view at the data folder 

# Conlusion:
- Wash Time Analysis Summary:
    - Lowest predicted wash time: 27.93 minutes
    - Number of dishes at lowest time: [10]
    - Dirtiness levels at lowest time: [20]

- Top 5 best combinations (high dishes, low wash time):

| dishes | dirtiness | predicted_wash_time |
| ------ | --------- | ------------------- |
| 15 | 30 | 31.471367 |
| 15 | 25 | 32.474016 |
| 15 | 20 | 33.004624 |
| 10 | 20 | 27.927807 |
| 10 | 15 | 28.725242 |

---

## Implementation
### step 0. Git clone this repository to local

### step 1. Set up environment:
>Use **'anaconda'** to create an envs
```bash
conda create --name Fuzzy python=3.12
```

> Activate the environment:
```bash
conda activate Fuzzy
```

>pip install all the requested packages:
```bash
pip install scikit-fuzzy matplotlib
pip install scipy
pip install networkx
pip install seaborn
```

### step 2. Define the input,output and rules
>Define at 'fuzz_config.py'

### Step 3. Run (2. Simple FIS GUI application.py)
>To try
---
