import os
import shutil
import pathlib
from textnode import TextNode, TextType
from markdown_to_htmlnode import markdown_to_html_node


def clean_up_dest(dest):
    shutil.rmtree(dest)
    os.mkdir(dest)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_content = os.listdir(dir_path_content)
    for item in dir_content:
        print(f"source: {dir_path_content}")
        print(f"dest: {dest_dir_path}")
        print(f"template: {template_path}")
        print(f"item: {item}")
        is_file = os.path.isfile(os.path.join(dir_path_content, item))
        file_path = pathlib.Path(os.path.join(dir_path_content, item))
        if not is_file and not os.path.exists(os.path.join(dest_dir_path, item)):
            os.mkdir(os.path.join(dest_dir_path, item))
            generate_pages_recursive(
                os.path.join(dir_path_content, item),
                template_path,
                os.path.join(dest_dir_path, item),
            )
        # if not file_path.suffix == ".md":
        # raise Exception("Non..")
        else:
            html_filename = file_path.with_suffix(".html").name
            dest_file_path = os.path.join(dest_dir_path, html_filename)
            generate_page(
                os.path.join(dir_path_content, item), template_path, dest_file_path
            )


def source_to_dest(source, dest):
    dir_content = os.listdir(source)  # ["/folder", 'file.txt']
    for item in dir_content:
        print(f"source: {source}")
        print(f"dest: {dest}")
        print(f"item: {item}")
        is_file = os.path.isfile(os.path.join(source, item))
        if not is_file and not os.path.exists(os.path.join(dest, item)):
            os.mkdir(os.path.join(dest, item))
            source_to_dest(os.path.join(source, item), os.path.join(dest, item))
        else:
            shutil.copy(os.path.join(source, item), os.path.join(dest, item))


def init_static(source, dest):
    if not os.path.exists(source):
        raise Exception("invalid source")
    if os.path.exists(dest):
        clean_up_dest(dest)
    else:
        os.mkdir(dest)
    source_to_dest(source, dest)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        print(line)
        if line.strip().startswith("# "):
            return line.strip().strip("#").strip()
    raise Exception("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    template_file = open(template_path, "r")
    template = template_file.read()
    markdown_file.close()
    template_file.close()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    static_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # Create parent directory only
    with open(dest_path, "w") as f:
        f.write(static_page)
        f.close()


def main():
    init_static("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()
