# 🛵 Meals on Wheels – Food Delivery System

Meals on Wheels is a simple online food delivery web application built using **Python (Django)** and **MySQL**.  
Users can browse restaurants, order food, and make online payments, while vendors manage menus and orders.

---

## 🚀 Features
- User registration & login  
- Search nearby restaurants  
- Add to cart & place orders  
- Table booking  
- Vendor panel for menu & order management  
- Admin panel for system management  
- Online payment integration (PayUmoney)

---

## 🛠 Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Django)  
- **Database:** MySQL  

---

## ⚙️ Setup Instructions
```bash
git clone https://github.com/yourusername/meals-on-wheels.git
cd meals-on-wheels

python -m venv env
env\Scripts\activate      # Windows
# or
source env/bin/activate   # Linux/Mac

pip install -r requirements.txt               
```

## 🗄️ Database Setup

### Create MySQL Database
```sql
CREATE DATABASE mealsonwheels;
```

##🔧 Run Migrations & Start Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

##📄 License

MIT License
