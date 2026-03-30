from celery import shared_task

@shared_task
def log_product_view(product_name):
    print(f">>> [CELERY LOG]: Кто-то просмотрел товар: {product_name}")
    return True