# Wiki Encyclopedia

## About

**This project was created as part of Harvard University's CS50W course.**

Wiki Encyclopedia is a Django-based web application where users can browse, search, create, and edit encyclopedia entries.

I built this project to practice working with Django and learn more about how web applications handle routing, templates, user input, and dynamic content.

## Features

- Browse encyclopedia entries
- Search for specific topics
- Create new entries using Markdown
- Edit existing entries
- Convert Markdown content into HTML
- Dynamically generate pages based on user requests

## Technologies Used

- Python
- Django
- HTML
- CSS
- Markdown

## How It Works

The application stores encyclopedia entries as Markdown files and converts them into formatted HTML pages when they are viewed.

Django handles the backend logic, including:
- Managing URLs and routes
- Rendering templates
- Processing user requests
- Handling page creation and editing

The search system allows users to find entries by searching for their titles or related keywords.

## Screenshots

### Homepage

<img width="1004" height="451" alt="image" src="https://github.com/user-attachments/assets/96bf573e-6c78-4f7f-bd36-04a79a6dee62" />

### Entry Page

<img width="1301" height="452" alt="image" src="https://github.com/user-attachments/assets/b8bfa69a-4140-461a-b665-bb5f1ab9527d" />

### Search Results

<img width="1373" height="314" alt="image" src="https://github.com/user-attachments/assets/e066bdfc-c0d6-4345-8570-096e6cba3efb" />

## Installation

Clone the repository:

```bash
git clone https://github.com/Behrad01/Wiki-Encyclopedia.git
```

Navigate to the project folder:

```bash
cd wiki-encyclopedia
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the Django development server:

```bash
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000/
```

## Usage

- Browse existing encyclopedia pages from the homepage.
- Use the search bar to find specific entries.
- Create new pages with Markdown content.
- Edit existing entries whenever changes are needed.

## Future Improvements

- Add user accounts and authentication
- Improve the overall styling
- Add categories and tags for entries
- Keep track of page history and previous edits
