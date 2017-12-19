# dimagi.com

## Getting Started

1. Install `virtualenv` for `Python 3.6` and `pip3` and make your virtual environment.
2. Install `pipenv`
 ```
 pip3 install pipenv
 ```
 
3. Install from `Pipfile`
 ```
 pipenv install
 ```

4. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

todo: fill in the rest of this


## PR Approval Guidelines

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
