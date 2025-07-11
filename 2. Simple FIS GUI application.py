
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
import sys
import tkinter as tk
import matplotlib.pyplot as plt

from skfuzzy import control as ctrl
from skfuzzy import interp_membership
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from fuzzy_config import dishes, dirtiness, wash_time, rules

# == Initialization ==
# Set defuzzification method (centroid for Mamdani)
wash_time.defuzzify_method = 'centroid'

# Build control system
washing_ctrl = ctrl.ControlSystem(rules)
simulator = ctrl.ControlSystemSimulation(washing_ctrl)

# == HELPER FUNCTIONS ==
# GUI application
# Get fuzzy label with highest membership
def get_fuzzy_label(value, fuzzy_var, labels):
    max_membership = 0
    best_label = None
    for label in labels:
        mf_array = fuzzy_var[label].mf
        membership = interp_membership(fuzzy_var.universe, mf_array, value)
        if membership > max_membership:
            max_membership = membership
            best_label = label.upper()
    return best_label

# Update plot
def update_plot():
    d_val = dishes_scale.get()
    di_val = dirtiness_scale.get()

    try:
        if d_val == 0:
            predicted_time = 0
            w_val = 0
        else:
            simulator.input['dishes'] = d_val
            simulator.input['dirtiness'] = di_val
            simulator.compute()
            predicted_time = simulator.output['wash_time']
            w_val = predicted_time
    except Exception as e:
        print("!* Simulation error:", e)
        predicted_time = 0
        w_val = 0  # fallback to prevent crash

    # Clear and redraw plots
    ax1.clear()
    ax2.clear()
    ax3.clear()

    for term in dishes.terms:
        ax1.plot(dishes.universe, dishes[term].mf, label=term.upper())
    ax1.axvline(d_val, color='red', linestyle='--')
    ax1.set_title("Number of Dishes")
    ax1.legend()

    for term in dirtiness.terms:
        ax2.plot(dirtiness.universe, dirtiness[term].mf, label=term.upper())
    ax2.axvline(di_val, color='red', linestyle='--')
    ax2.set_title("Dirtiness Level")
    ax2.legend()

    for term in wash_time.terms:
        ax3.plot(wash_time.universe, wash_time[term].mf, label=term.upper())
    ax3.axvline(w_val, color='red', linestyle='--')
    ax3.set_title(f"Predicted Wash Time: {w_val:.2f} min")
    ax3.legend()

    # Fuzzy label output
    time_label = get_fuzzy_label(w_val, wash_time, ['short', 'average', 'long', 'maximum'])
    label_var.set(f"Fuzzy output: {time_label}")
    
    canvas.draw()

# Handle window close event
def on_closing():
    plt.close('all')     # Closes all matplotlib figures
    root.quit()          # Stops the Tkinter event loop
    root.destroy()       # Destroys the Tkinter window
    sys.exit()           # Fully exits the Python script

# == START ==
if __name__ == "__main__":
    # Create tkinter window
    root = tk.Tk()
    root.title("Fuzzy Logic Membership Viewer")
    root.geometry("900x850")
    root.resizable(False, False)

    # Create left and right frames
    left_frame = tk.Frame(root, width=600, height=800)
    left_frame.pack(side=tk.LEFT)
    left_frame.pack_propagate(False)

    # Create left and right frames
    right_frame = tk.Frame(root, width=300, height=800)
    right_frame.pack(side=tk.RIGHT, padx=10)
    right_frame.pack_propagate(False)
    
    # Create plots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 8))
    fig.subplots_adjust(hspace=0.5)
    canvas = FigureCanvasTkAgg(fig, master=left_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Create scales
    tk.Label(right_frame, text="Number of Dishes").pack()
    dishes_scale = tk.Scale(right_frame, from_=0, to=50, orient=tk.HORIZONTAL, command=lambda x: update_plot())
    dishes_scale.set(25)
    dishes_scale.pack()

    # Create scales
    tk.Label(right_frame, text="Dirtiness Level (%)").pack()
    dirtiness_scale = tk.Scale(right_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda x: update_plot())
    dirtiness_scale.set(50)
    dirtiness_scale.pack()

    # Output label
    label_var = tk.StringVar()
    label_result = tk.Label(right_frame, textvariable=label_var, font=("Arial", 10), fg="blue")
    label_result.pack(pady=20)

    # Update plot
    update_plot()

    # Handle window close event
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Run tkinter event loop
    root.mainloop()

# == END ==