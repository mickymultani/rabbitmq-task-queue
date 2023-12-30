import pika
import time
import random

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    simulate_processing_time = body.count(b'.')
    time.sleep(simulate_processing_time)
    if random.choice([True, False]):  # Randomly simulate failed processing
        print(" [x] Message processing failed, requeuing...")
        ch.basic_nack(delivery_tag=method.delivery_tag)
    else:
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
