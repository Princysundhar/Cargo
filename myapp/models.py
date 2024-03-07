from django.db import models


# Create your models here.


class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=20)

class company(models.Model):
    company_name =models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # contact_information = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)
    COMPANY = models.ForeignKey(company,default=1,on_delete=models.CASCADE)

class fuel_wage(models.Model):
    fuel_type = models.CharField(max_length=100)
    wage_per_km = models.CharField(max_length=100)
    fuel_price = models.CharField(max_length=100)

class complaint(models.Model):
    USER= models.ForeignKey(user,default=1,on_delete=models.CASCADE,related_name="u")
    driver =models.ForeignKey(user,default=1,on_delete=models.CASCADE,related_name="d")
    complaint = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)


class feedback(models.Model):
    USER = models.ForeignKey(user,default=1,on_delete=models.CASCADE,related_name="USER")
    driver = models.ForeignKey(user,default=2,on_delete=models.CASCADE,related_name="driver")
    feedback = models.CharField(max_length=200)
    feedback_date = models.CharField(max_length=100)

class route(models.Model):
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    no_of_requests = models.CharField(max_length=100)


class user_request(models.Model):
    USER = models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    ROUTE = models.ForeignKey(route,default=1,on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

class transaction(models.Model):
    USERREQUEST = models.ForeignKey(user_request,default=1,on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user,default=1,on_delete=models.CASCADE)

