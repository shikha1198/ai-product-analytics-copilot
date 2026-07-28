from app.analytics.metrics import calculate_cohort_retention

retention = calculate_cohort_retention()

print(retention.head())