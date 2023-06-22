from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BloodDonor
from .serializers import BloodDonorSerializer

@api_view(['GET','POST'])
def blood_donor(request):
    if request.method == 'GET':
        donors = BloodDonor.objects.all().order_by('-id')
        serializer=BloodDonorSerializer(donors,many=True)
        return Response(serializer.data)
    


    if request.method == 'POST':
        serializer= BloodDonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.data)
        

@api_view(['GET','PUT','DELETE'])
def blood_donor_detail(request,id):
    try:
        blood_donor = BloodDonor.objects.get(id=id)
    except BloodDonor.DoeNotExit as e:
        return Response({'data':"Donor doesn't exit"},status=404)
    if request.method=='GET':
        serializer=BloodDonorSerializer(blood_donor)
        return Response(data=serializer.data)
    
    elif request.method=='PUT':
        serializer=BloodDonorSerializer(blood_donor, data=request.data)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(data=serializer.data)
    elif request.method=='DELETE':
        blood_donor.delete()
        return Response(data=None,status=204)
    else :
        return Response(data={'detail':'NOT allowed'},status=400)
    



        








@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})