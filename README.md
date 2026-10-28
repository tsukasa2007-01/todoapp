# todoapp(Python 版)

TypeScript / Express で作った TODO アプリのバックエンドを、Python で書き換えたものです。
フロント(`public/index.html`)は TypeScript 版のものをそのまま使っています。

## 使った道具

| 役割 | TypeScript 版 | Python 版 |
|---|---|---|
| パッケージ管理・実行 | npm / npx | uv |
| Web API | Express | FastAPI |
| リクエストの型・検証 | 手書き | pydantic |
| SQLite 操作 | better-sqlite3 | sqlite3(標準ライブラリ) |
| テスト | Vitest | pytest(FastAPI の TestClient) |
| 整形・Lint | Prettier / ESLint | ruff |
| 型チェック | tsc | mypy |

## API

| メソッド | パス | 機能 |
|---|---|---|
| GET | `/api/todos` | 一覧取得 |
| POST | `/api/todos` | 追加(空・100文字超は 400) |
| PUT | `/api/todos/{todo_id}` | 完了切替(なければ 404) |
| DELETE | `/api/todos/{todo_id}` | 削除(なければ 404) |

## セットアップ

```bash
uv sync
```

## 起動(プロジェクトの一番上で実行)

```bash
uv run fastapi dev practice/api_hello.py
```

ブラウザで `http://127.0.0.1:8000` を開きます。API の説明は `http://127.0.0.1:8000/docs` です。

## テスト

```bash
uv run pytest practice/
```

## 整形・静的チェック・型チェック

```bash
uv run ruff check practice/
uv run ruff format --check practice/
uv run mypy practice/api_hello.py practice/validate.py
```

## 主なファイル

| ファイル | 役割 |
|---|---|
| `practice/api_hello.py` | API 本体(FastAPI)、SQLite の読み書き |
| `practice/validate.py` | タイトルのバリデーション |
| `practice/test_api.py` | API の結合テスト |
| `practice/test_validate.py` | バリデーションの単体テスト |
| `public/index.html` | フロント(TypeScript 版と同じ) |