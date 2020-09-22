# sneakers_choose
Shoes classification with python - flask and Azure project

# Requirements 
python => flask \
html \
Subscription on azure 

# Steps to run the code and see the application on localhost

1 - command line at previous folder : python -m venv env \
2 - command line at previous folder : env\scripts\activate \
3 - command line at the starter folder : set FLASK_ENV=development \
4 - command line at the starter folder : flask run 

Make sure that you have :

	A - Creating a custom vision service.
		- Create a new resource group in portal.azure.com 
	B- Gathering the dataset and creating a classifier : Custom-vision-SDK.py
		- Creating a dataset : folder images
		- 1. Custom Vision API ENDPOINT in Azure portal in main ressource
		- 2. training_key in Azure portal in main ressource
		- 3. prediction_key in Azure portal in Prediction ressource
		- 4. prediction_resource_id in Azure portal in Prediction ressource - Properties
    
  And then  past the right keys in the app.py before running flask 
