# ninja-authtoken
## A simple Django app for django-ninja authentication tokens

## source code : [Visit GitHub!](https://github.com/MoriZoki/ninja-authtoken/)

#### installaton

```shell
pip install ninja-authtoken
```

#### add ninja-authtoken to django installed app

```python
INSTALLED_APPS = [
    ...
    "authtoken",
    ...
]
```

#### set user model in settings.py
#### Example {AUTH_USER_MODEL = "accounts.USER"}


## Usage
**for routers**

```python
from authtoken.security import APIKeyAuth

auth = APIKeyAuth()

@router.get('profile/', auth=auth)
def profile(request):
    return f"Hello, {request.user}!"
```

**Api Base**

```python
from ninja import NinjaAPI
from authtoken.security import APIKeyAuth

#  ...

api = NinjaAPI(auth=APIKeyAuth())

# ...

@api.get("/profile")
def profile(request):
    return f"Hello, {request.user}!"
```



**ـ The token is generated automatically as soon as a new user is created by Signal ـ**



