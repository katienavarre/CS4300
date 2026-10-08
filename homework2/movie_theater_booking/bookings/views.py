from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()

    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.booking_status:
            messages.error(request, 'Sorry, this seat is already booked.')
            return redirect('book_seat', movie_id=movie.id)

        # Use the first existing user for this basic booking workflow.
        user = User.objects.first()

        if user is None:
            messages.error(
                request,
                'No user account exists yet. Create a user before booking.'
            )
            return redirect('book_seat', movie_id=movie.id)

        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=user
        )

        seat.booking_status = True
        seat.save()

        messages.success(request, 'Your seat has been booked!')
        return redirect('booking_history')

    return render(
        request,
        'bookings/seat_booking.html',
        {'movie': movie, 'seats': seats}
    )


def booking_history(request):
    bookings = Booking.objects.select_related(
        'movie', 'seat', 'user'
    ).all().order_by('-booking_date')

    return render(
        request,
        'bookings/booking_history.html',
        {'bookings': bookings}
    )