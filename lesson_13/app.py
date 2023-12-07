from lesson_13.DataStorageWrite import DataStorageWrite
json = DataStorageWrite()
json.connect()
print(f'File status = {json.status}')
print(f'File contents: {json.content}')
json.append("TEST")
print(f'File contents: {json.content}')
json.disconnect()
