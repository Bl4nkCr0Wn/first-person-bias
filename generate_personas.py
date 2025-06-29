import csv
import itertools
import random

PATH = 'personas.csv'
sexes = ['male', 'female']
age_ranges = [(18, 30), (31, 55), (56, 80)]  
occupations = ['engineer', 'teacher', 'doctor', 'artist', 'chef']
countries = ['USA', 'Brazil', 'Indonesia', 'Germany', 'France', 'Iran', 'Israel', 'Japan', 'China', 'India']
marital_status = ['single', 'married', 'divorced', 'widowed']

# Generate all combinations (using range index for age)
combinations = itertools.product(sexes, range(len(age_ranges)), occupations, countries, marital_status)

def generate_persona():
    for sex, age_idx, occupation, country, status in combinations:
            age = random.randint(age_ranges[age_idx][0], age_ranges[age_idx][1])
            yield [sex, age, occupation, country, status]

def main():
    # Write to CSV
    with open(PATH, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['sex', 'age', 'occupation', 'country', 'marital_status'])  # header
        for persona in generate_persona():
            writer.writerow(persona)

if __name__ == '__main__':
    main()
