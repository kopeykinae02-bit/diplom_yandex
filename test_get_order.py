import sender_stand_request
import data
# Екатерина Копейкина, 40-я когорта — Финальный проект. Инженер по тестированию плюс

def get_track():
    response = sender_stand_request.post_create_order(data.order_body)
    assert response.status_code == 201
    return response.json()["track"]

def test_get_order():
    track = get_track()
    order_response = sender_stand_request.get_order(track)

    assert order_response.status_code == 200