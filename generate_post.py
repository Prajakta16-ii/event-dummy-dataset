import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ----------------------------
# NUMBER OF POSTS
# ----------------------------
num_posts = 3000

# ----------------------------
# MASTER DATA
# ----------------------------
user_ids = list(range(1, 501))

college_ids = [101, 102, 103, 104]

content_types = [
    "TEXT",
    "IMAGE",
    "VIDEO"
]

post_descriptions = [
    "Campus life moments",
    "Workshop on AI and Data Science",
    "Placement drive updates",
    "Hackathon highlights",
    "Cultural fest memories",
    "Great learning experience"
]

media_names = [
    "campus.jpg",
    "workshop.jpg",
    "placement.jpg",
    "hackathon.jpg",
    "fest.jpg",
    None  # for TEXT posts
]

# ----------------------------
# CREATE POSTS DATAFRAME
# ----------------------------
posts = pd.DataFrame({
    "post_id": range(1, num_posts + 1),
    "user_id": np.random.choice(user_ids, num_posts),
    "college_id": np.random.choice(college_ids, num_posts),
    "content_type": np.random.choice(content_types, num_posts),
    "post_description": np.random.choice(post_descriptions, num_posts),
    "media_name": np.random.choice(media_names, num_posts),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(1, 180))
        for _ in range(num_posts)
    ],
    "updated_at": [
        datetime.now() - timedelta(days=random.randint(0, 30))
        for _ in range(num_posts)
    ]
})

# ----------------------------
# EXPORT TO CSV
# ----------------------------
posts.to_csv("posts.csv", index=False)

print("posts.csv created successfully!")
