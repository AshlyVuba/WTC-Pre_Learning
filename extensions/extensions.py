def extensions():
    file_name = input("File name:" ).lower().strip()
    if file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".jpg"):
        return "image/jpeg"
    elif file_name.endswith("jpeg"):
        return "image/jpeg"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"
    
print(extensions())