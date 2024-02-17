from chalice import Chalice

# create a new chalice app
app = Chalice(app_name='invoke')


@app.lambda_function(name="invoke")
def first_function(event, context):
    print(event['nome'])
    print(event['idade'])
    return True