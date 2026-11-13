import os
import argparse


def list_files_in_folder(folder_path, recursive=False, extensions=None):
    """Returns a list of files in the folder with optional recursion and filtering."""
    file_list = []

    try:
        paths = (
            os.walk(folder_path)
            if recursive
            else [(folder_path, [], os.listdir(folder_path))]
        )

        for root, directories, files in paths:
            directories.sort(key=str.casefold)
            files.sort(key=str.casefold)

            for file in files:
                if extensions and not file.lower().endswith(tuple(extensions)):
                    continue  # Skip files that don’t match the specified extensions
                file_list.append(os.path.join(root, file) if recursive else file)

        return file_list, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
    except NotADirectoryError:
        return None, "Not a directory"
    except OSError as e:
        return None, f"OS error: {e}"


def main():
    parser = argparse.ArgumentParser(
        description="List files in a folder with optional recursion and filtering."
    )
    parser.add_argument("folders", nargs="+", help="Folder paths to scan")
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="List files recursively"
    )
    parser.add_argument(
        "-e", "--extensions", nargs="*", help="Filter by file extensions (e.g., .txt .py)"
    )

    args = parser.parse_args()

    for folder_path in args.folders:
        print(f"\n📂 Checking: {folder_path}")
        files, error_message = list_files_in_folder(
            folder_path, args.recursive, args.extensions
        )

        if files:
            print(f"📄 Files in '{folder_path}':")
            for file in files:
                print(f"  - {file}")
            print(f"✅ Total files found: {len(files)}")
        else:
            print(f"❌ Error in '{folder_path}': {error_message}")


if __name__ == "__main__":
    main()
