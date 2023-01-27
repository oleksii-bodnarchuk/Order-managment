# Order-managment

### Description
This is a Django web application that allows users to view products, filter them by category, and place orders for them.

### Prerequisites
- Python 3.x
- Django 3.x
- Django REST framework 3.x

### Installation
1. Clone the repository: `git clone https://github.com/your-username/product-ordering-app.git`
2. Change directory to the project folder: `cd product-ordering-app`
3. Create a virtual environment and activate it: 
- `python3 -m venv venv`
- `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Run the migrations: 
- `python manage.py makemigrations`
- `python manage.py migrate`
6. Create a superuser to access the admin panel: `python manage.py createsuperuser`
7. Run the development server `python manage.py runserver`
8. Access the application in your browser at [http://127.0.0.1:8000]()

### Usage
View products
You can view all the products at the homepage of the application. You can filter the products by category by using the filter form on the top of the page.

### Place an order
You can place an order for a product by visiting the product detail page and submitting the order form.

### Admin panel
You can access the admin panel by visiting http://127.0.0.1:8000/admin. You can use the admin panel to add, edit, and delete products and categories. You can also view all the orders placed by the users.

### Contribution
Feel free to fork the repository and make pull requests to contribute to the project.
