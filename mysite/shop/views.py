from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from .models import AllJewellerys, user, Product, Semi_Bridal_Sets, Short_Choker_Necklace, Long_Necklace_Sets, Sliver_Earrings, Golden_Earrings, Trending_design
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.db import connection

glob_login_username = ''
glob_user = False


def index(request):
    global glob_user, glob_login_username
    # return HttpResponse('Hello World')  if you want print text then use HttpResponse
    Jewellery = AllJewellerys.objects.all()
    Semi_Bridal_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Semi Bridal Sets';")
    short_Choker_Necklace = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Short Choker Necklace';")
    long_Necklace_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Long Necklace Sets';")
    sliver_Earrings = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Sliver Earrings';")
    Golden_Earrings = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Golden Earrings';")

    lis = []
    for i in range(0, 5):
        lis.append(i)

    dics = {'name': 'Company Name', 'lastname': 'JOGU', 'count': lis, 'All_Jewellery': Jewellery, 'Semi_Bridal_Sets': Semi_Bridal_Sets, 'short_Choker_Necklace': short_Choker_Necklace,
            'long_Necklace_Sets': long_Necklace_Sets, 'sliver_Earrings': sliver_Earrings, 'Golden_Earrings': Golden_Earrings,
            'user': glob_user, 'username': glob_login_username}
    return render(request, 'index.html', dics)


def register(request):

    # register User in database
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email_phone']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        username = request.POST['username']
        # print(username)
        if len(username) > 10:
            text = {'username_alert': "yes"}
            return render(request, 'register_page.html', text)
        if not username.isalnum():
            # messages.error(request, 'Username Should Only Contain Letters And Numbers')
            text = {'username_LN_alert': "yes"}
            return render(request, 'register_page.html', text)
        if password != conpassword:
            # messages.error(request, 'Password Do Not Match')
            text = {'password': "yes"}
            return render(request, 'register_page.html', text)
        if len(password) < 8:
            # messages.error(request, 'Password Do Not Match')
            text = {'password2': "yes"}
            return render(request, 'register_page.html', text)

        user1 = user(Username=username, Password=password,
                     Email_Phone=email, First_name=first_name, Last_name=last_name)
        user1.save()
        print('User created')
        # messages.success(request,'Your Registration Has Been Successfully Done !!!!')
        return redirect('/shop/index')
    else:
        # messages.error(request, 'Something Wen Wrong Please Try again !!!!!')
        # return HttpResponse('404- error')
        return render(request, 'register_page.html')


def handle_login(request):
    if request.method == 'POST':
        login_username = request.POST['lg_username']
        login_password = request.POST['lg_password']
        User_list = user.objects.raw(
            f"SELECT * FROM shop_user WHERE Username='{login_username}' AND PASSWORD='{login_password}';")

        if len(User_list) > 0:
            print('Valid Username And Password')
            return redirect('/shop/index')
        else:
            print('invalid Username Password, please try again')
            dic = {'invaid_U_P': 'Error'}
            return redirect('/shop/index', dic)

    return HttpResponse('404 - error')


def handle_logout(request):
    logout(request)
    print('Logout Successfully')
    global glob_user, glob_login_username
    glob_login_username = ''
    glob_user = False
    return redirect('/shop/index')


def forget_pass(request):
    # test = request.user
    # print(test)
    return render(request, 'forgetpass.html')


def contact_us(request):

    return render(request, 'contactus.html')


def about_us(request):

    return render(request, 'aboutus.html')


def blog(request):

    return render(request, 'blog.html')


def return_refund_replacement(request):
    return render(request, 'return_refund_replacement.html')


def All_Jewellery_Sets(request):

    Jewellery = AllJewellerys.objects.all()
    Haram_Set = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Haram Set';")
    long_Necklace_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Long Necklace Sets';")
    Short_Necklace = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Short Necklace';")
    Pendant_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Pendant Sets';")
    Mangalsutra_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Mangalsutra Sets';")

    dic = {'Jewellery': Jewellery, 'Haram_Set': Haram_Set, 'long_Necklace_Sets': long_Necklace_Sets,
           'Short_Necklace': Short_Necklace, 'Pendant_Sets': Pendant_Sets, 'Mangalsutra_Sets': Mangalsutra_Sets}

    return render(request, 'All Jewellery Sets.html', dic)


def Haram_Set(request):
    Haram_Set = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Haram Set';")

    dic = {'Haram_Set': Haram_Set}
    return render(request, 'Haram Set.html', dic)


def Long_Necklace_Sets_fun(request):
    long_Necklace_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Long Necklace Sets';")

    dic = {'long_Necklace_Sets': long_Necklace_Sets}
    return render(request, 'Long Necklace Sets.html', dic)


def Short_Necklace_fun(request):
    Short_Necklace = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Short Necklace';")
    dic = {'Short_Necklace': Short_Necklace}
    return render(request, 'Short Necklace.html', dic)


def Pendant_Sets_fun(request):
    Pendant_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Pendant Sets';")
    dic = {'Pendant_Sets': Pendant_Sets}
    return render(request, 'Pendant Sets.html', dic)


def Mangalsutra_Sets_fun(request):
    Mangalsutra_Sets = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Mangalsutra Sets';")
    dic = {'Mangalsutra_Sets': Mangalsutra_Sets}
    return render(request, 'Mangalsutra Sets.html', dic)


def Earrings_fun(request):

    sliver_Earrings = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Sliver Earrings';")
    Golden_Earrings = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Golden Earrings';")

    dic = {'sliver_Earrings': sliver_Earrings,
           'Golden_Earrings': Golden_Earrings}
    return render(request, 'Earrings.html', dic)


def Maang_Tikkas_And_Daminis_fun(request):
    Maang_Tikkas_And_Daminis = AllJewellerys.objects.raw(
        "SELECT * FROM shop_alljewellerys WHERE category='Maang Tikkas And Daminis';")
    dic = {'Maang_Tikkas_And_Daminis': Maang_Tikkas_And_Daminis}
    return render(request, 'Maang Tikkas And Daminis.html', dic)


def product(request='', category='', title='', id='Default'):
    dic = {'title': title, 'id': id}
    if id != 'Default':
        Buy_now_product = AllJewellerys.objects.raw(
            f"SELECT * FROM `shop_alljewellerys` WHERE id='{id}' AND product_name='{str(title)}';")
        Related_product = AllJewellerys.objects.raw(
            f"SELECT * FROM `shop_alljewellerys` WHERE category='{category}' ORDER BY id ASC LIMIT 10 ")
        dic = {'Buy_now_product': Buy_now_product,
               'title': title, 'Related_product': Related_product}

        return render(request, 'product.html', dic)
    return render(request, 'product.html', dic)


def admin(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        print(first_name)
        last_name = request.POST['lname']
        print(last_name)
        email_phone = request.POST['emailphone']
        print(email_phone)
        password = request.POST['password']
        print(password)
        username = request.POST['username']
        print(username)

        Userlist = user.objects.raw(
            "SELECT * FROM shop_user WHERE Username='premjogu';")
        if len(Userlist) > 0:
            user2 = user.objects.all()
            user_name = {'User_exist': "yes", 'user': user2}
            return render(request, 'admin_page.html', user_name)
        if not username.isalnum():
            # messages.error(request, 'Username Should Only Contain Letters And Numbers')
            user2 = user.objects.all()
            user_name = {'user_name_without_symbol': "Error", 'user': user2}
            return render(request, 'admin_page.html', user_name)
        elif len(username) > 10:
            user2 = user.objects.all()
            user_name = {'user_name': 'Error', 'user': user2}
            return render(request, 'admin_page.html', user_name)
        elif len(password) < 8:
            user2 = user.objects.all()
            password = {'password': 'Error', 'user': user2}
            return render(request, 'admin_page.html', password)
        user1 = user(Username=username, Password=password,
                     Email_Phone=email_phone, First_name=first_name, Last_name=last_name)
        user1.save()
    user2 = user.objects.all()
    dic = {'user': user2}
    return render(request, 'admin_page.html', dic)


def admin_Add_Jewellerys(request):

    if request.method == 'POST':
        productname = request.POST['productname']
        Category = request.POST.get('Category', 'Please Select Category')
        Price = request.POST['Price']
        Discription = request.POST['Discription']
        prod_date = request.POST['prod_date']
        image = request.FILES.get('image', 'Please Select Image')
        image1 = request.FILES.get('image1', 'Please Select Image')
        image2 = request.FILES.get('image2', 'Please Select Image')
        image3 = request.FILES.get('image3', 'Please Select Image')
        if image == 'Please Select Image' and image1 == 'Please Select Image' and image2 == 'Please Select Image' and image3 == 'Please Select Image':
            image_error = {'image_error': 'Please Select Image'}
            return render(request, 'admin_Add_Jewellerys.html', image_error)
        elif Category == 'Please Select Category':
            error = {'error': 'Please Select Category'}
            return render(request, 'admin_Add_Jewellerys.html', error)
        AllJewellerys1 = AllJewellerys(product_name=productname, category=Category, price=Price,
                                       desc=Discription, pub_date=prod_date, image=image, image1=image1, image2=image2, image3=image3)
        AllJewellerys1.save()
    Jewellery = AllJewellerys.objects.all()
    # print(Jewellery)
    dic = {'Jewellery': Jewellery}
    return render(request, 'admin_Add_Jewellerys.html', dic)
