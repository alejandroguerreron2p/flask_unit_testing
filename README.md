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
Once you ran the application, just run the following:
```shell
cd tests
pytest
```

## Run Code Coverage
Run the code coverage of each test file.
```shell
cd tests
coverage run -m pytest
coverage report
```

The report should look like this.
```
Name                                                                         Stmts   Miss  Cover
------------------------------------------------------------------------------------------------
C:\Users\alguerrero\Documents\coding\flask_unit_testing\api_dict.py              1      0   100%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\book.py                  4      0   100%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\book_repository.py      52     18    65%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\main.py                 40      0   100%
C:\Users\alguerrero\Documents\coding\flask_unit_testing\service.py              36      4    89%
__init__.py                                                                      0      0   100%
conftest.py                                                                     10      0   100%
test_database.py                                                                35      0   100%
test_endpoints.py                                                               71      0   100%
test_factory.py                                                                  4      0   100%
test_service.py                                                                 35      0   100%
------------------------------------------------------------------------------------------------
TOTAL                                                                          288     22    92%
```
