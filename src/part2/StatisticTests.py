import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, shapiro, mannwhitneyu

# Read the original file in
df_main = pd.read_csv("../../InstructionMaterial/cell-count.csv") 

# Read in the file with the frequencies
df_frequency = pd.read_csv("../../OutputFiles/PartOneCellFrequencies.csv")

df_combined = pd.merge(df_frequency, df_main[['sample', 'condition', 'sample_type', 'treatment', 'response']], 
                       on='sample', how='left')
# print(df_combined)


populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

# Filter out what we want
df_filtered = df_combined[(df_combined['treatment'] == 'tr1') & # Filter just tr1
                          (df_combined['condition'] == 'melanoma') & # Filter just melanoma
                          (df_combined['sample_type'] == 'PBMC')] # Filter just PBMC (blood) sample

output_file = '../../OutputFiles/statistical_analysis.txt'
with open(output_file, 'w') as f:
    f.write("Statistical Analysis:\n\n")
    for pop in populations:
        population_col = df_filtered[df_filtered['population'] == pop]
        responders = population_col[population_col['response'] == 'y']['percentage']
        nonResponders = population_col[population_col['response'] == 'n']['percentage']

        # Run Shapiro-Wilk test to see if the data is normally distributed
        f.write(f"{pop}:\n")
        stat_r, p_r = shapiro(responders)
        stat_nr, p_nr = shapiro(nonResponders)
        f.write(f'Shapiro-Wilk Responders: p = {p_r:.3f}\n')
        f.write(f'Shapiro-Wilk Non-Responders: p = {p_nr:.3f}\n')


        if p_r >= 0.05 and p_nr >= 0.05: # If data is normal
            f.write("  Data is normal, using t-test:\n")
            t_stat, p_val = ttest_ind(responders, nonResponders, nan_policy='omit')
            f.write(f"    t-statistic = {t_stat:.3f}, p-value = {p_val:.3f}\n")
            if p_val < 0.05:
                f.write(f"        {pop} -> Significant difference (p < 0.05)\n")
            else:
                f.write(f"        {pop} -> No significant difference (p > 0.05)\n")
        else: # If data is not normal
            f.write("  Data is not normal, using Mann-Whitney U test:\n")
            u_stat, p_stat = mannwhitneyu(responders, nonResponders, alternative='two-sided')
            f.write(f"    U-statistic = {u_stat:.3f}, p-value = {p_stat:.3f}\n")
            if p_stat < 0.05:
                f.write(f"        {pop} -> Significant difference (p < 0.05)\n")
            else:
                f.write(f"        {pop} -> No significant difference (p > 0.05)\n")
        f.write("\n")