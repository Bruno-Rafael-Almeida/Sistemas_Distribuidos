import pika

class RabbitmqPublisher:
    def __init__(self, exchange, routing_key):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = exchange
        self.__routing_key = routing_key   #Define pra quem vai ser enviado a msg
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel

    def send_message(self, body):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2  #Modo de entrega com persistencia dos dados
            )
        )