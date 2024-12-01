from django.shortcuts import render
from .models import Meals

def meal_list(request):
    if request.method == 'GET':
        name = request.GET.get('meal')
        ingredients = request.GET.get('address')
        price = request.GET.get('price')
        cuisine = request.GET.get('cuisine')
        gender = request.GET.get('gender')

        if name and ingredients and price and cuisine and gender:
            Meals.objects.create(
                name=name,
                ingredients=ingredients,
                price=price,
                cuisine=cuisine,
                gender=gender,
            )

    # Ro'yxatni olish
    meals = Meals.objects.all()
    ctx = {'meals': meals}
    return render(request, 'meals/index.html', ctx)
