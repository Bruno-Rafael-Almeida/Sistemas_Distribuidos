import pika

class RabbitmqConsumer:  ##Colocar os conceitos em um prrojeto com maior praticidade
    def __init__(self, callback, queue) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = queue
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(  ### Nos conectamos
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()  ###Fizemos um canal
        channel.queue_declare(  ###Declaramos a nossa queue
            queue=self.__queue,
            durable=True
        )
        channel.basic_consume(  ###Como consumimos a nossa queue
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback  ##Ação para quando chegar uma mensagem
        )

        return channel  ###O proprio canal criada ja vai ficar como atributo

    def start(self):  ##O canal aqui é o que a gente criou na instancia do nosso objeto
        print(f'Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()


def minha_callback(ch, method, properties, body):
    print(body)