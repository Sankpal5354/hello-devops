
import pandas as pd
from sklearn.datasets import load_iris
from evidently import Report
from evidently.presets import DataDriftPreset

# Load sample data
iris = load_iris(as_frame=True)
data = iris.frame

# Split into reference and current datasets
reference_data = data.iloc[:75].copy()
current_data = data.iloc[75:].copy()

# Generate a data drift report
report = Report([DataDriftPreset()])
result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save the report as HTML
result.save_html("evidently_report.html")

print("Evidently monitoring completed successfully!")
print("Report saved as evidently_report.html")
