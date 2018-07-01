# Card Game #

A multi-player card game.

## Initial Setup ##

This was written using python 3.6.5. Here are the steps I used:

1) In the root directory, run: `pyenv local 3.6.5`
2) Set up the virtual environment: `python -m venv venv`
3) Activate it: `source venv/bin/activate`
4) Install the requirements: `pip install -r requirements.txt`

Note that you will need to activate the venv for each new shell!

## Managing Requirements ##

There are a couple of python tools that I use for development, but I do not want those to be part of
the `requirements.txt` file. In addition, there are only a handful of direct dependencies, and I wish
to keep those separate from the transitive closure.

For that to happen, I use two files: `requirements-to-freeze.txt`, which contains the direct dependencies,
without any versions. This allows upgrading requirements by executing:

    pip install -r requirements-to-freeze.txt --upgrade

The dev tools and their dependencies are kept in the second file, `requirements-to-ignore.txt`. Keeping
these separate allows regeneration of the `requirements.txt` file using the following command:

    pip freeze -r requirements-to-freeze.txt | grep -vFxf requirements-to-ignore.txt > requirements.txt

The `requirements-to-ignore.txt` file was generating by installing all the dev dependencies first,
then running `pip freeze > requirements-to-ignore.txt`.

This is all based on the [better pip workflow](https://www.kennethreitz.org/essays/a-better-pip-workflow) blog entry, plus this [SO post](https://stackoverflow.com/a/43137206/282725).

## Common Tasks ##

To run, do:

1) `export FLASK_APP=cardgame.py`
2) `flask run`

## Possibly useful links ##

### Flask ###

* [Home](http://flask.pocoo.org/) - [Quick Start](http://flask.pocoo.org/docs/1.0/quickstart/)
* [Awesome Flask](https://github.com/humiaozuzu/awesome-flask) - curated list of Flask resources and plugins
* [Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Flask Extensions ###

* [Assets](http://flask-assets.readthedocs.io/en/latest/) - Flask binding for [webassets](https://webassets.readthedocs.io/en/latest/index.html)
* Flask [socket IO](https://github.com/miguelgrinberg/Flask-SocketIO) extension

### Front-End Tools ###

* [Knockout](http://knockoutjs.com/index.html)

### Possibly useful Reddit Discussions ###

* [Multiplayer turn-based card game architecture](https://www.reddit.com/r/gamedev/comments/6xti6g/multiplayer_turn_based_card_game_architecture/)
* [Multiplayer game design for turn-based card game](https://www.reddit.com/r/Python/comments/8q2slw/multiplayer_game_design_for_turnbased_card_game/)
* [What protocol for turn-based multiplayer game](https://www.reddit.com/r/Python/comments/1yzdb4/what_protocol_would_you_use_for_turnbased/)

### Possibly useful samples ###

* [Hangman](https://github.com/rohit-jamuar/Hangman) - single `app.py` implementation of multiplayer hangman game

