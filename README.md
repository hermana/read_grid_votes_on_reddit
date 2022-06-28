# read_grid_votes_on_reddit

Niche script that reads comment votes of a grid table posted in Reddit. 

# About 

This code reads comments that are votes on a specific grid system posted to Reddit. It was used to count votes for student sneaker designs on /r/sneakers. Here's an [example](https://www.reddit.com/r/Sneakers/comments/v2l22i/yeezy_700_grade_67_classroom_competition_please/). 

# Set up

You will need anaconda or miniconda installed. Create the environment from `environment.yaml` :

```conda env create -f environment.yaml```
```conda activate read_grid_votes_on_reddit```

Alternatively, if you can `pip-install praw` you will probably be able to run everything, it's not that complex of a script. Conda was overkill.

# Running the script

First you will need to set up a `personal_config.py` in the `src` directory. This file will contain your credentials to scrape the reddit post. You will need a client ID (CLIENT_ID), client secret (CLIENT_SECRET), and user agent (AGENT). Follow the instructions [here](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/) to get them. 

In the `src` directory, run

```python main.py```

You will be asked for the url of the reddit post in question. The results will be output to a file called `results.csv`. 

