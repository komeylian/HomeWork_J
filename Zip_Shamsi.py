import os
import zipfile
import mysql.connector
import subprocess
from jdatetime import datetime


def zip_folders(folder_paths):
    now = datetime.now()
    jalali_date = now.strftime('%Y-%m-%d-%H%M%S')
    zip_filename = f'C:/Users/komeylian/Desktop/Python_{jalali_date}.rar'

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for folder_path in folder_paths:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(
                        file_path, os.path.dirname(folder_path))
                    zipf.write(file_path, arcname)


def backup_database(db_config, backup_path):
    mysqldump_path = '"C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqldump.exe"'
    mysqldump_cmd = f'{mysqldump_path} --host={db_config["host"]} --user={db_config["user"]} --password={db_config["password"]} --databases {db_config["database"]} > {backup_path}'
    subprocess.call(mysqldump_cmd, shell=True)


# Example usage
folders_to_zip = [
    r'C:/Users/komeylian/Desktop/MyPython',
    r'C:/Python',
    # Add other folder paths here
]

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root123',
    'database': 'drug_store'
}

now = datetime.now()
jalali_date2 = now.strftime('%Y-%m-%d-%H')
backup_path = F'C:/Users/komeylian/Desktop/MyPython/DB_MySql/MySql_{jalali_date2}.sql'

zip_folders(folders_to_zip)
backup_database(db_config, backup_path)
