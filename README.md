# FastAPI Project README

This FastAPI project serves as a platform for users to post and interact with advertisements (Ads) along with commenting
features. Below are the details regarding the setup, technologies used, and business specifications implemented within
this project.

## Technologies Used

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Database Migrations:** Alembic
- **Testing Framework:** Pytest

## Requirements

The following requirements are implemented in this project:

- Users must be authenticated to perform actions such as adding Ads and comments.
- Registration requires a unique email as username and a password.
- Each user can only comment on an Ad once.
- Ads and their related comments are visible to all users, whether logged in or not.
- Users can delete and edit their own Ads.
- Users can post Ads and also comment on other people's Ads.

## Database Configuration

Two PostgreSQL databases are used:

1. **Production Database:** For storing production data.
2. **Test Database:** For running tests without affecting production data.

## Setting Up the Environment

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up PostgreSQL databases for production and testing environments.
4. create .env file based on .env.sample
5. Apply database migrations using Alembic: `alembic upgrade head`.

## Running the Application

- Start the FastAPI server using `uvicorn app.main:app --reload`.
- Access the API documentation at `http://localhost:8000/docs`.

## Running Tests

1. Apply database migrations using Alembic: `alembic -c alembic_test.ini upgrade head`.
2. Run tests using Pytest: `pytest`.
