# Introduction
This repository is a template for building a Python Flask application

# Instructions
### 1. How to run the application
`python app.py`

### 2. Flask application route explained
```python
@app.route('/', methods=['GET', 'POST']) # Add the method to Flask
def index(): # Name the method (this will be the reference when using flask.redirect)
    # Do stuff
    return render_template( # Render the html template (all variables used in the template must be included here)
        'index.html'
    )
```

### 3. Files and folders explained
The repository includes a `templates` folder and a `static` folder.
```
.
├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
├── static
│   ├── main.js
│   └── style.css
└── templates
    ├── base.html
    └── index.html
```

**The templates folder** is for your html files.\
html files can be included within eachother to separate page sections, increase readability and decrease duplicate code.\
Example: `{% extends 'base.html' %}`

**The static folder** is for your static files such as .css, .js, images etc.

### 4. Template html with Jinja2
Jinja2 is a full-featured template engine for Python.\
Example:
```jinja
{% extends "layout.html" %}
{% block body %}
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}
```
*Note: Remember to include python variables in render_template()*
*From the example above this would be a python dictionary `{'user':{'name':'myName', 'username':'myUsername'}}`*