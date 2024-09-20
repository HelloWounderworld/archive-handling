# To run Fast API project in a server:
Go to the directory where main.py founded it and run

    fastapi dev main.py

Or running in development mode, for production use

    fastapi run

You can access following ports:

- Serving at: http://127.0.0.1:8000

- API docs: http://127.0.0.1:8000/docs (or http://127.0.0.1:8000/redoc)

The advantage to access "http://127.0.0.1:8000/docs" it will be unnecessary to install Postman to test each request type to check if your program is working.

Tip: To get out of the api serve mode just type Ctrl+C

## Other form to run your project in virtual environment:
Go to the your directory that you want to run and just type

    uvicorn main:app --reload

where "main" is the name os file "main.py" and "app" is the name of variable "app" defined at the code. Finally, the "reload" as the name wants to say is to reload as the code is changed.

If you instance the class FastAPI like following

    my_awesome_api = FastAPI()

so when you activate the uvicorn it will be

    uvicorn main:my_awsome_api --reload

The local url for this case is the same above.

Tip: Shows the schema of the OpenAPI, the FastAPI shows whole details of its api

    http://127.0.0.1:8000/openapi.json

## References:

1. [Swagger UI][1]
2. [Redoc UI][2]
3. [Open API Specification][3]
4. [The class FastAPI is inherited by Starlette][4]

[1]: https://github.com/swagger-api/swagger-ui
[2]: https://github.com/Redocly/redoc
[3]: https://github.com/OAI/OpenAPI-Specification
[4]: https://www.starlette.io/