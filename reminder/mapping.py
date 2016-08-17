host_url = 'http://0.0.0.0:8000/'
site_mapping = {
    "authorization": {
        "url": host_url + "/register/login/",
        "username": "//input[@name='username']",
        "password": "//input[@name='password']",
        "login button": "//button[@name='login']",
    },
}
