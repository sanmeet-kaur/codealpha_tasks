import os
import csv
import shutil

def organize_jpg_files(source_folder):
    if not os.path.isdir(source_folder):
        print("ERROR:The source folder does not exist")
        return

    destination_folder = os.path.join(source_folder, "Organized_JPGs")
    os.makedirs(destination_folder, exist_ok=True)

    moved_files=0
    skipped_files=0
    failed_files=0

    print("\nStarting file organization...")
    print("-"*50)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if not os.path.isfile(source_path):
            continue

        if not filename.lower().endwith((".jpg",".jpeg")):
            continue

        destination_path = os.path.join(destination_folder, filename)

        if os.path.exists(destination_path):
            print(f"Skipped: {filename} (already exists in destination)")
            skipped_files += 1
            continue

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_files += 1
            
        except OSError as error:
            print(f"Failed to move {filename}: {error}")
            failed_files +=1

    print("\n"+ "="*50)
    print("File Organization Summary")
    print("="*50)
    print(f"Files moved succesfully : {moved_files}")
    print(f"Files skipped : {skipped_files}")
    print(f"Files failed to move : {failed_files}")
    print(f"Destination folder : {destination_folder}")
    print("="*50)
    print("File organization completed successfully")

def main():
    print("="*50)
    print("JPG FILE ORGANIZER")
    print("="*50)
    print("This tool moves JPG/JPEG files into a separate folder.")

    source_folder = input("\nEnter the full path of the folder to organize:").strip().strip('\'"')

    if not source_folder:
        print("Error: Folder path cannot be empty.")
        return

    organize_jpg_files(source_folder)

if __name__ == "__main__":
    main()



