from rest_framework import serializers
from .models import TownshipProperty
from users.models import User


#This serializer is used to convert TownshipProperty model instances into JSON format and vice versa. It includes all fields of the TownshipProperty model.
class TownshipPropertySerializer(serializers.ModelSerializer):
    # owner_username = serializers.SerializerMethodField()
    class Meta:
        model = TownshipProperty
        fields = '__all__'
        # ["id", "sg_code_21", "township", "erf_no", "category", "township_name_ext"]
        # '__all__',

    

    # def get_owner_username(self, obj): 
    #     try: 
    #         user = User.objects.get(id_number=obj.id_number) 
    #         return user.username 
    #     except User.DoesNotExist: 
    #         return None