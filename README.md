# Part 1: Django Appointment Booking with Stripe Mock Payment

## Description
This is a simple Django project that allows users to book an appointment and make a mock payment using Stripe test keys.

## Demo

[Demo Video](https://drive.google.com/file/d/1vwCXofD4w3wXY3tbqUS2j0kGKrmUzXBg/view?usp=sharing)

## Setup Instructions

### Step 1 — Clone Repository
```bash
git clone <your-repo-url>
cd appointments_project
````

### Step 2 — Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Create `.env` file

In the root folder (`appointments_project/`), create `.env` with:

```
STRIPE_SECRET_KEY=sk_test_51SDUorGXNxWpAetFbCoDqs4Em5kpZDS7KoGaY2fdk6sxBIpKl6DIBuuWO8d3gfiNy2nVO2dEhaoxXDMNBbAELdtC00KIWmiQTh
STRIPE_PUBLISHABLE_KEY=pk_test_51SDUorGXNxWpAetF8D9ln2qYkxd6MI6k52UQKdSVpXlZ4Q75ZhO5oMnjfpBUa6T1LXN2HRy5j3sz6LUAK0M61YZZ00zrrZVXb2
```

### Step 5 — Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6 — Run Server

```bash
python manage.py runserver 8080
```

### Step 7 — Open in Browser

Visit:

```
http://127.0.0.1:8080/
```

Fill the appointment form and click "Book Appointment" to see the payment flow.

## Stripe Integration

* Uses Stripe test keys.
* Creates a **PaymentIntent** when booking an appointment.
* Simulated payment using Stripe's test card `tok_visa`.

## Part 2 : Problem-Solving & Communication

**1. If this appointment feature had to handle thousands of bookings per day, what one or two changes would you make first?**  
To handle thousands of bookings per day, I would add database indexes on fields like `appointment_time` and `provider_name` for faster queries, and implement background processing (e.g., Celery) to handle tasks like sending confirmation emails and processing payments asynchronously so that the main booking process stays fast and scalable.

**2. How would you communicate progress and blockers to a non-technical founder?**  
I would use plain language without technical jargon. For progress, I’d explain what’s completed (“The appointment booking and payment feature is now live and tested in a staging environment”). For blockers, I’d clearly describe the issue and its impact (“We are waiting for updated Stripe API keys to complete testing, which may delay release by one day”), along with an estimated timeline and possible alternatives to keep things moving.
