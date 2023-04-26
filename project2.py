import argparse
import json
import string
import numpy as np
import pandas as pd 
import re
import sys
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import KNeighborsClassifier


#converts list into a singe string
def  list_to_string(ingredients_list):
    STRING = ' '.join([str(elem) for elem in ingredients_list])
    STRING = STRING.lower()
    return STRING


#print in json format.
def print_json(predicted_cuisine,cuisine_score,closest_cuisines):
    closest = []
    if isinstance(closest_cuisines,list):
        for id,score in closest_cuisines:
            closest.append({'id':id, 'score': score })
    output = {
            'cuisine': predicted_cuisine,
            'score': cuisine_score,
            'closest': closest
        }
    print("\n")
    # prints the result to console in json format
    print(json.dumps(output,indent=4))


##cleans the data
def preprocess_data(ingredients_string):
    chars_to_be_removed = {'(', ')', u'\u2122', u'\u00AE', u'\u0025'}
    # Remove special characters
    for char in chars_to_be_removed:
        ingredients_string = ingredients_string.replace(char, '')
    # Remove digits
    ingredients_string= ''.join(filter(lambda c: not c.isdigit(),ingredients_string))
    # Remove extra whitespace
    ingredients_string = ' '.join(ingredients_string.split())
    # Remove any remaining punctuation
    ingredients_string = ingredients_string.translate(str.maketrans('', '', string.punctuation))
    #returns preprocessed data without any special characters
    return ingredients_string


def vectorize_data(clean_data, tdfVectorizer):
    ingredient_matrix = tdfVectorizer.fit_transform(list(clean_data['ingredients']))
    ingredient_array = ingredient_matrix.toarray()
    return ingredient_matrix, ingredient_array


def split_data(ingredient_array, cuisine_labels):
    X_train, _, y_train, _ = train_test_split(ingredient_array, cuisine_labels, train_size=0.8, test_size=0.2)
    return X_train, _, y_train, _


def train_model(X_train, y_train, n_neighbors):
    k_classifier = KNeighborsClassifier(n_neighbors=n_neighbors)
    k_classifier.fit(X_train, y_train)
    return k_classifier



def main(no_of_cuisine_requested,input_ingredients=[]):
    
    #reading the json file and adding into dataframe
    with open('docs/yummly.json', 'r') as f:
      file_contents = json.load(f)
    sample_data = pd.json_normalize(file_contents)
    #converting the "ingredients" from dataframe into a single list and then normalizing it 
    sample_data['ingredients'] = sample_data['ingredients'].map(lambda ingredients_list: preprocess_data(list_to_string(ingredients_list)))
    clean_data= sample_data.copy()
    #vectorizing the data 
    tdfVectorizer=TfidfVectorizer(ngram_range=(1,1))
    ingredient_matrix, ingredient_array = vectorize_data(clean_data, tdfVectorizer)
    
    X_train, _, y_train, _ = split_data(ingredient_array, clean_data['cuisine'])
    
    k_classifier = train_model(X_train, y_train, args.N)
    new_data=preprocess_data(list_to_string(input_ingredients))
   
    input_ingredients_matrix=tdfVectorizer.transform([new_data])
    input_ingredients_array=input_ingredients_matrix.toarray()        
  
    predict_cuisine=k_classifier.predict(input_ingredients_array)[0]
    probability=k_classifier.predict_proba(input_ingredients_array)
    score=max(probability[0])


    #calculating the similarityu score
    similarity_score = np.max(cosine_similarity(ingredient_array, input_ingredients_array), axis=1)
    sample_data['Similarity'] = similarity_score
     
     #getting the top n cuisines
    closest_cuisines = [(row['id'], row['Similarity']) for _, row in sample_data.sort_values('Similarity', ascending=False).head(args.N).iterrows()]
    print_json(predict_cuisine,score,closest_cuisines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--N",
        type=int,
)

    parser.add_argument(
        "--ingredient",
        action="append",
        type=str,
        required=True,
)
    args = parser.parse_args()
    main(no_of_cuisine_requested=int(args.N), input_ingredients=args.ingredient)
   
