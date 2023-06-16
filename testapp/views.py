from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from.models import Phone

# @api_view--->
# Django me @api_view decorator ek third-party package, yani ki Django REST framework (DRF), ke andar upalabdh hota hai.
# DRF Django me APIs banane ke liye commonly istemal kiya jaata hai.

# @api_view decorator, ek function-based view ko ek API view mein badal deta hai. Isse, aapko kisi bhi HTTP request method 
# (GET, POST, PUT, DELETE, etc.) ko handle karne ke liye alag-alag if-else ya switch-case logic likhne ki zaroorat nahi hoti.
# Iske bajaye, aap ek function-based view mein direct @api_view decorator ka upyog kar sakte hai.

@api_view(['POST'])
def send_otp(request):
    data =request.data
    print("data is >.....",data)
    
    if data.get('phone_number') is None:
        return Response({
            'status' : 400,
            'message' : 'key phone_number is required'
        })
        
    # if data.get('email') is None:
    #     return Response({
    #         'status' : 400,
    #         'message' : ' key password is required'
    #     })
        
    user = Phone.objects.create(
        phone_number = data.get('phone_number'),
        otp = send_otp_to_phone(data.get('phone_number'))
    )
    # user.set_email = data.get('set_email')
    user.save()
    
    return Response({
        'status' : 200, 'message' : 'otp sent'
    })
    
    
    
    
    
@api_view(['POST'])
def verify_otp(request):
    data =request.data
    print(data)
    if data.get('phone_number') is None:
        print("phone is none ///")
        return Response({
            'status' : 400,
            'message' : 'key phone_number is required'
        })
        
    if data.get('otp') is None:
        print("data is otp////")
        return Response({
            'status' : 400,
            'message' : ' key otp is required'
        })
        
    try:
        user_obj = Phone.objects.get(phone_number=data.get('phone_number'))
        print("user_object//////",user_obj.otp,"and opt....0")
        if user_obj.otp == data.get('otp'):
            return Response({
            'status' : 200,
            'message' : 'otp matched'
        })
    
        
    except Exception as e: 
            print("error in code")
        # return Response({
        #     'status' : 200,
        #     'message' : 'success'
        # })
        #if user_obj.otp == data.get('otp'):
            return Response({
            'status' : 400,
            'message' : 'invalid phone'
        })
    
        
    
    # if user_obj.otp == data.get('otp'):
    #     return Response({
    #         'status' : 200,
    #         'message' : 'otp matched'
    #     })
        
    return Response({
            'status' : 400,
            'message' : ' invalid otp'
        })
