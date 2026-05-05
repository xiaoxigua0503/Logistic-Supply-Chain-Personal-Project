import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Bước 1: Tạo DataFrame mẫu (bạn thay bằng file của bạn)
customer_order = pd.read_csv(r'D:\LSCM - Raw data\customer_order_clean.csv')
link = pd.read_csv(r'D:\LSCM - Raw data\link_clean.csv')
product = pd.read_csv(r'D:\LSCM - Raw data\product_clean.csv')
product_type = pd.read_csv(r'D:\LSCM - Raw data\product_type_clean.csv')
route = pd.read_csv(r'D:\LSCM - Raw data\route_clean.csv')
warehouse = pd.read_csv(r'D:\LSCM - Raw data\warehouse_clean.csv')

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[()]", "", regex=True)
    )
    return df
tables = {
    "customer_order": customer_order,
    "link": link,
    "product": product,
    "product_type": product_type,
    "route": route,
    "warehouse": warehouse
}

# clean column name
for name in tables:
    tables[name] = clean_column_names(tables[name])
# Bước 2: Thông tin kết nối BigQuery
project_id = "jda-k1"
dataset_id = "practice_data_pipeline"
key_path = r"D:\LSCM - Raw data\jda-k1-2afad6d8f47e.json"


# Bước 3: Tạo client BigQuery
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=project_id)

# Bước 4: Tạo table mapping
tables = {
    "xiguacustomer_order": customer_order,
    "xigualink": link,
    "xiguaproduct": product,
    "xiguaproduct_type": product_type,
    "xiguaroute": route,
    "xiguawarehouse": warehouse
}

# Bước 5: Cấu hình ghi đè bảng nếu đã tồn tại
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    autodetect=True,  
)

# Bước 6: Load DataFrame vào BigQuery
for table_name, df in tables.items():
    table_ref = f"{project_id}.{dataset_id}.{table_name}"

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()

    print(f"✅ Loaded {df.shape[0]} rows → {table_ref}")
