from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer , LoginSerializer
from rest_framework import status


class Registerview(APIView) :
    def post(self , request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            
            if not  serializer.is_valid():
                return Response({
                    'data' : serializer.errors ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )
            
            serializer.save()

            return Response({
                'data' : {} ,
                'message' : 'your account is created seccesfully' ,
            } , status= status.HTTP_201_CREATED)


            
        except Exception as e :
            print(e)
            return Response({
                    'data' : {} ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )


class Loginview(APIView) :

    def post(self , request) :
        try:

            data = request.data  
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid() :
                return Response({
                    'data' : serializer.errors ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )

            respones = serializer.get_jwt_token(serializer.data)
            return Response( respones , status= status.HTTP_201_CREATED )


            
        except Exception as e :
            print(e)
            return Response({
                    'data' : {} ,
                    'message' : 'something went wrong' ,
                } , status = status.HTTP_400_BAD_REQUEST )
