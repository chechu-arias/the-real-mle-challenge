
Challenge 1 - Refactor DEV code

In this challenge, I got the code from the notebooks and moved it to python files. Specifically, I created a src directory, which has:

- data: loads and prepares the raw data.
- features: parses that raw data to a dataset and creates features used by the model.
- models: has the code used to interact with the model (train and predict).

I also created a config with global constant variables used in all the application.

-------

Challenge 2 - Build an API

For this challenge, I created an api.py file with the endpoints defined, as there are not that many to create different files for them. I then created a train endpoint to train a new model, which will write it to folder models and return the name of the new versioned model. In inference endpoint, I defined the input type, making sure that it checks all the necessary validators. Finally, I created a models endpoint to return a list of all available models to select the specific one you want to use.

I also added type annotations to all the code to make it more clear.
