FROM python:3.11-slim

# システムパッケージの更新とインストール
RUN apt-get update && apt-get install -y \
  curl \
  git \
  vim \
  postgresql-client \
  && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの作成
WORKDIR /app

# requirements.txtをコピーして依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# ポートの公開
EXPOSE 8888 5000

# デフォルトコマンド
CMD ["python", "-c", "print('Python学習環境へようこそ!')"]
