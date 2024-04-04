import time
import publisher
import random

exchange = "data_exchange"
routing_key = "temperatura"
print("Produtor enviando os dados de temperatura:")

for i in range(0, 1000):
    x = random.randint(5, 35)
    time.sleep(1)
    print(x)

    rabbitmq_publisher = publisher.RabbitmqPublisher(exchange, routing_key)
    rabbitmq_publisher.send_message(str(x))

