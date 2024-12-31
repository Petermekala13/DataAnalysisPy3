import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(
        kind="bar", figsize=(10, 6), legend=True, xlabel="Years", ylabel="Average Page Views"
    ).figure
    plt.legend(
        title="Months",
        labels=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
    )
    plt.title("Average daily page views for each month grouped by year")

    # Save image and return fig
    fig.savefig("bar_plot.png")
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.strftime("%b")
    df_box["month_num"] = df_box.index.month
    df_box = df_box.sort_values("month_num")

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)

    sns.boxplot(
        x="year", y="value", data=df_box, ax=axes[0]
    ).set(
        title="Year-wise Box Plot (Trend)",
        xlabel="Year",
        ylabel="Page Views"
    )

    sns.boxplot(
        x="month", y="value", data=df_box, ax=axes[1]
    ).set(
        title="Month-wise Box Plot (Seasonality)",
        xlabel="Month",
        ylabel="Page Views"
    )

    # Save image and return fig
    fig.savefig("box_plot.png")
    return fig
