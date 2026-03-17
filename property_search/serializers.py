from rest_framework import serializers
from .models import FarmProperty
from users.models import User


#This serializer is used to convert FarmProperty model instances into JSON format and vice versa. It includes all fields of the FarmProperty model.
class FarmPropertySerializer(serializers.ModelSerializer):
    # owner_username = serializers.SerializerMethodField()
    class Meta:
        model = FarmProperty
        fields = ["id", "sg_code_21", "farm_name", "owner_status",
                  "regdiv", "category", "owner", "erf_no", "ptn",
                  "unit", "extent", "ha", "physical_address", "remarks"]
        # ['id', 'sg_code_21', 'farm_name']

    

    # def get_owner_username(self, obj): 
    #     try: 
    #         user = User.objects.get(id_number=obj.id_number) 
    #         return user.username 
    #     except User.DoesNotExist: 
    #         return None