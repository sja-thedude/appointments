from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()

            # Create a mock payment intent
            payment_intent = stripe.PaymentIntent.create(
                amount=5000,  # 50.00 USD
                currency="usd",
                metadata={"appointment_id": appointment.id}
            )

            return render(request, "appointments/payment.html", {
                "client_secret": payment_intent.client_secret,
                "appointment": appointment,
                "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY
            })

    else:
        form = AppointmentForm()
    return render(request, "appointments/create_appointment.html", {"form": form})
