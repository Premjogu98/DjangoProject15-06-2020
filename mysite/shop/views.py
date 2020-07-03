from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login,logout
from .models import AllJewellerys,user,Product,Semi_Bridal_Sets,Short_Choker_Necklace,Long_Necklace_Sets,Sliver_Earrings,Golden_Earrings,Trending_design
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

glob_login_username = ''
glob_user = False


def index(request):
    global glob_user,glob_login_username
    # return HttpResponse('Hello World')  if you want print text then use HttpResponse
    products = Product.objects.all()
    semi_Bridal_Sets = Semi_Bridal_Sets.objects.all()
    short_Choker_Necklace = Short_Choker_Necklace.objects.all()
    long_Necklace_Sets = Long_Necklace_Sets.objects.all()
    sliver_Earrings = Sliver_Earrings.objects.all()
    golden_Earrings = Golden_Earrings.objects.all()
    trending_design = Trending_design.objects.all()

    lis = []
    for i in range(0, 5):
        lis.append(i)

    dics = {'name': 'Company Name', 'lastname': 'JOGU', 'count': lis ,'product' : products,'semi_Bridal_Sets' : semi_Bridal_Sets,'short_Choker_Necklace' : short_Choker_Necklace,
            'long_Necklace_Sets': long_Necklace_Sets,'sliver_Earrings' : sliver_Earrings,'golden_Earrings' : golden_Earrings,'trending_design' : trending_design,'user': glob_user ,'username': glob_login_username}
    return render(request,'index.html',dics)


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
            text = {'username_alert':"yes"}
            return render(request, 'register_page.html',text)
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

        user1 = user(Username=username,Password=password,Email_Phone=email,First_name=first_name,Last_name=last_name)
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
        print(login_username)
        print(login_password)
        user1 = user.objects.all()
        print(user1)
        username = False
        password = False
         
        usernames = []
        for a in user1:
            usernames.append(a.Username)
        # print(usernames)

        passwords = []
        for a in user1:
            passwords.append(a.Password)
        # print(passwords)

        if login_username in usernames:
            username = True

        if login_password in passwords:
            password = True

        if username == True and password == True: 
            print('Successfully Loged IN')
            global glob_user, glob_login_username
            glob_user = True
            glob_login_username = login_username
            if glob_login_username == 'admin':
                return redirect('admin')
            return redirect('index')
        else:
            print('invalid credentials, please try again')
            return redirect('/shop')
    return HttpResponse('404 - error')


def handle_logout(request):
    logout(request)
    print('Logout Successfully')
    global glob_user,glob_login_username
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
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product':lis}
    return render(request, 'All Jewellery Sets.html',dic)


def Haram_Set(request):
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product': lis}
    return render(request, 'Haram Set.html',dic)


def Long_Necklace_Sets_fun(request):
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product': lis}
    return render(request, 'Long Necklace Sets.html',dic)


def Short_Necklace_fun(request):
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product': lis}
    return render(request, 'Short Necklace.html',dic)


def Pendant_Sets_fun(request):
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product': lis}
    return render(request, 'Pendant Sets.html',dic)


def Mangalsutra_Sets_fun(request):
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product': lis}
    return render(request, 'Mangalsutra Sets.html',dic)


def Earrings_fun(request):
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product': lis}
    return render(request, 'Earrings.html',dic)


def Maang_Tikkas_And_Daminis_fun(request):
    lis = []
    for i in range(0, 15):
        lis.append(i)
    dic = {'product': lis}
    return render(request, 'Maang Tikkas And Daminis.html',dic)


def product(request,title):
    title1 = title
    dic = {'Product_title':title}
    # return HttpResponse("<h1>{}</h1>".format(title))
    products = user.objects.filter(Email_Phone=str(title1))
    if products != "":
        for i in products:
            print(i.Password)
    else:
        print('Null')
    print(products)
    return render(request,'product.html',dic)

def admin(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email_phone = request.POST['emailphone']
        password = request.POST['password']
        username = request.POST['username']
        if not username.isalnum():
            # messages.error(request, 'Username Should Only Contain Letters And Numbers')
            user_name = {'user_name_without_symbol': "Error"}
            return render(request, 'admin_page.html', user_name)
        elif len(username) > 10:
            user_name = {'user_name':'Error'}
            return render(request,'admin_page.html',user_name)
        elif len(password) < 8:
            password = {'password':'Error'}
            return render(request,'admin_page.html',password)
        user1 = user(Username=username,Password=password,Email_Phone=email_phone,First_name=first_name,Last_name=last_name)
        user1.save()
    user2 = user.objects.all()
    dic = {'user':user2}
    return render(request,'admin_page.html',dic)


def admin_Add_Jewellerys(request):

    if request.method == 'POST':
        productname = request.POST['productname']
        Category = request.POST.get('Category','Please Select Category')
        Price = request.POST['Price']
        Discription = request.POST['Discription']
        prod_date = request.POST['prod_date']
        jewellery_image = request.FILES.get('image','Please Select Image')
        if jewellery_image == 'Please Select Image':
            image_error = {'image_error':'Please Select Image'}
            return render(request,'admin_Add_Jewellerys.html',image_error)            
        elif Category == 'Please Select Category':
            error = {'error':'Please Select Category'}
            return render(request,'admin_Add_Jewellerys.html',error)
        AllJewellerys1 = AllJewellerys(product_name=productname,category=Category,price=Price,desc=Discription,pub_date=prod_date,image=jewellery_image)
        AllJewellerys1.save()
    Jewellery = AllJewellerys.objects.all()
    # print(Jewellery)
    dic = {'Jewellery':Jewellery}
    return render(request,'admin_Add_Jewellerys.html',dic)

