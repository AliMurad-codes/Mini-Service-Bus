from event_bus.bus import event_bus

import invoice_service.main
import notification_service.main
import analytics_service.main


def complete_job(job_id, customer_id, amount):

    print(f"✅ Job {job_id} completed")

    event_data = {
        "job_id": job_id,
        "customer_id": customer_id,
        "amount": amount
    }

    event_bus.publish(
        "JobCompleted",
        event_data
    )


complete_job(
    job_id=101,
    customer_id=5,
    amount=500
)