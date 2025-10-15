import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.7)

    # First line of best fit (1880 - most recent)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = range(1880, 2051)
    y_pred = [intercept + slope * x for x in x_pred]
    plt.plot(x_pred, y_pred, 'r', label="Best Fit (1880-present)")

    # Second line of best fit (2000 - most recent)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred_recent = range(2000, 2051)
    y_pred_recent = [intercept2 + slope2 * x for x in x_pred_recent]
    plt.plot(x_pred_recent, y_pred_recent, 'g', label="Best Fit (2000-present)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save and return the plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
