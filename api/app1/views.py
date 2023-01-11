from django.http import HttpResponse
from firebase import Firebase
import json


config = {
    "apiKey": "AIzaSyDs3f_7dEjYttSIaS_gyA96Iv6Kyw6d31w",
    "authDomain": "demodb-38d29.firebaseapp.com",
    "projectId": "demodb-38d29",
    "storageBucket": "demodb-38d29.appspot.com",
    "serviceAccount" : "C:\\Data\\5th semester\\AI Lab\\Project\\Project\\service-account-file.json",
    "messagingSenderId": "322915066206",
    "messagingSenderId": "322915066206",
    "appId": "1:322915066206:web:656ceedbf352d925db6fcf",
    "measurementId": "G-3BRJQ6K3ZM",
    "databaseURL": "https://demodb-38d29-default-rtdb.firebaseio.com/",
}

firebase = Firebase(config)
database = firebase.database()


def home(request):
    brands = database.child('Brands').get().val()
    users = database.child('Users').get().val()
    crousal = database.child('Crousal').get().val()
    brandsJson = json.dumps({'Brands' : brands,'Users' : users, 'Crousal': crousal})
    return HttpResponse(brandsJson)