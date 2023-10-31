from celery import Celery
import requests

celery = Celery(
    "my_celery_app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)


@celery.task
def send_message_task(message_text, message_sender):
    try:
        response = requests.post(
            "http://localhost:8000/messages/",
            json={"content": message_text, "sender": message_sender},
        )

        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(response.json())
            print("Failed to send the message.")

    except Exception as e:
        print(f"Error sending message: {str(e)}")
