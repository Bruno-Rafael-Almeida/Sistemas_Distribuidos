import consumer

queue = "queue_devolutiva"


def minha_callback(ch, method, properties, body):
    print(body.decode('utf-8'))


rabitmq_consumer = consumer.RabbitmqConsumer(minha_callback, queue)
print("Consumidor final:")
rabitmq_consumer.start()
