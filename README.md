![{8841D508-6074-4560-9BAA-D8CB2B259006}](https://github.com/user-attachments/assets/2f70bf5c-c05d-4dcb-9197-425730cdaa41)
![Uploading {D257518A-57B4-400C-8AFC-650021FF195E}.png…]()

FAQ Project

This project is a Django-based application for managing Frequently Asked Questions (FAQs) with multilingual support, using a WYSIWYG editor for the answers. It includes a REST API for managing FAQs, supports language translation, and provides a user-friendly admin interface.

Table of Contents
	•	Installation
	•	Usage
	•	API Usage
	•	Admin Panel
	•	Testing
	•	Contributing
	•	License

Installation

Follow the steps below to set up the project locally.

Prerequisites
	•	Python 3.x
	•	pip
	•	Redis (for caching)

Step-by-Step Setup
	1.	Clone the repository

git clone https://github.com/sudeepa90/faq_project.git
cd faq_project


	2.	Create a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


	3.	Install the required dependencies
Ensure that you have all the necessary Python packages:

pip install -r requirements.txt


	4.	Set up Redis (for caching)
If you don’t have Redis installed, you can download it from here. Make sure it’s running locally before proceeding.
	5.	Apply database migrations
Run the migrations to set up the database schema.

python manage.py migrate


	6.	Create a superuser for the Django admin panel

python manage.py createsuperuser

Follow the prompts to create a superuser.

	7.	Run the development server
Start the server to test the project:

python manage.py runserver

Your application should be accessible at http://127.0.0.1:8000/.

Usage

After setting up, you can use the application to manage FAQs with multilingual support via the Django Admin Panel. Additionally, the FAQs can be accessed and managed via the API.

API Usage

Fetch FAQs
	•	Get FAQs in English (default)

curl http://localhost:8000/api/faqs/


	•	Get FAQs in Hindi

curl http://localhost:8000/api/faqs/?lang=hi


	•	Get FAQs in Bengali

curl http://localhost:8000/api/faqs/?lang=bn



POST a New FAQ

You can use POST requests to add new FAQs.

curl -X POST -H "Content-Type: application/json" -d '{"question": "What is Django?", "answer": "Django is a Python web framework.", "question_hi": "डjango क्या है?", "answer_hi": "Django एक पाइथन वेब फ्रेमवर्क है."}' http://localhost:8000/api/faqs/

Admin Panel

You can access the Django admin panel by navigating to:

http://127.0.0.1:8000/admin/

Log in with the superuser credentials you created, and you can manage the FAQs from a user-friendly interface. You can add, edit, and delete FAQs, and they will be reflected in all supported languages.

Testing

The project includes unit tests for the models and API.

Run Tests

To run the tests, use the following command:

python manage.py test

Alternatively, if you’re using pytest, you can run:

pytest

Contributing
	1.	Fork the repository and clone it to your local machine.
	2.	Create a new branch for your feature or bug fix:

git checkout -b feature/your-feature


	3.	Make your changes and commit them:

git commit -m "feat: Add multilingual FAQ model"


	4.	Push your changes to your fork:

git push origin feature/your-feature


	5.	Open a pull request to the main repository.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Notes
	•	This project uses django-ckeditor for the WYSIWYG editor integration and supports multilingual FAQ management.
	•	It includes a caching mechanism using Redis to improve performance, especially when serving translated FAQ data.
	•	Google Translate API or googletrans is used for automatic translation during FAQ creation.
