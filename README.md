# House Information Django App

To start this application make sure you have Python3.7.4 installed as well as a pip installer on your system.

# Steps for first time deploy:
## Setting us system Requirements:
In the folder where requirements.txt is located (should be the root directory in this case): run
```
pip install -r requirements.txt
```
## Steps for setting up the ingestion portion of the application:
1. To ingest the csv file, `cd` into the 'houseApp' folder. If you run `ls` you should see a file called manage.py, if its not there check to confirm that you are in the 'houseApp' folder. 
2. Run the command to create an sqlite3 database (which will be used for the deployment of this application). To use another database you will need to update 'settings.py'
```
touch db.sqlite3
```
3. Run migrations on this database to create the table folders.
```
python manage.py migrate
```

# Running CSV file ingestion:
I had put the csv file into a csvfiles folder located in the root directory. To run the application run the following command below from the 'houseApp'.

```
python manage.py ingestCSV --file './csvfiles/backend_project_data.csv'
```
The csv file can be moved to other locations or another csv file can be used, just make sure to update file route + file name in the run command above.

# Running the API endpoint:
## Run the API Server
To run the API endpoints. You will need to run the django API server. To do so run the command below from the 'houseApp' folder:
```
python manage.py runserver
```
## To access the endpoint from browser
To access the endpoint from the browser you can directly go to:
[localhost:8000/api/house/](http://localhost:8000/api/house/) on your local machine
Utilize the browser to view more information on the endpoint itself.

## using an external applications
To access the endpoint from another machine, set you application to point to this url:
[localhost:8000/api/house/](http://localhost:8000/api/house/)
As this api uses django viewset it supports GET, POST, HEAD, OPTIONS requests.

This will allow you to add new instance of a house to the database.
The media format that my application will be accepting is json for new post requests. MediaType is `application/json`.
The format for post requests is as such:

```
{
    "area_unit": "",
    "bathrooms": null,
    "bedrooms": null,
    "home_size": null,
    "home_type": "",
    "last_sold_date": null,
    "last_sold_price": null,
    "link": "",
    "price": null,
    "property_size": null,
    "rent_price": null,
    "rentzestimate_amount": null,
    "rentzestimate_last_updated": null,
    "tax_value": null,
    "tax_year": null,
    "year_built": null,
    "zestimate_amount": null,
    "zestimate_last_updated": null,
    "zillow_id": null,
    "address": "",
    "city": "",
    "state": "",
    "zipcode": null
}
```

If you know the id of the record you would like to modify you can access it's instance directly through the addition of the id to the Url request. 

Example is:[localhost:8000/api/house/](http://localhost:8000/api/house/1/)

The request types currently being supported through direct instance access are: 
GET, PUT, PATCH, DELETE, HEAD, OPTIONS
