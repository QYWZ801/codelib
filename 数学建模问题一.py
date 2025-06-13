import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt


class ContributorCounter:
    def __init__(self):
        # 基因座峰高阈值（过滤噪声峰）
        self.marker_thresholds = {
            'D8S1179': 50, 'D21S11': 50, 'FGA': 50, 'AMEL': 50
        }

    def preprocess_data(self, data_df):
        """提取有效峰（峰高>阈值）"""
        valid_peaks = []
        for _, row in data_df.iterrows():
            sample_file = row['Sample File']
            marker = row['Marker']
            threshold = self.marker_thresholds.get(marker, 50)
            # 遍历所有等位基因列
            for i in range(1, 51):
                size = row.get(f'Size {i}')
                height = row.get(f'Height {i}')
                if size and height and height >= threshold:
                    valid_peaks.append({
                        'Sample File': sample_file,
                        'Marker': marker,
                        'Size': size,
                        'Height': height
                    })
        return pd.DataFrame(valid_peaks)

    def estimate_contributor_count(self, sample_data):
        """估计贡献者人数"""
        if sample_data.empty:
            return 0

        # 优先使用信息丰富的基因座（如FGA）
        fga_data = sample_data[sample_data['Marker'] == 'FGA']
        if fga_data.empty:
            fga_data = sample_data[sample_data['Marker'].first_valid_index()]

        # 1. 基于峰高分布的GMM拟合
        heights = fga_data['Height'].values.reshape(-1, 1)
        if len(heights) < 2:
            return len(heights)  # 最少1人

        # 尝试1-5人混合模型
        best_bic = float('inf')
        best_n = 1
        for n in range(1, 6):
            try:
                gmm = GaussianMixture(n_components=n, random_state=42)
                gmm.fit(heights)
                bic = gmm.bic(heights)
                if bic < best_bic:
                    best_bic = bic
                    best_n = n
            except:
                continue

        # 2. 用等位基因数量约束修正（每个贡献者最多2个等位基因）
        unique_sizes = len(set(fga_data['Size']))
        max_contributors = unique_sizes // 2  # 向下取整
        estimated = min(best_n, max_contributors, 5)  # 最多5人
        return estimated if estimated >= 1 else 1

    def evaluate_accuracy(self, predicted, actual):
        """评估准确率"""
        return sum(p == a for p, a in zip(predicted, actual)) / len(actual)


# 使用示例（假设已加载附件1数据）
if __name__ == "__main__":
    # 模拟数据加载（实际需替换为真实文件）
    sample_files = ["2人混合样本.fsa", "5人混合样本.fsa"]
    actual_counts = [2, 5]

    counter = ContributorCounter()
    predicted = []
    for file in sample_files:
        # 模拟数据（实际需从Excel读取）
        mock_data = pd.DataFrame({
            'Sample File': [file] * 10,
            'Marker': ['FGA'] * 10,
            'Size': [100, 105, 110, 115, 120, 125, 130, 135, 140, 145],
            'Height': [200, 180, 160, 140, 120, 100, 80, 60, 40, 20]
        })
        processed = counter.preprocess_data(mock_data)
        count = counter.estimate_contributor_count(processed)
        predicted.append(count)

    accuracy = counter.evaluate_accuracy(predicted, actual_counts)
    print(f"贡献者人数识别准确率: {accuracy:.2f}")