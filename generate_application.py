import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ----------------------------
# NUMBER OF APPLICATIONS
# ----------------------------
num_applications = 4000

# ----------------------------
# MASTER DATA
# ----------------------------
user_ids = list(range(1, 1001))       # 1000 users
job_ids = list(range(1, 1001))        # jobs from jobs.csv
college_ids = [101, 102, 103, 104]

application_statuses = [
    "Applied",
    "Shortlisted",
    "Interview",
    "Selected",
    "Rejected"
]

# ----------------------------
# CREATE APPLICATIONS DATAFRAME
# ----------------------------
applications = pd.DataFrame({
    "application_id": range(1, num_applications + 1),
    "user_id": np.random.choice(user_ids, num_applications),
    "job_id": np.random.choice(job_ids, num_applications),
    "college_id": np.random.choice(college_ids, num_applications),
    "application_status": np.random.choice(application_statuses, num_applications),
    "applied_at": [
        datetime.now() - timedelta(days=random.randint(1, 120))
        for _ in range(num_applications)
    ],
    "updated_at": [
        datetime.now() - timedelta(days=random.randint(0, 30))
        for _ in range(num_applications)
    ],
    "deleted_at": [
        None if random.random() > 0.1
        else datetime.now() - timedelta(days=random.randint(1, 10))
        for _ in range(num_applications)
    ]
})

# ----------------------------
# EXPORT TO CSV
# ----------------------------
applications.to_csv("application.csv", index=False)

print("application.csv created successfully!")
