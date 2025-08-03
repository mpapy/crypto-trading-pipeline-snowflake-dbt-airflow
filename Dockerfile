FROM apache/airflow:2.8.1-python3.10

# Přepneme se na airflow usera (standardní doporučený postup)
USER airflow

# Instalace potřebných balíčků pomocí requirements.txt (nejčistší způsob)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
