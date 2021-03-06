# DJANGO TAG APPLICATION
![pypi](https://img.shields.io/pypi/v/ahlev-django-tag) ![pypi](https://img.shields.io/pypi/status/ahlev-django-tag)

This django application is used to create tag.

## prerequisites
The instructions below assume that you have a django project already set up; and a python virtual environment already installed and activated. 

## styles
All ahlev-django applications are using styles from [mdbootstrap.com](https://mdbootstrap.com), so please make sure you install [ahlev-django-css-js](https://github.com/ohahlev/ahlev-django-css-js.git) first.

## install from this repository
### clone
```
git clone https://github.com/ohahlev/ahlev-django-tag.git
```

### go to directory ahlev-django-tag
```
cd ahlev-django-tag
```

### create installer package
```
make package
```

### install package
Let's say ahlev-django-tag directory is in the same level as the project directory.

cd into project directory
```
cd ../my_project_dir
```
install ahlev-django-tag from the project directory
```
pip install ../ahlev-django-tag/dist/ahlev-django-tag-0.0.1.tar.gz
```

## install from pypi
[ahlev-django-tag](https://pypi.org/project/ahlev-django-tag/)

## project configuration
### update settings.py as the following
```
INSTALLED_APPS = [
    'tag', # add this line
    ...
]
```

### add these lines to the end of settings.py
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/medias/'
```

## screenshots
### frontend: partial tag
![](screenshot/tag_frontend.png)

### backend: tag management
![](screenshot/tag_backend1.png)

### backend: list all tags
![](screenshot/tag_backend2.png)

### backend: edit a tag
![](screenshot/tag_backend3.png)
