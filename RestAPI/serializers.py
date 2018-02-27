from .models import Trade, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')

class TradeSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Trade
        fields = '__all__'

    def validate(self):
        return True

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = TradeSerializer.create(UserSerializer(), validated_data=user_data)
        trade, created = Trade.objects.update_or_create(user=user,
                id=validated_data.pop('id'),
                type=validated_data.pop('type'),
                stock_price= validated_data.pop('stock_price'),
                stock_quantity=validated_data.pop('stock_quantity'),
                stock_symbol=validated_data.pop('stock_symbol'))
        return trade