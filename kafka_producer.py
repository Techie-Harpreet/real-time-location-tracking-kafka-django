from confluent_kafka import Producer
import json
import os
import time

conf = {
    'bootstrap.servers':  'localhost:9092',
}
producer = Producer(**conf)

start_latitude = 19.0760
start_longitude = 72.8777
end_latitude = 18.5204
end_longitude = 73.8567

num_steps= 1000
step_size_lat = (end_latitude - start_latitude) / num_steps
step_size_lon = (end_longitude - start_longitude) / num_steps
current_step = 0

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

topic = 'location_updates'
while True:
    # Calculate the current latitude and longitude
    latitude = start_latitude + (step_size_lat * current_step)
    longitude = start_longitude + (step_size_lon * current_step)

    # Create a message
    data = {
        'latitude': latitude,
        'longitude': longitude,
    }

    print(f"Producing message: {data}")

    # Produce the message to the Kafka topic
    producer.produce(topic,json.dumps(data).encode('utf-8'), callback=delivery_report)
    producer.flush()

    # Increment the step
    current_step += 1

    # Break the loop if we reach the end point
    if current_step > num_steps:
        current_step = 0

    time.sleep(2)