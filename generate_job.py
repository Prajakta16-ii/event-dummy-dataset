import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ----------------------------
# NUMBER OF JOB RECORDS
# ----------------------------
num_jobs = 1000

# ----------------------------
# MASTER DATA
# ----------------------------
user_ids = list(range(1, 501))

college_ids = [101, 102, 103, 104]

job_names = [
    "Software Engineer",
    "Data Analyst",
    "Gen-AI Engineer",
    "Data Scientist",
    "AI Engineer",
    "Frontend Developer",
    "Full Stack Developer",
    "Backend Developer",
    "Machine Learning Engineer",
    "UX Design Internship"
]

job_types = [
    "Full-time",
    "Internship",
    "Part-time"
]

company_names = [
    "TCS",
    "INFOSYS",
    "GOOGLE",
    "DELOITTE",
    "ONEGO",
    "ALLSTATE",
    "UBS",
    "MPHASIS",
    "LTMINDTREE",
    "ACCENTURE"
]

job_locations = [
    "Pune",
    "Mumbai",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Remote"
]

salaries = [
    "₹ 6 LPA",
    "₹ 8 LPA",
    "₹ 10 LPA",
    "₹ 12 LPA",
    "₹ 15,000",
    "₹ 25,000"
]

job_statuses = [
    "Open",
    "Closed",
    "Expired"
]

# ----------------------------
# CREATE JOBS DATAFRAME
# ----------------------------
jobs = pd.DataFrame({
    "user_id": np.random.choice(user_ids, num_jobs),
    "job_id": range(1, num_jobs + 1),
    "college_id": np.random.choice(college_ids, num_jobs),
    "job_name": np.random.choice(job_names, num_jobs),
    "job_type": np.random.choice(job_types, num_jobs),
    "company_name": np.random.choice(company_names, num_jobs),
    "job_location": np.random.choice(job_locations, num_jobs),
    "salary": np.random.choice(salaries, num_jobs),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(1, 120))
        for _ in range(num_jobs)
    ],
    "updated_at": [
        datetime.now() - timedelta(days=random.randint(0, 30))
        for _ in range(num_jobs)
    ],
    "job_status": np.random.choice(job_statuses, num_jobs)
})

# ----------------------------
# EXPORT TO CSV
# ----------------------------
jobs.to_csv("jobs.csv", index=False)

print("jobs.csv created successfully!")
