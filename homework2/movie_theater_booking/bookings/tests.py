from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class MovieModelTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A movie for testing",
            release_date=date(2025, 1, 1),
            duration=120
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)

    def test_movie_string_representation(self):
        self.assertEqual(str(self.movie), "Test Movie")


class SeatModelTest(TestCase):

    def test_seat_creation(self):
        seat = Seat.objects.create(
            seat_number="A1",
            booking_status=False
        )

        self.assertEqual(seat.seat_number, "A1")
        self.assertFalse(seat.booking_status)

    def test_seat_string_representation(self):
        seat = Seat.objects.create(seat_number="A1")
        self.assertEqual(str(seat), "A1")


class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A movie for testing",
            release_date=date(2025, 1, 1),
            duration=120
        )

        self.seat = Seat.objects.create(
            seat_number="A1",
            booking_status=True
        )

        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)

    def test_booking_string_representation(self):
        self.assertEqual(
            str(self.booking),
            "testuser - Test Movie - A1"
        )


class MovieAPITest(APITestCase):

    def test_movie_list_endpoint(self):
        url = reverse('movie-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_creation_endpoint(self):
        url = reverse('movie-list')

        data = {
            "title": "Integration Test Movie",
            "description": "A movie created during an API test",
            "release_date": "2025-01-01",
            "duration": 120
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Integration Test Movie")


class SeatAPITest(APITestCase):

    def test_seat_list_endpoint(self):
        url = reverse('seat-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookingAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="bookingtest",
            password="testpassword"
        )

        self.movie = Movie.objects.create(
            title="Booking Test Movie",
            description="A movie for booking tests",
            release_date=date(2025, 1, 1),
            duration=120
        )

        self.seat = Seat.objects.create(
            seat_number="B1",
            booking_status=False
        )

        self.url = reverse('booking-list')

    def test_booking_list_endpoint(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_creation_marks_seat_as_booked(self):
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booking_status)

        self.assertTrue(
            Booking.objects.filter(
                movie=self.movie,
                seat=self.seat,
                user=self.user
            ).exists()
        )

    def test_booking_rejected_for_already_booked_seat(self):
        self.seat.booking_status = True
        self.seat.save()

        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(Booking.objects.count(), 0)