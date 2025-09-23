import random
import string

# Function to generate random names
def random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Movies
movies = [f"Movie_{i}" for i in range(1, 11)]  # 10 movies

# --- Generate actors_gen with 50 actors ---
actors_output = "actors_gen_50.csv"
with open(actors_output, "w") as f:
    f.write("Actor,Movie\n")
    for i in range(50):
        actor_name = f"{random_name()} {random_name()}"
        movie = random.choice(movies)
        f.write(f"{actor_name},{movie}\n")

print(f"✅ Created {actors_output}")

# --- Generate last_watched_gen with 10,000,000 rows ---
last_watched_output = "last_watched_gen_10m.csv"
batch_size = 100_000
total_rows = 10_000_000

with open(last_watched_output, "w") as f:
    f.write("UserID,First Name,Last Name,Movie\n")
    
    user_id = 1
    while user_id <= total_rows:
        batch_end = min(user_id + batch_size, total_rows + 1)
        rows = []
        for i in range(user_id, batch_end):
            first = random_name()
            last = random_name()
            movie = random.choice(movies)
            rows.append(f"{i},{first},{last},{movie}\n")
        f.writelines(rows)
        user_id = batch_end
        print(f"Written {batch_end-1:,} rows...")

print(f"✅ Created {last_watched_output} with {total_rows:,} rows")
