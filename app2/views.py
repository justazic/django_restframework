from django.shortcuts import render
from app.serializers import CarsSerializer
from app.models import Cars
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# class ListView(APIView):
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
    
        
 
# class DetailView(APIView):
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
        
# class CreateView(APIView):
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
    
# class UpdateView(APIView):
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


# class DeleteView(APIView):
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

class CarList(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Cars.objects.all().order_by('id')
        
        search = request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(make__icontains=search) | Q(model__icontains=search)
            )

        page_num = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)
        
        paginator = Paginator(queryset, limit)

        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        serializer = CarsSerializer(page_obj.object_list, many=True)

        data = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': page_obj.number,
            'next': page_obj.has_next(),
            'previous': page_obj.has_previous(),
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    
class CarUpdate(UpdateAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    lookup_field = 'pk'
    
    def update(self, request, *args, **kwargs):
        isinstanceance = self.get_object()
        serializer = self.get_serializer(instance=isinstanceance, data=request.data, partial= True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            "message":"Car updated successfully",
            "data":serializer.data
        },
        status=status.HTTP_200_OK
        )
        
        
class SearchView(APIView):
    def get(self, request):
        search = request.query_params.get('q', '')
        
        if not search:
            raise ValueError("Qidirish parametri kiritilmadi")
        
        queryset = Cars.objects.filter( Q(make__icontains=search) |  Q(model__icontains=search))
        if not queryset.exists():
            raise ValueError("Malumot topilmadi")
        serializer = CarsSerializer(queryset, many=True)
        return Response(
            {
                "message":"Malumot topildi",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )