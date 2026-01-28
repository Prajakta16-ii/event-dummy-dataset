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
users = [
    "kunalll",
    "suyog",
    "praju123",
    "saurabh123",
    "admin01",
    "faculty01"
]

roles = ["ADMIN", "STUDENT", "FACULTY"]

college_ids = [101, 102, 103, 104]

content_types = ["IMAGE", "TEXT", "VIDEO"]

post_descriptions = [
    "Travel and enjoy the journey!",
    "Campus fest memories ❤️",
    "Workshop on AI & Data Science",
    "Placement drive updates",
    "Hackathon highlights",
    "Great learning experience at college"
]

media_files = [
    "mountain.jpg",
    "campus_event.jpg",
    "seminar.jpg",
    "hackathon.jpg",
    "placement.jpg",
    None  # for TEXT posts
]

# ----------------------------
# CREATE POSTS DATAFRAME
# ----------------------------
posts = pd.DataFrame({
    "post_id": range(1, num_posts + 1),
    "created_by": np.random.choice(users, num_posts),
    "role": np.random.choice(roles, num_posts),
    "college_id": np.random.choice(college_ids, num_posts),
    "post_date": [
        datetime.now() - timedelta(days=random.randint(0, 180))
        for _ in range(num_posts)
    ],
    "content_type": np.random.choice(content_types, num_posts),
    "post_description": np.random.choice(post_descriptions, num_posts),
    "media_name": np.random.choice(media_files, num_posts),
    "likes_count": np.random.randint(0, 500, num_posts),
    "comments_count": np.random.randint(0, 100, num_posts)
})

# ----------------------------
# EXPORT TO CSV
# ----------------------------
posts.to_csv("posts.csv", index=False)

print("posts.csv created successfully!")
