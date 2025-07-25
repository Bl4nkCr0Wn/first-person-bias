import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
df = pd.read_csv('Qwen2.5-7B-Instruct_result.csv')

# --- Data Cleaning and Preparation ---

# Get the list of first-person and third-person score columns
first_person_scores = [f'first_score{i}' for i in range(1, 6)]
third_person_scores = [f'third_score{i}' for i in range(1, 6)]

# Convert score columns to numeric, coercing errors to NaN
for col in first_person_scores + third_person_scores:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculate the average sentiment score for first-person and third-person responses for each row
df['first_person_avg_score'] = df[first_person_scores].mean(axis=1)
df['third_person_avg_score'] = df[third_person_scores].mean(axis=1)

# --- Overall Sentiment Comparison ---

# Calculate the overall average sentiment scores
overall_avg_first_person = df['first_person_avg_score'].mean()
overall_avg_third_person = df['third_person_avg_score'].mean()

# --- Visualization 1: Overall Average Sentiment Comparison ---

plt.figure(figsize=(8, 6))
bars = plt.bar(['First-Person', 'Third-Person'], [overall_avg_first_person, overall_avg_third_person], color=['skyblue', 'salmon'])
plt.ylabel('Average Sentiment Score')
plt.title('Overall Average Sentiment Score: First-Person vs. Third-Person')
plt.ylim(0, 1)

# Adding the values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom', ha='center') # va: vertical alignment

plt.savefig('overall_sentiment_comparison.png')
plt.close()

# --- Sentiment Comparison by Occupation ---

# Group by occupation and calculate the average sentiment for each perspective
occupation_sentiment = df.groupby('occupation')[['first_person_avg_score', 'third_person_avg_score']].mean().reset_index()

# --- Visualization 2: Sentiment by Occupation ---

# Plotting the results
plt.figure(figsize=(12, 7))
bar_width = 0.35
index = np.arange(len(occupation_sentiment['occupation']))

plt.bar(index, occupation_sentiment['first_person_avg_score'], bar_width, label='First-Person', color='skyblue')
plt.bar(index + bar_width, occupation_sentiment['third_person_avg_score'], bar_width, label='Third-Person', color='salmon')

plt.xlabel('Occupation')
plt.ylabel('Average Sentiment Score')
plt.title('Average Sentiment Score by Occupation: First-Person vs. Third-Person')
plt.xticks(index + bar_width / 2, occupation_sentiment['occupation'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig('sentiment_by_occupation.png')
plt.close()

# --- Sentiment Comparison by Marital Status ---

# Group by marital status
marital_status_sentiment = df.groupby('marital_status')[['first_person_avg_score', 'third_person_avg_score']].mean().reset_index()

# --- Visualization 3: Sentiment by Marital Status ---

plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(marital_status_sentiment['marital_status']))

plt.bar(index, marital_status_sentiment['first_person_avg_score'], bar_width, label='First-Person', color='skyblue')
plt.bar(index + bar_width, marital_status_sentiment['third_person_avg_score'], bar_width, label='Third-Person', color='salmon')

plt.xlabel('Marital Status')
plt.ylabel('Average Sentiment Score')
plt.title('Average Sentiment Score by Marital Status: First-Person vs. Third-Person')
plt.xticks(index + bar_width / 2, marital_status_sentiment['marital_status'])
plt.legend()
plt.tight_layout()
plt.savefig('sentiment_by_marital_status.png')
plt.close()

# --- Sentiment Comparison by Country ---

# Group by country
country_sentiment = df.groupby('country')[['first_person_avg_score', 'third_person_avg_score']].mean().reset_index()

# --- Visualization 4: Sentiment by Country ---

plt.figure(figsize=(12, 7))
bar_width = 0.35
index = np.arange(len(country_sentiment['country']))

plt.bar(index, country_sentiment['first_person_avg_score'], bar_width, label='First-Person', color='skyblue')
plt.bar(index + bar_width, country_sentiment['third_person_avg_score'], bar_width, label='Third-Person', color='salmon')

plt.xlabel('Country')
plt.ylabel('Average Sentiment Score')
plt.title('Average Sentiment Score by Country: First-Person vs. Third-Person')
plt.xticks(index + bar_width / 2, country_sentiment['country'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig('sentiment_by_country.png')
plt.close()