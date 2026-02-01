import os
import json
import re

# CONFIGURATION
folder_name = "private-media"
output_file = "media_list.js"
valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webm', '.mov', '.avi')

def natural_sort_key(s):
    """
    Splits string into a list of integers and strings for natural sorting.
    Example: 'image_10.jpg' becomes ['image_', 10, '.jpg']
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

try:
    # 1. GET ALL FILES
    files = []
    if not os.path.exists(folder_name):
         print(f"Error: Folder '{folder_name}' not found.")
         exit()

    for filename in os.listdir(folder_name):
        if filename.lower().endswith(valid_extensions):
            files.append(filename)
    
    # 2. SORT NATURALLY
    files.sort(key=natural_sort_key)

    print(f"Found {len(files)} media files.")

    # 3. WRITE TO JS FILE
    with open(output_file, "w") as f:
        json_data = json.dumps(files)
        f.write(f"const mediaList = {json_data};")

    print(f"Success! List saved to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")