# %% import pandas and read the csv file 
# modify the path if needed
import pandas as pd

df = pd.read_csv("DATA475_lab_rectangles_data.csv") ##. represents current folder, .. represents parent folder
# df["area"] = ?
df["area"] = df['width'] * df['length']
df

# %%
summary = [
    ("Total Count", df["area"].shape[0]),
    ("Total Area", df["area"].sum()),
    ("Average Area", df["area"].mean()),
    ("Maximum Area", df["area"].max()),
    ("Minimum Area", df["area"].min()),
]

for key, value in summary:
    print(f"{key}: {str(value)}")

# %%
pd.DataFrame(dict(summary), index=['2022']).to_csv("summary.csv", index=False)

# %%
