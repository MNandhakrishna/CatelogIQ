from azure.storage.filedatalake import DataLakeServiceClient
account_name = "textloganalyticssa"
account_key = "UTPb4J2V47ehvuE3jYY+5wWVq6Eded5C3U9pkfrCyjzRwFlDsNPLDwz9kXe+kxRBl2nsPVU5DYPK+AStCVEL7g=="
file_system = "rawfiles"
service_client = DataLakeServiceClient(
    account_url=f"https://{account_name}.dfs.core.windows.net",
    credential=account_key
)
file_system_client = service_client.get_file_system_client(file_system)
print(list(file_system_client.get_paths()))