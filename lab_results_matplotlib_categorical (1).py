import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("Lab Results.csv")

print("Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
<<<<<<< HEAD
# Plot 1: Grouped bar-style plot (Top 10 combinations)
=======
# Plot 1: Top 10 Combinations of Column 1 & 2
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048
# -----------------------------
col_a = df.columns[0]
col_b = df.columns[1]

group_counts = (
    df.groupby([col_a, col_b])
      .size()
      .reset_index(name="count")
      .sort_values("count", ascending=False)
      .head(10)
)

fig1, ax1 = plt.subplots()
ax1.bar(range(len(group_counts)), group_counts["count"])

ax1.set_xticks(range(len(group_counts)))
ax1.set_xticklabels(
    group_counts[col_a].astype(str) + " | " + group_counts[col_b].astype(str),
    rotation=45,
    ha="right"
)

ax1.set_xlabel(f"{col_a} + {col_b}")
ax1.set_ylabel("Count")
<<<<<<< HEAD
ax1.set_title("Top 10 Lab Record Combinations")
=======
ax1.set_title("Top 10 Lab Record Combinations")

>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048
plt.tight_layout()
<<<<<<< HEAD
=======
fig1.savefig("grouped_bar_plot.png")
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048

# -----------------------------
<<<<<<< HEAD
# Plot 2: Horizontal bar chart
=======
# Plot 2: Horizontal Bar Chart (Top 10 Column 3 Values)
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048
# -----------------------------
col2 = df.columns[2]
counts2 = df[col2].value_counts().head(10)

fig2, ax2 = plt.subplots()
<<<<<<< HEAD
ax2.barh(counts2.index.astype(str), counts2.values)

ax2.set_xlabel("Count")
ax2.set_ylabel(col2)
ax2.set_title(f"Top 10 {col2} Values (Horizontal)")
=======
ax2.barh(counts2.index.astype(str), counts2.values)

ax2.set_xlabel("Count")
ax2.set_ylabel(col2)
ax2.set_title(f"Top 10 {col2} Values (Horizontal)")

>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048
plt.tight_layout()
<<<<<<< HEAD
=======
fig2.savefig("horizontal_bar_plot.png")
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048

# -----------------------------
<<<<<<< HEAD
# Plot 3: Scatter plot using record index
=======
# Plot 3: Scatter Plot (Column 4 Distribution)
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048
# -----------------------------
<<<<<<< HEAD
col3 = df.columns[3] if len(df.columns) > 3 else df.columns[0]
=======
if len(df.columns) > 3:
    col3 = df.columns[3]
else:
    col3 = df.columns[0]
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048

counts3 = df[col3].value_counts().reset_index()
counts3.columns = [col3, "count"]

fig3, ax3 = plt.subplots()
ax3.scatter(range(len(counts3)), counts3["count"])

ax3.set_xlabel("Category Index")
ax3.set_ylabel("Count")
<<<<<<< HEAD
ax3.set_title(f"Distribution of {col3} Values (Scatter)")
=======
ax3.set_title(f"Distribution of {col3} Values (Scatter)")

>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048
plt.tight_layout()
<<<<<<< HEAD
=======
fig3.savefig("scatter_plot.png")
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048

<<<<<<< HEAD
# Show all plots
=======
# -----------------------------
# Show All Plots
# -----------------------------
>>>>>>> 12d46eedc81387a25ebffd6ee51098a351ee6048
plt.show()

print("Plots saved successfully:")
print(" - grouped_bar_plot.png")
print(" - horizontal_bar_plot.png")
print(" - scatter_plot.png")
