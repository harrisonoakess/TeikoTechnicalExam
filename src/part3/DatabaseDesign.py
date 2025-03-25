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
    response CHAR(1)
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