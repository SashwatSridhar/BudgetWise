#libraries
import pandas as pd
from sklearn.model_selection import train_test_split #used for training and testing the model
from sklearn.feature_extraction.text import CountVectorizer #used to convert text to numerical data
from sklearn.naive_bayes import MultinomialNB #best option for word counts and frequencies the alternatives are used for other things
from sklearn.metrics import accuracy_score #to check the accuracy


# Read the CSV file
csvFile = pd.read_csv('budget_dataset.csv', header=0, names=['combined']) #reads the data and says the header is the row at index 0 and they are combined

# Skip the first row if it's just a header
if csvFile.iloc[0, 0] == "description,category":
    csvFile = csvFile.iloc[1:].reset_index(drop=True) #starts from index 1 of the dataset so it doesnt count the header

# Split the combined column
csvFile[['description', 'category']] = csvFile['combined'].str.split(',', expand=True) 



#put the data into features and target
X = csvFile['description'] #features
y = csvFile['category'] #target

#train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 30) #random state just makes the split of the data the same 

#process the text data into numerical form so the model can understand
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train) #learns the new vocab and converts into numerical form
#fit learns the new vocab and transform, changes from text into a vector where each position is a word in the vocab, the value at each position is the count of that word
X_test_vectors = vectorizer.transform(X_test) #converts the test into numerical form

#add the naives bayes 
nb_classifier = MultinomialNB() #initialize M_nb
nb_classifier.fit(X_train_vectors, y_train) #train the model using vectorized training data
y_pred = nb_classifier.predict(X_test_vectors) #make predictions using testing data

accuracy = accuracy_score(y_test, y_pred)  #Evaluate the model's performance
print(f"Accuracy: {accuracy:.2f}")

print("predictions vs the actual category")
results = pd.DataFrame({ #dataframe with the description, the actual and predicted categories
    'Description': X_test.values,
    'Actual Category': y_test.values,
    'Predicted Categories': y_pred
})

results = results.reset_index(drop=True) #resets index
results['Correct'] = results['Actual Category'] == results['Predicted Categories'] #makes a new column in dataframe called correct and puts in the correct predictions from the dataset
results = results.drop_duplicates().reset_index(drop=True)
display_count = min(10, len(results)) #outputs the first 10 results
print(results.head(display_count)) #prints the rows of display count

print("\nCategory-wise performance:")
for category in results['Actual Category'].unique(): #loop through the categories in the actual category in the dataframe
    category_results = results[results['Actual Category'] == category] #creates a filtered dataframe 
    correct = category_results['Correct'].sum() #sum the correct results in the filtered dataframe
    total = len(category_results) #total in the results 
    print(f"{category}: {correct}/{total} correct ({correct/total:.2%})") # print statement 


def predict_description(description): #used when someone enters another description in the dataset
    description_vector = vectorizer.transform([description]) #transform into vector
    prediction = nb_classifier.predict(description_vector) #predict using description
    return prediction[0] #returns the prediction with just the prediction and nothing else printed



