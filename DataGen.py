from faker import Faker
import pandas as pd
import numpy as np
import random

fObj = Faker()


input_df = pd.read_csv('masked_data.csv')
print(input_df.user_id.nunique())
print(input_df.Title.nunique())
print(input_df.Genre.nunique())

# 1. Initially, generated random data for all 641 users - 
#   a. For each user, pick a random number of movies, randomly from the list of movies  
#   b. Assign a random rating and interest values for each movie picked. (rating 1-5, interest 0-1)
#   c. Map the movie title to the language and genre and write to csv

# 2. Pick a list of random users
#    a. For each random user from the list, follow the above steps
#    b. Vary the below 3 params to get different size of data for each user, different interactions of each user across movies etc.

user_list_size = 300
random_seed = 414
max_data_size = 3000

user_list = input_df.user_id.unique()
user_list = np.random.choice(user_list, size=user_list_size)
title_list = input_df.Title.unique()
genre_list = input_df.Genre.unique()
language_list = input_df.language.unique()


# Get title -> Language mapping
#def get_title_language_mapping():
    
# Get title -> Genre mapping



random.seed(random_seed)
final_df = pd.DataFrame(columns= ['user_id', 'title', 'rating', 'interest'])

total_size = 0
print(final_df.shape)
# 1. For each unique user, get permutation combination of various movies
for user in user_list:
    temp_df = pd.DataFrame(columns= ['user_id', 'title', 'rating', 'interest'])
    data_size = random.randint(1,max_data_size)
    total_size += data_size
    print('Generated ', str(data_size), ' new data points for user - ', str(user))
    #for i in range(1, data_size):
    temp_df.title = np.random.choice(title_list, size=data_size)
    temp_df.rating = list(np.random.randint(low=1, high=5,size=data_size))
    temp_df.interest = list(np.random.rand(data_size))
    temp_df.user_id = np.random.choice([user], size=data_size)
    
    final_df = pd.concat([temp_df, final_df], ignore_index=True, axis=0)
print('Total rows generated - ', str(total_size))
final_df.to_csv('generated_data-8.csv')
        
    
        
# Insert random null values to rating, title, interest (<20% of total size)
# Randomize title watch counts
# Users with no watch counts and movies with no watch counts
# Generate 10M data
# Generate new userId - total ~100,000
# New movies - total ~20000-50000 (scrape from imdb)
# Movie upload time column. Same for a particular movie.
# New data sources after 10M records 
