# Flask server 
- Python 3.7.7
- Flask
- SQLAlchemy
- 
- create virtual venv
> python -m venv venv

- Upgrade pip
> python -m pip install --upgrade pip

- Install requirements
> pip install -r requirements.txt

## Run App
>python app.py
or
> flask run

## Flask migration
> flask db init
> flask db migrate -m "Create asset table"
> flask db upgrade

