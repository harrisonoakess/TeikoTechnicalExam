## Task 1: Python Program for Cell Count Conversion

### Objective
Write a Python program to convert cell counts in `cell-count.csv` to relative frequencies (in percentage) of the total cell count for each sample. The total cell count for a sample is the sum of cells across five populations within that sample.

### Requirements
- **Input**: `cell-count.csv`
- **Output**: A CSV file with the following columns:
  - `sample`: Sample ID (as in the `sample` column of `cell-count.csv`)
  - `total_count`: Total cell count of the sample
  - `population`: Name of the immune cell population (e.g., `b_cell`, `cd8_t_cell`, etc.)
  - `count`: Cell count for the population
  - `percentage`: Relative frequency in percentage (calculated as `(count / total_count) * 100`)

### Output File
The program will generate a CSV file containing cell counts and their corresponding relative frequencies for each population of each sample.

---

## Task 2: Analysis of Treatment Response in Melanoma Patients

### Objective
Among patients receiving treatment `tr1`, compare the differences in cell population relative frequencies between melanoma patients who respond (responders) and those who do not (non-responders) to predict response to `tr1`. Use only PBMC (blood) samples.

### Data Details
- Response information is in the `response` column of `cell-count.csv`:
  - `y`: Responder
  - `n`: Non-responder

### Subtasks
#### a. Boxplots
For each immune cell population, generate a boxplot comparing the relative frequencies of responders (`y`) versus non-responders (`n`) among PBMC samples.

#### b. Statistical Analysis
Identify which cell populations show significant differences in relative frequencies between responders and non-responders. Provide statistical evidence (e.g., p-values from appropriate tests) to support conclusions.

---

## Database Design

### Task 1: Schema Design
Design a database to capture the type of information in `cell-count.csv`, scalable for hundreds of projects, thousands of samples, and various analytics (e.g., responder vs. non-responder comparisons).

#### Prototype Schema
A rough schema might include the following tables:
- **Projects**: Stores project metadata
  - `project_id` (PK)
  - `project_name`
  - `description`
- **Subjects**: Stores patient/subject information
  - `subject_id` (PK)
  - `sex` (e.g., male, female)
  - `condition` (e.g., melanoma)
- **Samples**: Stores sample metadata
  - `sample_id` (PK)
  - `project_id` (FK to Projects)
  - `subject_id` (FK to Subjects)
  - `sample_type` (e.g., PBMC)
  - `time_from_treatment_start` (e.g., 0 for baseline)
  - `treatment` (e.g., `tr1`)
  - `response` (e.g., `y`, `n`)
- **Cell_Counts**: Stores cell count data
  - `count_id` (PK)
  - `sample_id` (FK to Samples)
  - `population` (e.g., `b_cell`, `cd8_t_cell`)
  - `count` (integer)
  - `total_count` (calculated total for the sample)
  - `percentage` (relative frequency)

### Task 2: Advantages of a Database
- **Scalability**: Handles large datasets across multiple projects and samples.
- **Query Efficiency**: Enables fast retrieval and analysis (e.g., filtering by treatment or response).
- **Data Integrity**: Enforces relationships and constraints (e.g., foreign keys).
- **Flexibility**: Supports diverse analytics without restructuring raw files.

### Task 3: Query - Subjects per Condition
Summarize the number of subjects available for each condition:
```sql
SELECT condition, COUNT(DISTINCT subject_id) as subject_count
FROM Subjects
GROUP BY condition;
