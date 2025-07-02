"""
データサイエンス学習用サンプルコード
pandas, numpy, matplotlib の基本的な使い方
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def data_science_example():
    print("📊 データサイエンス学習サンプル")
    print("=" * 50)

    # サンプルデータの作成
    print("1. サンプルデータの作成")
    np.random.seed(42)
    data = {
        'name': ['太郎', '花子', '次郎', '美咲', '健太'],
        'age': [25, 30, 22, 28, 35],
        'score': [85, 92, 78, 88, 95],
        'city': ['東京', '大阪', '名古屋', '福岡', '札幌']
    }

    df = pd.DataFrame(data)
    print(df)

    # 基本的な統計情報
    print("\n2. 基本的な統計情報")
    print(df.describe())

    # データフィルタリング
    print("\n3. データフィルタリング")
    high_scorers = df[df['score'] > 85]
    print("スコアが85以上の人:")
    print(high_scorers[['name', 'score']])

    # グループ化と集計
    print("\n4. 年齢グループ別の平均スコア")
    df['age_group'] = pd.cut(df['age'], bins=[20, 25, 30, 40], labels=['20-25', '26-30', '31-40'])
    age_group_stats = df.groupby('age_group')['score'].agg(['mean', 'count'])
    print(age_group_stats)

    # 簡単な可視化
    create_visualization(df)

def create_visualization(df):
    """データの可視化例"""
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 1. 年齢とスコアの散布図
    axes[0, 0].scatter(df['age'], df['score'], alpha=0.7, color='blue')
    axes[0, 0].set_xlabel('年齢')
    axes[0, 0].set_ylabel('スコア')
    axes[0, 0].set_title('年齢 vs スコア')

    # 2. スコアのヒストグラム
    axes[0, 1].hist(df['score'], bins=5, alpha=0.7, color='green')
    axes[0, 1].set_xlabel('スコア')
    axes[0, 1].set_ylabel('頻度')
    axes[0, 1].set_title('スコア分布')

    # 3. 都市別スコア
    city_scores = df.groupby('city')['score'].mean().sort_values(ascending=False)
    axes[1, 0].bar(city_scores.index, city_scores.values, color='orange')
    axes[1, 0].set_xlabel('都市')
    axes[1, 0].set_ylabel('平均スコア')
    axes[1, 0].set_title('都市別平均スコア')
    axes[1, 0].tick_params(axis='x', rotation=45)

    # 4. 年齢グループ別スコア分布
    df.boxplot(column='score', by='age_group', ax=axes[1, 1])
    axes[1, 1].set_xlabel('年齢グループ')
    axes[1, 1].set_ylabel('スコア')
    axes[1, 1].set_title('年齢グループ別スコア分布')

    plt.tight_layout()
    plt.savefig('/app/data_visualization.png', dpi=150, bbox_inches='tight')
    print("\n📈 グラフを保存しました: /app/data_visualization.png")
    plt.show()

if __name__ == "__main__":
    data_science_example()
