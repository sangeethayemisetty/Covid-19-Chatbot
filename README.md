# COVID-19-CHATBOT


## DESCRIPTION :

Covid-19 bot is a chatbot that is used to answer any queries related to Covid-19 pandemic situation. It gives the local and also national statistics of covid cases, symptoms and preventive measures etc...

## TECHNOLOGIES USED:

Google dialog flow, Flask, AWS, Heroku, Mongo DB, REST API, Webhooks

## HOW TO USE:
 
Download telegram messenger app and search for "Covid-19 care"(@Covidcare_bot), then start interacting using keywords like covid symptoms, covid cases, covid-19 etc..
 
## FUNCTIONAL ARCHITECTURE 

![Image description](https://github.com/sangeethayemisetty/Covid-19-Chatbot/blob/master/FunctionalArchiticture.PNG)


## SEQUENCE DIAGRAM 

![Image description](https://github.com/sangeethayemisetty/Covid-19-Chatbot/blob/master/SequenceDiagram1.PNG)

## FUNCTIONALITIES :

-  The bot is trained using intents and contexts that were created using google dialog flow 

-  The response for all the cutomer requests are fetched from WHO published live document by creating knowledge base in        google dialog flow

-  For the local information of covid cases, it fetches the info related to the given zipcode locality using the api            http://covid19india.p.rapidapi.com/getStateData and mails it to the users mail id.

-  Mailing functionality is implemented using SMTPLIB in python

-  It also uploads the covid related statistics to AWS, such that on search of global view it gives the following view(Right    now this is paid version because of AWS storage fee, for sample I have used my training AWS account)

![Image description](https://github.com/sangeethayemisetty/Covid-19-Chatbot/blob/master/ChatbotGlobalview.PNG)

-  The connectivity between the fetching of data and mailing it to user is implementd by using #Flask

-  The deployment of application is done using #Heroku 

-  Data is stored using #MongoDB

-  It is Integrated using webbhook with telegram and Facebook messenger


 
 ## Output Images
 
 ![Email Output](https://github.com/sangeethayemisetty/Covid-19-Chatbot/blob/master/CahatbotEmail.PNG)
 
 ![Messenger Output](https://github.com/sangeethayemisetty/Covid-19-Chatbot/blob/master/MessengerOutput2.PNG)

 
 
