# iClinic Test

Suppose you live in Ribeirão Preto. Should you take an umbrella?

You tell us!

If the air humidity on a given day is greater than 70%, it is a good idea to take an umbrella with you. Your goal is to fetch the Ribeirão Preto air humidity forecast for the next five days from https://openweathermap.org/api and display the following message template:

You should take an umbrella in these days: ....

For instance, if on the next five days air humidity will be greater than 70% on Monday, Tuesday and Wednesday, you must display the message:

You should take an umbrella in these days: Monday, Tuesday and Wednesday.


### STEP 1: Get the source code

Create a folder to be the working directory and execute a git clone. If you don't have *access* or *user*, contact the [Administrator].

```bash
$ git clone git@github.com:rrgaya/raining_days.git

```


### STEP 2: Creating the environment

Access the folder created by git on the terminal shell and you must run the following command, where env is the name of the base directory for pip3 will install all project library without conflict or affect the machine libraries. Also will assure that only python3 will be running in the virtual environment.


```bash
$ pip install pipenv
$ pipenv --three
```

### STEP 3: Activating the virtual enviroment

Run this commmand in the same folder where the env folder is located.

```bash
$ pipenv shell
```


### STEP 4: Installing the requirements


```bash
$ pipenv install
``` 


### STEP 5: Execute app.py


```bash
$ python3 app.py
``` 

