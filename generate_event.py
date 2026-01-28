import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ----------------------------
# NUMBER OF EVENTS
# ----------------------------
num_events = 5000

# ----------------------------
# MASTER DATA
# ----------------------------
event_names = [
    "Tech Fest 2025",
    "MindSpark",
    "Aarohan",
    "Campus Placement Drive",
    "Persona Fest",
    "Hack-o-heist 2025"
]

event_descriptions = [
    "A large-scale technical festival with workshops and competitions.",
    "The 19th edition, themed The Quantum Nexus, was held from October 3rd to 5th, 2025. Highlights included a 24-hour national hackathon, a BikeExpo, and The Game of Innovations exhibition.",
    "Aarohan is divided into cultural, technical, management, fine arts, sports, and informal events.",
    "Campus placement drive with multiple recruiters.",
    "The primary mission of the fest is to provide a platform for social harmony and cultural diversity while empowering young minds to build leadership skills beyond academics.",
    "A 24-hour coding hackathon solving real-world problems."
]

event_types = [
    "Workshop",
    "Technical",
    "Seminar",
    "sports",
    "cultural",
    "Hackathon"  
]

locations = ["Mumbai", "Pune", "Baner", "Bangalore", "Loni"]

created_by_users = ["praju123", "saurabh123", "admin01", "faculty01", "prajwal123"]

# ONLY IMAGE NAMES (NO PATH)
event_images = [
    "tech_fest.jpg",
    "mindspark.jpg",
    "Aarohan.jpg",
    "placement_drive.jpg",
    "persona.jpg",
    "hackathon.jpg"
]

# ----------------------------
# CREATE EVENTS DATAFRAME
# ----------------------------
events = pd.DataFrame({
    "event_id": range(1, num_events + 1),
    "event_name": np.random.choice(event_names, num_events),
    "event_description": np.random.choice(event_descriptions, num_events),
    "event_type": np.random.choice(event_types, num_events),
    "location": np.random.choice(locations, num_events),
    "created_by": np.random.choice(created_by_users, num_events),
    "event_image": np.random.choice(event_images, num_events),
    "start_date": [
        datetime.now() + timedelta(days=random.randint(1, 60))
        for _ in range(num_events)
    ],
    "end_date": [
        datetime.now() + timedelta(days=random.randint(61, 90))
        for _ in range(num_events)
    ]
})

# ----------------------------
# EXPORT TO CSV
# ----------------------------
events.to_csv("events.csv", index=False)

print("events.csv created successfully!")
