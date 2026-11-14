import requests

def test_get_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

def test_post():
    url = url = "https://jsonplaceholder.typicode.com/users"
    pylod = {
        "name" : "Mahesh",
        "email" : "mahes@gmail.com"

    }

    response = requests.post(url,json = pylod)

    assert response.status_code == 201