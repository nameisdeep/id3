# Generating a meaningful classification dataset with 3 numerical columns
import pandas as pd
import numpy as np
np.random.seed(42)

# Define sample size
sample_size = 100

# Columns: Age, Salary, and PurchaseDecision (0: No, 1: Yes)
# Assumption: Higher age and salary might increase the likelihood of making a purchase.

# Generate data
ages = np.random.randint(18, 65, sample_size)  # Ages between 18 and 65
salaries = np.random.randint(30000, 100000, sample_size)  # Salaries between 30,000 and 100,000
purchase_decisions = np.array([(1 if (age > 40 and salary > 50000) else 0) for age, salary in zip(ages, salaries)])

# Create DataFrame
df_classification = pd.DataFrame({
    'Age': ages,
    'Salary': salaries,
    'PurchaseDecision': purchase_decisions
})

# Save the DataFrame to a CSV file
classification_csv_path = 'classification_sample_data.csv'
df_classification.to_csv(classification_csv_path, index=False)

classification_csv_path
