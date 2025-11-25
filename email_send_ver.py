from redis import Redis
from rq import Queue
from tasks import send_email_task

redis_conn = Redis()
q = Queue(connection=redis_conn)

job = q.enqueue(send_email_task, 
                "enviropr1@gmail.com",
                "hello from me",
                "This is a hehehehe test.")

print('job enqueued')
print('job id : ', job.get_id())