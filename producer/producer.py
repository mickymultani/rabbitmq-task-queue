import pika
import sys
import time

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue to send messages to
channel.queue_declare(queue='task_queue', durable=True)

# Construct the message
message = ' '.join(sys.argv[1:]) or "Hello World!"
# Get the current time in seconds since the Epoch as an integer
timestamp = int(time.time())

# Determine the priority from the arguments, defaulting to 0
priority = 0 if len(sys.argv) < 3 else int(sys.argv[2])

# Send the message
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
        priority=priority,
        timestamp=timestamp  # use the integer timestamp
    ))

print(" [x] Sent %r" % message)
connection.close()
