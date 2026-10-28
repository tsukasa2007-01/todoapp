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
uv run fastapi dev src/todoapp/presentation/server.py
```

ブラウザで `http://127.0.0.1:8000` を開きます。API の説明は `http://127.0.0.1:8000/docs` です。

## テスト

```bash
uv run pytest src/
```

## 整形・静的チェック・型チェック

```bash
uv run ruff check src/
uv run ruff format --check src/
uv run mypy src/
```

## 主なファイル

| ファイル | 役割 |
|---|---|
| `src/todoapp/domain/todo/types.py` | TODO の共通型 |
| `src/todoapp/domain/todo/validate.py` | タイトルのバリデーション |
| `src/todoapp/application/todo/service.py` | TODO の一覧・追加・完了切替・削除の流れ |
| `src/todoapp/infrastructure/todo/repository.py` | SQLite 接続、SQL、0/1 と bool の変換 |
| `src/todoapp/presentation/server.py` | FastAPI の HTTP 受け口 |
| `src/todoapp/test_api.py` | API の結合テスト |
| `practice/` | 練習用ファイル |
| `public/index.html` | フロント(TypeScript 版と同じ) |