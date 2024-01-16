# flask_unit_testing
This is a small application to use as a reference for future unit testings on projects.
## Run the application
Go to the cloned folder and run the following in Terminal or Command Prompt:

MacOS/Linux:
```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app main run
```

Windows:
```shell
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
flask --app main run
```

## Run tests
Once you ran the application, just run the following:
```shell
cd tests
pytest
```

## Run Code Coverage
### Command Report
Run the code coverage of the project, in the root folder.
```shell
coverage run -m pytest
coverage report
```

The report should look like this.
```
Name                 Stmts   Miss  Cover
----------------------------------------
api_dict.py              1      0   100%
book.py                  4      0   100%
book_repository.py      27      0   100%
main.py                 40      0   100%
service.py              32      0   100%
----------------------------------------
TOTAL                  104      0   100%
```

### HTML Version Report
For the HTML Version, which is for user friendly and checks for missing statements.
```shell
coverage run -m pytest
coverage html
```
It will pop up this message
```
Wrote HTML report to htmlcov\index.html
```
In the File Explorer, go to your app folder and go to the 'htmlcov' folder, click on index.html
It will open a Coverage report, something like this.
![image](https://github.com/alejandroguerreron2p/flask_unit_testing/assets/150069261/256a5f9e-04e0-41e9-b997-d73d2393055e)
