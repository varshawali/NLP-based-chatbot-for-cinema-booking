import nltk
import random
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

lemmatizer = WordNetLemmatizer()

#Loading the dataset
qa_data = pd.read_csv("Book_da.csv")

kb_data = pd.read_csv("QADataset.csv")
questions = kb_data["Question"].tolist()
answers = kb_data["Answer"].tolist()
kb_dict = dict(zip(questions, answers))


#User Intents and the responses given by chatbot for small talk 
intents = {
    "greeting": ["hello", "hi", "hey", "howdy"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thank you", "thanks a lot", "thanks"],
    "job": ["What is your job", "What is your work", "what can you do"],
    "feeling": ["How are you today", "How are you"],
    "good": ["I am good too", "I feel fine", "Good!", "Fine", "I am good", "I am great", "great","good"],
    "bad":["Bad","Not good","Not well","Not fine","Not feeling well"],
}

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "job": ["I can help you book cinema tickets", "I can show you list of cinemas and you can book"],
    "feeling": ["I am feeling good, you?", "Very good and you?", "Actually, I'm okay and you?"],
    "good": ["That is perfect!"],
    "bad":["Oh no!feel better","Hope you feel better","Sorry to hear that"]
}

#Tokenizing and lemmatizing the user input 
def tokenize_and_lemmatize(text):
    tokens = nltk.word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

#Preprocess and vecotorize the user input
vectorizer = TfidfVectorizer(tokenizer=tokenize_and_lemmatize)
intent_examples = []
intent_labels = []
for label, examples in intents.items():
    intent_examples.extend(examples)
    intent_labels.extend([label] * len(examples))
intent_vectors = vectorizer.fit_transform(intent_examples)

#Cosine similarity based Intent matching to give best matching intent response
def get_intent(user_input):
    lemmatized_input = " ".join(tokenize_and_lemmatize(user_input))
    user_vector = vectorizer.transform([lemmatized_input])
    similarities = cosine_similarity(user_vector, intent_vectors)
    most_similar_intent_index = similarities.argmax()
    return intent_labels[most_similar_intent_index], similarities[0, most_similar_intent_index]

#Random choice for best matched Intent responses
def get_random_response(intent):
    intent_data = responses.get(intent, [])
    return random.choice(intent_data) if intent_data else None

#Preprocessing the cinema dataset
qa_data['Processed_Question'] = qa_data['Question'].apply(
    lambda x: ' '.join([word.lower() for word in word_tokenize(str(x)) if word.isalnum() and word not in stopwords.words('english')]))

#Tokenzing the user input
def preprocess(user_input):
    return ' '.join([word.lower() for word in word_tokenize(user_input) if word.isalnum() and word not in stopwords.words('english')])

#Calculating the similairty scores for user input and the dataset
def calculate_similarity(user_input, qa_data):
    vectorizer = TfidfVectorizer()
    processed_user_input = preprocess(user_input)
    corpus = qa_data['Processed_Question'].tolist() + [processed_user_input]
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    return similarity_scores[0]

a=0.0 #variable used to calculate the threshold
#Finding the best match of user input with cinema dataset
def get_best_match(user_input, qa_data):
    global a
    similarity_scores = calculate_similarity(user_input, qa_data)
    a=max(similarity_scores) 
    best_match_index = similarity_scores.argmax()
    return qa_data.loc[best_match_index, 'Answer']

#Function to list all the cinema playing
def cinema():
    print('Chatbot:KGF\nRRR\nHome Alone\nAvengers\nIron Man\nSpider Man\nGrinch\n')

book_id=0    
#Function to book the cinema tickets
def book():
    cinema = ["KGF", "RRR", "Home Alone", "Avengers", "Iron Man", "Spider Man", "Grinch\n"]
    print('Chatbot:Wohoo!Lets get started!')
    print('Chatbot:Here is a list of all the cinemas\n KGF\nRRR\nHome Alone\nAvengers\nIron Man\nSpider Man\nGrinch\n')
    cinema_name = input("Chatbot:Please give me a cinema name: ")
    if cinema_name not in cinema:
        print("Chatbot:Please select from cinemas available only!")
        book()
    print('Chatbot:That is a good choice')
    
    theatre = ["Cinemaworld", "Inox", "PVR", "Victoria Theatre"]
    print('Chatbot:Here is the list of theatres\n Cinemaworld \n Inox \n PVR \n Victoria Theatre\n')
    theatre_name = input("Chatbot:Enter the theatre name: ")
    if theatre_name not in theatre:
        print("Chatbot:Please select from theatres available only!")
        book()

    timings = ["12PM", "3PM", "9PM"]
    time = input("Chatbot:Choose a time from the below\n12PM\n3PM\n9PM:\n")
    if time not in timings:
        print("Chatbot:Please select from timing available only!")
        book()
    print('Chatbot:you are almost there!\n')
    
    date=int(input('Chatbot:Which date do you want to see the cinema?\n'))
    if 1<=date<=31:
        print(f'Chatbot:Alright {date} it is!\n')
    else:
        print('Chatbot:Please choose a date from 1 to 31')
    
    tickets = int(input("Chatbot:Please enter the number of tickets: "))
    booking_id = f"{random.randint(10000, 99999)}"
    global book_id
    book_id=booking_id
    print(f'Chatbot: cinema is: {cinema_name},and {tickets} Tickets at{time}')
    print(f"Chatbot:Booking successful! Your Booking ID is {booking_id}.")
    print(f'Chatbot:Enjoy the cinema {username}:)')

#Function to cancel the cinema tickets
def cancel_booking(book_id):
    ans=input('Have you booked tickets?(Y/N)')
    if ans.lower()=='y':
        cancelled_id = input('Chatbot:Please enter the booking id: ')
        if cancelled_id == book_id:
            print(f"Chatbot:Booking {book_id} has been canceled.")
        else:
            print(f"Chatbot:Booking ID  not found.")
    else:
        print('Please book the tickets first')        

#Function to list all the theatres 
def theatre():
    print('Chatbot:Here is the list of theatres\n Cinemaworld \n Inox \n PVR \n Victoria Theatre')

#Function to recommend cinema
def recommendation():
    list=["KGF", "RRR", "Home Alone", "Avengers", "Iron Man", "Spider Man", "Grinch"]
    recommend=random.choice(list)
    print(f'How about {recommend} cinema?')     

#Function to update the booking    
def update_booking():
    booking_id=int(input("Chatbot:Enter the booking ID"))
    new_cinema_name = input("Chatbot:Enter the new cinema name: ")
    new_theatre = input('Enter the theatre name')
    new_tickets = int(input("Chatbot:Enter the new number of tickets: "))
    new_time = input("Chatbot:Enter the new time (12PM, 3PM, 9PM): ")
    print(f'Chatbot:Here is your updated information! cinema is: {new_cinema_name}, Tickets: {new_tickets}, Time: {new_time}')
    

#Intializing the user input and retrieving the name
username = None
if username is None:
        username = input("Chatbot: Hello!Welcome to cinema booking! What's your name?\n(you can type exit to leave:/)")
        print(f"Chatbot: Nice to meet you, {username}!\n")
        print('Chatbot:You can type help to know what all you can do')

#Main while loop for the chatbot        
while True:
    user_input = input("User: ")
    #Case for if user asks for their name
    if user_input.lower() == 'what is my name?':
        print(f'Chatbot:your name is {username}')
        continue
    #Defining the keyword help to get user familiar with chatbot
    if user_input.lower() == 'help':
        print("Here is some of the things you can type\n 1.Can you show me the list of available cinemas?\n 2.I want to book cinema tickets\n 3. I want to cancel the tickets\n 4.I want to change my tickets\n 5.List of cinemas\n 6.Show me the list of theatres\n 7.Hi/Hello")
        continue

    #Case for if user wants to quit 
    if user_input.lower() == 'exit':
        print(f"Chatbot: Goodbye! Have a nice day {username}.")
        break
    if user_input in kb_dict:
        print(f"Chatbot: {kb_dict[user_input]}")
        continue
    #Setting the threshold and calling the function for the best matched     
    best_match_answer = get_best_match(user_input, qa_data)
    if a>0.7:
        if best_match_answer == 'cinema':
            cinema()
        if best_match_answer == 'Book': 
            book()
        if best_match_answer == 'Theatre':
            theatre()
        if best_match_answer == 'Cancel':
            cancel_booking(book_id)
        if best_match_answer == 'Update':   
            update_booking()
        if best_match_answer == 'recommend':
            recommendation()    
    #Case for error handling and outputting the closest matched Intent        
    elif 0.3>a>0.7:
        if best_match_answer == 'cinema':
            ans=input('Do you mean you want to list the cinema?(Y/N)')
            if ans=='Y': 
                cinema()
            else:
                print("Chatbot: I'm sorry, I didn't understand that.Could you please rephrase")
                
        if best_match_answer == 'Book':
            ans=input('Do you mean you want to book tickets?(Y/N)')
            if ans=='Y': 
                book()
            else:
                print("Chatbot: I'm sorry, I didn't understand that.Could you please rephrase")
            
        if best_match_answer == 'Theatre':
            ans=input('Do you mean you want to see the list of theatres?(Y/N)')
            if ans=='Y': 
                theatre()
            else:
                print("Chatbot: I'm sorry, I didn't understand that.Could you please rephrase")
                
        if best_match_answer == 'Cancel':
            ans=input('Do you mean you want to see the list of theatres?(Y/N)')
            if ans=='Y': 
                cancel_booking(book_id)
            else:
                print("Chatbot: I'm sorry, I didn't understand that.Could you please rephrase")
            
            
        if best_match_answer == 'Update':  
            ans=input('Do you mean you want to see the list of theatres?(Y/N)')
            if ans=='Y': 
                update_booking()
            else:
                print("Chatbot: I'm sorry, I didn't understand that.Could you please rephrase")
            
    else:  
            #Intent matching for small talk
            user_intent, score = get_intent(user_input)
            chatbot_response = get_random_response(user_intent)
            
            #Checking if the score is matches the threshold 
            if user_intent is None or score < 0.1:
                print("Chatbot: I'm sorry, I didn't understand that.Could you please rephrase")
            else:  
                print(f"Chatbot: {chatbot_response}")
    continue







