# EdexCare
Basic full stack web application with HTML, CSS, Bootstrap, Material UI, JavaScript and Python-Django.

## Installation

### Prerequisites
Anyone with a basic knowledge of HTMl, CSS and JavaScript and the Knack of Programming. It is good if you know python and django.

#### 1. Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Setup virtual environment
Reference : https://docs.python.org/3/library/venv.html
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv ./envs/

# Activate virtual environment
source envs/bin/activate
```

#### 3. Clone git repository
```bash
git clone "https://github.com/Akash-Kumar-Sen/EdexCare.git"
```

#### 4. Install requirements
```bash
cd EdexCare/
pip install -r requirements.txt
```

#### 5. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver

# your server is up on port 8000
```
Try opening [http://localhost:8000](http://localhost:8000) in the browser.
Now you are good to go.
