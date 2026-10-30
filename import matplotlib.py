import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set style for plots
sns.set_theme(style="whitegrid")

# --- Import Dataset into Pandas DataFrame ---
# Replace 'CreditCard_Customers.csv' with your actual file path
df_cc = pd.read_csv("CreditCard_Customers.csv")

print("Initial Dataset Shape:", df_cc.shape)

# --- Remove Unnecessary Columns ---
columns_to_drop = [
    "CLIENTNUM",
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_1_month_cnt_Dependent_count_Education_Level_Months_on_book_Dependent_count_0",
]
existing_columns_to_drop = [col for col in columns_to_drop if col in df_cc.columns]
df_cc.drop(columns=existing_columns_to_drop, inplace=True)

# --- Handle Missing Values ---
print("\nMissing values per column:\n", df_cc.isnull().sum())

# Impute numerical columns with median, categorical columns with mode safely
for col in df_cc.select_dtypes(include=[np.number]).columns:
    df_cc[col] = df_cc[col].fillna(df_cc[col].median())

for col in df_cc.select_dtypes(include=["object", "category"]).columns:
    if not df_cc[col].mode().empty:
        df_cc[col] = df_cc[col].fillna(df_cc[col].mode()[0])

# --- Compute Descriptive Statistics ---
print("\n--- Descriptive Statistics (Numerical) ---")
print(df_cc.describe())

print("\n--- Descriptive Statistics (Categorical) ---")
print(df_cc.describe(include=["O"]))

# --- Plot Attrition Flag Ratio ---
plt.figure(figsize=(6, 4))
attrition_counts = df_cc["Attrition_Flag"].value_counts(normalize=True) * 100
ax = sns.barplot(
    x=attrition_counts.index,
    y=attrition_counts.values,
    hue=attrition_counts.index,
    palette="Set2",
    legend=False,
)
plt.title("Attrition Flag Ratio (%)")
plt.ylabel("Percentage")
plt.xlabel("Attrition Flag")
for p in ax.patches:
    ax.annotate(
        f"{p.get_height():.2f}%",
        (p.get_x() + p.get_width() / 2.0, p.get_height()),
        ha="center",
        va="center",
        xytext=(0, 5),
        textcoords="offset points",
    )
plt.show()

# --- Create Bar Charts and Box Plots ---
# 1. Bar Chart: Card Category Distribution
plt.figure(figsize=(8, 4))
sns.countplot(
    data=df_cc,
    x="Card_Category",
    hue="Card_Category",
    palette="viridis",
    order=df_cc["Card_Category"].value_counts().index,
    legend=False,
)
plt.title("Distribution of Card Categories")
plt.xlabel("Card Category")
plt.ylabel("Count")
plt.show()

# 2. Box Plot: Credit Limit by Attrition Flag
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df_cc,
    x="Attrition_Flag",
    y="Credit_Limit",
    hue="Attrition_Flag",
    palette="coolwarm",
    legend=False,
)
plt.title("Credit Limit Distribution by Attrition Flag")
plt.xlabel("Attrition Flag")
plt.ylabel("Credit Limit")
plt.show()

# --- Generate a Correlation Heatmap ---
plt.figure(figsize=(10, 8))
numerical_df = df_cc.select_dtypes(include=[np.number])
correlation_matrix = numerical_df.corr()
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    cbar=True,
)
plt.title("Correlation Heatmap of Numerical Features")
plt.show()