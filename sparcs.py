import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Change exponents into decminals
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Load csv data
df = pd.read_csv('./sparcs_2022.csv')

# Remove white spaces, lowercase, replace spaces with underscores, replace parentheses with empty string, and replace hyphens with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-','_' )

# Convert columns to numeric columns
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')

# Check for missing values
df['total_charges'].isna().sum()
df['total_costs'].isna().sum()
df['length_of_stay'].isna().sum()

# Using specific columns
columns_to_use = ['age_group', 'gender', 'length_of_stay', 'type_of_admission', 
                  'total_charges', 'total_costs']
df_columns = df[columns_to_use]

# Drop missing values
df.dropna(inplace=True)

# Data type cleaning and conversion
df['total_charges'] = df['total_charges'].astype(str).str.replace(',', '').astype(float)
df['total_costs'] = df['total_costs'].astype(str).str.replace(',', '').astype(float)

#  Drop missing values for specific columns
df.dropna(subset=['length_of_stay', 'total_charges', 'total_costs'], inplace=True)

# Descriptive statistics for length_of_stay
print("Descriptive statistics for Length of Stay:")
print("Mean:", df['length_of_stay'].mean())
print("Median:", df['length_of_stay'].median())
print("Standard Deviation:", df['length_of_stay'].std())
print("Min:", df['length_of_stay'].min())
print("Max:", df['length_of_stay'].max())
print("25th Percentile:", df['length_of_stay'].quantile(0.25))
print("50th Percentile (Median):", df['length_of_stay'].quantile(0.50))
print("75th Percentile:", df['length_of_stay'].quantile(0.75))

# Descriptive statistics for total_charges
print("\nDescriptive statistics for Total Charges:")
print("Mean:", df['total_charges'].mean())
print("Median:", df['total_charges'].median())
print("Standard Deviation:", df['total_charges'].std())
print("Min:", df['total_charges'].min())
print("Max:", df['total_charges'].max())
print("25th Percentile:", df['total_charges'].quantile(0.25))
print("50th Percentile (Median):", df['total_charges'].quantile(0.50))
print("75th Percentile:", df['total_charges'].quantile(0.75))

# Descriptive statistics for total_costs
print("\nDescriptive statistics for Total Costs:")
print("Mean:", df['total_costs'].mean())
print("Median:", df['total_costs'].median())
print("Standard Deviation:", df['total_costs'].std())
print("Min:", df['total_costs'].min())
print("Max:", df['total_costs'].max())
print("25th Percentile:", df['total_costs'].quantile(0.25))
print("50th Percentile (Median):", df['total_costs'].quantile(0.50))
print("75th Percentile:", df['total_costs'].quantile(0.75))

# Group by age and mean costs
age_group_costs = df.groupby('age_group')['total_costs'].mean()
print("Average Total Costs by Age Group:")
print(age_group_costs)


# Display distribution of Age Group
print("Distribution of Age Group:")
age_group_distribution = df['age_group'].value_counts()
print(age_group_distribution)

# Bar plot for Age Group
plt.figure(figsize=(8, 6))
sns.barplot(x=age_group_distribution.index, y=age_group_distribution.values, palette="crest")
plt.title('Distribution of Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Display the distribution of Gender
print("Distribution of Gender:")
gender_distribution = df['gender'].value_counts()
print(gender_distribution)

# Bar plot of Gender
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_distribution.index, y=gender_distribution.values, palette="plasma")
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Display the distribution of Type of Admission
print("Distribution of Type of Admission:")
admission_type_distribution = df['type_of_admission'].value_counts()
print(admission_type_distribution)

#Bar plot for Type of Admission
plt.figure(figsize=(8, 6))
sns.barplot(x=admission_type_distribution.index, y=admission_type_distribution.values, palette="Set2")
plt.title('Distribution of Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.show()

# Histogram of Length of Stay
plt.figure(figsize=(10, 6))
sns.histplot(df['length_of_stay'], bins=20, kde=False, color='blue')
plt.title('Histogram of Length of Stay')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Frequency')
plt.show()

# Boxplot of Total Charges
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['total_charges'], color='red')
plt.title('Boxplot of Total Charges')
plt.xlabel('Total Charges ($)')
plt.show()

# Bar plot for Type of Admission
plt.figure(figsize=(8, 6))  
sns.barplot(x=type_of_admission_counts.index, y=type_of_admission_counts.values, palette="rocket")
plt.title("Distribution of Type of Admission")
plt.xlabel("Type of Admission")
plt.ylabel("Count")
plt.xticks(rotation=45)  
plt.show()

