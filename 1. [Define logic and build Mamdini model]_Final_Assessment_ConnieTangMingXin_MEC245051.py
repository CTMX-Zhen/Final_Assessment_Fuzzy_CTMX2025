
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

    # GitHub: 
    
"""
    STUDENT'S OUTCOMES
"""
# pip install scikit-fuzzy, matplotlib, scipy, networkx, seaborn

# == IMPORT LIBRARIES ==
import os
import numpy as np
import pandas as pd
import skfuzzy as fuzz
import matplotlib.pyplot as plt

from skfuzzy.control import Rule
from skfuzzy import control as ctrl

# == HELPER FUNCTIONS ==
# Convert crisp value to fuzzy label using highest membership
def get_fuzzy_label(value, fuzzy_var, labels):
    """Map crisp value to its highest membership fuzzy label."""
    max_membership = 0
    best_label = None
    for label in labels:
        mf_array = fuzzy_var[label].mf
        membership = fuzz.interp_membership(fuzzy_var.universe, mf_array, value)
        if membership > max_membership:
            max_membership = membership
            best_label = label.upper()
    return best_label

# == START ==
if __name__ == "__main__":

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

    # Create 'data' folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Plot and visualize membership functions
    print("Number of dishes:")
    dishes.view()
    plt.savefig("data\\1.membership_dishes.png", dpi=300, bbox_inches='tight')
    plt.show()

    print("Dirtiness level:")
    dirtiness.view()
    plt.savefig("data\\2.membership_dirtiness.png", dpi=300, bbox_inches='tight')
    plt.show()

    print("Wash time:")
    wash_time.view()
    plt.savefig("data\\3.membership_wash_time.png", dpi=300, bbox_inches='tight')
    plt.show()

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

    # Print all fuzzy rules to console (copy to report if needed)
    print("All fuzzy logic rules used in the system:")
    for i, rule in enumerate(rules, 1):
        print(f"Rule {i}: {rule}\n")

    # Set up debluring method for Mandini FIS
    wash_time.defuzzify_method = 'centroid'

    # Combine the 10 rules with Mamdini FIS
    washing_ctrl = ctrl.ControlSystem(rules)

    # Create a simulator to test the result
    simulator = ctrl.ControlSystemSimulation(washing_ctrl)

    # Test multiple sample inputs and visualize the predictions result
    test_cases = [
        (10, 20), # LOW number + LIGHT dirtiness
        (25, 40), # AVERAGE number + LIGHT (max) dirtiness
        (35, 70), # AVERAGE nunmber + MEDIUM (max) dirtiness
        (45, 90), # HIGH number + HEAVY dirtyness
        (50, 100) # HIGH (max) number + HEARY (max) dirtyness
    ]

    # Run the simulation
    results = []
    # for dishes_input, dirtiness_input in test_cases:
    for dishes_input, dirtiness_input in test_cases:
        simulator.input['dishes'] = dishes_input
        simulator.input['dirtiness'] = dirtiness_input
        simulator.compute()
        results.append((dishes_input, dirtiness_input, simulator.output['wash_time']))

    # Plot
    plt.figure(figsize=(8, 5))
    # for d, di, w in results:
    for d, di, w in results:
        print(f"Wash time for {d} dishes with {di} dirtyness level is {w} min")
        plt.scatter(di, w, s=100, label=f'{d} dishes')

    # Add labels and title
    plt.title('Wash Time vs Dirtiness (for different dishes count)')
    plt.xlabel('Dirtiness Level (%)')
    plt.ylabel('Predicted Wash Time (min)')
    plt.legend()
    plt.grid(True)
    plt.savefig("data\\4.WashTimevsDirtiness.png", dpi=300, bbox_inches='tight')
    plt.show()

    # Input a sample data
    d = simulator.input['dishes'] = 35 # AVERAGE number of dishes
    di = simulator.input['dirtiness'] = 70 # (max) MEDIUM dirtiness level

    # Perform fuzzy inference
    simulator.compute()

    # Output result (wash time) for sample data
    predicted_time = simulator.output['wash_time']
    print(f"Predicted wash time: {predicted_time:.2f} minutes")

    # Map inputs and output to fuzzy categories
    dish_label = get_fuzzy_label(d, dishes, ['low', 'average', 'high'])
    dirt_label = get_fuzzy_label(di, dirtiness, ['light', 'medium', 'heavy'])
    time_label = get_fuzzy_label(predicted_time, wash_time, ['short', 'average', 'long', 'maximum'])

    # Explan the output result based on fuzzy labels
    explanation = f"Number of dishes = {dish_label}, Dirtiness level = {dirt_label} → Wash Time = {time_label}"
    print("Explanation:", explanation)

    # Visualize the output result
    wash_time.view(sim=simulator)
    plt.axvline(predicted_time, color='red', linestyle='--', label='Predicted Value')
    plt.legend()
    plt.title("Output Membership Function\n(Predicted Wash Time Highlighted)")
    plt.savefig("data\\5.membership_dishes.png", dpi=300, bbox_inches='tight')
    plt.show()

    # Test output wash time for different input combinations (number of dishes x dirtiness level) 
    dishes_range = np.arange(0, 51, 5)
    dirtiness_range = np.arange(0, 101, 5)

    wash_surface = np.zeros((len(dishes_range), len(dirtiness_range)))

    # Run the simulation
    for i, d in enumerate(dishes_range):
        for j, di in enumerate(dirtiness_range):
            simulator.input['dishes'] = d
            simulator.input['dirtiness'] = di
            simulator.compute()
            wash_surface[i, j] = simulator.output['wash_time']

    # Convert to 2D grid
    X, Y = np.meshgrid(dirtiness_range, dishes_range)
    Z = wash_surface

    # Contour plot (2D view of wash_time)
    cp = plt.contourf(X, Y, Z, cmap='viridis', levels=20)
    plt.colorbar(cp, label='Predicted Wash Time (min)')
    plt.title('Contour Map: Wash Time Prediction')
    plt.xlabel('Dirtiness Level (%)')
    plt.ylabel('Number of Dishes')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data\\6.ContourMap_WashTimePrediction.png", dpi=300, bbox_inches='tight')
    plt.show()

    # Convert plot to 3D surface (3D view of wash_time)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('Dirtiness Level (%)')
    ax.set_ylabel('Number of Dishes')
    ax.set_zlabel('Predicted Wash Time (min)', labelpad=1)
    ax.set_title('Fuzzy Inference Surface: Wash Time')
    plt.tight_layout()
    plt.savefig("data\\7.FuzzyInference_WashTime.png", dpi=300, bbox_inches='tight')
    plt.show()

    # Test wash time and dirtiness at same number of dishes (Multiple line plots)
    for d in [10, 25, 35, 45, 50]:
        times = []
        for di in dirtiness_range:
            simulator.input['dishes'] = d
            simulator.input['dirtiness'] = di
            simulator.compute()
            times.append(simulator.output['wash_time'])
        plt.plot(dirtiness_range, times, marker='o', label=f'{d} dishes')

    plt.title('Wash Time vs Dirtiness')
    plt.xlabel('Dirtiness Level (%)')
    plt.ylabel('Predicted Wash Time (min)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data\\8.WashTimevsDirtiness.png", dpi=300, bbox_inches='tight')
    plt.show()

    # Convert plot to 3D surface (3D view of wash_time)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Plot multiple lines
    for d in [10, 25, 35, 45, 50]:
        z_vals = []
        for di in dirtiness_range:
            simulator.input['dishes'] = d
            simulator.input['dirtiness'] = di
            simulator.compute()
            z_vals.append(simulator.output['wash_time'])
        x_vals = dirtiness_range
        y_vals = [d] * len(dirtiness_range)
        ax.plot(x_vals, y_vals, z_vals, label=f'{d} dishes')

    ax.set_xlabel('Dirtiness Level (%)')
    ax.set_ylabel('Number of Dishes')
    ax.set_zlabel('Predicted Wash Time (min)', labelpad=1)
    ax.set_title('3D Line Plot: Wash Time vs Dirtiness')
    ax.legend()
    plt.savefig("data\\9.3DLinePlot_WashvsDirtiness.png", dpi=300, bbox_inches='tight')
    plt.show()

    # Save the simulation results to a CSV
    records = []
    # Run the simulation
    for d in dishes_range:
        for di in dirtiness_range:
            simulator.input['dishes'] = d
            simulator.input['dirtiness'] = di
            simulator.compute()
            records.append({
                'dishes': d,
                'dirtiness': di,
                'predicted_wash_time': simulator.output['wash_time']
            })

    # Export to CSV
    df = pd.DataFrame(records)
    df.to_csv("data\\wash_time_simulation_output.csv", index=False)

    # Load the CSV
    df = pd.read_csv("data\\wash_time_simulation_output.csv")

    # Find the minimum wash time
    min_time = df['predicted_wash_time'].min()
    min_records = df[df['predicted_wash_time'] == min_time]

    # Dish and dirtiness levels at minimum wash time
    lowest_dishes = min_records['dishes'].unique().tolist()
    lowest_dirtiness = min_records['dirtiness'].unique().tolist()

    # Best combinations: high dishes, low wash time
    #   - Define "best" as: top 10% lowest wash time with max dishes
    #   - Which mean the best combination can wash a lot number of dishes with the shortest time
    threshold = df['predicted_wash_time'].quantile(0.10)
    best_combos = df[df['predicted_wash_time'] <= threshold]
    best_combos = best_combos.sort_values(by=['dishes', 'predicted_wash_time'], ascending=[False, True])

    # Optionally export best combos
    best_combos.to_csv("data\\best_dish_dirtiness_combos.csv", index=False)

    # Print the summary results
    print("Wash Time Analysis Summary:")
    print("-" * 40)

    print(f"Lowest predicted wash time: {min_time:.2f} minutes")
    print(f"Number of dishes at lowest time: {lowest_dishes}")
    print(f"Dirtiness levels at lowest time: {lowest_dirtiness}")

    print(f"\nTop 5 best combinations (high dishes, low wash time):")
    print(best_combos.head(5).to_string(index=False))

    print("\n Saved full list to: best_dish_dirtiness_combos.csv")

# == END ==