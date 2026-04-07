def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) > 0

    for details in payload.values():
        assert expected_required_fields.issubset(details.keys())
