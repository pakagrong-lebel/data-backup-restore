import shutil
def backup_database(database_path, backup_directory):
shutil.copy(database_path, backup_directory)
def restore_database(backup_path, database_directory):
shutil.copy(backup_path, database_directory)
