-- Database Design

-- Projects table: Stores project metadata
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Subjects table: Stores patient/subject info
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    sex CHAR(1),
    age INT,
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Samples table: Stores sample metadata
CREATE TABLE samples (
    sample_id VARCHAR(50) PRIMARY KEY,
    subject_id INT,
    condition VARCHAR(50),
    sample_type VARCHAR(50),
    treatment VARCHAR(50),
    response CHAR(1),
    time_from_treatment_start INT,
    collection_date DATE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Cell_Counts table: Stores cell count measurements
CREATE TABLE cell_counts (
    count_id INT PRIMARY KEY AUTO_INCREMENT,
    sample_id VARCHAR(50),
    population VARCHAR(50),
    count INT NOT NULL,
    FOREIGN KEY (sample_id) REFERENCES samples(sample_id)
);


"""
2. Advantages in a database
    Some key advantages of using a Database:
        - Collaboration is made much smoother. Multiple users can update and access the database at the same time
        - Becuase it seperates the data into it's respective groups, Querying data can be much faster.
        - Data is easily scaleable
        - Can add fields if needed
""" 

-- 3. Write a query to summarize the number of subjects available for each condition:
SELECT
    samples.condition, -- gets condition from samples
    COUNT(DISTINCT samples.subject_id) AS num_subjects -- gets the sumber of unique subject_id's
FROM 
    samples
GROUP BY
    samples.condition;

-- 4. Write a query that returns all melanoma PBMC samples at basline. Only patients who have treatment tr1
CREATE TEMPORARY TABLE melanoma_PBMC_baseline_tr1 AS
SELECT 
    samples.sample_id,
    samples.subject_id,
    samples.condition,
    samples.sample_type,
    samples.treatment,
    samples.response,
    samples.time_from_treatment_start
FROM 
    samples
WHERE 
    samples.condition = 'melanoma'
    AND samples.sample_type = 'PBMC'
    AND samples.treatment = 'tr1'
    AND samples.time_from_treatment_start = 0;

-- 5. Write queries to provide the following

-- a. How many samples from each project
SELECT
    projects.project_id,
    projects.project_name,
    COUNT(melanoma_PBMC_baseline_tr1.sample_id) AS num_samples -- counts the sumber of sample_id's, adds it to a column names num_samples
FROM
    melanoma_PBMC_baseline_tr1
JOIN 
    samples ON melanoma_PBMC_baseline_tr1.sample_id = samples.sample_id -- links to samples and gets subject_id
JOIN
    subjects ON samples.subject_id = subjects.subject_id -- then links to subjects to get sex 
JOIN 
    projects ON subjects.project_id = projects.project_id
GROUP BY 
    projects.project_id,
    projects.project_name;

-- b. How many responders/non-responders
SELECT
    melanoma_PBMC_baseline_tr1.response,
    COUNT(melanoma_PBMC_baseline_tr1.sample_id) AS num_samples -- counts the sumber of sample_id's, adds it to a column names num_samples
FROM
    melanoma_PBMC_baseline_tr1
GROUP BY 
    melanoma_PBMC_baseline_tr1.response

-- c. How many males and females
SELECT
    subjects.sex,
    COUNT(melanoma_PBMC_baseline_tr1.sample_id) AS num_samples -- counts the number of sample_id's, adds it to a column names num_samples
FROM
    melanoma_PBMC_baseline_tr1
JOIN
    samples ON melanoma_PBMC_baseline_tr1.sample_id = samples.sample_id -- links to samples and gets subject_id
JOIN
    subjects ON samples.subject_id = subjects.subject_id -- then links to subjects to get sex
GROUP BY 
    subjects.sex;
