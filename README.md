![](https://github.com/sitamadex11/CovidHelp/blob/develop/Assets/HackOctoberFestBanner.png)
# EdexCare 👩‍🎓
This is a basic full stack web application with HTML, CSS, Bootstrap, Material UI, JavaScript and Python-Django.
### Welcome!
<br>


![Minimum API Level](https://img.shields.io/badge/Min%20API%20Level-23-green)
![Maximum API Level](https://img.shields.io/badge/Max%20API%20Level-30-orange)
![GitHub repo size](https://img.shields.io/github/repo-size/sitamadex11/CovidHelp)
[![License](https://img.shields.io/badge/license-MIT-%2397ca00.svg)](https://github.com/sitamadex11/CovidHelp/blob/develop/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 
![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) 
![Maintenance](https://img.shields.io/maintenance/yes/2021)

## Tech Stack
### Front-End
![html](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![css](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![sass](https://img.shields.io/badge/SASS-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![material-ui](https://img.shields.io/badge/Material_UI-0081CB?style=for-the-badge&logo=material-ui&logoColor=white)
![javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![jquery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)

### Back-End
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)


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
