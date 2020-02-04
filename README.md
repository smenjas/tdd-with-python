# Test-Driven Development with Python

These are my notes from the book [Test-Driven Development with Python](https://www.obeythetestinggoat.com/pages/book.html).

I've used the book as a guide, and deviated occasionally.

## [Prerequisites and Assumptions](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html)
- The book uses [Python](https://www.python.org/) 3.6 and [Django](https://www.djangoproject.com/) 1.11.
- I'm using Python 3.7, Django 1.11, [macOS](https://en.wikipedia.org/wiki/MacOS) 10.15, and [Homebrew](https://brew.sh/) 2.2.
- ["venv" is the general convention used globally.](https://docs.python-guide.org/dev/virtualenvs/#basic-usage)

First, install dependencies and create the environment.
```bash
# Install Homebrew.
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install the project dependencies.
brew install python3
brew install geckodriver
brew cask install firefox

# Create a Git repository.
git init ~/src/myproject
cd ~/src/myproject

# Create a virtual environment, in the directory "venv".
python3 -m venv virtualenv venv

# Create a .gitignore file.
echo '*.log' >> .gitignore
echo '*.pyc' >> .gitignore
echo '__pycache__' >> .gitignore
echo 'db.sqlite3' >> .gitignore
echo 'venv' >> .gitignore
git add .gitignore

# Commit the .gitignore file.
git commit -m "Add a .gitignore file."
```

For development and testing, activate virtualenv with this command:
```bash
source venv/bin/activate
```

Once you've activated the virtualenv, install Django & Selenium:
```bash
pip install "django<1.12" "selenium<4"
```

When you're done with development and testing, deactivate virtualenv:
```bash
deactivate
```

## [Chapter 1](https://www.obeythetestinggoat.com/book/chapter_01.html)

Create a new Django project:
```bash
django-admin startproject myproject .
```

Start a web server:
```bash
python manage.py runserver
```

Run my functional tests.
```bash
python functional_tests.py
```

## License

Released as open source software under the terms of the [ISC License](https://en.wikipedia.org/wiki/ISC_license).
