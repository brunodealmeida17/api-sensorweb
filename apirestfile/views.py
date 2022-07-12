from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Fileupload
from rest_framework import viewsets
from apirestfile.serializers import FileUploadSerializer, ReadFileView



class UploadFileCSV(generics.CreateAPIView):
    queryset = Fileupload.objects.all()
    serializer_class = FileUploadSerializer
    
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file'] 
        xid = serializer.validated_data['xid']       
        reader = pd.read_csv(file)
        monitoramento_list = []
        for _, row in reader.iterrows():
            new_file = Fileupload(
                       xid=xid,
                       ts= row["ts"],
                       dado= row['dado'],                       
                       )
                       
            new_file.save()
        Fileupload.objects.bulk_create(monitoramento_list)

        return Response("upload Feito")


class ReadFileView(viewsets.ModelViewSet):
    queryset = Fileupload.objects.all()
    serializer_class = ReadFileView

    
    

    

    
    
    
    

