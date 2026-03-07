
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# -------------------------------
# Visualization 1: Line Plot
# Content Growth Over Time
# -------------------------------

year_counts = df['release_year'].value_counts().sort_index()

fig, ax = plt.subplots()

ax.plot(year_counts.index, year_counts.values, marker='o')

ax.set_title("Growth of Netflix Content Over Time")
ax.set_xlabel("Release Year")
ax.set_ylabel("Number of Titles")

plt.tight_layout()
plt.savefig("netflix_content_growth.png")
plt.show()


# -------------------------------
# Visualization 2: Horizontal Bar Chart
# Top Countries Producing Content
# -------------------------------

country_counts = (
    df['country']
    .dropna()
    .str.split(',')
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots()

ax.barh(country_counts.index, country_counts.values)

ax.set_title("Top 10 Countries Producing Netflix Content")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Country")

plt.tight_layout()
plt.savefig("top_countries_netflix.png")
plt.show()


# -------------------------------
# Visualization 3: Sorted Bar Plot
# Most Common Genres
# -------------------------------

genre_counts = (
    df['listed_in']
    .str.split(',')
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots()

ax.bar(genre_counts.index, genre_counts.values)

ax.set_title("Top 10 Netflix Genres")
ax.set_xlabel("Genre")
ax.set_ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("top_genres_netflix.png")
plt.show()
