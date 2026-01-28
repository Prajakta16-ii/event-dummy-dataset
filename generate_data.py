import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ======================
# CREATE USERS CSV
# ======================
num_users = 1000

users = pd.DataFrame({
    "user_id": range(1, num_users + 1),
    "username": [f"user_{i}" for i in range(1, num_users + 1)],
    "role": np.random.choice(["student", "faculty", "admin"], num_users),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(0, 365))
        for _ in range(num_users)
    ]
})

users.to_csv("users.csv", index=False)
print("users.csv created")

# ======================
# CREATE EVENTS CSV
# ======================
num_events = 5000

event_names = [
    "Tech Fest 2025",
    "AI & Data Science Seminar",
    "Campus Placement Drive",
    "Hackathon 2025",
    "Entrepreneurship Bootcamp"
]

event_types = ["Workshop", "Seminar", "Hackathon", "Conference"]
locations = ["Mumbai", "Pune", "Delhi", "Bangalore"]
created_by = ["admin01", "faculty01", "pritish123"]

events = pd.DataFrame({
    "event_id": range(1, num_events + 1),
    "user_id": np.random.choice(users["user_id"], num_events),
    "event_name": np.random.choice(event_names, num_events),
    "event_type": np.random.choice(event_types, num_events),
    "location": np.random.choice(locations, num_events),
    "created_by": np.random.choice(created_by, num_events),

    "start_date": [
        datetime.now() + timedelta(days=random.randint(1, 60))
        for _ in range(num_events)
    ],
    "end_date": [
        datetime.now() + timedelta(days=random.randint(61, 90))
        for _ in range(num_events)
    ],
    "interaction_timestamp": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_events)
    ]
})

events.to_csv("events.csv", index=False)
print("events.csv created")
