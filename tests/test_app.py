from app import app

def test_add():
    client = app.test_client()
    r = client.get("/add?x=2&y=3")
    assert r.status_code == 200
    assert r.get_json()["result"] == 5
