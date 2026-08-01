# Wiki Encyclopedia

## About

**This project was created as part of Harvard University's CS50W course.**

This project is a wiki-style encyclopedia application built with Django. Users can browse existing entries, search for topics, create new pages, and edit existing content.

The project helped me practice building web applications with Django, working with URL routing, templates, views, and handling user-generated content.

## Features

- View encyclopedia entries
- Search for entries
- Create new encyclopedia pages
- Edit existing pages
- Convert Markdown content into HTML
- Dynamic page rendering

## Technologies Used

- Python
- Django
- HTML
- CSS
- Markdown

## How It Works

The application stores encyclopedia entries as Markdown files and dynamically converts them into HTML pages when users visit an entry.

Django handles:
- URL routing
- Views
- Templates
- User requests

The search feature allows users to quickly find entries based on their titles or related keywords.

## Screenshots

<img width="1004" height="451" alt="image" src="https://github.com/user-attachments/assets/96bf573e-6c78-4f7f-bd36-04a79a6dee62" />

<img width="1301" height="452" alt="image" src="https://github.com/user-attachments/assets/b8bfa69a-4140-461a-b665-bb5f1ab9527d" />

<img width="1373" height="314" alt="image" src="https://github.com/user-attachments/assets/e066bdfc-c0d6-4345-8570-096e6cba3efb" />


Examples:
- Homepage
- Entry page
- Search results
- Creating a new page
- Editing an entry

## Installation

Clone the repository:

```bash
git clone https://github.com/Behrad01/wiki-encyclopedia.git
```

Navigate into the project folder:

```bash
cd wiki-encyclopedia
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Django development server:

```bash
python manage.py runserver
```

Open the application at:

```
http://127.0.0.1:8000/
```

## Usage

- Select an entry from the homepage to view it.
- Use the search bar to find entries.
- Create new pages through the "Create New Page" option.
- Edit existing entries using the edit feature.
