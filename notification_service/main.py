from event_bus.bus import event_bus


def send_notification(data):
    print(
        f"📱 Notification sent to Customer {data['customer_id']} "
        f"for Job {data['job_id']}"
    )


event_bus.subscribe("JobCompleted", send_notification)