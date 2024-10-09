
# Challenge 1 - Refactor DEV code

In this challenge, I got the code from the notebooks and moved it to python files. Specifically, I created a `src` directory, which has:

- `data` directory: has the code dedicated to load raw data and prepare it. This code is only accessed by features folder.
- `features` directory: takes `load_data` processed data and then creates features and prepares the resulting dataframe to be used by the model.
- `models` directory: has the code used to interact with the model (train and predict).

I also created a config with global constant variables. This variables are defined in only a single point of the application and are then used everywhere.

-------

# Challenge 2 - Build an API

For this challenge, I created an api.py file with all the endpoints:

- training
- inference
- listing all the models trained

I defined all of them in a single file as there were not that many and I do not expect the api to grow in size. However, if that was the case, I would group this endpoints in a preffix and then add other groups. The endpoints have the following workflow:

- The train endpoint is used to train a new model, which will be saved locally in folder `models`. The user will receive the name of the new versioned model.
- The inference endpoint is used to make a prediction for a single input house. For this, defined in folder `src/DTO` the endpoint input object, making sure that it checks all the necessary validators.
- The models endpoint returns a list of all available models to select the specific one you want to use in the inference endpoint.

-------

# Challenge 3 - Dockerize your solution

For this challenge, I created a Dockerfile in which I install the requirements, copy all the code and launch the application from uvicorn. To run this docker, run:

```bash
docker build -t intelygenz .
```

and then do:

```bash
docker run -p 8080:8080 intelygenz
```

Apart from that, I was testing the API in the web browser (/docs), but that cannot be accessible in a production environment, so I turned it off and created a test for the dockerized API using Python. I also modified the prediction endpoint to return to the user the model that was used, so he can be certain that the model that he selected was used.

Finally, I added some basic tests to check that the inference, training and api work correctly.
