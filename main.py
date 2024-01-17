# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import pyarrow.parquet as pq

# 打开Parquet文件
parquet_file = pq.ParquetFile('malicious_contract_training_dataset_final.parquet')

# 读取整个文件内容
table = parquet_file.read()
print(table)

# 获取列名称
column_names = table.column_names
print(column_names)

column_data = table.column('column_name')
print(column_data)


