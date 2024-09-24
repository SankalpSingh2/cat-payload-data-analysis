import pandas as pd

data_path = "/Users/sanky/Work/cat-payload-data-analysis/R2R00116_20231031.csv"

df = pd.read_csv(data_path)

print("Columns in the dataset:", df.columns)

if 'segment_id' in df.columns:

    result = df.groupby('segment_id').agg(
        max_load=('Payload_Wt', 'max'),
        min_load=('Payload_Wt', 'min'),
        avg_load=('Payload_Wt', 'mean')
    ).reset_index()

    print(result)
else:
    print("'segment_id' column not found in the dataset.")
