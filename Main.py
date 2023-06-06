import os
import shutil

def sort_files_by_extension(directory):
    # Create a dictionary to store file extensions and their corresponding directories
    file_extensions = {}

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1][1:]

            # Check if the file extension already exists in the dictionary
            if file_extension in file_extensions:
                # Move the file to the corresponding directory
                shutil.move(
                    os.path.join(directory, filename),
                    os.path.join(directory, file_extensions[file_extension], filename)
                )
            else:
                # Create a new directory for the file extension
                new_directory = os.path.join(directory, file_extension)
                os.makedirs(new_directory)

                # Move the file to the new directory
                shutil.move(
                    os.path.join(directory, filename),
                    os.path.join(new_directory, filename)
                )

                # Update the dictionary
                file_extensions[file_extension] = file_extension

    print("Files sorted successfully!")

# Ask the user for the directory path
directory_path = input("Enter the directory path: ")

# Call the function to sort files by extension
sort_files_by_extension(directory_path)
