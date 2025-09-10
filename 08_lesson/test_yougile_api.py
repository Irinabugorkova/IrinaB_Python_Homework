import requests


class YougileAPI:
    def __init__(self, token: str) -> None:
        self.base_url = "https://yougile.com/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str) -> requests.Response:
        payload = {"title": title}
        return requests.post(
            self.base_url,
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id: str) -> requests.Response:
        url = f"{self.base_url}/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(
            self, project_id: str, new_title: str) -> requests.Response:
        url = f"{self.base_url}/{project_id}"
        payload = {"title": new_title}
        return requests.put(url, json=payload, headers=self.headers)


class TestYougileAPI:
    def setup_class(self) -> None:
        token = (
            "вставить токен"
        )
        self.api = YougileAPI(token)

    def test_create_project_positive(self) -> None:
        response = self.api.create_project("My project")
        assert response.status_code in [200, 201], response.text
        data = response.json()
        assert "id" in data, f"Ответ не содержит 'id': {data}"

    def test_create_project_negative(self) -> None:
        response = requests.post(
            self.api.base_url,
            json={},
            headers=self.api.headers
        )
        assert response.status_code in [400, 422], response.text

    def test_get_project_positive(self) -> None:
        create_resp = self.api.create_project("My project")
        data = create_resp.json()
        assert "id" in data, f"Ответ не содержит 'id': {data}"
        project_id = data["id"]

        get_resp = self.api.get_project(project_id)
        assert get_resp.status_code == 200, get_resp.text
        get_data = get_resp.json()
        assert get_data["id"] == project_id

    def test_get_project_negative(self) -> None:
        response = self.api.get_project("999999999")
        assert response.status_code == 404, response.text

    def test_update_project_positive(self) -> None:
        create_resp = self.api.create_project("My project")
        data = create_resp.json()
        assert "id" in data, f"Ответ не содержит 'id': {data}"
        project_id = data["id"]

        update_resp = self.api.update_project(project_id, "My project")
        assert update_resp.status_code == 200, update_resp.text
        update_data = update_resp.json()
        assert "id" in update_data, f"Ответ не содержит 'id': {update_data}"

    def test_update_project_negative(self) -> None:
        response = self.api.update_project("invalid_id", "My project")
        assert response.status_code in [400, 404], response.text
