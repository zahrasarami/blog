# blog website 
simple blog webpage for my network course at university built on the Django Web Framework and react.
## Backend
### Usage 
first activate your virtual environment .

all requirements is collected in `requirements.txt` and you can easily install them using command bellow .
```bash
pip install -r requirements.txt
```
to activate server : 
```bash
python manage.py runserver
```
### Models
* #### user
  >Used Django user authentication model
* #### Blog
  >Many to one realtionship between user and Blog .
### feturers
* Login and Registration
  >using jwt tokens
* Creation, deletion and updation of blog posts

* search and post's pagination
### DataStorage
it is implemented using `sqlite` and post's images saved in `/blogs` directory .
## Frontend
it's implemented in react (in fron-end branch) and it isn't completed yet:)
## Installation
