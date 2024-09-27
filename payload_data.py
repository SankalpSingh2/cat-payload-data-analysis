import pandas as pd

data_path = "/Users/sanky/Work/cat-payload-data-analysis/R2R00116_20231031.csv"
df = pd.read_csv(data_path)

trucks = {
    '785': 492221,
    '789': 654594,
    '793': 824197
}

def check_violations(truck, FRP):
    threshold_110 = 1.10 * FRP
    threshold_120 = 1.20 * FRP

    print(f"\nTruck {truck} (FRP: {FRP} tons)")

    violates_120 = df[df['Payload_Wt'] > threshold_120]
    if not violates_120.empty:
        print("Violations of the 120% rule detected!")
    else:
        print("No violations of the 120% rule.")

    total_payloads = len(df)
    exceeds_110 = df[df['Payload_Wt'] > threshold_110]
    percentage_exceeds_110 = (len(exceeds_110) / total_payloads) * 100

    if percentage_exceeds_110 > 10:
        print(f"Violations of the 110% rule: {percentage_exceeds_110:.2f}% of payloads exceed 110% of FRP.")
    else:
        print(f"No violations of the 110% rule: {percentage_exceeds_110:.2f}% of payloads exceed 110% of FRP.")

    mean_payload = df['Payload_Wt'].mean()
    if mean_payload > FRP:
        print(f"Violation of the mean rule: Mean payload is {mean_payload:.2f} tons, exceeding FRP of {FRP} tons.")
    else:
        print(f"No violation of the mean rule: Mean payload is {mean_payload:.2f} tons.")

    print("\nSummary of violations:")
    if not violates_120.empty:
        print("Violations of the 120% rule detected.")
    if percentage_exceeds_110 > 10:
        print(f"{percentage_exceeds_110:.2f}% of payloads exceed 110% of FRP, violating the 10% rule.")
    if mean_payload > FRP:
        print(f"Mean payload exceeds FRP, violating the mean rule.")
    if violates_120.empty and percentage_exceeds_110 <= 10 and mean_payload <= FRP:
        print("No violations of the 10/10/20 policy.")

for truck, FRP in trucks.items():
    check_violations(truck, FRP)
