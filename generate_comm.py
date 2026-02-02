import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ----------------------------
# NUMBER OF COMMENTS
# ----------------------------
num_comments = 4000

# ----------------------------
# MASTER DATA
# ----------------------------
user_ids = list(range(1, 1001))  # 1000 users

content_names = [
    "Post",
    "Event",
    "Job",
    "Department",
    "Announcement"
]

comment_texts = [
    "Great update!",
    "Very informative.",
    "Thanks for sharing.",
    "This is helpful.",
    "Nice initiative.",
    "Looking forward to this.",
    "Good opportunity for students."
]

# ----------------------------
# CREATE COMMENTS DATAFRAME
# ----------------------------
comments = pd.DataFrame({
    "comment_id": range(1, num_comments + 1),
    "user_id": np.random.choice(user_ids, num_comments),
    "content_name": np.random.choice(content_names, num_comments),
    "content_id": np.random.randint(1, 5000, num_comments),
    "comment_text": np.random.choice(comment_texts, num_comments),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(1, 180))
        for _ in range(num_comments)
    ],
    "updated_at": [
        datetime.now() - timedelta(days=random.randint(0, 30))
        for _ in range(num_comments)
    ],
    "deleted_at": [
        None if random.random() > 0.1
        else datetime.now() - timedelta(days=random.randint(1, 10))
        for _ in range(num_comments)
    ]
})

# ----------------------------
# EXPORT TO CSV
# ----------------------------
comments.to_csv("comments.csv", index=False)

print("comments.csv created successfully!")
