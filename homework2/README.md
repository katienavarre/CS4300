# Movie Theater Booking App

## Project Description

This project is a movie theater booking application built with Django. It allows users to view available movies, select seats, book seats, and view their booking history. The project also includes a REST API for managing movie and seat information.

**Deployed Application:** https://movie-theater-booking-ghv3.onrender.com

## Features

* View a list of movies and their details.
* Access movie and seat information through the REST API.
* View available seats for a movie.
* Book available seats.
* Prevent seats from being booked again after they have been reserved.
* View booking history.
* Manage movies and seats through Django Admin.
* Automated tests for application functionality.
* Behavior-driven testing with Behave.

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* HTML and Bootstrap
* Gunicorn
* WhiteNoise
* Render for deployment
* Django testing framework
* Behave
* Coverage.py

## Project Structure

```text
movie_theater_booking/
├── bookings/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── features/
│   ├── steps/
│   └── movie_list.feature
├── movie_theater_booking/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### Prerequisites

Install Python 3.12 or another Python version compatible with the project's dependencies, along with Git.

### 1. Clone the Repository

Clone the course repository and navigate to the project directory:

```bash
git clone https://github.com/katienavarre/CS4300.git
cd CS4300/homework2/movie_theater_booking
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment in the homework directory:

```bash
python -m venv ../myenv
```

Activate it on Linux or in the DevEdu terminal:

```bash
source ../myenv/bin/activate
```

On Windows, if using a Windows-based Python environment, activate the environment with the appropriate Windows activation script.

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Create or update the local SQLite database:

```bash
python manage.py migrate
```

### 5. Create an Administrator Account (Optional)

To access Django Admin locally, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email address, and password.

### 6. Start the Development Server

Run the application locally:

```bash
python manage.py runserver
```

Open the local development URL shown in the terminal, usually:

http://127.0.0.1:8000/

To access the Django administration page, visit `/admin/` on your local development server.

## Running the Tests

### Django Automated Tests

Run the automated test suite:

```bash
python manage.py test
```

The project has 18 Django tests, which passed during the final testing checks.

### Test Coverage

Run the tests with Coverage.py:

```bash
coverage run manage.py test
coverage report --include="bookings/*,movie_theater_booking/*,manage.py"
```

The reported total test coverage during the final checks was **94%**, exceeding the assignment's 80% coverage target.

### Behave Tests

Run the behavior-driven tests:

```bash
behave
```

The movie listing feature was tested successfully, with one scenario and three steps passing during the final checks.

## Using the Application

1. Open the deployed application.
2. View the movie listing page.
3. Select **Book Seat** for a movie.
4. Choose an available seat and submit the booking.
5. Visit **Booking History** to verify the reservation.
6. Confirm that a booked seat is no longer listed as available.

Administrators can manage movie and seat records through the Django Admin interface at `/admin/`.

## Deployment

The application is deployed using Render.

The deployment uses Gunicorn to serve the Django application. Dependencies are installed during the build process, static files are collected, and database migrations are applied.

The Django secret key and other deployment configuration values are provided through environment variables in Render.

**Live application:** https://movie-theater-booking-ghv3.onrender.com

## Database

The project uses SQLite as its database.

The database contains movie information, seat availability, and booking records. The local development database is separate from the deployed database.

Render's free web service uses an ephemeral filesystem, so SQLite data may not persist through service restarts, spin-downs, or redeployments.

## AI Use Disclosure

AI assistance was used during development to help explain Django concepts, troubleshoot errors, understand deployment configuration, and assist with testing and documentation. The application was tested by running the Django test suite, running the Behave scenario, and manually testing movie listings, seat booking, and booking history.

## Conclusion

This project demonstrates the use of Django and Django REST Framework to build a movie theater booking application. It includes movie and seat management, booking functionality, booking history, automated testing, behavior-driven testing, and deployment through Render.
