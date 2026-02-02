import pandas as pd

# Step 1: Create application data
data = {
    "application_id": [1, 2, 3, 4, 5],

    # Foreign Keys
    "user_id": [101, 102, 103, 101, 104],      # FK → users.user_id
    "job_id": [201, 202, 201, 203, 204],       # FK → jobs.job_id
    "college_id": [301, 301, 302, 303, 301],   # FK → colleges.college_id

    # Application type
    "application_type": ["Job", "Internship", "Job", "Event", "Job"],

    # Status
    "application_status": ["Applied", "Applied", "Selected", "Rejected", "Applied"],

    # Timestamps
    "applied_at": [
        "2025-01-10 10:30:00",
        "2025-01-12 11:00:00",
        "2025-01-15 09:45:00",
        "2025-01-18 14:20:00",
        "2025-01-20 16:10:00"
    ],
    "updated_at": [
        "2025-01-10 10:30:00",
        "2025-01-13 12:00:00",
        "2025-01-16 10:00:00",
        "2025-01-19 15:00:00",
        "2025-01-21 17:00:00"
    ],
    "deleted_at": [
        None,
        None,
        None,
        None,
        None
    ]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Save to CSV
df.to_csv("applications.csv", index=False)

print("✅ applications.csv created successfully!")
