from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import generics, status
import pandas as pd
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Fileupload
from rest_framework import viewsets
from apirestfile.serializers import FileUploadSerializer, ReadFileView



class UploadFileCSV(generics.CreateAPIView):   
    serializer_class = FileUploadSerializer  

    def get(self, request):
       return Response('Classe para upload de arquivos')

    def post(self, request, *args, **kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file'] 
        xid = serializer.validated_data['xid']       
        reader = pd.read_csv(file)        
        for _, row in reader.iterrows():
            new_file = Fileupload(
                       xid=xid,
                       ts= row["ts"],
                       dado= row['dado'],                       
                       )
                       
            new_file.save()    
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
                            


class ReadFileView(viewsets.ModelViewSet):
    queryset = Fileupload.objects.all()
    serializer_class = ReadFileView

    
    

    

    
    
    
    

