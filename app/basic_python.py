"""
Python学習用サンプルコード
基本的な構文とデータ型の学習
"""

def main():
    print("🐍 Python学習環境へようこそ！")
    print("=" * 50)

    # 基本的なデータ型
    print("1. 基本的なデータ型")
    number = 42
    text = "Hello, Python!"
    is_learning = True

    print(f"数値: {number}")
    print(f"文字列: {text}")
    print(f"真偽値: {is_learning}")

    # リストと辞書
    print("\n2. リストと辞書")
    fruits = ["apple", "banana", "orange"]
    person = {
        "name": "太郎",
        "age": 25,
        "city": "東京"
    }

    print(f"フルーツリスト: {fruits}")
    print(f"人物情報: {person}")

    # ループ処理
    print("\n3. ループ処理")
    for i, fruit in enumerate(fruits, 1):
        print(f"{i}. {fruit}")

    # 関数の使用例
    print("\n4. 関数の使用例")
    result = calculate_area(5, 3)
    print(f"長方形の面積 (5x3): {result}")

    # リスト内包表記
    print("\n5. リスト内包表記")
    squares = [x**2 for x in range(1, 6)]
    print(f"1-5の二乗: {squares}")

def calculate_area(length, width):
    """長方形の面積を計算する関数"""
    return length * width

if __name__ == "__main__":
    main()
