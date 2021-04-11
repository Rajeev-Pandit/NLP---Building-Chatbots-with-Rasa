# NLP---Building-Chatbots-with-Rasa

Please install all the dependent libraries used in this project from 'requirements.txt', this text file is available in this folder.
A short description of this Rasa Chatbot study is provided in file 'ReadMeText'.

Problem statement:
Here the main objective is to build a conversational bot (chatbot) which can help users quickly discover restaurants across several Indian cities, also at the end to provide a good restaurant discovery experience.
Mainly three things have been accomplished in this project - NLU training, Build actions for the bot (Zomato API used here), creating more stories.

One of the formats of the chat with user, this chatbot provides is as following:

User: Hi
Bot: Hi there! How may I help you?
User: Can you suggest some good restaurants in Bangalore
Bot: What kind of cuisine would you like to have?
1. Chinese
2. Mexican
3. Italian
4. American
5. Thai
6. North Indian
User: american
Bot: What's the average budget for two people?
1. Lesser than Rs. 300
2. Rs. 300 to 700
3. More than 700
User: <300
Bot: Showing you top rated restaurants:
1. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
2. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
3. .
4. .
5. .
Bot: Should I send you details of all the restaurants on email?
User: yes. Please
Bot: To what email id should I send it to?
User: jddk.2jmd@kdl.co.in
Bot: Sent. Bon Appetit!
