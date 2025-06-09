import base64
key = "UTPb4J2V47ehvuE3jYY+5wWVq6Eded5C3U9pkfrCyjzRwFlDsNPLDwz9kXe+kxRBl2nsPVU5DYPK+AStCVEL7g=="
try:
    base64.b64decode(key)
    print("Key is valid")
except Exception as e:
    print(f"Key is invalid: {e}")