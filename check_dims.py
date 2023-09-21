import pandas as pd


df1 = pd.read_csv('generated_data-1.csv')
df2 = pd.read_csv('generated_data-2.csv')
df3 = pd.read_csv('generated_data-3.csv')
df4 = pd.read_csv('generated_data-4.csv')
df5 = pd.read_csv('generated_data-5.csv')
df6 = pd.read_csv('generated_data-6.csv')
df7 = pd.read_csv('generated_data-7.csv')
df8 = pd.read_csv('generated_data-8.csv')
df8 = pd.read_csv('generated_data-8.csv')
df9 = pd.read_csv('generated_data-8.csv')

a = np.rand()

df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])
print(df.shape)

print(df.user_id.nunique())
user_titles = df.groupby('user_id').agg({'title':'nunique', 'rating':'mean'})
#user_titles.to_csv('user_titles_distribution.csv')

title_ratings = df.groupby('title').agg({'user_id':'nunique', 'rating':'mean'})
#title_ratings.to_csv('movie_rating_distribution.csv')


df.to_csv('final_merger_data.csv')


