# demographic_data_analyzer.py
import pandas as pd

def calculate_demographic_data(df):
    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. What percentage of people with advanced education make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = df[higher_education & (df['salary'] == '>50K')]
    percentage_higher_education_rich = round((len(higher_education_rich) / len(df[higher_education])) * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = ~higher_education
    lower_education_rich = df[lower_education & (df['salary'] == '>50K')]
    percentage_lower_education_rich = round((len(lower_education_rich) / len(df[lower_education])) * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round((len(rich_min_workers) / len(min_workers)) * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = round((rich_country_counts / country_counts * 100).max(), 1)
    highest_earning_country = (rich_country_counts / country_counts * 100).idxmax()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_education_rich': percentage_higher_education_rich,
        'percentage_lower_education_rich': percentage_lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
