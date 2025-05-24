# Hotel Booking Website (Skyline)


[SKYLINE](https://skyline-frontend-five.vercel.app/)  is a full-featured hotel booking system developed using Django REST Framework. It offers a seamless experience for users to search for hotels, make bookings, complete secure payments, and share reviews — all in one platform.

The key features of Skyline include:
User Authentication & Authorization
Secure registration, login, email verification, and role-based access control ensure only authorized access.

Hotel and Booking Management
Complete CRUD (Create, Read, Update, Delete) operations for hotels and bookings, with user-specific booking history tracking.
Secure Payment Integration
Integrated with SSLCommerz, providing a reliable and secure payment gateway for real-time transactions.

Review and Rating System
Users can leave honest reviews and rate hotels based on their experience, helping others make informed decisions.
User profile password forget system.
Skyline is designed to be scalable, user-friendly, and secure — making it an ideal solution for real-world hotel booking needs.

---

### User Access Information
- **Admin:**
```
Username: admin
Password: admin
```

- **User:**
```
Username: arman
Password: arman
```
---

### Key Features
- **User Authentication** via Gmail OAuth
- **User Registration Login Logout** via Gmail OAuth
- **CRUD Operations** for hotel and booking management
- **User Profile password Forget** view profile
- **SSLCommerz Payment Integration** for secure payments
- **Hotel Review System** for customer feedback
- **Scalable PostgreSQL Database** with Django Rest Framework API

---

### Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** OAuth2 via Gmail
- **Payment Gateway:** SSLCommerz
- **Frontend Technology:** HTML/Tailwind/Js (deployed on Vercel)
- **Backend Technology:** Django/postgresql (deployed on Vercel and Database Hosted Superbase)

---

### Project Live Access Information
- **Skyline Frontend Vercel Live Site:** [Skyline-Frontend](https://skyline-frontend-five.vercel.app/)
- **Skyline Backend Vercel Server Site:** [Skyline-Backend](https://skyline-backend.vercel.app/)
---

### Project GitHub Access Information
- **Skyline GitHub Frontend:** [github.com/mohammadarmanhossen/Skyline_frontend](https://github.com/mohammadarmanhossen/Skyline_frontend)
- **Skyline GitHub Backend :** [github.com/mohammadarmanhossen/Skyline_backend](https://github.com/mohammadarmanhossen/Skyline_backend)
---

### Api Intigration Hotel App:
---
District:
```
https://skyline-backend.vercel.app/district/

```
Hotels :
```
https://skyline-backend.vercel.app/hotels/
```

Review:
```
https://skyline-backend.vercel.app/reviews/
```
Bookes:
```
https://skyline-backend.vercel.app/bookeds/
```


User App:
---
User Login :
```
https://skyline-backend.vercel.app/client/login/
```
User Register :
```
https://skyline-backend.vercel.app/client/register/
```

User Logout:
```
https://skyline-backend.vercel.app/client/logout/
```
Admin login:
```
https://skyline-backend.vercel.app/client/admin/login/
```
Admin logout :
```
https://skyline-backend.vercel.app/client/admin/logout/
```

User :
```
https://skyline-backend.vercel.app/client/users/
```
Contact:
```
https://skyline-backend.vercel.app/client/contact/
```
Change password:
```
https://skyline-backend.vercel.app/client/change_password/${user_id}/
```


Payment App:
---
Checkout :
```
https://skyline-backend.vercel.app/checkout/

```
Order :
```
https://skyline-backend.vercel.app/order/
```

Created Payment:
```
https://skyline-backend.vercel.app/payment/create_payment/
```
Payment Success:
```
https://skyline-backend.vercel.app/payment/success/
```
Payment Cencel :
```
https://skyline-backend.vercel.app/payment/cancel /
```
Payment Failed :
```
https://skyline-backend.vercel.app/payment/failed /
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
