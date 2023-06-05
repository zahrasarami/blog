from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BlogSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog
from django.db.models import Q


class BlogView(APIView) :
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    
    def get(self , request):
        try:
            blogs = Blog.objects.filter(user=request.user)
            if  request.GET.get('search'):
                search = request.GET.get('search')
                blogs = blogs.filter(Q(title__icontains= search) | Q(blog_text__icontains=search))
            serializer = BlogSerializer(blogs , many=True)
            return Response({
                'data' : serializer.data ,
                'message' : 'blogs fetched seccesfully' ,
            } , status= status.HTTP_201_CREATED)

        except Exception as e :
            print(e)
            return Response({
                    'data' : {} ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )



    def post(self , request):
        try:
            data = request.data  
            data['user'] = request.user.id
            serializer = BlogSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data' : serializer.errors ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )

            serializer.save()
            return Response({
                'data' : serializer.data ,
                'message' : 'blog is created seccesfully' ,
            } , status= status.HTTP_201_CREATED)

        except Exception as e :
            print(e)
            return Response({
                    'data' : {} ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )


    def patch(self , request) :
        try:
            data = request.data  
            blog = Blog.objects.filter(uid= data.get('uid'))

            if not blog.exists():
                return Response({
                    'data' : {} ,
                    'message' : 'invalid blog uid' ,
                } , status = status.HTTP_400_BAD_REQUEST )


            print(1)
            if request.user != blog[0].user :
                return Response({
                    'data' : {} ,
                    'message' : 'you are nor authorize to do this' ,
                } , status = status.HTTP_400_BAD_REQUEST )
            print(2)
            serializer = BlogSerializer(blog[0], data=data ,  partial= True)
            
            if not serializer.is_valid():
                return Response({
                    'data' : serializer.errors ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )
            serializer.save()
            
            return Response({
                'data' : serializer.data ,
                'message' : 'blog is updated seccesfully' ,
            } , status= status.HTTP_201_CREATED)
        
        
        except Exception as e :
            print(e)
            return Response({
                    'data' : {} ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )
            
            
            
