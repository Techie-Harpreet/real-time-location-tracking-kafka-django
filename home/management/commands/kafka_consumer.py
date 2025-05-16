from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaException, KafkaError
import json
from home.models import LocationUpdate

class Command(BaseCommand):
    help = 'Run a Kafka consumer to receive location updates'

    def handle(self, *args, **options):
        conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'location_group',
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(conf)
        consumer.subscribe(['location_updates'])

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        raise KafkaException(msg.error())

                try:
                    data = json.loads(msg.value().decode('utf-8'))
                    LocationUpdate.objects.create(
                        latitude=data['latitude'],
                        longitude=data['longitude']
                    )
                    self.stdout.write(self.style.SUCCESS(f"Saved location update: {data}"))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error saving location: {e}"))

        except KeyboardInterrupt:
            print("Kafka consumer interrupted by user.")
        finally:
            consumer.close()
