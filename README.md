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
