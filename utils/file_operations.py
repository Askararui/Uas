import os
import shutil

def sort_files(folder_path, action="move"):
    """
    Sort files in the given folder into appropriate subdirectories.
    
    Args:
        folder_path (str): Path to the folder containing files to sort
        action (str): Either "move" to move files or "copy" to copy them
        
    Returns:
        int: Number of files processed
    """
    folders = {
        '📷 Gambar': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'],
        '📄 Dokumen': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.xls', '.ppt'],
        '🎥 Video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
        '🎵 Musik': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg'],
        '📦 Arsip': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        '📁 Lainnya': []
    }

    # Create destination folders if they don't exist
    for folder in folders:
        path = os.path.join(folder_path, folder)
        if not os.path.exists(path):
            os.makedirs(path)

    # Get all files in the directory
    files = [f for f in os.listdir(folder_path) 
             if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        return 0

    moved_count = 0

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        _, ext = os.path.splitext(file_name)
        moved = False

        for folder, extensions in folders.items():
            if ext.lower() in extensions:
                dest = os.path.join(folder_path, folder, file_name)
                if action == "move":
                    shutil.move(file_path, dest)
                else:
                    shutil.copy2(file_path, dest)
                moved = True
                break

        if not moved:
            dest = os.path.join(folder_path, '📁 Lainnya', file_name)
            if action == "move":
                shutil.move(file_path, dest)
            else:
                shutil.copy2(file_path, dest)

        moved_count += 1

    return moved_count
