import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'TEST_SECRET'
    with app.test_client() as client:
        yield client

def test_home_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"What is" in response.data

def test_home_post_correct(client):
    with client.session_transaction() as session:
        session['correct_answer'] = 15
    response = client.post('/', data={'answer': '15'})
    assert response.status_code == 200
    assert b"Correct! Well done." in response.data

def test_home_post_wrong(client):
    with client.session_transaction() as session:
        session['correct_answer'] = 15
    response = client.post('/', data={'answer': '10'})
    assert response.status_code == 200
    assert b"Wrong! The correct answer was 15." in response.data

def test_question_generation(client):
    response = client.get('/')
    assert response.status_code == 200
    with client.session_transaction() as session:
        correct_answer = session.get('correct_answer')
        question = session.get('question')
        assert correct_answer is not None
        assert question is not None
