from rest_framework.serializers import ModelSerializer
from .models import Advocate, Company


class CompanySerializer(ModelSerializer):
    # employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = ['name','logo']

class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields =[
            'name',
            'username',
            'profile_pic',
            'bio',
            'twitter',
            'company'
        ]


class AdvocateDetailSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = [
            'name',
            'username',
            'profile_pic',
            'bio',
            'twitter',
            'company',

        ]




