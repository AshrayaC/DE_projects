import pandas as pd

def grades_colors(students_df):
    # Filter the dataframe based on favorite color and grade conditions
  
    filtered_df = students_df[(students_df['favorite_color'].isin(['green', 'red'])) & (students_df['grade'] > 90)]
    return filtered_df

# Example usage
data = {
    'name': ['Tim Voss', 'Nicole Johnson', 'Elsa Williams', 'John James', 'Catherine Jones'],
    'age': [19, 20, 21, 20, 23],
    'favorite_color': ['red', 'yellow', 'green', 'blue', 'green'],
    'grade': [91, 95, 82, 75, 93]
}
students_df = pd.DataFrame(data)
print(students_df)
result = grades_colors(students_df)
print(result)
