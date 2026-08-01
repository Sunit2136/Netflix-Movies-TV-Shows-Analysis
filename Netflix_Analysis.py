import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Netflix Movies & TV Shows Analysis
# ==========================================

# Load Dataset
df = pd.read_csv("netflix_titles.csv")
# Data Cleaning

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# Convert date column
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

# Create Year Added column
df["year_added"] = df["date_added"].dt.year

# Dataset Overview

print("=" * 50)
print("NETFLIX DATASET OVERVIEW")
print("=" * 50)

print("\nFirst 5 Rows")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# 1. Movies vs TV Shows

type_counts = df["type"].value_counts()

print("\nMovies vs TV Shows")
print(type_counts)

plt.figure(figsize=(6, 4))
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.show()

# 2. Content Added Per Year

yearly = df["year_added"].value_counts().sort_index()

print("\nContent Added Per Year")
print(yearly)

plt.figure(figsize=(10, 5))
plt.plot(yearly.index, yearly.values, marker="o")
plt.title("Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()

# 3. Top 10 Countries

top_countries = (
    df["country"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

print("\nTop 10 Countries")
print(top_countries)

plt.figure(figsize=(10, 5))
top_countries.plot(kind="bar")
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()

# 4. Top 10 Genres

top_genres = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

print("\nTop 10 Genres")
print(top_genres)

plt.figure(figsize=(10, 5))
top_genres.plot(kind="bar")
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()

# 5. Ratings Distribution

ratings = df["rating"].value_counts()

print("\nRatings Distribution")
print(ratings)

plt.figure(figsize=(10, 5))
ratings.plot(kind="bar")
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 6. Top 10 Longest Movies

movies = df[
    (df["type"] == "Movie") &
    (df["duration"].str.contains("min", na=False))
].copy()

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"].str.replace(" min", "", regex=False),
    errors="coerce"
)

movies.dropna(subset=["duration_minutes"], inplace=True)

longest_movies = (
    movies.sort_values(
        by="duration_minutes",
        ascending=False
    )
    .head(10)
)

print("\nTop 10 Longest Movies")
print(longest_movies[["title", "duration_minutes"]])

plt.figure(figsize=(10, 6))
plt.barh(
    longest_movies["title"],
    longest_movies["duration_minutes"]
)
plt.gca().invert_yaxis()
plt.title("Top 10 Longest Movies")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Movie")
plt.show()

# 7. Top 10 Directors

top_directors = (
    df["director"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_directors = (
    top_directors[top_directors != "Unknown"]
    .value_counts()
    .head(10)
)

print("\nTop 10 Directors")
print(top_directors)

plt.figure(figsize=(10, 5))
top_directors.plot(kind="bar")
plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()

# Save Cleaned Dataset

df.to_csv("netflix_cleaned.csv", index=False)

print("\nCleaned dataset saved as 'netflix_cleaned.csv'")
print("\nProject Completed Successfully!")