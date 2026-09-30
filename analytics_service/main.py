from event_bus.bus import event_bus


def record_analytics(data):
    print(
        f"📊 Analytics recorded for Job {data['job_id']}"
    )


event_bus.subscribe("JobCompleted", record_analytics)