import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ----------------------------
# NUMBER OF JOBS
# ----------------------------
num_jobs = 1000

# ----------------------------
# MASTER DATA (FROM UI)
# ----------------------------
job_names = [
    "COO",
    "Demigod",
    "Software Engineer II",
    "UX Design Internship",
    "Test Engineer Internship",
    "Software Engineer"
]

job_types = ["Full-time", "Internship"]

company_names = [
    "Next Electronics",
    "Demo",
    "TCS",
    "Google India",
    "Creative Studios Inc",
    "TechCorp Pvt Ltd"
]

locations = [
    "Narniwadi",
    "SCOE Campus",
    "Austin, TX",
    "San Francisco, CA",
    "Pune"
]

salaries = [
    "₹ 20,000",
    "₹ 56,546",
    "₹ 4 LPA",
    "₹ 6 LPA",
    "₹ 10,000"
]

college_ids = [101, 102, 103, 104]

# ----------------------------
# CREATE JOBS DATAFRAME
# ----------------------------
jobs = pd.DataFrame({
    "job_id": range(1, num_jobs + 1),
    "college_id": np.random.choice(college_ids, num_jobs),
    "job_name": np.random.choice(job_names, num_jobs),
    "job_type": np.random.choice(job_types, num_jobs),
    "company_name": np.random.choice(company_names, num_jobs),
    "job_location": np.random.choice(locations, num_jobs),
    "salary": np.random.choice(salaries, num_jobs),
    "apply_by_date": [
        datetime.now() + timedelta(days=random.randint(-30, 120))
        for _ in range(num_jobs)
    ]
})

# ----------------------------
# DERIVE JOB STATUS
# ----------------------------
jobs["job_status"] = jobs["apply_by_date"].apply(
    lambda x: "Expired" if x < datetime.now() else "Open"
)

# ----------------------------
# EXPORT TO CSV
# ----------------------------
jobs.to_csv("jobs.csv", index=False)

print("jobs.csv created successfully!")
