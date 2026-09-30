from event_bus.bus import event_bus


def create_invoice(data):
    print(
        f"🧾 Invoice created for Job {data['job_id']} "
        f"Amount: ${data['amount']}"
    )


event_bus.subscribe("JobCompleted", create_invoice)