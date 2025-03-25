import pandas as pd
import matplotlib.pyplot as plt

# Read the original file in
df_main = pd.read_csv("InstructionMaterial/cell-count.csv") 

# Read in the file with the frequencies
df_frequency = pd.read_csv("OutputFiles/PartOneCellFrequencies.csv")

df_combined = pd.merge(df_frequency, df_main[['sample', 'condition', 'sample_type', 'treatment', 'response']], 
                       on='sample', how='left')
# print(df_combined)


populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

# Filter out what we want
df_filtered = df_combined[(df_combined['treatment'] == 'tr1') & # Filter just tr1
                          (df_combined['condition'] == 'melanoma') & # Filter just melanoma
                          (df_combined['sample_type'] == 'PBMC')] # Filter just PBMC (blood) samples

plt.figure(figsize=(12, 8))                          

for i, pop in enumerate(populations, 1):
    plt.subplot(2,3,i)
    population_col = df_filtered[df_filtered['population'] == pop]

    # responders and nonresponders
    responders = population_col[population_col['response'] == 'y']['percentage']
    nonResponders = population_col[population_col['response'] == 'n']['percentage']


    data = [responders, nonResponders]
    
    plt.title(f'{pop} Percentage')
    plt.boxplot(data, labels=['y','n'])
    plt.xlabel("Responder (y) vs. Non-Responder (n)")
    plt.ylabel("Relative Frequencies")

plt.tight_layout()
plt.savefig('OutputFiles/boxplots.png')
plt.close()
print("Boxplots saved to OutputFiles/boxplots.png")
