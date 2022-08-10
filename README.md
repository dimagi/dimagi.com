# Dimagi.com

[![Build Status](https://travis-ci.org/dimagi/dimagi.com.svg?branch=master)](https://travis-ci.org/dimagi/dimagi.com)

1. [Getting Started Locally](#getting-started-locally)
2. [Deploying to Heroku](#deploying-to-heroku)
3. [PR Guidelines](#pr-guidelines)

## Getting Started Locally

1. `git clone` this repo to your machine.

1. Install [pyenv](https://github.com/pyenv/pyenv#installation) to manage python versions. ([Instructions for Ubuntu](https://ubunlog.com/en/pyenv-instala-multiples-versiones-de-python-en-tu-sistema/))

    NOTE: This repository has been tested to run on Python `3.9.x`

1. Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) ([Installation instructions for Ubuntu](https://www.liquidweb.com/kb/how-to-install-pyenv-virtualenv-on-ubuntu-18-04/))


1. Install python 3.9 with pyenv:
    ```
    pyenv install 3.9.11
    ```

    To set Python 3.9 as the global python, run:
    ```
    pyenv global 3.9.11
    ```

1. Install `pipenv`
    ```
    pip install pipenv
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

1. Install postcss
    ```
    sudo npm install -g postcss-cli
    sudo npm install -g autoprefixer
    ```

1. Create a `.env` file, and make any necessary edits.
    ```
    cp dev.env .env
    ```
    
1. Initialize the database
    ```
    manage.py createdb
    ```

1. Run the server using
    ```
    manage.py runserver
    ```


## Deploying to Heroku

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

1. Login with the Heroku CLI to your invited heroku account that manages the dimagidotcom app.
Make sure to add your keys with the CLI. These instructions should have been emailed to you with the
Heroku team member invite.

1. Make sure you followed the steps from [Getting Started Locally](#getting-started-locally)

1. Set up your origins:

```
git remote add heroku-prod https://git.heroku.com/dimagidotcom.git
git remote add heroku-staging https://git.heroku.com/dimagidotcom-staging.git
```

1. Deploy to production via command line:

```
git push heroku-prod master
```

Or Deploy to production from the web UI under the [Deploy](https://dashboard.heroku.com/apps/dimagidotcom/deploy/github) tab.


### Deploying & building off a specific branch to Staging

1. Deploying `master` to `heroku-staging` will automatically trigger a build but if you want to build a specific branch on staging,
first push that branch to github, and then manually Deploy that branch from the [Heroku web UI](https://dashboard.heroku.com/apps/dimagidotcom-staging/deploy/github.


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
