# Django REST framework (DRF) Practice

Create an application with Django REST framework (DRF) to show contents and their ratings.

## Practice
![Practice Screenshot](doc/practice.jpg)

## Document

[Document.pdf](doc/document.pdf)

## How to run:

Follow these steps to set up and run the project:

### 1. Clone the repository
Clone the repository to your local machine:
```
git clone https://github.com/m-shahrestani/DRF-Practice
cd DRF-Practice
```
### 2. Set up a virtual environment
Create and activate a virtual environment:

For Linux/macOS:
```
python3 -m venv venv
source venv/bin/activate
```
For Windows:
```
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
Install the required dependencies from the `requirements.txt` file:
```
pip install -r requirements.txt
```
### 4. Apply database migrations
Apply the database migrations to set up the database:
```
python manage.py migrate
```
### 5. Create a superuser
Create a superuser to access the Django admin panel (optional):
```
python manage.py createsuperuser
```
Follow the prompts to set up the superuser.

### 6. Run the server
Start the development server:
```
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

### 7. Access the API
You can access the content and rating API at:

`http://127.0.0.1:8000/api/schema/swagger/`

#### GET and POST Request for posts:
Send a GET request to view a list of contents along with their average score and ratings count.

Response example for GET request:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "title": "string",
      "content": "string",
      "average_score": 0,
      "ratings_count": 0,
      "created_at": "2024-12-31T19:58:29.366Z",
      "updated_at": "2024-12-31T19:58:29.366Z"
    }
  ]
}
```

Send a POST request to create content with the JSON body to `http://127.0.0.1:8000/posts/`.

Example for POST request:
```
{
    "title": "New post",
    "content": "New post is good.",
    "average_score": 0,
    "ratings_count": 0
}
```

Response example for POST request:
```
{
    "uuid": "9e68d37d-1cef-497e-8132-bf3b56f9526b",
    "title": "New post",
    "content": "New post is good.",
    "average_score": 0.0,
    "ratings_count": 0,
    "created_at": "2024-12-31T20:11:24.314219Z",
    "updated_at": "2024-12-31T20:11:24.314219Z"
}
```

#### POST and PUT request for rating:
Send a POST request to create or a PUT request to update the score with the JSON body to `http://127.0.0.1:8000/rating/`.

Example for POST and PUT request:
```
{
    "post_uuid": "219687ce-ac9e-405d-a54b-d10d121f5add",
    "user_name": "ali",
    "score": 4
}
```

Response example for POST request:
```
{
    "message": "Rating created successfully.",
    "score": 4
}
```

Response example for PUT request:
```
{
    "message": "Rating updated successfully.",
    "score": 4
}
```