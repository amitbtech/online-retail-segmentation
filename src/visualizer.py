
import matplotlib.pyplot as plt
import seaborn as sns

def save_cluster_boxplots(rfm, output_dir='visuals/'):
    sns.set(style='whitegrid')
    plt.figure(figsize=(18, 5))

    for i, col in enumerate(['Recency', 'Frequency', 'Monetary']):
        plt.subplot(1, 3, i+1)
        sns.boxplot(x='Cluster', y=col, data=rfm)
        plt.title(f'{col} by Cluster')

    plt.tight_layout()
    plt.savefig(f"{output_dir}/rfm_cluster_boxplots.png")
    plt.close()
