import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

# --- 1. Response Length Analysis ---

# Calculate the length of each response and then the average length
for i in range(1, 6):
    df[f'first_q{i}_len'] = df[f'first_q{i}'].str.len()
    df[f'third_q{i}_len'] = df[f'third_q{i}'].str.len()

first_person_len_cols = [f'first_q{i}_len' for i in range(1, 6)]
third_person_len_cols = [f'third_q{i}_len' for i in range(1, 6)]

df['first_person_avg_len'] = df[first_person_len_cols].mean(axis=1)
df['third_person_avg_len'] = df[third_person_len_cols].mean(axis=1)

# Overall average length
overall_avg_len_first = df['first_person_avg_len'].mean()
overall_avg_len_third = df['third_person_avg_len'].mean()

# Visualization 1a: Overall Average Response Length
plt.figure(figsize=(8, 6))
bars = plt.bar(['First-Person', 'Third-Person'], [overall_avg_len_first, overall_avg_len_third], color=['#87CEEB', '#F08080'])
plt.ylabel('Average Response Length (characters)')
plt.title('Overall Average Response Length: First-Person vs. Third-Person')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.0f}', va='bottom', ha='center')
plt.savefig('average_response_length.png')
plt.close()

# Group by occupation for length analysis
occupation_len = df.groupby('occupation')[['first_person_avg_len', 'third_person_avg_len']].mean().reset_index()

# Visualization 1b: Average Response Length by Occupation
plt.figure(figsize=(12, 7))
bar_width = 0.35
index = np.arange(len(occupation_len['occupation']))
plt.bar(index, occupation_len['first_person_avg_len'], bar_width, label='First-Person', color='#87CEEB')
plt.bar(index + bar_width, occupation_len['third_person_avg_len'], bar_width, label='Third-Person', color='#F08080')
plt.xlabel('Occupation')
plt.ylabel('Average Response Length (characters)')
plt.title('Average Response Length by Occupation')
plt.xticks(index + bar_width / 2, occupation_len['occupation'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig('response_length_by_occupation.png')
plt.close()

# --- 2. Age vs. Sentiment Correlation ---

# Visualization 2: Scatter plot for Age vs. Sentiment
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='age', y='first_person_avg_score', scatter_kws={'alpha':0.6}, label='First-Person', color='#87CEEB')
sns.regplot(data=df, x='age', y='third_person_avg_score', scatter_kws={'alpha':0.6}, label='Third-Person', color='#F08080')
plt.title('Age vs. Sentiment Score with Trend Line')
plt.xlabel('Age')
plt.ylabel('Average Sentiment Score')
plt.legend()
plt.grid(True)
plt.savefig('age_vs_sentiment.png')
plt.close()

# --- 3. Sentiment Score Distribution ---

# Visualization 3: Histograms of Sentiment Scores
plt.figure(figsize=(10, 6))
sns.histplot(df['first_person_avg_score'], color="#87CEEB", label='First-Person', kde=True, stat="density", linewidth=0)
sns.histplot(df['third_person_avg_score'], color="#F08080", label='Third-Person', kde=True, stat="density", linewidth=0)
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Average Sentiment Score')
plt.ylabel('Density')
plt.legend()
plt.savefig('sentiment_distribution.png')
plt.close()

# --- 4. Response Length vs. Sentiment Score ---

# Visualization 4: Scatter plot for Response Length vs. Sentiment Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='first_person_avg_len', y='first_person_avg_score', label='First-Person', color='#87CEEB')
sns.scatterplot(data=df, x='third_person_avg_len', y='third_person_avg_score', label='Third-Person', color='#F08080')
plt.title('Response Length vs. Sentiment Score')
plt.xlabel('Average Response Length (characters)')
plt.ylabel('Average Sentiment Score')
plt.legend()
plt.grid(True)
plt.savefig('length_vs_sentiment.png')
plt.close()

# --- 5. Sentiment Score by Occupation ---

# Visualization 5a: Boxplot for First-Person Sentiment Score by Occupation
plt.figure(figsize=(14, 7))
sns.boxplot(data=df, x='occupation', y='first_person_avg_score', color='#87CEEB')
plt.title('First-Person Sentiment Score by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Average Sentiment Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('boxplot_sentiment_by_occupation_first.png')
plt.close()

# Visualization 5b: Boxplot for Third-Person Sentiment Score by Occupation
plt.figure(figsize=(14, 7))
sns.boxplot(data=df, x='occupation', y='third_person_avg_score', color='#F08080')
plt.title('Third-Person Sentiment Score by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Average Sentiment Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('boxplot_sentiment_by_occupation_third.png')
plt.close()

# --- 6. Sentiment Score by Sex (Male vs. Female) ---

# Group by sex for average sentiment
sex_sentiment = df.groupby('sex')[['first_person_avg_score', 'third_person_avg_score']].mean().reset_index()

plt.figure(figsize=(8, 6))
bar_width = 0.35
index = np.arange(len(sex_sentiment['sex']))
plt.bar(index, sex_sentiment['first_person_avg_score'], bar_width, label='First-Person', color='#87CEEB')
plt.bar(index + bar_width, sex_sentiment['third_person_avg_score'], bar_width, label='Third-Person', color='#F08080')
plt.xlabel('Sex')
plt.ylabel('Average Sentiment Score')
plt.title('Average Sentiment Score by Sex')
plt.xticks(index + bar_width / 2, sex_sentiment['sex'])
plt.legend()
plt.tight_layout()
plt.savefig('sentiment_by_sex.png')
plt.close()

# Optional: Boxplots for more detailed distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='sex', y='first_person_avg_score', color='#87CEEB')
plt.title('First-Person Sentiment Score by Sex')
plt.xlabel('Sex')
plt.ylabel('Average Sentiment Score')
plt.tight_layout()
plt.savefig('boxplot_sentiment_by_sex_first.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='sex', y='third_person_avg_score', color='#F08080')
plt.title('Third-Person Sentiment Score by Sex')
plt.xlabel('Sex')
plt.ylabel('Average Sentiment Score')
plt.tight_layout()
plt.savefig('boxplot_sentiment_by_sex_third.png')
plt.close()