# E-COMMERCE-WEBSITE-USING-DJANGO

# E-commerce Website using Django

An e-commerce platform built using Django to facilitate online shopping. This website provides features like product browsing, user authentication, cart functionality, and order management.

## Features

- **User Authentication**: Register, login, logout.
- **Product Browsing**: View products by category, search products.
- **Cart**: Add products to cart, view cart, and modify quantity or remove products.
- **Checkout**: Place orders, provide shipping information.
- **Order Management**: View past orders, check order status.

## Installation

1. **Clone the repository**
   
   \```
   git clone https://github.com/vishnudev-p/E-COMMERCE-WEBSITE-USING-DJANGO.git
   \```

2. **Navigate to the project directory**

   \```
   cd Eshop
   \```

3. **Set up a virtual environment**

   \```
   python -m venv venv
   \```

4. **Activate the virtual environment**

   - Windows:
     \```
     .\venv\Scripts\activate
     \```

   - macOS and Linux:
     \```
     source venv/bin/activate
     \```

5. **Install required packages**

   \```
   pip install -r requirements.txt
   \```

6. **Run migrations**

   \```
   python manage.py migrate
   \```

7. **Start the development server**

   \```
   python manage.py runserver
   \```

Visit `http://127.0.0.1:8000/` in your browser to access the website.

## Usage

1. **Admin Panel**: Access the Django admin panel by navigating to `http://127.0.0.1:8000/admin`.
   
2. **Browse Products**: Click on 'Store' to view all available products.
   
3. **User Registration**: Click on 'Signup' to register a new account.
   
4. **User Login**: Click on 'Login' if you're a returning customer.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
