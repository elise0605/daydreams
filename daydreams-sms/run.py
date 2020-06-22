from flask import Flask, request, redirect
from urllib.parse import urlparse
from twilio.twiml.messaging_response import Message, MessagingResponse
import pika, os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():

    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)

    url_str = os.environ.get('CLOUDAMQP_URL','amqp://mysecretURL')
    url = urlparse(url_str)

    params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
        credentials=pika.PlainCredentials(url.username, url.password))

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='texts')

    message = str(from_number) + ": " + str(body)

    channel.basic_publish(exchange='', routing_key='texts', body=message)
    connection.close()


    message_body = request.form['Body']
    resp = MessagingResponse()

    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
