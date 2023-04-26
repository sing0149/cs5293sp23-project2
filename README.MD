### cs5293sp23-project2

## Name: Sagar Singh

## Requirements
argparse
json
string
numpy
pandas
re
sys
pickle
sklearn


## Installations
 If the above requirements are not already installed, they can be installed using pip or conda
This code requires the following libraries:

!pip install pandas
!pip install scikit-learn
!pip install numpy

## Running the project
1. Clone the repository to local machine , ro download the file in ZIP format and extract it.

2. The project can be run from the command line using the following command:
pipenv run python project2.py --N 5 --ingredient paprika   --ingredient banana 
3. This will give the output in desired formar
                               

## Assumptions made before writing the code
1. The input ingredients are given as a list of strings.
2. The input ingredients do not contain any special characters like (, ), ™, ®, % etc.
3. The input ingredients are in English.
4. The training data (Yummly dataset) is in a JSON file format and it contains two keys - "cuisine" and "ingredients".
5. The JSON file contains a list of dictionaries, where each dictionary represents a recipe and contains cuisine and ingredients information.
6. The cuisine labels in the training data are not already encoded and need to be encoded for training the model.
7. The data preprocessing involves removing special characters, digits, extra whitespace, and punctuation from the input text.
8. The vectorization of input text is done using the TfidfVectorizer with unigrams only (ngram_range=(1,1)).
9. The KNeighborsClassifier is used to train the model, and the number of neighbors (n_neighbors) is given as an input parameter.
10. The input data is split into 80% training data and 20% testing data for training the model.

## functions used
1. list_to_string(ingredients_list) - This function takes a list of ingredients as input and returns a single string by joining all the elements in the list. It converts the string to lowercase before returning it.
 Parameters:
   ingredients_list: A list of ingredients.
Returns:
  A single string that contains all the ingredients joined together.

2. print_json(predicted_cuisine, cuisine_score, closest_cuisines) - This function takes the predicted cuisine, cuisine score, and a list of closest cuisines as input and prints the output in JSON format.
 Parameters:
  predicted_cuisine: A string that represents the predicted cuisine.
  cuisine_score: A float that represents the probability of the predicted cuisine.
  closest_cuisines: A list of tuples where each tuple contains the ID and similarity score of a cuisine.
 Returns:
  None. It prints the output in JSON format.

3. preprocess_data(ingredients_string) - This function preprocesses the input text by removing special characters, digits, extra whitespace, and punctuation.
 Parameters:
 ingredients_string: A string that represents the input text.
 Returns:
  A string that represents the preprocessed input text.

4. vectorize_data(clean_data, tdfVectorizer) - This function vectorizes the input data using TfidfVectorizer.
  Parameters:
   clean_data: A pandas dataframe that contains the preprocessed input data.
   tdfVectorizer: A TfidfVectorizer object that is used to vectorize the data.
  Returns:
   ingredient_matrix: A sparse matrix that represents the vectorized input data.
   ingredient_array: A numpy array that contains the vectorized input data.
   
5. split_data(ingredient_array, cuisine_labels) - This function splits the input data into training and testing data.
 Parameters:
  ingredient_array: A numpy array that contains the vectorized input data.
  cuisine_labels: A pandas series that contains the cuisine labels.
  Returns:
   X_train: A numpy array that contains the training data.
   X_test: A numpy array that contains the testing data.
  y_train: A pandas series that contains the cuisine labels of the training data.
  y_test: A pandas series that contains the cuisine labels of the testing data.

6. train_model(X_train, y_train, n_neighbors) - This function trains the KNeighborsClassifier model.
 Parameters:
  X_train: A numpy array that contains the training data. 
  y_train: A pandas series that contains the test data.

## Test Functions

1. test_list_to_string: This function tests the list_to_string function in project2.py, which takes in a list of strings and returns a single string with all words in lowercase and separated by a space. The test function provides different input lists and expected output strings to ensure the function is working correctly.

2. test_preprocess_data: This function tests the preprocess_data function in project2.py, which takes in a string and returns a new string with all non-alphanumeric characters removed and all words in lowercase. The test function provides a sample input string and the expected output string to ensure the function is working correctly.

3. test_print_Json: This class tests the print_json function in project2.py, which takes in a predicted cuisine, a cuisine score, and a list of tuples with the closest cuisines and their scores, and prints the information in JSON format. The test function creates a mock stdout and checks that the printed JSON output matches the expected output.

4. test_split_data: This function tests the split_data function in project2.py, which takes in a numpy array of ingredient data and a numpy array of cuisine labels, splits the data into training and testing sets, and returns the split data. The test function provides sample input data and checks that the returned training and testing arrays have the correct shapes and split ratios.

5. test_train_model: This function tests the train_model function in project2.py, which takes in training data and target labels, trains a K-Nearest Neighbors classifier, and returns the trained classifier. The test function provides sample input data and checks that the returned classifier is an instance of KNeighborsClassifier and has been trained on the correct data.

6. test_vectorize_data: This function tests the vectorize_data function in project2.py, which takes in a dictionary of ingredient data and a TfidfVectorizer instance, vectorizes the ingredient data, and returns the vectorized matrix and array. The test function provides sample input data and checks that the returned matrix has the correct shape and that it is sparse.


## Bugs and Assumption

As the code stands, there are no known bugs. However, there are several potential areas where errors could occur, such as:

If the 'yummly.json' file is not present or not properly formatted, the code will fail to read the data correctly.
If the input ingredients provided by the user are not in the correct format or contain errors, the code may produce unexpected results.
If the preprocessing steps taken to clean the data are not sufficient for the particular dataset being used, the model may produce less accurate predictions.
The KNeighborsClassifier algorithm used for training the model may not be the most suitable algorithm for this particular problem, and may produce less accurate predictions than other algorithms


## Workflow

The code is a Python script that takes input ingredients and predicts the cuisine type that corresponds to the input ingredients. It uses the K-Nearest Neighbors (KNN) algorithm to predict the cuisine type based on the similarity between the input ingredients and the ingredients in a pre-existing dataset of recipes. The code uses the following workflow:

Importing the necessary libraries such as argparse, json, numpy, pandas, re, sys, and scikit-learn modules such as MultinomialNB, TfidfVectorizer, cosine_similarity, and KNeighborsClassifier.

Defining the following functions:

list_to_string(): This function takes a list of ingredients as input and returns a single string that concatenates all the ingredients in the list. The function also converts the string to lowercase characters.
print_json(): This function takes three inputs, i.e., the predicted cuisine, the score of the predicted cuisine, and the closest cuisines. The function converts the inputs into a JSON format and prints the result to the console.
preprocess_data(): This function takes an input string of ingredients and preprocesses it by removing special characters, digits, extra whitespace, and punctuation from the string. The function returns the preprocessed ingredients string.
vectorize_data(): This function takes two inputs, i.e., a preprocessed data and a TfidfVectorizer object, and returns an ingredient matrix and an ingredient array.
split_data(): This function takes two inputs, i.e., an ingredient array and cuisine labels and splits the data into training and testing datasets.
train_model(): This function takes two inputs, i.e., the training dataset and the number of neighbors for KNN, and returns a trained KNeighborsClassifier object.
The main function takes two inputs, i.e., the number of cuisine requested (N) and a list of input ingredients. It reads a JSON file of recipes and adds the contents into a dataframe. The function preprocesses the ingredients of each recipe and vectorizes the data using the TfidfVectorizer. The function then splits the data into training and testing datasets and trains a KNN classifier using the training data. The input ingredients are preprocessed and vectorized using the TfidfVectorizer, and the KNN classifier predicts the cuisine type based on the similarity between the input ingredients and the recipes in the training data. The function returns the predicted cuisine, the score of the predicted cuisine, and the closest cuisines to the input ingredients. Finally, the function uses the print_json() function to print the results in JSON format.

The script uses the argparse module to parse the command-line arguments. The script takes two arguments, i.e., the number of cuisine requested (N) and the list of input ingredients.

In summary, the script preprocesses the recipe data and input ingredients, vectorizes the data, and trains a KNN classifier to predict the cuisine type based on the similarity between the input ingredients and the recipes in the training data. The script then returns the predicted cuisine, the score of the predicted cuisine, and the closest cuisines to the input ingredients in JSON format.

## How to run# cs5293sp23-project2

![Untitled design](https://user-images.githubusercontent.com/124123388/234463660-a8d00628-892f-4c06-9603-5c9efe253e80.gif)

