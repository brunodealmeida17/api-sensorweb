from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import generics, status
import pandas as pd
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Fileupload
from rest_framework import viewsets
from apirestfile.serializers import FileUploadSerializer, ReadFileView


"""
Classe referente a upload do arquivo CSV, e pegando dados usando pandas e salvando no banco de dados as informações
como TS e dado e XID, conforme solitado no teste

"""
class UploadFileCSV(generics.CreateAPIView):   
    serializer_class = FileUploadSerializer  

    def get(self, request):
       return Response('Classe para upload de arquivos')

    def post(self, request, *args, **kwargs):        
        try:
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
        except:
            return Response({"status": "Falha na expectativa! procure o administrador"},
                        status.HTTP_417_EXPECTATION_FAILED)

                            

"""
Classe referente a leitura dos dados do banco de dados, mostrando dados como: TS e dado,XID e ID, conforme solitado no teste

"""
class ReadFileView(viewsets.ModelViewSet):
    queryset = Fileupload.objects.all()
    serializer_class = ReadFileView

    
    

    

    
    
    
    

