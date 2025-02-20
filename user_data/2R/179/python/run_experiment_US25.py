# -*- coding: utf-8 -*-
"""
シナリオ: 関税引き上げの影響シミュレーション
"""

import model_2R_179  # SYMプロセッサで生成されたPythonモジュール（例）
import matplotlib.pyplot as plt
import pandas as pd

def run_tariff_scenario(tariff_increase):
    # 1. モデルの初期設定・パラメータ設定
    # ここでは、関税率に相当するパラメータを更新します。
    # ※パラメータ名は実際のモデル定義に合わせて変更してください。
    model_2R_179.set_parameter('tariff_rate', tariff_increase)

    # 2. シミュレーション期間の設定（例：2020～2030）
    start_year = 2025
    end_year = 2030

    # 3. シミュレーションの実行
    results = model_2R_179.run_simulation(start_year, end_year)

    # 4. 結果の整形と表示（例：GDPの推移をプロット）
    df = pd.DataFrame(results)
    plt.figure(figsize=(10, 5))
    plt.plot(df['year'], df['GDP'], marker='o')
    plt.title('関税引き上げシナリオ：GDPの推移')
    plt.xlabel('年')
    plt.ylabel('GDP')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # 例：通常よりも関税率を5%ポイント引き上げた場合のシナリオを実行
    run_tariff_scenario(tariff_increase=0.05)
