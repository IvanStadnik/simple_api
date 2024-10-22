from celery import shared_task


@shared_task
def print_task(user_pk):
    print(f'Hello user {user_pk}')
