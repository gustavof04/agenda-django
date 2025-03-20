# 📒 Django Agenda

Electronic agenda made in Python using the Django framework. It is used as a system for creating, editing, and removing contacts that are stored in an SQLite database and managed by a logged-in owner (user).

> Project Status: ✔️ (completed)

## 🔧 Technologies Used
Python V.: 3.11.1 || Django V.: 4.2.5 || SQLite || Whitenoise V.: 6.6.0

## ⚙️ Setting Up the Virtual Environment
* In your terminal, navigate to the project's root folder and run the following command to create a virtual environment:
  ```bash
  python -m venv name_of_virtualenv
  ```

* Run the command according to your system to activate your virtual environment:

  Windows
  ```bash
  .\name_of_virtualenv\Scripts\activate
  ```

  Linux or macOS
  ```bash
  source name_of_virtualenv/bin/activate
  ``` 

## 🧑‍🔬 Installing Dependencies
* With the virtual environment **activated**, install the project dependencies with the following command:

  ```bash
  pip install -r requirements.txt
  ```

## 🚀 Starting the Agenda
* Apply the migrations with the command below:
  ```bash
  python manage.py migrate
  ```

* Run the following command to start the server:
  ```bash
  python manage.py runserver
  ```

* In a browser of your choice, go to the address <code>127.0.0.1:8000</code> to be redirected to the agenda.
* Create your user by clicking on "Register" and filling in your information.
* Start creating your contacts!

## 🔓 Bonus (Accessing the Admin)
* Create a superuser in your terminal with <code>python manage.py createsuperuser</code>.
* If you are logged into the agenda, log out.
* Access the admin panel in your browser at <code>127.0.0.1:8000/admin</code> and log in with the superuser you just created.
* Now, as an administrator, you can analyze the models, their fields, and all the data in operation, as well as manipulate them as you wish.
