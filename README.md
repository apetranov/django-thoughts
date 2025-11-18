# Django thoughts 💭🐍

# How to run locally:

## Step 1: clone repo
```bash
git clone https://github.com/apetranov/django-thoughts.git
```
## Step 2: create virtual environment
```bash
python -m venv venv
```
## Step 3: activate virtual environment
### Windows
```bash
venv\Scripts\activate
```
### MacOS/Linux
```bash
source venv/bin/activate
```
## Step 4: install dependencies
```bash
pip install -r requirements.txt
```
## Step 5: set up SECRET_KEY
Change ".env.example" and rename to ".env" and pick a value for your secret key.
You can create a secret key with the following command:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
