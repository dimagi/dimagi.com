# Dimagi.com Stylesheets

## Build Process

The stylesheets are built using [SASS](https://sass-lang.com/).

We use python's `libsass` library to compile the `.scss` files via
the CLI during deployment.

```
pipenv install libsass
```

The django APP `sass_processor` (`pipenv install django-sass-processor`)
does the compilation via the management command:

```
python manage.py compilescss
```

[See relevant sass processor settions](https://github.com/dimagi/dimagi.com/blob/master/settings.py#L128-L134).

We wrap parts of the stylesheet library with `sass-jacket`. This splits
the final output into several component levels, discussed in the next section,
which we use to optimize our css.

We then serve the files using Django Compressor `compressor`
(`pipenv install django_compressor`)

During the compression process, we apply a postcss filter `autoprefixer`
(`pipenv install autoprefixer`). This adds the necessary vendor-specific
prefixes to the stylesheets for cross-browser support. Prefixes are added
as necessary based on the `browserslist` in `package.json`.

The next compressor filter is `CssAbsoluteFilter` which converts all of
the relative image paths into absolute paths. This is really only necessary
on Dimagi.com specifically, as the core `app.scss` does not reference any
external images.

The final compressor filter is `rCSSMinFilter` which minifies the css.


## SASS Jacket Component Levels

`essential`

Embeds the compiled output of `app.essential.css` in the `<head>`.
Cannot be larger than 50 kb due to Google AMP rules.

`standard`

Includes all the non-essential CSS. Linked asynchronously as `app.standard.css`

### What is considered `critical` css?

`critical` css is anything that's definitely needed to render page structure and
especially render absolutely everything "above the fold"---with anything below
the fold looking a little more skeleton-like (but still structurally sound)

`critical` css should *NOT* include:

- `:hover`, `:focus`, `:active` states
- `!important` tags
- the `transition` property

