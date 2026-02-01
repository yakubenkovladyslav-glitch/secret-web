import os
import json

# CONFIGURATION
folder_name = "private-media"
output_file = "media_list.js"
valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webm', '.mov', '.avi')

# 1. GET ALL FILES
files = []
try:
    for filename in os.listdir(folder_name):
        if filename.lower().endswith(valid_extensions):
            files.append(filename)
    
    # Sort them so they appear in order (1, 2, 10, etc.)
    files.sort()

    print(f"Found {len(files)} media files.")

    # 2. WRITE TO A JAVASCRIPT FILE
    # We write it as a JS variable so index.html can read it easily without server errors
    with open(output_file, "w") as f:
        json_data = json.dumps(files)
        f.write(f"const mediaList = {json_data};")

    print(f"Success! List saved to {output_file}")

except FileNotFoundError:
    print(f"Error: Could not find folder '{folder_name}'. Make sure it exists!")