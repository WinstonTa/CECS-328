# Winston Ta and Mindy Yun

import csv
from collections import Counter

def actor_movie_counts(last_watched_file, actors_file):
    movies_to_actors = {}
    with open(actors_file, newline='', encoding="utf-8") as file:
        data = csv.DictReader(file)
        for row in data:
            movie = row["Movie"].strip()
            actor = row["Actor"].strip()
            if movie not in movies_to_actors:
                movies_to_actors[movie] = []
            movies_to_actors[movie].append(actor)
    
    actor_counts = Counter()
    with open(last_watched_file, newline='', encoding='utf-8') as file:
        data = csv.DictReader(file)
        for row in data:
            movie = row["Movie"].strip()
            if movie in movies_to_actors:
                for actor in movies_to_actors[movie]:
                    actor_counts[actor] += 1
    
    for actor, count in actor_counts.items():
        if count > 1:
            print(f"{actor}: {count}")
