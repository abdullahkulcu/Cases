from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, date

import pika
import json
from ....redis_worker import Redis
from ...models import Subscriber

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='form_save_queue')


class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        channel.basic_consume(on_message_callback=self.callback,
                              queue='form_save_queue',
                              auto_ack=True)
        # # FOR WINDOWS
        # channel.basic_consume(consumer_callback=self.callback,
        #                       queue='form_save_queue',
        #                       no_ack=False)
        channel.start_consuming()

        pass

    def callback(self, ch, method, properties, body):
        try:
            form_data = json.loads(body)
            Redis.set_array_data(key="subscriber", value=body)
            Subscriber.insert(**form_data)
            channel.stop_consuming()
        except Exception as e:
            print(e)
