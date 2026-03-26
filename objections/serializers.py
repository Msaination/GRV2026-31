from rest_framework import serializers
from .models import TownshipObjection, FarmObjection, TownshipObjectionAttachment, TownshipAuthRepAttachment


# This serializer is used to convert TownshipObjection model instances into JSON format and vice versa. It includes all fields of the TownshipObjection model.
class TownshipObjectionSerializer(serializers.ModelSerializer):
    township_objection_attachments = serializers.ListField(
        child=serializers.FileField(), write_only=True, required=False
    )
    auth_rep_attachments = serializers.ListField(
        child=serializers.FileField(), write_only=True, required=False
    )
   
    class Meta:
        model = TownshipObjection
        fields = [
            # foreign keys manual from vue
            'user',
            'township_property',

            # auto generated
            "id",
            "objection_number",

            # objectorDetails from and to Vue
            "objector_status",
            "auth_rep_attachments",
            "not_owner_description",
            "full_name",
            "id_number",
            "companyreg",
            "physical_address",
            "postal_address",
            "phone_home",
            "phone_work",
            "phone_mobile",
            "fax_number",
            "email",

            # categoryAndAdministrative from and to Vue
            "incorrect_valuation",
            "omitted_property",
            "incorrect_owner_name",
            "incorrect_category_rating",
            "incorrect_extent",
            "incorrect_physical_address",
            "incorrect_postal_address",
            "rates_query",

            # objectionDetails from and to Vue
            "property_description",
            "property_physical_address",
            "category",
            "extent",
            "market_value",
            "owner",
            "township_objection_attachments",

          
        ]

    def create(self, validated_data):
        objection_files = validated_data.pop("township_objection_attachments", [])
        auth_rep_files = validated_data.pop("auth_rep_attachments", [])

        objection = TownshipObjection.objects.create(**validated_data)

        for f in objection_files:
            TownshipObjectionAttachment.objects.create(
                township_objection=objection, file=f
            )
        for f in auth_rep_files:
            TownshipAuthRepAttachment.objects.create(
                auth_rep_attachment=objection, file=f
            )
        return objection


class TownshipObjectionAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TownshipObjectionAttachment
        fields = fields = ["id", "file"]


class TownshipAuthRepAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TownshipAuthRepAttachment
        fields = fields = ["id", "file"]




# This serializer is used to convert FarmObjection model instances into JSON format and vice versa. It includes all fields of the TownshipObjection model.
class FarmObjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmObjection
        fields = '__all__'
