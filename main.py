import os

# Configurable variables
project_folder = r'C:\Dev\Python\StreamBattle-du-bled'  # Path to the project folder
exclude_file_names = ['README.md', '.env', '.gitignore']
exclude_file_extensions = ['.pyc']
exclude_folder_names = ['.git', '.idea', '.venv', '__pycache__']
extractable_extensions = ['.py', '.js', '.html', '.css']
output_file = 'project_extracted.txt'

extension_language_map = {
    '.py': 'python',
    '.js': 'javascript',
    '.html': 'html',
    '.css': 'css'
}

project_name = os.path.basename(os.path.normpath(project_folder))


def build_file_tree_and_collect_files(root_dir, exclude_file_names, exclude_file_extensions, exclude_folder_names,
                                      extractable_extensions):
    file_tree = []
    files_to_extract = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories
        dirnames[:] = [d for d in dirnames if d not in exclude_folder_names]

        # Build the relative path for current directory
        rel_dirpath = os.path.relpath(dirpath, root_dir)

        if rel_dirpath == '.':
            rel_dirpath = ''

        indent_level = rel_dirpath.count(os.sep)
        indent = '    ' * indent_level

        # Add current directory to the file tree
        if rel_dirpath != '':
            file_tree.append(f"{indent}{os.path.basename(dirpath)}/")
        else:
            file_tree.append(f"{os.path.basename(root_dir)}/")

        # Process files
        for filename in filenames:
            filename_lower = filename.lower()
            # Exclude files by name or extension
            if (filename_lower in exclude_file_names or
                    any(filename_lower.endswith(ext) for ext in exclude_file_extensions)):
                continue

            # Add file to file tree
            file_indent = '    ' * (indent_level + 1)
            file_tree.append(f"{file_indent}{filename}")

            # Check if file has extractable extension
            if any(filename.endswith(ext) for ext in extractable_extensions):
                # Store the file path relative to root_dir
                file_rel_path = os.path.join(rel_dirpath, filename)
                files_to_extract.append(file_rel_path)

    return file_tree, files_to_extract


# Build file tree and collect files to extract
file_tree, files_to_extract = build_file_tree_and_collect_files(
    project_folder,
    exclude_file_names,
    exclude_file_extensions,
    exclude_folder_names,
    extractable_extensions
)

# Write the output file
with open(output_file, 'w', encoding='utf-8') as f_out:
    # Write project name
    f_out.write(f"{project_name}\n\n")

    # Write the file tree
    f_out.write("File Tree:\n")
    for line in file_tree:
        f_out.write(line + '\n')
    f_out.write('\n')

    # For each extractable file, write the filename and content
    for file_rel_path in files_to_extract:
        file_full_path = os.path.join(project_folder, file_rel_path)
        filename = os.path.basename(file_full_path)
        file_extension = os.path.splitext(filename)[1]
        language = extension_language_map.get(file_extension, '')

        # Read the file content
        with open(file_full_path, 'r', encoding='utf-8') as f_in:
            content = f_in.read()

        # Write the filename
        f_out.write(f"{file_rel_path} :\n")

        # Write the code block
        f_out.write(f"```{language}\n")
        f_out.write(content)
        f_out.write("\n```\n\n")
