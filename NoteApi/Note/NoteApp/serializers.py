from .models import KeepNote
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import bleach

class NoteSerializer(serializers.ModelSerializer):
    """
    To serialize all object from the models into json format from the database and ensure validation
    """
    
    def validate(self, attrs):
        """This method is
        To avoid sql injection and javascript injection
        Ensure validation and data cleaning    
        """
        attrs['title'] = bleach.clean(attrs['title'])
        attrs['content'] = bleach.clean(attrs['content'])
        return super().validate(attrs)
    
    class Meta:
        model = KeepNote
        fields = ['id', 'title', 'content']
        extra_kwargs = {
     'title': {
     'validators': [
             UniqueValidator(
                 queryset=KeepNote.objects.all()
             )
         ]
             }
         }