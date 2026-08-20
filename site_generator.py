import base64
import json
import os
import shutil
import sys

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('site_generator', 'templates'),
    autoescape=select_autoescape()
)
page_template = env.get_template("page.html.jinja")

def generate_site():
    if os.path.exists("out"):
        shutil.rmtree("out")
    os.mkdir("out")
    for page in os.scandir("pages"):
        if page.is_dir():
            item_files_map = {}
            for item_file in os.scandir(page.path):
                if item_file.is_file():
                    item_files_map[item_file.name] = item_file
            required_files = ["back.png", "front.png", "info.json"]
            for item_file_name in item_files_map.keys():
                if item_file_name in required_files:
                    required_files.remove(item_file_name)
            if  len(required_files) > 0:
                required_filenames = ", ".join(required_files)
                print(f"Error parsing page {page.name}: Missing required file(s) {required_filenames}", file=sys.stderr)
                exit(1)

            back_image_base64 = None
            front_image_base64 = None
            info_json = None
            with open(item_files_map["info.json"].path) as info_file:
                info_json = json.load(info_file)
                print(info_json)
            with open(item_files_map["back.png"].path, "rb") as image_file:
                back_image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            with open(item_files_map["front.png"].path, "rb") as image_file:
                front_image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            with open(f"out/{page.name}.html", "w") as page_file:
                page_file.write(page_template.render(back_image=back_image_base64, front_image=front_image_base64, info=info_json))
                page_file.flush()

    # TODO: GitHub CI to automatically run this file when a new commit is made, publishing the resulting out directory straight to GitHub Pages!
    # TODO: Style the template
    # TODO: Homepage with navigation to the sub-pages?

if __name__ == "__main__":
    generate_site()