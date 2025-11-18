# Django thoughts 💭🐍

# How to run locally 🤔🐍

## Step 1: clone repo
```bash
git clone https://github.com/apetranov/django-thoughts.git
```
## Step 2: enter folder
```bash
cd django-thoughts
```
## Step 3: create virtual environment
```bash
python -m venv venv
```
## Step 4: activate virtual environment
### Windows
```bash
venv\Scripts\activate
```
### MacOS/Linux
```bash
source venv/bin/activate
```
## Step 5: install dependencies
```bash
pip install -r requirements.txt
```
## Step 6: set up SECRET_KEY
Rename ".env.example" to ".env" and pick a value for your secret key.
You can create a secret key with the following command:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
## Step 7: apply database migrations
```bash
python manage.py migrate
```
## Step 8: run development server
```bash
python manage.py runserver
```
## Step 9: open this url in browser and enjoy :)
```bash
127.0.0.1:8000
```
# How to use the app 🤔🐍
## 1. Click the register option on the navbar and register yourself
![register](https://github.com/user-attachments/assets/bcc96d37-2026-4bd4-960e-fdb1850915b1)

## You will be taken to this screen
![successregister](https://github.com/user-attachments/assets/810740e2-f733-4d0c-82a6-d400352c9d69)
## 2. Add thought
## Click on "Add one now" to add a thought
![successregister](https://github.com/user-attachments/assets/810740e2-f733-4d0c-82a6-d400352c9d69)
## 3. On this screen type your thought in the "What is on your mind today?" field. Also choose a mood and optionally type a tag
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/cbf5c699-43bb-4d6f-9ade-446ebbdc19eb" />
## 4. You get redirected to this page where your thought was added and you also see a quote picked based on the mood which you chose
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/70e2502d-db05-47dd-a216-a1077355d1c4" />

