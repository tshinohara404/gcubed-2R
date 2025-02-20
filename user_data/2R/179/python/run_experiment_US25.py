# run_experiment_US25.py
from gcubed.model_parameters.parameters import Parameters
from gcubed.data.database import Database
from gcubed.runner import Runner

# Step 1: データベースとパラメータ校正のセットアップ
# ※ "path/to/your/database" を実際のデータベースパスに置き換えてください。
database = Database("path/to/your/database")
base_year = 2025

# カスタムパラメータクラスを定義します。
class CustomParameters(Parameters):
    def __init__(self, database, base_year):
        super().__init__(database=database, base_year=base_year)
        # MFN関税率変数 "TIM" を25%に設定
        self.TIM = 0.25

# カスタムパラメータをインスタンス化
params = CustomParameters(database=database, base_year=base_year)

# Step 2: Runnerオブジェクトを作成して実験を実行
# Runnerは、ベースライン予測に対してシミュレーション層（ショック）を順次適用し、結果を生成します。
runner = Runner(params)

# Step 3: 実験を実行（25%関税引き上げの影響をシミュレーション）
experiment_results = runner.run_experiment()

# Step 4: 結果を出力または保存
print("実験が完了しました。結果は以下の通りです:")
print(experiment_results)

# 各シミュレーション層のプロジェクションにアクセスする場合:
all_projections = runner.all_projections
for i, projection in enumerate(all_projections):
    print(f"シミュレーション層 {i} のプロジェクション:", projection)
