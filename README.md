### Recipe Finder Web App - Backend
## Description
This is the backend for the Recipe Finder Web App. It allows users to search for recipes, add their own recipes and interact with the community. The app is built using Python with Flask, connected to a PostgreSQL database, and integrates with the Spoonacular API for recipe data.

## Features
- User Authentication 
- Recipe Search 
- Add and Manage Recipes 
- User Interaction 

## Technologies Used
- Python: Backend language
- Flask: Web framework for building APIs
- PostgreSQL: Database for storing user data and recipes
- Spoonacular API: For fetching recipe data
- JWT: JSON Web Tokens for secure user authentication

## Installation
## Prerequisites
- Python 3.x
- PostgreSQL
- Flask
- Pip (Python package installer)

## Steps
## Clone the repository:
git clone https://github.com/wahome-joy/recipe-finder-backend.git
cd recipe-finder-backend
## Create a virtual environment:
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
## Install the dependencies:
pip install -r requirements.txt
## Set up environment variables:
Create a .env file in the root of the project and add the following:
DATABASE_URL=postgresql://yourusername:yourpassword@localhost:5432/yourdbname
SECRET_KEY=yoursecretkey
SPOONACULAR_API_KEY=yourapiKey

### Run the application:
python app.py


## Endpoints
POST /register: User registration
POST /login: User login
GET /recipes: Fetch a list of recipes (using Spoonacular API)
POST /recipes: Add a new recipe (logged-in users only)

## Database Schema
Users: Stores user information (username, email, hashed password)
Recipes: Stores recipe details (name, ingredients, instructions, user ID)

## Contributing
Feel free to fork this repository and create pull requests for any improvements or fixes!

## License
This project is licensed under the MIT License.

