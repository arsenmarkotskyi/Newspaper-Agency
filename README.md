# Newspaper-Agency

Django project for managing newspapers, topics and authors

## Check it out

Newspaper agency project deployed to Render

## Installation

Python3 must be installed

```shell
git clone https://github.com/arsenmarkotskyi/Newspaper-Agency
cd newspaper_agency
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

```

## Features
* Authentication functionality for Redactor/User
* Managing topics, newspapers & redactors directly from website interface
* Powerful admin panel for advanced managing

## Demo

![[Website Interface]](demo.png)

## Models

### Newspaper
- `title`: The title of the newspaper article.
- `content`: The content of the newspaper article.
- `published_date`: The date the article was published.
- `topics`: Many-to-many relationship with `Topic`.
- `publishers`: Many-to-many relationship with `Redactor`.

### Topic
- `name`: The name of the topic (e.g., Politics, Economics, IT).

### Redactor
- Inherits from `AbstractUser` and adds a `years_of_experience` field.


## Templates
- ** (`base.html`)**: is the main template for the entire web application.
This file contains common UI elements that are reused across all pages, such as:
**Header**
**Navigation Menu**
**Content Blocks**

- **Homepage (`index.html`)**: Displays the list of topics and recent newspapers.
- **Topic List (`topic_list.html`)**: Shows all available topics for the user to browse.
- **Topic Update, Create (`topic_form.html`)**: Form for create or update Topic.
- **Topic Delete (`topic_confirm_delete.html`)**: Form for Delete Topic.
- **Newspaper List (`newspaper_list.html`)**: Displays all newspapers, with options to filter by topics.
- **Newspaper Detail (`newspaper_detail.html`)**: Shows the full content of a selected newspaper.
- **Newspaper Update, Create (`newspaper_form.html`)**: Form for create or update Newspaper.
- **Newspaper Delete (`newspaper_confirm_delete.html`)**: Form for Delete Newspaper.
- **Redactor List (`redactor_list.html`)**: Displays all newspapers, with options to filter by topics.
- **Redactor Create (`redactor_create.html`)**: Form for adding a new redactor.
- **Redactor Update, Create (`redactor_form.html`)**: Form for create or update Newspaper.
- **Redactor Delete (`redactor_confirm_delete.html`)**: Form for Delete Newspaper.
- **Login (`registration/login.html`)**: User login page.
- **Logged out (`registration/logged_out.html`)**: User logged out page.


## Forms

This project uses various forms to handle user input for managing newspapers, redactors, and topics. These forms include:

- **ModelForms** for creating and editing models like `Newspaper` and `Redactor`.
- **Search Forms** for filtering and searching records based on certain fields.
- **Validation** for custom checks, such as password strength in the `RedactorForm`.


### Testing Models

## AdminTests

1. **Redactor List View**: Verifies that the `years_of_experience` field is visible in the list view of `Redactor` in the Django admin.
2. **Redactor Detail View**: Verifies that the `years_of_experience` field is displayed in the detailed view when editing a `Redactor` record in the admin interface.
3. **Redactor Add View**: Verifies that the `years_of_experience` field is included in the form when adding a new `Redactor` through the Django admin.


## Form Test

# NewspaperFormTest

1. **Test Valid Form Submission**: Verifies that the `NewspaperForm` is valid when all required fields are provided, including `title`, `content`, `published_date`, `topics`, and `publishers`.

# RedactorFormTest

1. **Test Valid Form Submission with Correct Data**: Verifies that the `RedactorForm` is valid when all required fields are provided with correct data, including a strong password.
2. **Test Invalid Form Submission with Weak Password**: Verifies that the `RedactorForm` is invalid if the password does not meet the required strength criteria.
3. **Test Password Validation Error**: Verifies that the `RedactorForm` raises a validation error for weak passwords (less than 8 characters or missing required elements).

## ModelTests

1. **Test Topic String Representation (`test_topic_str`)**:
   - Verifies that the string representation of a `Topic` instance returns the correct name of the topic.

2. **Test Newspaper String Representation (`test_newspaper_str`)**:
   - Verifies that the string representation of a `Newspaper` instance returns the correct title of the newspaper.
   - The test creates a `Topic` and a `Redactor` (as the publisher) and associates them with the `Newspaper`.

3. **Test Redactor String Representation (`test_redactor_str`)**:
   - Verifies that a `Redactor` user can be created with the correct username, password, and years of experience.
   - Ensures that the `username` is set properly, the password is checked correctly, and `years_of_experience` matches the provided value.


## View Test

# PublicAccessTest
Tests if unauthenticated users are restricted from accessing protected pages:
- **test_login_required_for_protected_pages**: Ensures users without login can't access protected URLs (e.g., topics, newspapers, and redactors).

# PrivateAccessTest
Tests access for authenticated users:
- **test_retrieve_topics**: Verifies logged-in users can view topics.
- **test_retrieve_newspaper**: Verifies logged-in users can view newspapers.
- **test_retrieve_redactor**: Verifies logged-in users can view redactors.


### Running the Tests
Run tests with:

```bash
python manage.py test
```

