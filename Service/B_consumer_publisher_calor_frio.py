import consumer
import publisher

exchange = "data_exchange"
routing_key = "devolutiva"
queue = "queue_temperatura"


def minha_callback(ch, method, properties, body):

    temperatura = body.decode('utf-8')
    temperatura = int(temperatura)

    print(temperatura)

    rabbitmq_publisher = publisher.RabbitmqPublisher(exchange, routing_key)

    if temperatura < 20:
        rabbitmq_publisher.send_message("Frio")
        print("Envia: Frio")

    else:
        rabbitmq_publisher.send_message("Calor")
        print("Envia: Calor")

print("Consumidor que tambem publica:")
rabitmq_consumer = consumer.RabbitmqConsumer(minha_callback, queue)
rabitmq_consumer.start()

