# Dimagi.com

1. [Getting Started Locally](#getting-started-locally)
2. [Pushing to Heroku](#pushing-to-heroku)
3. [PR Guidelines](#pr-guidelines)

## Getting Started Locally

1. `git clone` this repo to your machine.

1. Install `virtualenv` for `Python 3.6` and `pip3` and make your virtual environment. If you have `virtualenv` installed for
    ```
    virtualenv -p python3 .venv
    source .venv/bin/activate
    ```

1. Install `pipenv`
    ```
    pip3 install pipenv
    ```
 
1. Install `Pipfile` dependencies
    ```
    pipenv install
    ```

1. Install [Yarn](https://yarnpkg.com/en/docs/install) dependencies
    ```
    yarn install
    ```

1. Install & Run [Redis](https://redis.io/).

1. Create a `.env` file, and make any necessary edits.
    ```
    cp dev.env .env
    ```

1. Run the server using
    ```
    manage.py runserver
    ```


## Pushing to Heroku

Todo

## PR Guidelines

### HTML

Are `</div>` (and other deeply nested) tags properly commented with a selector for easy identification?
```
<div class="content">
  ...
</div> {# .content #}
```


Is all human readable text in a `{% blocktrans %}`?
```
{% blocktrans %}
  Human Readable Text!
{% endblocktrans %}
```
