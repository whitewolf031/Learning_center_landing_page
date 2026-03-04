# O‘quv Markazi Landing Page Backend Tizimi

## Umumiy maqsad

O‘quv markazi uchun to‘liq ishlaydigan landing page uchun backend API tizimini ishlab chiqish.  
Tizim quyidagi asosiy bo‘limlarni o‘z ichiga oladi:

- Course – kurslar ro‘yxati va ma’lumotlari
- Feedback – o‘quvchilarning fikrlari va baholari
- Instructor – o‘qituvchilar (ustozlar) haqida ma’lumot
- News – yangiliklar va e’lonlar
- Statistic – o‘quv markazi statistikasi
- Accounts – foydalanuvchi autentifikatsiyasi va boshqaruvi

## Texnologiyalar stack’i

- Python
- Django REST Framework
- PostgreSQL (tavsiya etiladi)
- JWT Authentication (djangorestframework-simplejwt)
- Swagger / drf-yasg (dokumentatsiya uchun)
- (ixtiyoriy) Docker + docker-compose

## Modullar va talablar

### 1. Course moduli

**API endpointlari**
- `GET /api/courses/` – barcha kurslar ro‘yxati (pagination bilan)
- `GET /api/courses/{id}/` – bitta kursning to‘liq ma’lumoti
- `POST /api/courses/` – yangi kurs qo‘shish (admin)
- `PUT/PATCH /api/courses/{id}/` – kursni yangilash (admin)
- `DELETE /api/courses/{id}/` – kursni o‘chirish (admin)

**Kurs maydonlari**
- title
- description
- duration
- level (Beginner / Intermediate / Advanced)
- price
- students_count
- rating (avtomatik hisoblanishi mumkin)
- instructor (ForeignKey)
- category
- image
- skills (JSONField yoki ManyToMany)

**Qo‘shimcha**
- Pagination majburiy
- Rating feedbacklar asosida hisoblanishi mumkin

### 2. Feedback moduli

**API endpointlari**
- `GET /api/feedback/` – tasdiqlangan fikrlar ro‘yxati
- `GET /api/feedback/{id}/` – bitta fikr
- `POST /api/feedback/` – yangi fikr yozish (faqat autentifikatsiya qilingan foydalanuvchi)
- `PATCH/DELETE /api/feedback/{id}/` – admin tasdiqlashi yoki o‘chirishi

**Maydonlar**
- name
- role
- image
- content
- rating (1–5)
- course (ForeignKey)
- created_at

### 3. Instructor moduli

**API endpointlari**
- `GET /api/instructors/` – o‘qituvchilar ro‘yxati
- `GET /api/instructors/{id}/` – bitta o‘qituvchi ma’lumotlari
- `POST/PUT/PATCH/DELETE /api/instructors/` – admin uchun CRUD

**Maydonlar**
- name
- title
- company
- bio
- image
- skills
- rating
- students
- experience
- achievements
- social_links (JSONField)

### 4. News moduli

**API endpointlari**
- `GET /api/news/` – yangiliklar ro‘yxati (public)
- `GET /api/news/{id}/` – bitta yangilik
- `POST/PUT/PATCH/DELETE /api/news/` – faqat admin uchun

**Talablar**
- Faqat admin yangilik yozishi mumkin
- Author avtomatik saqlanadi (request.user)
- Sana bo‘yicha tartiblanadi (eng yangisi birinchi)

### 5. Statistic moduli

**API endpointi**
- `GET /api/statistics/` – landing page uchun umumiy statistika

**Qaytariladigan ma’lumotlar**
- total_courses_count
- total_students_count
- total_instructors_count
- total_feedback_count
- latest_news (oxirgi 3 ta)

**Talab**
- Ma’lumotlar database aggregation orqali real vaqtda hisoblanadi

### 6. Accounts moduli

**Custom User modeli**
- username
- first_name
- last_name
- phone
- password

**API endpointlari**
- `POST /api/auth/register/` – ro‘yxatdan o‘tish
- `POST /api/auth/login/` – kirish (JWT token qaytaradi)
- `POST /api/auth/logout/` – tokenni blacklist qilish

**Authentication**
- JWT (djangorestframework-simplejwt)

## Permission tizimi

| Rol                  | Ruxsatlar                                      |
|----------------------|------------------------------------------------|
| Public (no auth)     | Kurslarni ko‘rish, yangiliklarni ko‘rish       |
| Authenticated user   | Feedback yozish                                |
| Admin / Staff        | Barcha CRUD operatsiyalari                     |

## Performance talablari

- `select_related` va `prefetch_related` faol ishlatilishi kerak
- Pagination har bir list endpointda majburiy
- Image fayllari optimallashtirilishi (masalan, django-imagekit yoki cloud storage)
- Cache (agar kerak bo‘lsa Redis yoki Django cache framework)

## Dokumentatsiya

- Swagger UI (drf-yasg yoki drf-spectacular) orqali to‘liq API dokumentatsiyasi
- Har bir endpoint uchun description va misollar bo‘lishi shart

## Testing

- Postman yoki Insomnia collection tayyorlanadi
- Har bir endpoint sinovdan o‘tkaziladi (200, 201, 401, 403, 404 holatlari)

## Deployment talablari

- Docker + docker-compose bilan deploy qilinishi mumkin
- `.env` fayli orqali environment variables boshqariladi
- `DEBUG = False` production muhitda
- Static va media fayllar uchun to‘g‘ri sozlamalar (Whitenoise yoki Nginx)

---

# Loyihani ishga tushirish bo'yicha qo'llanma

## 1. Loyihani klon qilish

git clone https://github.com/username/repository.git
cd repository

# Linux / MacOS
python -m venv venv
source venv/bin/activate

# Windows (cmd)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt