from django.shortcuts import render
from django.shortcuts import redirect
from .models import category, subcategory,savecategorys
from django.db.models import Q
from django.contrib import messages

from sampleapp.categoryForm import CategoryForm

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


# Create your views here.
def category_form(request):
    try:
        if request.method == 'POST':
            data = savecategorys(categories_id = request.POST['categories'],subcategory_id=request.POST['subcategory'],isactive=1)
            data.save()
            messages.add_message(
                    request, messages.SUCCESS, 'Categories added successfully.',
                    fail_silently=True,
                )
            return redirect('category_form')
            # if form.is_valid():
            #             #     print(321)
                #data = category(item_name=request.POST['item_name'],description=request.POST['description'],food_type=request.POST['food_type'],calories=request.POST['calories'],protein=request.POST['protein'],fat=request.POST['fat'],carbohydrates=request.POST['carbohydrates'],fibre=request.POST['fibre'],image=request.FILES['image'],item_category_id=request.POST['item_category_id'],item_order_type=item_order_type,is_active=1)
            #return HttpResponse(123)
        
        form = CategoryForm()
        return render(request, 'category.html',{'form': form})
    except Exception as e:
        return HttpResponse(e)
    #logout(request)
    #return redirect('/')

def subcategoryajax(request):
    if request.method == 'POST':
        try:
            cat_id = request.POST['categories_id']
            data = []
            subcategorys = subcategory.objects.values('id','subcategory').filter(Q(categories_id=cat_id))
            for i in range(len(subcategorys)):
                subcat = {}
                subcat['id'] = subcategorys[i]['id']
                subcat['subcategory'] = subcategorys[i]['subcategory']
                data.append(subcat)
            #return HttpResponse(list(subcategorys))
            return JsonResponse({'subcategorys':list(data)},safe=True)
        except:
            return HttpResponse(e)
    #logout(request)
        return redirect('/')

def uploadfile(request):
    try:
        if request.method == 'POST':
            data = savecategorys(categories_id = request.POST['categories'],subcategory_id=request.POST['subcategory'],isactive=1)
            data.save()
            messages.add_message(
                    request, messages.SUCCESS, 'Categories added successfully.',
                    fail_silently=True,
                )
            return redirect('category_form')
            # if form.is_valid():
            #             #     print(321)
                #data = category(item_name=request.POST['item_name'],description=request.POST['description'],food_type=request.POST['food_type'],calories=request.POST['calories'],protein=request.POST['protein'],fat=request.POST['fat'],carbohydrates=request.POST['carbohydrates'],fibre=request.POST['fibre'],image=request.FILES['image'],item_category_id=request.POST['item_category_id'],item_order_type=item_order_type,is_active=1)
            #return HttpResponse(123)
        
        form = UploadForm()
        return render(request, 'excel.html',{'form': form})
    except Exception as e:
        return HttpResponse(e)
