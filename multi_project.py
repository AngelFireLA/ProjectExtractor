import os

import single_project

projects_folder1 = r'C:\Dev\Python'
final_file = 'final_file.txt'
excluded_folders = ["archives"]
final_file_content = """"""
for folder in os.listdir(projects_folder1):
    print(folder)
    if folder in excluded_folders:
        continue
    project_folder = os.path.join(projects_folder1, folder)
    file_content = single_project.main(project_folder, final_file)
    #count lines
    file_content_line_count = file_content.count('\n')
    if file_content_line_count > 1000:
        print(f"{folder} has many lines, file_content_line_count: {file_content_line_count}")
    final_file_content += file_content

with open(final_file, 'a', encoding='utf-8') as f_out:
    f_out.write(final_file_content)
    f_out.write('\n\n')

projects_folder2 = r'C:\Dev\Python\archives'
final_file = 'final_file.txt'
excluded_folders = ["archives"]
print("\n")
for folder in os.listdir(projects_folder2):
    print(folder)
    if folder in excluded_folders:
        continue
    project_folder = os.path.join(projects_folder2, folder)
    file_content = single_project.main(project_folder, final_file)
    #count lines
    file_content_line_count = file_content.count('\n')
    if file_content_line_count > 1000:
        print(f"{folder} has many lines, file_content_line_count: {file_content_line_count}")
    with open(final_file, 'a', encoding='utf-8') as f_out:
        f_out.write(file_content)
        f_out.write('\n\n')