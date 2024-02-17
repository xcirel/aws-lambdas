from chalice import Chalice

app = Chalice(app_name='scheduled')


@app.schedule("cron(*/15 * ? * * *)")
def scheduled(event):
    print("Function executed successfully!")
    return True

