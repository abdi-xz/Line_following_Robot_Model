import os

# Define the dataset base directory
base_dir = "dataset"  # Change this to your dataset folder path

# Define the subdirectories (classes/labels)
categories = ["straight", "left", "right"]

# Iterate over each category folder
for category in categories:
    folder_path = os.path.join(base_dir, category)
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        continue

    # Counter for renaming files
    count = 0

    # Iterate through all image files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.png')):  # Only process image files
            # Generate the initial target filename
            new_filename = f"{category}_{count:04d}.jpg"
            dst_path = os.path.join(folder_path, new_filename)

            # Ensure the new filename is unique
            while os.path.exists(dst_path):
                count += 1
                new_filename = f"{category}_{count:04d}.jpg"
                dst_path = os.path.join(folder_path, new_filename)

            # Rename the file
            src_path = os.path.join(folder_path, filename)
            os.rename(src_path, dst_path)

            # Increment the counter for the next file
            count += 1

    print(f"Renamed files in folder: {category}")
