# CV Builder

This is a Django-based web application designed to create Online Resume Builder API - Application that lets users create their own CV

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- A PostgreSQL database (other databases may work but are not officially supported)

## Setup

1. **Clone this repository:**

    ```
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. **Set up a virtual environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the requirements:**

    ```
    pip install -r requirements.txt
    ```

4. **Setup the database:**

    Update the `DATABASES` section in `settings.py` with your database information. Then run the following command to apply migrations:

    ```
    python manage.py migrate
    ```

5. **Collect static files:**

    ```
    python manage.py collectstatic
    ```

6. **Run the server:**

    ```
    python manage.py runserver
    ```

    Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to see the application.

## Running Tests

To run tests, use the following command:

```
python manage.py test
```

## Deployment

Deployment steps can vary depending on the platform (like Heroku, AWS, GCP, etc.) you are using. Check the platform-specific guidelines for more information.

## Contributing

We love contributions! Please see the `CONTRIBUTING.md` file for details on how you can help out.

## License

This project is licensed under the terms of the MIT license.
