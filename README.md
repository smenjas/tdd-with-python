# Test-Driven Development with Python

These are my notes from the book [Test-Driven Development with Python](https://www.obeythetestinggoat.com/pages/book.html).

## [Prerequisites and Assumptions](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html)
- The book uses [Python](https://www.python.org/) 3.6 and [Django](https://www.djangoproject.com/) 1.11.
- I'm using a [Mac](https://en.wikipedia.org/wiki/Macintosh) and [Homebrew](https://brew.sh/).
- [venv is the general convention used globally.](https://docs.python-guide.org/dev/virtualenvs/#basic-usage)
```bash
# Install Homebrew.
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install caskroom/cask/brew-cask

brew install python3
brew install geckodriver
brew cask install firefox
pip3 install selenium

git init ~/my/project
cd ~/my/project
python3 -m venv virtualenv venv
echo "venv" >> .gitignore
git add .gitignore
git commit -m "Add a .gitignore file."
```

Activate virtualenv with this command:
```bash
source virtualenv/bin/activate
```

Once you've activated the virtualenv, install Django & Selenium:
```bash
pip install "django<1.12" "selenium<4"
```

Deactivate virtualenv with this command:
```bash
deactivate
```

[Chapter 1](https://www.obeythetestinggoat.com/book/chapter_01.html)

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
