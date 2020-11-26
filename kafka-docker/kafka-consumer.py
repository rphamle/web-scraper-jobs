from kafka import KafkaConsumer
import json

# kafka_server = 'localhost:32771'            # Reference kafka when run locally (not in container)
# kafka_server = '172.22.0.3:9092'            # Reference kafka by container IP
kafka_server = 'kafka-docker_kafka_1:9092'    # Reference kafka by hostname

# Set topic to read from
topic = 'test-topic'

# Set group id
group_id = 'consumer-1'

# initialize consumer to given topic and broker
consumer = KafkaConsumer(topic,
                        group_id = group_id,
                        bootstrap_servers = kafka_server,
                        value_deserializer = lambda m: json.loads(m.decode('utf-8')))

# (this is infinite) loop and print messages
for msg in consumer:
    print (msg)

