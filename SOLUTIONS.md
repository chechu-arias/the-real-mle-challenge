
Challenge 1 - Refactor DEV code

In this challenge, I got the code from the notebooks and moved it to python files. Specifically, I created a src directory, which has:

- data: loads and prepares the raw data.
- features: parses that raw data to a dataset and creates features used by the model.
- models: has the code used to interact with the model (train and predict).

I also created a config with global constant variables used in all the application.

