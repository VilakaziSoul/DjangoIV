# Hyperion Django Project

This Django project, named "Hyperion," consists of a blog, polls, and webapp components. Each component is designed to serve a specific purpose within the project.

## Project Structure

The project is structured with separate apps for each component:

- `webapp`: This app handles the main structure of the project.
- `blog`: This app manages a blog section where posts can be created and displayed.
- `polls`: This app implements a polling system with questions and choices for users to vote on.

## URLs Configuration (`urls.py`)

The root `urls.py` configuration file contains URL patterns for routing to different views within the project:

- `webapp/urls.py`: URL patterns for the main webapp component.
- `blog/urls.py`: URL patterns for the blog component.
- `polls/urls.py`: URL patterns for the polls component.

## Django Settings (`settings.py`)

The project's settings are defined in the `settings.py` file. Key configurations include database settings, installed apps, static files, and template directories.

## Models (`models.py`)

In the `models.py` files of each app, the following models are defined:

- `blog/models.py`: Defines the `Post` model for blog posts.
- `polls/models.py`: Defines the `Question` and `Choice` models for polls.

## Views (`views.py`)

Each app has its own set of view functions:

- `webapp/views.py`: Contains the `index` view function for the main webapp.
- `blog/views.py`: Contains views for displaying a list of posts and a single post.
- `polls/views.py`: Contains views for displaying polls, voting, and displaying results.

## Templates (`templates` directory)

Templates are provided for each app's views:

- `blog/templates/blog.html`: Template for displaying a list of blog posts.
- `blog/templates/post.html`: Template for displaying a single blog post.
- `polls/templates/polls/index.html`: Template for displaying a list of polls.
- `polls/templates/polls/detail.html`: Template for voting on a poll.
- `polls/templates/polls/results.html`: Template for displaying poll results.

## Static Files (`static` directory)

Static files like CSS, images, and JavaScript are stored in the `static` directory.


## Usage

### To run the Hyperion Django project, follow these steps:

1. Clone the repository: git clone https://github.com/vilakazisoul/DjangoIV.git
2. Navigate to project directory: cd DjangoIV
3. Set up a virtual environment: python -m venv venv
4. Activate the virtual envirnoment:
   Windows: venv\Scripts\activate
   macOS and Linux: source venv/bin/activate
5. Install the required dependencies listed in requirements.txt: pip install -r requirements.txt
6. Configure the database settings in `settings.py`.
7. Run migrations to create the database schema: `python manage.py makemigrations` and `python manage.py migrate`.
8. Start the development server: `python manage.py runserver`.
9. Access the project components using the provided URLs.
   
  [Main webapp](http://127.0.0.1:8000/)

  [Blog](http://127.0.0.1:8000/blog/)

  [Polls](http://127.0.0.1:8000/polls/)

  [Personal Webpage](http://127.0.0.1:8000/webapp/)

Feel free to modify the templates, views, and models to customize the project according to your needs.

## Acknowledgments

This Django project was created by [Kathide Vilakazi]. It includes components for a blog, polls, and a personal webpage template.
