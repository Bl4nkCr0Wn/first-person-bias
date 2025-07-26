import pandas as pd
import numpy as np
from scipy.stats import fisher_exact

def main():
    df = pd.read_csv("Mistral-7B-Instruct-v0.3_result_cleaned.csv")
    # return
    # print("regular")
    regular = (run_for_df(df))
    df_male = df[df["sex"] == "male"]
    # print("male")
    male = run_for_df(df_male)
    df_female = df[df["sex"] == "female"]
    female = run_for_df(df_female)

    results = {}
    results ["all"] = regular
    results["male"] = male
    results["female"] = female

    for occupation in df["occupation"].unique():
        df_oc = df[df["occupation"] == occupation]
        results[occupation] = run_for_df(df_oc)
    results["q_num"] = []
    for i in range(len(regular)):
        
        results["q_num"].append(f"q_{i+9}")

    # print(pd.DataFrame(results))
    pd.DataFrame(results).to_csv("bool_results_mistral.csv")

    for i in range(6,9):
        curr_df = df[[f"first_q{i}",f"third_q{i}"]]
        print(f"q_{i}",perm_test_numeric(curr_df,i))

def perm_test_numeric(df, i, n_perm=20_000, seed=123):
    rng         = np.random.default_rng(seed)
    num_first   = df[ f'first_q{i}'].astype(str).str.extract(r'(^\d*\.?\d+)')[0].astype(float)
    num_third   = df[ f'third_q{i}'].astype(str).str.extract(r'(^\d*\.?\d+)')[0].astype(float)
    obs_diff    = num_first.mean() - num_third.mean()

    combined    = np.concatenate([num_first, num_third])
    labels      = np.r_[np.zeros(len(num_first)), np.ones(len(num_third))]
    more_extreme = 0
    for _ in range(n_perm):
        rng.shuffle(labels)
        diff = combined[labels == 0].mean() - combined[labels == 1].mean()
        if abs(diff) >= abs(obs_diff):
            more_extreme += 1
    p_value = more_extreme / n_perm
    return {'mean_first': num_first.mean(),
            'mean_third': num_third.mean(),
            'mean_diff':  obs_diff,
            'p_value':   p_value}

def run_for_df(df):
    res = []
    for i in range(9,19):
        first = df[f"first_q{i}"].str.upper().str.startswith("YES")
        third = df[f"third_q{i}"].str.upper().str.startswith("YES")
        first_counts = first.value_counts()
        third_counts = third.value_counts()

        first_true = 0
        first_false = 0
        third_true = 0
        third_false =0

        if True in first_counts:
            first_true = first_counts[True]
        if False in first_counts:
            first_false = first_counts[False]

        if True in third_counts:
            third_true = third_counts[True]
        if False in third_counts:
            third_false = third_counts[False]
        odds_ratio, p_value = fisher_exact([[first_true,third_true],[first_false,third_false]])
        res.append(p_value)
    return(res)
main()
# df = pd.read_csv("./Qwen_cleaned.csv")
# print(df.columns)


def create_overleaf_table():
    pd.set_option('display.max_columns', None)

    df = pd.read_csv('bool_results_mistral.csv')
    df = df.drop('Unnamed: 0', axis=1)
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]

    df = (df[cols])
    for _, row in df.iterrows():
        formatted = []
        for x in row:
            if pd.isna(x):
                formatted.append("")  # blank for NaN
            elif isinstance(x, (int, float)) and not isinstance(x, bool):
                formatted.append(f"{x:.2E}")  # scientific notation with 2 decimals
            else:
                formatted.append(str(x).replace("_"," "))
        print(" & ".join(formatted))

create_overleaf_table()
