from kafka import KafkaProducer
import time
import random
import json

# kafka_server = 'localhost:32771'            # Reference kafka when run locally (not in container)
# kafka_server = '172.22.0.3:9092'            # Reference kafka by container IP
kafka_server = 'kafka-docker_kafka_1:9092'    # Reference kafka by hostname

# Set topic to send to
topic = 'test-topic'

# Reference kafka by hostname
producer = KafkaProducer(bootstrap_servers = kafka_server,
                        value_serializer = lambda m: json.dumps(m).encode('utf-8'))

num = 0
while True:

    # generate a random integer
    # num = random.randint(0, 10)
    num += 1
    msg = {
        'value': num
    }

    # send to topic on broker
    producer.send(topic, msg)

    print('sent {}'.format(num))

    # wait 1 second
    time.sleep(1)