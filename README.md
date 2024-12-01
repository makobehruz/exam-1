
---

# Taomlarni Boshqarish Dasturi

**Ta'rif:**  
Bu dastur yordamida yangi taom qo'shishingiz, uning tarkibini, narxini, turi va oshxonasi haqida ma'lumot kiritishingiz mumkin. Shuningdek, barcha taomlarni ro'yxatda ko'rish imkoniyati mavjud.

---

## Xususiyatlari:
1. **Yangi Taom Qo'shish:**  
   - Taom nomi, tarkibi, narxi, turi va oshxona nomini kiriting.
   - "Create Meal" tugmasini bosish orqali taom qo'shiladi.

2. **Taomlar Ro'yxati:**  
   - Kiritilgan barcha taomlar jadval ko'rinishida namoyish qilinadi.
   - Jadval quyidagi ustunlardan iborat: 
     - **Name (Nomi)**
     - **Ingredients (Tarkibi)**
     - **Price (Narxi)**
     - **Type (Turi)**
     - **Cuisine (Oshxonasi)**

---

## Foydalanish Ko'rsatmalari:
1. **Dastur Ishga Tushirish:**  
   - Dasturni o'rnatish va ishga tushirish uchun quyidagi buyruqlarni terminalda kiriting:  
     ```bash
     pip install -r requirements.txt
     python manage.py runserver
     ```

2. **Yangi Taom Qo'shish:**
   - "Meal Name" maydoniga taom nomini kiriting.
   - "Ingredients" maydoniga tarkibini yozing.
   - "Price" maydoniga narxni kiriting.
   - "Cuisine" maydoniga oshxona turini yozing.
   - "Select Type" ro'yxatidan taom turini tanlang (masalan, "Main", "Dessert" va h.k.).
   - "Create Meal" tugmasini bosing.

3. **Taomlar Ro'yxatini Ko'rish:**
   - "Meal List" bo'limida qo'shilgan barcha taomlar jadvalda ko'rinadi.

---

## Talablar:
- **Python 3.8+**
- Django
- Brauzer (dastur veb-ilova ko'rinishida ishlaydi)

---

## Muallif:
- Ismingizni va aloqangizni kiriting.

--- 

Ushbu README ni dastur fayllari bilan birga saqlang. Agar kerak bo'lsa, tuzatishlar kiritishingiz mumkin!



---

# Taksi Boshqaruv Dasturi

**Ta'rif:**  
Ushbu dastur taksilarni boshqarish uchun mo'ljallangan. Foydalanuvchi yangi taksini qo'shishi, haydovchi nomi, raqam belgisi, sig'imi, avtomobil modeli va holati kabi ma'lumotlarni kiritishi mumkin. Barcha qo'shilgan taksilar ro'yxat ko'rinishida namoyish etiladi.

---

## Xususiyatlari:
1. **Yangi Taksi Qo'shish:**  
   - Taksi nomi, raqam belgisi, haydovchi nomi, yo'lovchi sig'imi, avtomobil modeli va holati haqida ma'lumot kiriting.
   - "Create Taxi" tugmasini bosish orqali yangi taksi qo'shiladi.

2. **Taksilar Ro'yxati:**  
   - Kiritilgan barcha taksilar jadval ko'rinishida ko'rinadi. 
   - Jadval quyidagi ustunlardan iborat:  
     - **Taxi Name (Taksi Nomi)**
     - **License Plate (Raqam Belgisi)**
     - **Driver (Haydovchi)**
     - **Passenger Capacity (Yo'lovchi Sig'imi)**
     - **Car Model (Avtomobil Modeli)**
     - **Status (Holati)**

---

## Foydalanish Ko'rsatmalari:
1. **Dastur Ishga Tushirish:**  
   - Dasturni o'rnatish va ishga tushirish uchun quyidagi buyruqlarni terminalda kiriting:  
     ```bash
     pip install -r requirements.txt
     python manage.py runserver
     ```

2. **Yangi Taksi Qo'shish:**
   - "Taxi Name" maydoniga taksi nomini kiriting.
   - "License Plate" maydoniga avtomobilning raqam belgisini yozing.
   - "Driver Name" maydoniga haydovchining ismini kiriting.
   - "Passenger Capacity" maydoniga taksining sig'imini kiriting.
   - "Car Model" maydoniga avtomobil modelini yozing.
   - "Status" maydonidan taksining holatini tanlang (masalan, "Available", "In Service" va h.k.).
   - "Create Taxi" tugmasini bosing.

3. **Taksilar Ro'yxatini Ko'rish:**
   - "Meal List" bo'limida qo'shilgan barcha taksilar jadvalda aks etadi.

---

## Talablar:
- **Python 3.8+**
- Django
- Brauzer (dastur veb-ilova ko'rinishida ishlaydi)

---

## Muallif:
- Ismingiz va aloqangizni kiriting.

---

Ushbu README faylini dastur fayllari bilan birga saqlang. Agar dasturga qo'shimcha funksiyalar qo'shilsa, README-ni yangilashingiz mumkin!
