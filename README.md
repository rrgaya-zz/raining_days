# Raining Days




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

