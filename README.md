# ✅ Expense Tracker API

A secure RESTful API built with Django and Django REST Framework to track personal expenses and incomes.

This project uses JWT-based authentication and supports multiple users — each user can view and manage only their own records, while a superuser can manage all.

---

## 🚀 Tech Stack

- **Backend**: Django 5, Django REST Framework  
- **Auth**: JWT (via `djangorestframework-simplejwt`)  
- **Database**: SQLite (development)  
- **Python Version**: 3.10  
- **Environment Management**: `.env`

---

## 🔑 Features

- User registration and login via JWT  
- Authenticated CRUD for expenses and income  
- Role-based access: superuser vs. regular user  
- Tax handling: flat and percentage  
- Secure secret handling using `.env` file  
- Pagination enabled on expense list  
- Admin branding customized to "Expense Tracker"

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   `git clone https://github.com/Swetakhadka7/Expense_tracker.git`  
   `cd expense-tracker`

2. **Create and activate virtual environment**  
   `python -m venv env`  
   `.\env\Scripts\activate` (Windows) or `source env/bin/activate` (Unix)

3. **Install dependencies**  
   `pip install -r requirements.txt`

4. **Create `.env` file**

   ```env
   SECRET_KEY=your-django-secret
   DEBUG=True
   ```

5. **Apply migrations and create a superuser**  
   `python manage.py migrate`  
   `python manage.py createsuperuser`

6. **Run the development server**  
   `python manage.py runserver`

7. **Visit**  
   - API: `http://127.0.0.1:8000/api/expenses/`  
   - Admin Panel: `http://127.0.0.1:8000/admin/`

---

✅ Part 5: API Endpoints
## 📬 API Endpoints

### 🔐 Authentication

| Method | Endpoint                 | Description               |
|--------|--------------------------|---------------------------|
| POST   | `/api/auth/register/`    | Register a new user       |
| POST   | `/api/auth/login/`       | Get JWT token pair        |
| POST   | `/api/auth/refresh/`     | Refresh access token      |

---

### 📊 Expenses

| Method | Endpoint                 | Description                        |
|--------|--------------------------|------------------------------------|
| GET    | `/api/expenses/`         | List expenses (with pagination)    |
| POST   | `/api/expenses/`         | Create a new expense               |
| GET    | `/api/expenses/{id}/`    | Get details of one expense         |
| PUT    | `/api/expenses/{id}/`    | Update an existing expense         |
| DELETE | `/api/expenses/{id}/`    | Delete an expense                  |

> 🔐 All expense routes require: `Authorization: Bearer <access-token>`

---

## 🧾 Expense Object Example

```json
// Expense Payload
{
  "title": "Bike Servicing",
  "description": "Changed oil and cleaned brakes",
  "amount": 1500,
  "transaction_type": "debit",
  "tax": 5,
  "tax_type": "percentage"
}

// ✅ Computed Response
{
  "id": 12,
  "title": "Bike Servicing",
  "total": 1575.0,
  "created_at": "2025-07-05T10:12:00Z"
}
```

---

✅ Part 7: Admin Panel Customization

```markdown
## 🎛️ Admin Panel

- Accessible at: `/admin/`
- Branded as **Expense Tracker Admin**
- Superusers can manage all expenses and users
- Custom display titles applied using:

```python
admin.site.site_header = "Expense Tracker Admin"
admin.site.site_title = "Expense Tracker Portal"
admin.site.index_title = "Welcome to Expense Tracker Dashboard"
```

---

## 👩‍💻 Author

Sweta Khadka  
Expense Tracker — Django  
2025

---

## 📄 License

This project is open source and available under the MIT License.








