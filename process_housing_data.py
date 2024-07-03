import pandas as pd
import os
from datetime import datetime
to_process_dir = '/Users/nguyenanhtien/Documents/ProjectM2/MiniProjData/toProcess'
result_dir = '/Users/nguyenanhtien/Documents/ProjectM2/MiniProjData/result'
already_processed_dir = '/Users/nguyenanhtien/Documents/ProjectM2/MiniProjData/already_processed'

def process_file(file_path):
    df = pd.read_csv(file_path)
    mean_price = df['price'].mean()
    result = pd.DataFrame({'mean_price': [mean_price]})
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    result_file = os.path.join(result_dir, f'result_{timestamp}.csv')
    result.to_csv(result_file, index=False)
    processed_file_path = os.path.join(already_processed_dir, os.path.basename(file_path))
    os.rename(file_path, processed_file_path)
    
for file_name in os.listdir(to_process_dir):
    if file_name.endswith('.csv'):
        process_file(os.path.join(to_process_dir, file_name))
