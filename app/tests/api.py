def test_get_rates(api_client_auth):
    response = api_client_auth.get('/api/v1/rates/')
    assert response.status_code == 200
    assert response.json()


def test_post_rates(api_client_auth):
    response = api_client_auth.post('/api/v1/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'source': ['This field is required.'],
    }


def test_get_source(api_client_auth):
    response = api_client_auth.get('/api/v1/source/')
    assert response.status_code == 200
    assert response.json()


def test_post_source(api_client_auth):
    response = api_client_auth.post('/api/v1/source/')
    assert response.status_code == 400
    assert response.json() == {
        'source_url': ['This field is required.'],
        'name': ['This field is required.'],
        'code_name': ['This field is required.'],
    }
