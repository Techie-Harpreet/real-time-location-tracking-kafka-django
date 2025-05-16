# Real-Time Location Tracking System
A scalable real-time location tracking application built with **Apache Kafka**, **Django**, and **Google Maps API**.

## Overview
This project streams simulated GPS coordinates from a Kafka producer to a Django backend via a Kafka consumer, storing location updates in the database. The frontend visualizes these updates live on a Google Map, enabling real-time tracking of a delivery vehicle.

## Features
- **Kafka Producer:** Simulates continuous GPS location data.
- **Kafka Consumer:** Listens for messages and stores updates in Django models.
- **Real-Time Frontend:** Displays live vehicle location on Google Maps with custom vehicle icon.
- **Easy Integration:** Modular setup allows future integration with Google Maps Directions API for road routing.
- **Extensible:** Designed to be extended for authentication, multiple users, and more.

## Tech Stack
- Python & Django (Backend & API)
- Apache Kafka (Message streaming platform)
- Google Maps JavaScript API (Frontend map visualization)

## Getting Started

### Prerequisites
- Python 3.11
- Apache Kafka (see installation guide below)
- Google Maps API key

### Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Techie-Harpreet/real-time-location-tracking-kafka-django.git
   cd real-time-location-tracking-kafka-django-main
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and run Kafka locally:**
   For detailed steps on Windows, follow this guide:
   [How to install and run Apache Kafka on Windows](https://www.geeksforgeeks.org/how-to-install-and-run-apache-kafka-on-windows/)

4. **Run Django migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start Kafka Producer to simulate location data:**
   ```bash
   python kafka_producer.py
   ```

6. **Start Kafka Consumer via Django management command:**
   ```bash
   python manage.py kafka_consumer.py
   ```

7. **Run Django development server:**
   ```bash
   python manage.py runserver
   ```

8. **View the application:**
   Open your browser and go to http://localhost:8000 to see the real-time tracking map.

## Important Note on Google Maps API
The project uses the Google Maps JavaScript API to render the map and display live locations.
You must replace the placeholder API key in the index.html file with your own valid Google Maps API key:

```html
<!-- Load Maps API with async/defer and correct callback -->
<script src="https://maps.googleapis.com/maps/api/js?key=ADD-YOUR-API-KEY-HERE&callback=initMap" async defer></script>
```

You can obtain an API key by following Google's official guide here:
[Get API Key](https://developers.google.com/maps/documentation/javascript/get-api-key)

## Future Roadmap
- Integrate Google Maps Directions API for route-based tracking.
- Add authentication and support for multiple delivery vehicles.
- Enhance Kafka consumer for improved scalability and fault tolerance.
- Deploy on cloud platforms with production-ready configurations.

## License
This project is licensed under the MIT License.

Feel free to ⭐ the repository if you find it useful or want to contribute!

**Author:** Your Name  
**GitHub:** https://github.com/Techie-Harpreet
