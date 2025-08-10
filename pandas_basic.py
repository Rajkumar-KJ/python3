import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, None, 28],
    'Score': [85, 90, 88, 92, None],
    'City': ['NY', 'LA', 'NY', 'SF', 'LA']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")


print("Head:\n", df.head(), "\n")
print("Shape:", df.shape)
print("Columns:", df.columns, "\n")


print("Age column:\n", df['Age'], "\n")
print("First 2 rows:\n", df.iloc[:2], "\n")
print("Name & Score:\n", df.loc[:, ['Name', 'Score']], "\n")


print("People from LA:\n", df[df['City'] == 'LA'], "\n")


df['Age'].fillna(df['Age'].mean(), inplace=True)
df.dropna(subset=['Score'], inplace=True)
print("After filling Age & dropping missing Score:\n", df, "\n")


df['Pass'] = df['Score'] >= 90
print("With Pass column:\n", df, "\n")


grouped = df.groupby('City')['Score'].mean()
print("Average Score by City:\n", grouped, "\n")


sorted_df = df.sort_values(by='Score', ascending=False)
print("Sorted by Score:\n", sorted_df, "\n")


df.rename(columns={'Score': 'ExamScore'}, inplace=True)
df.reset_index(drop=True, inplace=True)
print("Renamed & reset index:\n", df, "\n")


df.to_csv('output.csv', index=False)
print("DataFrame saved to output.csv")
