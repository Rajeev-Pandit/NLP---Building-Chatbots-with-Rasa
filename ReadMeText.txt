Details of the Rasa Chatbot study:
Please install all the dependent libraries used in this project from requirements.txt, this text file is available in this folder.
For this project creation rasa and different librariers were installed on 'demo' environment on my computer.

These are the few important steps followed in this study.

1) NLU.md file creation -

Supervised embeddings type of pipeline has been used for NLU model creation.
These are the policies used:
- name: MemoizationPolicy
- name: KerasPolicy
- name: MappingPolicy


Here all the required intents and entities required for this 'Foodie' chatbot were included.

Following intents were created:
- restaurant_search
- greet
- affirm
- place_price_search
- email
- deny
- thanks
- goodbye
- stop

Following entities were created:
- cuisine
- emailid
- facility_type
- location
- money

List of all the tier-1 & tier-2 cities were included in the intent 'place_price_search'. 
In this NLU file different synonyms were included for the different intents wherever it was required. 
Regex commands were also used for few intents to make it more generic.
After creation of this file, 'rasa train nlu' command was used to train the model. Then with command 'rasa shell nlu', accuracy of the different
intents and entities were tested. Accuracy was found for most of the cases more than 90%.
For detail, please refer the nlu.md file shared.


2) domain.yml file creation -

Here all the actions, intents, entities, responses and slots have been included.
Please refer the domain.yml file for detail.
These are the 4 different actions used in this study -
- action_check_cuisine
- action_check_location
- action_search_restaurants
- action_send_email

Python code for these actions have been written in the action.py file inside this main folder 'Rasa_NLP_Project'.
user key created from Zomato api site has been mentioned in the action.py file.
For checking tier -1 & 2 cities from the given list and also for checking cuisine, python codes have been mentioned under the classes
'ActionCheckLocation' & 'ActionCheckCuisine' in the action.py file.
For sending email, email and password has been mentioned in the class action 'ActionSendEmail' under action.py file.
Used 'rasa run actions' command to run all the actions on the server.

3) stories.md file creation -
rasa interactive I had run to create diffetent stories, from this I got schema of the main stories. Once having the main stories, 
I added many other stories for different scenarios which will cover the real requirements when a person interact with chatbot.

For dialogue flow management between NLU and Core mainly two files domain.yml and stories.md file are important, along with others.

This dialogue flow management between NLU, domain.yml and stories.md is taken care by the command 'rasa train core'. 
Finally, with command 'rasa shell' a user can interact with this chatbot.

After 1st time successful creation of this chatbot, and henceforth for any addition/modification of the story, single command 'rasa train' 
can be used to train the NLU and Core together. 

