import pika
import threading
import os

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.exchange_declare(exchange='data_exchange',
                         exchange_type='direct',
                         durable=True)

channel.queue_declare(queue='queue_temperatura',
                      durable=True
                      )

channel.queue_declare(queue='queue_devolutiva',
                      durable=True
                      )

channel.queue_bind(exchange='data_exchange',
                   queue='queue_temperatura',
                   routing_key="temperatura")

channel.queue_bind(exchange='data_exchange',
                   queue='queue_devolutiva',
                   routing_key="devolutiva")

def start_process(command):
    os.system(f"start cmd /c {command}")
    # subprocess.run(command, shell=True)

# Defina os comandos que você deseja executar em terminais separados
commands = [
    "python A_publisher_temperatura_CWB.py",
    "python B_consumer_publisher_calor_frio.py",
    "python C_Consumer_calor_frio.py"
]

# Inicie uma thread para cada comando
threads = []
for command in commands:
    thread = threading.Thread(target=start_process, args=(command,))
    threads.append(thread)
    thread.start()

# Aguarde todas as threads terminarem
for thread in threads:
    thread.join()

print("Todos os processos foram iniciados.")