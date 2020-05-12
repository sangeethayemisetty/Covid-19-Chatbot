## Despcription :

Covid-19 bot is a chatbot that  is used to answer any qiries related to covid19 pandemic situation. It gives the local and aslo national statistcis of covid cases, symptoms and preventive measures.
 
## Functional architecture 



## Functionalities :

-  The bot is trained using intents and contexts that were created using google dialog flow 

-  The answers for all the cutomer questions are fetched form WHO published live doc by creating knoeledge base in google dialog flow

-  For the local info of covid cases, it fetches the info related to the given zipcode loaclity using the api http://covid19india.p.rapidapi.com/getStateData and mails it to the users mail id.

-  Mailing functionality is implemented using SMTPLIB in python

-  It also uploads the covid related statistics to AWS, such that on serch of global view it gives the following view(Right now this is paid version because of AWS storage fee, for sample I have used my training AWS account)

<img src="https://github.com/sangeethayemisetty/Covid-19-Chatbot/blob/master/ChatbotGlobalview.PNG" alt="alt text" width="1000"/>

-  The connectivity between the fetching of data and mailing it ti user is implementd by using #Flask

-  The deployment of application is done using Heroku 

-  Data is stored using Mongo DB

-  It is Integrated using webbhook with telegram and Facebook messenger

## How to use :
 
 Download telegram messenger app and search for "Covid-19 care", then start asking questions 
 
 
