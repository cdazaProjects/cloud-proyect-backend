import os

# Setup RabitMQ
BROKER_URL = 'amqp://guest:guest@{}//'.format(":".join([os.environ.get(a) for a in ['RABBIT_IP', 'RABBIT_PORT']]))


# Setup Address
address = "0.0.0.0"
port    = 80
