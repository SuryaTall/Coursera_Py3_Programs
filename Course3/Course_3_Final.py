#Now, you’ll put it all together.
# Don’t forget to copy all of the functions that you have previously 
#defined into this code window. Define a function get_sorted_recommendations.
# It takes a list of movie titles as an input. It returns a sorted list of related 
#movie titles as output, up to five related movies for each input movie title. 
#The movies should be sorted in descending order by their Rotten Tomatoes rating, as
# returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that 
#‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

#THIS IS THE FINAL PROJECT PUT ALL TOGETHER, IGNORE THE IMPORT ERRORS, THIS PROGRAM WORKS IN THE RUNESTONE ENVIRONMENT

import requests_with_caching
import json

def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(dic):
    list_ = []
    for i in dic['Similar']['Results']:
        list_.append(i['Name'])
    return(list_)

def get_related_titles(titles_list):
    list_ = []
    for i in titles_list:
        new_list = extract_movie_titles(get_movies_from_tastedive(i))
        for i in new_list:
            if i not in list_:
                list_.append(i)
    print(list_)
    return list_

def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

def get_movie_rating(data):
    rating = 0
    for i in data['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            rating = int(i['Value'][:-1])
            #print(rating)
    return rating 

def get_sorted_recommendations(list_):
    new_list = get_related_titles(list_)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]
