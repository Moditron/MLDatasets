import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from scipy import stats

# Create a DataFrame
df = pd.read_csv('Dataset.csv')

print(f"Raw input:\n{df}")

# Imputation
imputer = SimpleImputer(strategy='mean')
df[['mks1', 'mks2', 'mks3']] = imputer.fit_transform(df[['mks1', 'mks2', 'mks3']])




# Anomaly detection
z = stats.zscore(df[['mks1', 'mks2', 'mks3']])
threshold = 3
outlier = (abs(z) > threshold).any(axis=1)

df['is_outlier'] = outlier

# Standardization
scale = StandardScaler()
df[['mks1', 'mks2', 'mks3']] = scale.fit_transform(df[['mks1', 'mks2', 'mks3']])

# Normalization
scale = MinMaxScaler()
df[['mks1', 'mks2', 'mks3']] = scale.fit_transform(df[['mks1', 'mks2', 'mks3']])

print(f'Final preprocessed:\n{df}')


#without using sklearn libraries


import pandas as pd

# Create a DataFrame
df = pd.read_csv('Dataset.csv')



# Imputation (Replace NaN with mean)
df[['mks1', 'mks2', 'mks3']] = df[['mks1', 'mks2', 'mks3']].fillna(df[['mks1', 'mks2', 'mks3']].mean())

# Anomaly detection (using Z-Score)
def detect_outliers_zscore(data, threshold=3):
    z_scores = (data - data.mean()) / data.std()
    is_outlier = (abs(z_scores) > threshold).any(axis=1)
    return is_outlier

outlier = detect_outliers_zscore(df[['mks1', 'mks2', 'mks3']])
df['is_outlier'] = outlier

# Standardization (z-score)
def standardize(data):
    return (data - data.mean()) / data.std()

df[['mks1', 'mks2', 'mks3']] = standardize(df[['mks1', 'mks2', 'mks3']])

# Normalization (min-max scaling)
def normalize(data):
    return (data - data.min()) / (data.max() - data.min())

df[['mks1', 'mks2', 'mks3']] = normalize(df[['mks1', 'mks2', 'mks3']])

print(f'Final preprocessed without using libraries:\n{df}')
