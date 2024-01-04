# Dish Search Application

This is a Django search application that allows you to search for dish names and get recommendations for the best matches.

## Installation

1. Create and activate a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   source venv/bin/activate
   ```

2. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Apply the database migrations:

   ```shell
   python manage.py migrate
   ```

4. Import data from the CSV file into the database(not required as SQLite file is provide only for reference):

   ```shell
   python manage.py shell -c "exec(open('dish_search/import_data.py').read())"
   ```

5. Create superuser to access the admin panel:

    ```shell
    python manage.py createsuperuser
    ```

## Usage

1. Start the development server:

   ```shell
   python manage.py runserver
   ```

2. Access the application by visiting `http://localhost:8000/search/` in your web browser.

3. Enter a dish name in the search field and click the "Search" button to get recommendations for the best matches.

