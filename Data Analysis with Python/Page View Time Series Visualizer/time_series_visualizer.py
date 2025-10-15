import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data (Make sure 'date' is parsed correctly and set as index)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data (Remove top and bottom 2.5%)
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Create a copy of the data
    df_plot = df.copy()

    # Plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_plot.index, df_plot['value'], color='red', linewidth=1)

    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save and return figure
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and prepare data
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group by year and month
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Plot
    fig = df_grouped.plot(kind='bar', figsize=(12, 8)).figure

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy().reset_index()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month

    # Sort months correctly
    df_box = df_box.sort_values('month_num')

    # Draw plots
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
