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
    "The 19th edition, themed 'The Quantum Nexus', held from October 3rd to 5th, 2025. Highlights included a 24-hour national hackathon, a BikeExpo, and The Game of Innovations exhibition.",
    "Aarohan is divided into cultural, technical, management, fine arts, sports, and informal events. It includes activities like dance, coding, business competitions, arts, games, and fun shows.",
    "Campus placement drive with multiple recruiters.",
    "The primary mission of the fest is to provide a platform for social harmony and cultural diversity while empowering young minds to build leadership skills beyond academics.",
    "A 24-hour coding hackathon solving real-world problems."
]

event_types = [
    "Workshop",
    "Technical",
    "Seminar",
    "Sports",
    "Cultural",
    "Hackathon"
]

locations = ["Mumbai", "Pune", "Baner", "Bangalore", "Loni"]

# ONLY IMAGE NAMES (NO PATH)
event_images = [
    "tech_fest.jpg",
    "mindspark.jpg",
    "aarohan.jpg",
    "placement_drive.jpg",
    "persona.jpg",
    "hackathon.jpg"
]

# ----------------------------
# USER IDS (INTEGER)
# ----------------------------
user_ids = list(range(1, 1001))  # assuming 1000 users

# ----------------------------
# CREATE EVENTS DATAFRAME
# ----------------------------
events = pd.DataFrame({
    "event_id": range(1, num_events + 1),
    "user_id": np.random.choice(user_ids, num_events),
    "event_name": np.random.choice(event_names, num_events),
    "event_description": np.random.choice(event_descriptions, num_events),
    "event_type": np.random.choice(event_types, num_events),
    "location": np.random.choice(locations, num_events),
    "event_image": np.random.choice(event_images, num_events),
    "start_date": [
        datetime.now() + timedelta(days=random.randint(1, 60))
        for _ in range(num_events)
    ],
    "end_date": [
        datetime.now() + timedelta(days=random.randint(61, 90))
        for _ in range(num_events)
    ],
    "created_at": [
        datetime.now() - timedelta(days=random.randint(30, 365))
        for _ in range(num_events)
    ],
    "updated_at": [
        datetime.now() - timedelta(days=random.randint(0, 30))
        for _ in range(num_events)
    ]
})

# ----------------------------
# EXPORT TO CSV
# ----------------------------
events.to_csv("events.csv", index=False)

print("events.csv created successfully!")
