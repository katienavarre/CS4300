from rest_framework import serializers
from .models import Movie, Seat, Booking


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, attrs):
        seat = attrs.get('seat')

        if seat and seat.booking_status:
            raise serializers.ValidationError({
                'seat': 'This seat is already booked.'
            })

        if seat and Booking.objects.filter(seat=seat).exists():
            raise serializers.ValidationError({
                'seat': 'This seat already has a booking.'
            })

        return attrs

    def create(self, validated_data):
        seat = validated_data['seat']

        booking = Booking.objects.create(**validated_data)

        seat.booking_status = True
        seat.save(update_fields=['booking_status'])

        return booking