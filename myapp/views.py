import datetime
import random

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def log(request):
    return render(request, 'login_index.html')


def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username, password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"
        if data.usertype == "admin":
            return HttpResponse("<script>alert('Login success');window.location='/admin_home'</script>")
        elif data.usertype == 'company':
            return HttpResponse("<script>alert('Login success');window.location='/company_home'</script>")
        else:
            return HttpResponse("<script>alert('Wait for authentication');window.location='/'</script>")



    else:
        return HttpResponse("<script>alert('invalid');window.location='/'</script>")


def admin_home(request):
    return render(request, 'admin/admin_index.html')


# CHARGE AMOUNT MANAGEMENT

def add_fuel(request):
    return render(request, 'admin/fuel_wage.html')


def add_fuel_post(request):
    Fuel_type = request.POST['textfield']
    Wage_per_km = request.POST['textfield2']
    Current_fuel_price = request.POST['textfield3']
    data = fuel_wage.objects.filter(fuel_type=Fuel_type, wage_per_km=Wage_per_km, fuel_price=Current_fuel_price)
    if data.exists():
        return HttpResponse("<script>alert('Already Exists');window.location='/add_fuel'</script>")
    else:
        obj = fuel_wage()
        obj.fuel_type = Fuel_type
        obj.wage_per_km = Wage_per_km
        obj.fuel_price = Current_fuel_price
        obj.save()
        return HttpResponse("<script>alert('Successfully Added');window.location='/add_fuel'</script>")


def view_fuel(request):
    data = fuel_wage.objects.all()
    return render(request, 'admin/view_fuel.html', {'data': data})


def fuel_update(request, id):
    data = fuel_wage.objects.get(id=id)
    return render(request, 'admin/fuelwageupdate.html', {'data': data})


def fuel_update_post(request, id):
    Fuel_type = request.POST['textfield']
    Wage_per_km = request.POST['textfield2']
    Current_fuel_price = request.POST['textfield3']
    fuel_wage.objects.filter(id=id).update(fuel_type=Fuel_type, wage_per_km=Wage_per_km, fuel_price=Current_fuel_price)
    return HttpResponse("<script>alert('Successfully Updated');window.location='/view_fuel#aaa'</script>")


def fuel_delete(request, id):
    fuel_wage.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Successfully Deleted');window.location='/view_fuel#aaa'</script>")


def view_complaint(request):
    data = complaint.objects.all()
    return render(request, 'admin/view_complaint.html', {'data': data})


def send_reply(request, id):
    return render(request, 'admin/send_reply.html', {'id': id})


def send_reply_post(request, id):
    Reply = request.POST['textfield']
    dt = datetime.datetime.now().strftime('%Y-%M-%D')
    complaint.objects.filter(id=id).update(reply=Reply, reply_date=dt)
    return HttpResponse("<script>alert('Successfully Replied');window.location='/view_complaint'</script>")


def view_feedback(request):
    data = feedback.objects.all()
    return render(request, 'admin/View_fdbck.html', {'data': data})


def view_user(request):
    data = user.objects.all()
    return render(request, 'admin/View_user.html', {'data': data})


def block_user(request, id):
    login.objects.filter(id=id).update(usertype="blocked")
    return redirect('/view_user')


def unblock_user(request, id):
    login.objects.filter(id=id).update(usertype="user")
    return redirect('/view_user')


# COMPANY APPROVE REJECT

def view_company(request):
    data = company.objects.filter(LOGIN__usertype="pending")
    return render(request, 'admin/view_company.html', {'data': data})


def approve_company(request, id):
    login.objects.filter(id=id).update(usertype="company")
    return HttpResponse("<script>alert('Approved');window.location='/view_company#aaa'</script>")


def reject_company(request, id):
    login.objects.filter(id=id).update(usertype="reject")
    return HttpResponse("<script>alert('Rejected');window.location='/view_company#aaa'</script>")


def view_approved_company(request):
    data = company.objects.filter(LOGIN__usertype="company")
    return render(request, 'admin/view_approved_company.html', {'data': data})


def user_req(request):
    data = user_request.objects.all()
    return render(request, 'admin/user_request_status.html', {'data': data})


def view_transaction_status(request, id):
    data = transaction.objects.filter(USERREQUEST=id)
    return render(request, 'admin/view_transaction_status.html', {'data': data})


def logout(request):
    request.session['lg'] = ""
    return redirect('/')



# .................................................................. COMPANY MODULE

def company_home(request):
    return render(request, "Company/company_index.html")


def company_register(request):
    return render(request, "Company/Register.html")


def company_register_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    latitude = request.POST['textfield8']
    longitude = request.POST['textfield9']
    email = request.POST['textfield5']
    contact = request.POST['textfield6']
    password = random.randint(0000, 9999)
    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already registered');window.location='/company_register'</script>")
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.usertype = 'pending'
        log_obj.save()

        obj = company()
        obj.company_name = name
        obj.place = place
        obj.latitude = latitude
        obj.longitude = longitude
        obj.email = email
        obj.phone = contact
        obj.LOGIN = log_obj
        obj.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location='/company_register'</script>")


def view_profile(request):
    data = company.objects.get(LOGIN=request.session['lid'])
    return render(request, "Company/view_profile.html", {"data": data})


# USER MANAGEMENT

def add_user(request):
    return render(request, "Company/add_user.html")


def add_user_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    contact = request.POST['textfield3']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\ICAR\myapp\static\photo\\" + dt + '.jpg', photo)
    path = '/static/photo/' + dt + '.jpg'
    data = user.objects.filter(name=name, email=email, phone=contact)
    if data.exists():
        return HttpResponse("<script>alert('User already exist');window.location='/add_user'</script>")
    else:

        log_obj = login()
        log_obj.username = email
        log_obj.password = random.randint(0000, 9999)
        log_obj.usertype = 'user'
        log_obj.save()
        obj = user()
        obj.name = name
        obj.email = email
        obj.phone = contact
        obj.photo = path
        obj.COMPANY = company.objects.get(LOGIN=request.session['lid'])
        obj.LOGIN = log_obj
        obj.save()
        return HttpResponse("<script>alert('User added Successfully');window.location='/add_user'</script>")


def view_users(request):
    data = user.objects.filter(COMPANY__LOGIN=request.session['lid'])
    return render(request, "Company/view_user.html", {"data": data})


def update_user(request, id):
    data = user.objects.get(id=id)
    return render(request, "Company/update_user.html", {"data": data, "id": id})


def update_user_post(request, id):
    # name = request.POST['textfield']
    # email = request.POST['textfield2']
    # contact = request.POST['textfield3']
    # if 'fileField' is request.FILES:
    #     photo = request.POST['fileField']
    #     fs = FileSystemStorage()
    #     dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    #     fs.save(r"C:\Users\DELL\PycharmProjects\ICAR\myapp\static\photo\\" + dt + '.jpg', photo)
    #     path = '/static/photo/' + dt + '.jpg'
    #     user.objects.filter(id=id).update(photo=path)
    #     return HttpResponse("<script>alert('User updated Successfully');window.location='/view_users#aaa'</script>")
    # else:
    #     user.objects.filter(id=id).update(name=name, email=email, phone=contact)
    #     return HttpResponse("<script>alert('User updated Successfully');window.location='/view_users#aaa'</script>")



    try:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        contact = request.POST['textfield3']
        photo = request.POST['fileField']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\ICAR\myapp\static\photo\\" + dt + '.jpg', photo)
        path = '/static/photo/' + dt + '.jpg'
        user.objects.filter(id=id).update(name=name, email=email, phone=contact,photo=path)
        return HttpResponse("<script>alert('User updated Successfully');window.location='/view_users#aaa'</script>")
    except Exception as e:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        contact = request.POST['textfield3']
        user.objects.filter(id=id).update(name=name, email=email, phone=contact)
        return HttpResponse("<script>alert('User updated Successfully');window.location='/view_users#aaa'</script>")



def delete_user(request, id):
    user.objects.get(id=id).delete()
    return HttpResponse("<script>alert('User deleted Successfully');window.location='/view_users'</script>")


def change_password(request):
    return render(request, "Company/change_password.html")


def change_password_post(request):
    old_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    data = login.objects.filter(id=request.session['lid'], password=old_password)
    if data.exists():
        if new_password == confirm_password:
            if login.objects.filter(password=new_password).exists():
                return HttpResponse("<script>alert('Already exists');window.location='/change_password#aaa'</script>")
            else:
                login.objects.filter(id=request.session['lid']).update(password=confirm_password)
                return HttpResponse("<script>alert('Password updated');window.location='/change_password#aaa'</script>")
        else:
            return HttpResponse("<script>alert('Password mismatch');window.location='/change_password#aaa'</script>")
    else:
        return HttpResponse("<script>alert('Error');window.location='/change_password#aaa'</script>")


# .......................................................................................... USER MODULE

def android_login(request):
    username = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username, password=password)
    if data.exists():
        lid = data[0].id
        type = data[0].usertype
        res = user.objects.get(LOGIN=lid)
        name = res.name
        print(name)
        email = res.email
        photo = res.photo
        return JsonResponse({"status": "ok", "lid": lid, "type": type,'name':name,'email':email,'photo':photo})
    else:
        return JsonResponse({"status": None})


def android_view_profile(request):
    lid = request.POST['lid']
    data = user.objects.get(LOGIN=lid)
    return JsonResponse({"status": "ok", "name": data.name, "email": data.email, "phone_no": data.phone,
                         "company": data.COMPANY.company_name, "photo": data.photo})


def android_send_feedback(request):
    feedbacks = request.POST['feedback']
    req_id = request.POST['req_id']
    print(req_id)
    req=user_request.objects.get(id=req_id)
    lid = request.POST['lid']
    obj = feedback()
    obj.feedback = feedbacks
    obj.feedback_date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.driver =req.ROUTE.USER
    obj.save()
    return JsonResponse({"status": "ok"})


def android_view_route(request):
    lid = request.POST['lid']
    res = route.objects.filter(USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "rid": i.id,
                "latitude": i.latitude,
                "longitude": i.longitude,
                "from": i.From,
                "to": i.To,
                "name": i.USER.name,
                "email": i.USER.email,
                "date": i.date,
                "no_of_requests": i.no_of_requests
            }
        )
    return JsonResponse({"status": "ok", "data": ar})


def android_add_route(request):
    lid = request.POST['lid']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    From = request.POST['from']
    to = request.POST['to']
    no_of_requests = request.POST['no_of_requests']
    date = request.POST['date']
    obj = route()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.latitude = latitude
    obj.longitude = longitude
    obj.From = From
    obj.To = to
    obj.date = date
    obj.no_of_requests = no_of_requests
    obj.save()
    return JsonResponse({"status": "ok"})


def android_delete_route(request):
    rid = request.POST['rid']
    route.objects.get(id=rid).delete()
    return JsonResponse({"status": "ok"})


# note: UPDATE HAS TO FUNCTIONS

def android_update_route(request):
    lid = request.POST['lid']
    data = route.objects.get(id=lid)
    return JsonResponse({"status": "ok", "latitude": data.latitude, "longitude": data.longitude,
                         "from": data.From, "to": data.To, "date": data.date, "no_of_requests": data.no_of_requests})


def android_update_routes(request):
    lid = request.POST['lid']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    From = request.POST['from']
    to = request.POST['to']
    date = request.POST['date']
    no_of_requests = request.POST['no_of_requests']
    route.objects.filter(id=lid).update(latitude=latitude, longitude=longitude,
                                        From=From, To=to, date=date, no_of_requests=no_of_requests)

    return JsonResponse({"status": "ok"})


def android_view_user_request(request):
    # rid = request.POST['rid']
    lid = request.POST['lid']
    res = user_request.objects.filter(USER__LOGIN=lid, status='pending')
    ar = []
    for i in res:
        ar.append(
            {
                "req_id": i.id,
                "date": i.date,
                "status": i.status,
                "latitude": i.latitude,
                "longitude": i.longitude,
                "no_of_request": i.ROUTE.no_of_requests
            }
        )
    return JsonResponse({"status": "ok", "data": ar})


def android_accept_request(request):
    req_id = request.POST['req_id']
    amount = request.POST['amount']
    user_request.objects.filter(id=req_id).update(status='accept',amount=amount)
    return JsonResponse({"status": "ok"})


def android_reject_request(request):
    req_id = request.POST['req_id']
    user_request.objects.filter(id=req_id).update(status='reject')
    return JsonResponse({"status": "ok"})

def android_view_reply(request):
    lid = request.POST['lid']
    res = complaint.objects.filter(USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "cid": i.id,
                "complaint": i.complaint,
                "date": i.complaint_date,
                "reply": i.reply,
                "reply_date": i.reply_date,
                "userinfo":i.USER.name
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def android_send_complaint(request):
    lid = request.POST['lid']
    req_id = request.POST['req_id']
    req = user_request.objects.get(id=req_id)
    complaints = request.POST['complaint']
    obj = complaint()
    obj.complaint = complaints
    obj.complaint_date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.reply = 'pending'
    obj.reply_date = 'pending'
    obj.USER = user.objects.get(LOGIN=lid)
    obj.driver = req.ROUTE.USER
    obj.save()

    return JsonResponse({"status":"ok"})

def android_view_uploaded_request(request):
    lid = request.POST['lid']
    res = route.objects.filter(~Q(USER__LOGIN=lid))
    ar = []
    for i in res:
        ar.append(
            {
                "route_id":i.id,
                "latitude":i.latitude,
                "longitude":i.longitude,
                "From":i.From,
                "To":i.To,
                "date":i.date,
                "no_of_request":i.no_of_requests
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_request_status(request):
    lid = request.POST['lid']
    res = user_request.objects.filter(USER__LOGIN=lid,status='accept')
    ar = []
    for i in res:
        ar.append(
            {
                "req_id":i.id,
                "date":i.date,
                "status":i.status,
                "route_info":i.ROUTE.From,
                "latitude":i.latitude,
                "longitude":i.longitude,
                "amount":i.amount
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_send_request(request):
    lid = request.POST['lid']
    route_id = request.POST['route_id']
    date = request.POST['date']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    obj = user_request()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.date = date
    obj.status = 'pending'
    obj.ROUTE_id = route_id
    obj.latitude = latitude
    obj.longitude = longitude
    obj.amount =0
    obj.save()
    return JsonResponse({"status":"ok"})

def android_offline_payment(request):
    lid = request.POST['lid']
    # mode = request.POST['mode']
    amount = request.POST['amount']
    req_id = request.POST['req_id']
    obj = transaction()
    obj.payment_status = 'offline'
    obj.amount = amount
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.USERREQUEST = user_request.objects.get(id=req_id)
    obj.save()

    return JsonResponse({"status": "ok"})


def android_online_payment(request):
    lid = request.POST['lid']
    # mode = request.POST['mode']
    amount = request.POST['amount']
    req_id = request.POST['req_id']
    obj = transaction()
    obj.payment_status = 'online'
    obj.amount = amount
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.USERREQUEST = user_request.objects.get(id=req_id)
    obj.save()
    user_request.objects.filter(id=req_id).update(status='paid')


    return JsonResponse({"status": "ok"})



