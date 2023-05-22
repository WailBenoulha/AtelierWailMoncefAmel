from rest_framework import serializers
from core import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','password', 'email', 'name', 'lastname', 'phonenumber', 'national_card_number', 'address', 'role')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','password', 'email', 'name', 'lastname', 'phonenumber', 'national_card_number', 'address')

    def create(self, validated_data):
        user = models.User.objects.create_user(
            role='ADMIN',
            password=validated_data['password'],
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            phonenumber=validated_data['phonenumber'],
            national_card_number=validated_data['national_card_number'],
            address=validated_data['address']
        )

        return user


class PrincipalmanagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','password', 'email', 'name', 'lastname', 'phonenumber', 'national_card_number', 'address')

    def create(self, validated_data):
        user = models.User.objects.create_user(
            role='PRINCIPALMANAGER',
            password=validated_data['password'],
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            phonenumber=validated_data['phonenumber'],
            national_card_number=validated_data['national_card_number'],
            address=validated_data['address']
        )

        return user

class AllocationmanagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','password', 'email', 'name', 'lastname', 'phonenumber', 'national_card_number', 'address')

    def create(self, validated_data):
        user = models.User.objects.create_user(
            role='ALLOCATIONMANAGER',
            password=validated_data['password'],
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            phonenumber=validated_data['phonenumber'],
            national_card_number=validated_data['national_card_number'],
            address=validated_data['address']
        )

        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','password', 'email', 'name', 'lastname', 'phonenumber', 'national_card_number', 'address')

    def create(self, validated_data):
        user = models.User.objects.create_user(
            role='STUDENT',
            password=validated_data['password'],
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            phonenumber=validated_data['phonenumber'],
            national_card_number=validated_data['national_card_number'],
            address=validated_data['address']
        )

        return user

class ResearcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','password', 'email', 'name', 'lastname', 'phonenumber', 'national_card_number', 'address')

    def create(self, validated_data):
        user = models.User.objects.create_user(
            role='RESEARCHER',
            password=validated_data['password'],
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            phonenumber=validated_data['phonenumber'],
            national_card_number=validated_data['national_card_number'],
            address=validated_data['address']
        )

        return user


class Categorie_EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categorie_Equipement
        fields = ('id', 'name', 'discription', 'created_on')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('id', 'name', 'discription','type', 'created_on')

# hna lazmni nzid les attributes fl fields
class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipement
        fields = ('id', 'created_by', 'name', 'brand', 'model', 'categorie', 'reference', 'num_serie', 'condition', 'facture_number', 'date_purchase', 'Location', 'date_assignment','discription', 'image', 'is_reserved')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stock
        fields = ('id', 'created_by', 'name', 'brand', 'model', 'categorie', 'condition', 'facture_number', 'date_purchase', 'Location', 'date_assignment', 'quantite','discription', 'image')

class AffectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Affectation
        fields = ('id', 'reference','Location', 'opperation', 'date_assignment')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventory
        fields = ('id', 'created_by', 'name', 'brand', 'model', 'categorie', 'reference', 'num_serie', 'condition', 'facture_number', 'date_purchase', 'Location', 'date_assignment','discription', 'image', 'is_reserved')


class NotificaionStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotificationStudent
        fields = ('id', 'message', 'reference', 'send_by')


class NotificationManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotificationManager
        fields =('id', 'message','reciever')


class AllocateEquipementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AllocateEquipements
        fields = ('id', 'Reserved_by', 'reference', 'start_date', 'finish_date', 'purpose', 'Message','status')

class AcceptAllocationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AcceptAllocationRequest
        fields = ('id', 'request', 'accept')