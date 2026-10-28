import pytest


@pytest.fixture(autouse=True)
def use_test_db(tmp_path, monkeypatch):
    # 本番の todo.db を汚さないよう、テストごとに使い捨ての DB を使う
    monkeypatch.setenv("TODO_DB_PATH", str(tmp_path / "test.db"))
