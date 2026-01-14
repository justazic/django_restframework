# from django.shortcuts import render
# from .serializers import CarsSerializer
# from .models import Cars
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class CarView(APIView):
#     def get(self, request):
#         cars = Cars.objects.all()
#         serializer = CarsSerializer(cars, many=True)
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'Products',
#             'count': len(cars),
#             'products': serializer.data
#         }
#         return Response(data)
    
#     def post(self, request):
#         serializer = CarsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_201_CREATED,
#                 'message': 'Product yaratildi',
#                 'product': serializer.data
#             }
#             return Response(data)
        
#         data = {
#                 'status': status.HTTP_400_BAD_REQUEST,
#                 'message': 'Product yaratilmadi',
#                 'eror': serializer.errors
#             }
#         return Response(data)
    
    
# class CarUpdateDeleteDetail(APIView):
#     def get(self, request, pk):
#         car = Cars.objects.filter(pk=pk).first()
#         serializer = CarsSerializer(car)
#         if car:
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Car detail',
#                 'product': serializer.data
#             }
#             return Response(data)
#         return Response({
#             "success": False, 
#             'message':'bunday maxsulot mavjud emas',
#             'status': status.HTTP_204_NO_CONTENT
#             })
        
        
#     def put(self, request, pk):
#         car = Cars.objects.filter(pk=pk).first()
#         serializer = CarsSerializer(car, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Product ozgartirildi',
#                 'product': serializer.data
#             }
#             return Response(data)
        
#         data = {
#                 'status': status.HTTP_400_BAD_REQUEST,
#                 'message': 'Product ozgartirilmadi',
#                 'eror': serializer.errors
#             }
#         return Response(data)
    
#     def patch(self, request, pk):
#         car = Cars.objects.filter(pk=pk).first()
#         if not car:
#             data = {
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'message': 'Product mavjud emas',
#                 }
#             return Response(data)
                            
#         serializer = CarsSerializer(instance=car, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Product ozgartirildi',
#                 'product': serializer.data
#             }
#             return Response(data)
        
#     def delete(self, request, pk):
#         car = Cars.objects.filter(pk=pk).first()
#         serializer = CarsSerializer(car)
#         if car:
#             car.delete()
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Car deleted',
#                 'product': serializer.data
#             }
#             return Response(data)
        