# TISB_Hackathon_GeneticsLab
 Our healthcare project (Name: Rachvik, Krish, Gautam, Pranad)


All other files that are not mentioned in number 2 and 3 should be saved in one folder



Homepage (TISBhackathon.html):
Homepage has various navigation buttons and information about our project and information related to our project. Launch the file and feel free to click any of the navigation buttons. [ The AI models page does not work because the models are only able to run in a development server, hence it can’t be used for production deployment. However the instructions to run the AI models are given

.
Mind Games: These games are designed to help children with various mental disorders enhance their comprehension skills and their memory skills with the memory game and the riddle game
	-just click any of the buttons to be redirected to one of the games



3) Drug AI:
Description: Supervised ML Model that is coded using python. The model is trained through a CSV file called  ‘genetic_data (1).csv’. It asks the user to input the genetic condition in an HTML webpage called ‘input.html’ and the predictions are outputted in an HTML file called ‘predictions.html’. 
How to run code:
1) Save all these files in a folder called ‘Drug_AI’
- ‘genetic_data (1).csv’
- ‘input.html’
-  ‘predictions.html’
-  ‘string_encoder.joblib’
-  ‘drug.pyt’
(make sure you save all file names as they are specified please)
2) Save the following folder in a folder called ‘templates’ in the same ‘Drug_AI’
-  ‘input.html’
-  ‘predictions.html’
3) Go to Terminal/Command Prompt:
- type: cd ‘path to Drug_AI folder’
-after that, type: python drug.pyt
- Now you’ll get a link, copy and paste this link into your browser and see the functionality of it.


4) Genetic Condition AI
Description: Supervised ML Model that is coded using python. The model is trained through a CSV file called  ‘genet.csv’. It asks the user to input the genetic condition in an HTML webpage called ‘IN.html’ and the predictions are outputted in an HTML file called ‘result.html’. 
How to run code:
1) Save all these files in a folder called ‘Gene_AI’
- ‘genet.csv’
- ‘IN.html’
-  ‘results.html’
-  ‘string_encoder.joblib’
-  ‘gene.pyt’
(make sure you save all file names as they are specified please)
2) Save the following folder in a folder called ‘templates’ in the same ‘Gene_AI’
-  ‘IN.html’
-  ‘result.html’
3) Go to Terminal/Command Prompt:
- type: cd ‘path to Gene_AI folder’
-after that, type: python gene.pyt
- Now you’ll get a link, copy and paste this link into your browser and see the functionality of it.


5) Global health statistics webpage:
Shows a few statistics related to genetic disorders on a global scale through a webpage made using HTML.
Contains a map that has different countries and their most prevalent genetic disease and its prevalence as well. 
Also gives the symptoms, treatment and outcomes, drug for treatment, and clinical trial data related to that particular genetic disease.
How to run it: 
After clicking on global health analytics on the homepage, you can explore the webpage.
Read through the webpage and look through ‘get involved’
Use the map- By clicking on a particular region, it will reveal a pop up about the most prevalent genetic disease in that region. 





     Medical Submission Form 

 6) This form is created for users to input their personal details and medical history. This page was created using HTML and JavaScript.

To run the code, you must click get started from the home page, and the web page for the form is displayed. 

First the user must type the first name and last name. Then must enter the date of birth. After that type, the medical problems of the patient, then there are Yes/No questions for the doctor to understand the problems in depth regarding the patient. 

If the User does not complete each field, there will be a prompt to the user stating that the user needs to fill in the essential details.

Through online forms, it becomes a benefit to the hospital, for keeping the records of the patient’s medical history throughout his/her life.

At the end, there is a submit button, and when the user completes the form, the form is downloaded as a pdf and outputs thank you and sends a copy of the patient’s information to the doctor.
