from rest_framework import serializers
from .models import Fileupload

XID_CHOICES = (
    ("ID0001_TEMP", "ARMAZEM" ),
    ("ID0002_TEMP", "HEPARINA"),
    ("ID0003_TEMP", "DIVISAO"),
)

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    xid = serializers.ChoiceField(choices=XID_CHOICES)
    
    

class ReadFileView(serializers.ModelSerializer):  
        
    class Meta:        
        model = Fileupload
        file = serializers.FileField()
        fields = ('id', 'xid', 'ts', 'dado')