# flask_unit_testing
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
Once you ran the application, to run the tests, just run ```pytest``` inside the cloned folder.

## Run Code Coverage
Run the code coverage of each test file.
```shell
cd tests
coverage run -m pytest <test_file>
coverage report
```

The report should look like this.
```
Name                                                                         Stmts   Miss  Cover
------------------------------------------------------------------------------------------------
C:\Users\alguerrero\Documents\coding\flask_unit_testing\api_dict.py              1      0   100%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\book.py                  4      0   100%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\book_repository.py      26      8    69%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\main.py                 23     18    22%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\service.py              30      6    80%
__init__.py                                                                      0      0   100%
conftest.py                                                                     10      3    70%
test_service.py                                                                 13      1    92%
------------------------------------------------------------------------------------------------
TOTAL                                                                          107     36    66%
```
