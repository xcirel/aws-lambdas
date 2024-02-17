from chalice import Chalice

app = Chalice(app_name='scheduled')


@app.lambda_function()
def first_function(event, context):
    return {'hello': 'world'}


@app.lambda_function()
def second_function(event, context):
    return {'hello': 'world2'}
