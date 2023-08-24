# SSH Sequencer Django Application

This project, hosted at [https://github.com/jcal0/ssh-sequencer-django](https://github.com/jcal0/ssh-sequencer-django), is a Django web application focused on SSH sequencing. Here, you'll find an overview of templates, views, and the `consumers.py` file (for Django Channels integration, if applicable).

## Prerequisites

- Python 3.x
- Pip (usually comes with Python)

## Setup & Installation

1. Clone this repository:
```
git clone https://github.com/jcal0/ssh-sequencer-django.git
cd ssh-sequencer-django
```

2. Create a virtual environment:

```
python3 -m venv venv
```
For Windows:
```
python -m venv venv
```
3. Activate the virtual environment:
```
source venv/bin/activate
```
For Windows:
```
.\venv\Scripts\activate
```
4. Install the required packages:
```
pip install -r requirements.txt
```
5. Apply migrations to set up your database:
```
python manage.py migrate
```
6. Run the Django development server:
```
python manage.py runserver
```


This will start the development server at `http://127.0.0.1:8000/`. Open this URL in your browser.

## Project Structure

- **Templates**: Located in the `templates` folder. This is where all the HTML files for the project reside.

- **Views**: Found in `views.py`. Defines the logic and control flow for handling requests and responses.

- **consumers.py**: If you're using Django Channels for WebSockets or other asynchronous protocols, the logic for handling those will be in `consumers.py`.

## Contributing

Contributions, feedback, and issues are always welcome! Feel free to dive into the project's [GitHub issues](https://github.com/jcal0/ssh-sequencer-django/issues).
