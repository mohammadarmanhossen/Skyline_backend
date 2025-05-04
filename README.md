# Hotel Booking Website (Skyline)

Skyline is a full-featured hotel booking system developed using Django REST Framework. It offers a seamless experience for users to search for hotels, make bookings, complete secure payments, and share reviews — all in one platform.

The key features of Skyline include:
User Authentication & Authorization
Secure registration, login, email verification, and role-based access control ensure only authorized access.

Hotel and Booking Management
Complete CRUD (Create, Read, Update, Delete) operations for hotels and bookings, with user-specific booking history tracking.
Secure Payment Integration
Integrated with SSLCommerz, providing a reliable and secure payment gateway for real-time transactions.

Review and Rating System
Users can leave honest reviews and rate hotels based on their experience, helping others make informed decisions.
Skyline is designed to be scalable, user-friendly, and secure — making it an ideal solution for real-world hotel booking needs.

- **Skyline Frontend Live Site:** [skyline-frontend.netlify.app](https://skyline-frontend.netlify.app/)
- **Skyline Backend Live Site:** [skyline-backend-krnt.onrender.com](https://skyline-backend-krnt.onrender.com/)
- **Skyline Frontend GitHub:** [Skyline-Frontend](https://github.com/mohammadarmanhossen/Skyline_frontend)
- **Skyline Backend GitHub:** [Skyline-Backend](https://github.com/mohammadarmanhossen/Skyline_backend)

### User Access Information
- **Admin Role:**
```
Username: admin
Password: admin
```

- **Normal User:**
```
Username: arman
Password: arman
```
---

## Key Features
- **User Authentication** via Gmail OAuth
- **CRUD Operations** for hotel and booking management
- **SSLCommerz Payment Integration** for secure payments
- **Hotel Review System** for customer feedback
- **Scalable PostgreSQL Database** with Django Rest Framework API

---

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** OAuth2 via Gmail
- **Payment Gateway:** SSLCommerz
- **Frontend (Optional):** React/Vue (deployed on Netlify)

---



## Api Intigration

---
Hotel App:
---
Distict :
```
http://skyline-backend-krnt.onrender.com/district/

```
Hotels :
```
http://skyline-backend-krnt.onrender.com/hotels/
```

Review:
```
http://skyline-backend-krnt.onrender.com/reviews/
```
Bookes:
```
ttp://skyline-backend-krnt.onrender.com/bookeds/
```


User App:
---
User Login :
```
https://skyline-backend-krnt.onrender.com/client/login/
```
User Register :
```
https://skyline-backend-krnt.onrender.com/client/register/
```

User Logout:
```
https://skyline-backend-krnt.onrender.com/client/logout/
```
Admin login:
```
https://skyline-backend-krnt.onrender.com/client/admin/login/
```
Admin logout :
```
https://skyline-backend-krnt.onrender.com/client/admin/logout/
```

User :
```
https://skyline-backend-krnt.onrender.com/client/users/
```
Contact:
```
https://skyline-backend-krnt.onrender.com/client/contact/
```
Change password:
```
https://skyline-backend-krnt.onrender.com/client/change_password/${user_id}/
```


Payment App:
---
Checkout :
```
https://skyline-backend-krnt.onrender.com/checkout/

```
Order :
```
https://skyline-backend-krnt.onrender.com/order/
```

Created Payment:
```
https://skyline-backend-krnt.onrender.com/payment/create_payment/
```
Payment Success:
```
https://skyline-backend-krnt.onrender.com/payment/success/
```
Payment Cencel :
```
https://skyline-backend-krnt.onrender.com/payment/cancel /
```
Payment Failed :
```
https://skyline-backend-krnt.onrender.com/payment/failed /
```

---
## Installation and Setup

 **Clone the repository:**
 ```bash
 
git clone https://github.com/mohammadarmanhossen/Skyline_backend
cd Skyline_backend
```

Install dependencies:
```
pip install -r requirements.txt

```
Run migrations:
```
 python manage.py migrate
```

Create a superuser:
```
python manage.py createsuperuser
```
Run the server:
```
python manage.py runserver
```

Run Tests:

```
python manage.py runserver
```
