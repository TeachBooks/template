import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def find_scenarios_with_segment_i(segments_fixed, df):
    """Given a list of segments, return set of dependent scenarios."""
    idx = []
    segments_fixed = set(segments_fixed)
    for i, row in enumerate(df['failed_segments'].values):
        segments_row = set([int(seg) for seg in row.split(",")])
        intersection = list(segments_fixed.intersection(segments_row))
        if len(intersection) > 0:
            idx.append(True)
        else:
            idx.append(False)
    segment_table = df.iloc[idx]
    return segment_table

def assemble_analysis_cases(df):
    """From scenario dataframe collect damage and fatality information."""
    econ_damage_case_1 = df.iloc[:,3] #  Unexpected, no evacuation
    econ_damage_case_2 = df.iloc[:,5] #  Unexpected, unorganised evacuation
    econ_damage_case_3 = df.iloc[:,7] #  Expected, unorganised evacuation
    econ_damage_case_4 = df.iloc[:,9] #  Expected, organised evacuation

    fatalities_case_1 = df.iloc[:,4]
    fatalities_case_2 = df.iloc[:,6]
    fatalities_case_3 = df.iloc[:,8]
    fatalities_case_4 = df.iloc[:,10]

    scenario_prob = df.iloc[:,1] #  scenario probability

    cases = {'damage': [econ_damage_case_1, econ_damage_case_2, econ_damage_case_3, econ_damage_case_4],
             'fatality': [fatalities_case_1, fatalities_case_2, fatalities_case_3, fatalities_case_4]}
    return cases

def exceedance_prob(cases, scenario_prob):
    """Compute exceedance probability."""
    case_1 = cases[0]
    case_2 = cases[1]
    case_3 = cases[2]
    case_4 = cases[3]
    
    key = case_1.index
    
    # Combine Evacuation Scenarios into new Dataframe
    scenarios = [pd.DataFrame({'Nr': key, 'N/D': case_1}),
                 pd.DataFrame({'Nr': key, 'N/D': case_2}),
                 pd.DataFrame({'Nr': key, 'N/D': case_3}),
                 pd.DataFrame({'Nr': key, 'N/D': case_4})]
    
    scen_combi = pd.concat(scenarios, ignore_index=True)
    
    # Sort values by key ('Nr')
    scen_combi_sorted = scen_combi.sort_values(by=['Nr']) # useful if scen_combi_nodup.sort_values(by=['Nr']) in case of no duplicates
#     scen_combi_sorted = scen_combi.reset_index(drop=True)  # Reset index starting from 0
    
    # Create new Dataframe for scenario prob with corresponding key
    prob = pd.DataFrame({'Nr': key, 'scen_prob':scenario_prob})
    
    # Join both Dataframes based on common key
    join_scen_prob = scen_combi_sorted.join(prob.set_index('Nr'), on='Nr')
    
    # Determine Exceedance Probability
    sorted_N_D = scen_combi.sort_values(by=['N/D'])  # Sort N/D based on ascending order
    complete_table = sorted_N_D.join(prob.set_index('Nr'), on='Nr')    
    
    N_D_prob_ordered = complete_table.iloc[:,2]
    
#     N_D = join_scen_prob.dropna(axis=0).iloc[:,1].reset_index(drop=True)  # N/D
#     N_D_prob = join_scen_prob.dropna(axis=0).iloc[:,2].reset_index(drop=True)  # Corresponding scenario prob
#     print('N_D', N_D)
#     print('N_D_PROB', N_D_prob)
#     order = N_D.argsort()  # Sort N/D based on ascending order
    
#     N_D_prob_ordered = N_D_prob[order]
    N_D_prob_cs = np.cumsum(N_D_prob_ordered[::-1])  # Take cumulative sum of reversed order
    
    exceed_prob = (1/4) * N_D_prob_cs[::-1]  # Reverse result (1-FN(n)) and /4 as 4 evacuation scenarios are considered
    complete_table = complete_table.join(exceed_prob, lsuffix='_orignal', rsuffix='_new') #  complete resulting table
#     N_D_ordered = N_D[order].reset_index(drop=True)
    N_D_ordered = complete_table.iloc[:,1]
    
    return N_D_ordered, exceed_prob, complete_table

def sensitivity_analysis(cases, scenario_prob, idx_segment, N_D_ordered_original, exceed_prob_original, complete_table):
    """Docstring incomplete."""
    case_1 = cases[0]
    case_2 = cases[1]
    case_3 = cases[2]
    case_4 = cases[3]
    
    # Dropping segment(s)
    case_1_exc = case_1.drop(idx_segment, axis=0).reset_index(drop=True)
    case_2_exc = case_2.drop(idx_segment, axis=0).reset_index(drop=True)
    case_3_exc = case_3.drop(idx_segment, axis=0).reset_index(drop=True)
    case_4_exc = case_4.drop(idx_segment, axis=0).reset_index(drop=True)
    
    scenario_prob_exc = scenario_prob.drop(idx_segment, axis=0).reset_index(drop=True)
    
    # Determine new exceedance probability - Excluding segment(s)
    N_D_ordered_new, exceed_prob_new, complete_table_new = exceedance_prob([case_1_exc, case_2_exc, case_3_exc, case_4_exc], scenario_prob_exc)
    
    # Plotting
    plot_curves(N_D_ordered_original, exceed_prob_original)
    plt.plot(N_D_ordered_new.dropna(axis=0), exceed_prob_new.dropna(axis=0), marker="o", linewidth=2, markersize=5, color= 'darkblue', label='Excluding segment(s)', zorder=10)
    
    # Plot dropped points
    x_point = []
    y_point = []
    for i in range(len(idx_segment)):
        row_i = complete_table[complete_table['Nr']== (idx_segment[i] + 1)]
        for j in range(len(row_i)):
            x_point.append(row_i.iloc[j, 1])
            y_point.append(row_i.iloc[j, 3])
    plt.scatter(x_point, y_point, label='Dropped Points', s=45, color='darkred', zorder=15)  # Plot the points corresponding to deleted segment
    plt.legend()
    plt.show()
    return N_D_ordered_new, exceed_prob_new, complete_table_new

def plot_curves(N_D, exceedance_prob):
    """Plot FN or FD risk curve."""
    plt.figure(figsize=(10,6))
    set_TUDstyle()
    
    # Plot FN/FD curve
    plt.plot(N_D, exceedance_prob, marker="o", linewidth=2, markersize=5, label='FN/D-curve',zorder=0)
    
    # Add acceptable limit line
    ND = np.linspace(1,100000,100000)  # fatalities
    alpha = 1
    C = 0.010
    limit_line = (C/ND**alpha)
    plt.plot(limit_line, linewidth=2, color='darkgreen', label='Acceptable Limit Line', zorder=5)
    
    # Styling
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True, which="both", axis='x')
    plt.grid(True, which="major", axis='y')
    plt.title('FN/D-curve')
    plt.ylabel('Probability of Exceedance, $1-F_N(n)$')
    plt.xlabel('Economic damage [meuro] / Fatalities')
    plt.xlim(1,100000)
    plt.ylim(10**(-7),10**(-3))
    plt.legend()

def compute_benefit(table_old, table_new):
    """Compute new and old consequences and net benefit."""
    old_consequences = np.sum(table_old["N/D"].values * table_old["scen_prob_new"].values)
    new_consequences = np.sum(table_new["N/D"].values * table_new["scen_prob_new"].values)
    benefit = old_consequences - new_consequences
    return old_consequences, new_consequences, benefit
    
def set_TUDstyle():
    TUcolor = {"cyan": "#00A6D6", "darkgreen": "#009B77", "purple": "#6F1D77",
               "darkred": "#A50034", "darkblue": "#0C2340",
               "orange": "#EC6842", "green": "#6CC24A",
               "lightcyan": "#00B8C8", "red": "#E03C31", "pink": "#EF60A3",
               "yellow": "#FFB81C", "blue": "#0076C2"}
    plt.rcParams.update({'axes.prop_cycle': plt.cycler(color=TUcolor.values()),
                         'font.size': 16, "lines.linewidth": 4})
    return TUcolor