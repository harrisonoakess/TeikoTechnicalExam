import pandas as pd
import os

# Read the file in
df = pd.read_csv("InstructionMaterial/cell-count.csv") 

# Name the different population column headers
populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

# Creates a new column that will sum up by row 
df['total_count'] = df[populations].sum(axis=1)

melt_df = df.melt(
    id_vars=['sample', 'total_count'], # id_vars tells us which column to not change
    value_vars=populations,           # value_vars tells us what column to pivot (make longer)
    var_name='population',             # var_name gives a new name for population column
    value_name='count'                 # value_name gives new name for cell counts
)

# Add a new column that gets percentage: Percentage = (cell count for pupulation/total cell count) * 100
melt_df['percentage'] = ((melt_df['count'] / melt_df['total_count'])*100)

output_df = melt_df[['sample', 'total_count', 'population', 'count', 'percentage']]
# print(output_df)

output_dir = 'OutputFiles'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# Output the file into my output folder
output_df.to_csv('OutputFiles/PartOneCellFrequencies.csv', index=False)
print('Output saved successfully to OutputFiles/PartOneCellFrequencies.csv')