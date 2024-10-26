# Spy Cat Agency Management Application

## Overview

This is a management application for the Spy Cat Agency (SCA) designed to simplify the processes of managing cats, missions, and targets. The application is built using Django and Django REST Framework and provides a RESTful API for CRUD operations.

## Features

- Create, read, update, and delete spy cats.
- Create missions with associated targets.
- Assign cats to missions.
- Mark targets as complete and update their notes.
- Validate cat breeds using TheCatAPI.

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework
- PostgreSQL

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sandor4ik/spy-cat-agency-test.git
   cd spy_cat_agency

2. **Create a virtual environment:**

    python -m venv venv
    `venv\Scripts\activate`

3. **Install dependencies:**

    pip install -r requirements.txt

4. **Set up the database:**

    Ensure you have PostgreSQL installed and create a database for your application. Update the database settings in settings.py accordingly.

5. **Run migrations:**

    python manage.py makemigrations
    python manage.py migrate

6. **Run the application:**

    python manage.py runserver

7. **Access the API:**

    Open your browser and navigate to http://127.0.0.1:8000/ to access the API endpoints.

## API Endpoints

    Below are the main API endpoints available in the application:

## Cats

    POST /cats/ - Create a new spy cat
    GET /cats/ - List all spy cats
    GET /cats/<id>/ - Retrieve a single spy cat
    PUT /cats/<id>/ - Update a spy cat
    DELETE /cats/<id>/ - Delete a spy cat
    
## Missions

    POST /missions/ - Create a new mission with targets
    GET /missions/ - List all missions
    GET /missions/<id>/ - Retrieve a single mission
    PUT /missions/<id>/ - Update a mission
    DELETE /missions/<id>/ - Delete a mission
    POST /missions/<id>/assign_cat/ - Assign a cat to a mission
    POST /missions/<id>/complete/ - Mark a mission as complete
    Targets

    POST /targets/ - Create a new target
    GET /targets/ - List all targets
    GET /targets/<id>/ - Retrieve a single target
    PUT /targets/<id>/ - Update a target

## Postman Collection
    
## Spy Cat Agency API Collection

## Description

    This Postman collection provides access to the API of the Spy Cat Agency application, allowing you to manage cats, missions, and targets. Use this collection to test and interact with the endpoints defined in the project.
    
## Endpoints

1. **Cats**

    a. Create a Cat
    Method: POST
    URL: /cats/
    { "name": "Cat1", "years_of_experience": 3, "breed": "Siamese", "salary": 500.00}

    b. Retrieve List of Cats
    Method: GET
    URL: /cats/

    c. Retrieve Specific Cat Information
    Method: GET
    URL: /cats/{id}/

    d. Update Cat Information
    Method: PUT
    URL: /cats/{id}/
    jsonКопировать код{ "salary": 550.00}

    e. Delete a Cat
    Method: DELETE
    URL: /cats/{id}/

2. **Missions**

    a. Create a Mission
    Method: POST
    URL: /missions/
    { "cat": 1, "targets": [ { "name": "Target1", "country": "USA", "notes": "Notes about the target", "is_complete": false }, { "name": "Target2", "country": "Canada", "notes": "Additional notes", "is_complete": false } ]}

    b. Retrieve List of Missions
    Method: GET
    URL: /missions/

    c. Retrieve Specific Mission Information
    Method: GET
    URL: /missions/{id}/

    d. Update a Mission
    Method: PUT
    URL: /missions/{id}/
    { "cat": 2, "is_complete": true}

    e. Delete a Mission
    Method: DELETE
    URL: /missions/{id}/

    f. Assign a Cat to a Mission
    Method: POST
    URL: /missions/{id}/assign_cat/
    { "cat_id": 1}

    g. Mark Mission as Complete
    Method: POST
    URL: /missions/{id}/complete_mission/

3. **Targets**

    a. Retrieve List of Targets
    Method: GET
    URL: /targets/

    b. Retrieve Specific Target Information
    Method: GET
    URL: /targets/{id}/

    c. Update a Target Note
    Method: PUT
    URL: /targets/{id}/
    { "notes": "Updated notes"}

## Usage

    Import the collection into Postman.
    Set your API URL (e.g., http://127.0.0.1:8000).
    Select the desired requests, modify parameters, and send them to interact with the API.

## Notes

    Make sure the server is running before executing requests.
    Don’t forget to check that all required fields are included in the request bodies.

