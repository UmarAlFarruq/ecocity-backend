from django.shortcuts import render
from rest_framework import generics
from . serializer import *
from rest_framework import views
from rest_framework import permissions,status
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from django.contrib.auth.models import User




class LoginView(views.APIView):

    

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)



class IndexView(generics.ListAPIView):

    queryset = Posts.objects.all().order_by('-dataCreated')
    serializer_class = Postserilizer
    

class SignUpView(generics.CreateAPIView):


    queryset = None
    serializer_class = SignUpSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)   

        if serializer.is_valid():

            serializer.save()

            return Response({'Created':True},status=201)
        
        else:

            return Response({'Created':False},status=400)


class AddPostView(generics.CreateAPIView):

    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):

        title = request.POST['title']
        description = request.POST['description']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        image = request.FILES['image']
        post = Posts.objects.create(
            title=title,
            description=description,
            longitude=longitude,
            latitude=latitude,
            image=image,
            user=request.user
            )
        return Response({'Created':True})

class ProfileReadView(generics.ListAPIView):

    queryset = Posts.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        data = []
        postuser = []
        posts = Posts.objects.filter(user=request.user)

        profile = Profile.objects.get(user_id=request.user.id)

        for i in posts:

            postuser.append({
                "title":i.title,
                "description":i.description,
                
                })

        indexslash = ((request.build_absolute_uri()).find('/',7))
        url = request.build_absolute_uri()[:indexslash]
        urlImg = url+"/media/"+str(profile.photo)
        data.append({
            "first_name":profile.name,
            "last_name":profile.surname,
            "photo":urlImg,
            "post":postuser
            })


        


        return Response(data)

class ProfileEditView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileEditSerializer

    def get_queryset(self):

        profil = Profile.objects.get(user_id=self.request.user.id)

        return profil
    def put(self,request):

        profile = self.get_queryset()
        
        serializer = self.serializer_class(profile,data=request.data)



        return Response("Ok")





    







        







