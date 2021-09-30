#!/usr/bin/python3

import sys
import os

if len(sys.argv) < 3:
    print("not enough arguments given")

dir_path = sys.argv[1]
if not os.path.isdir(dir_path):
    os.makedirs(dir_path)
components = sys.argv[2:]

def replace_dash(file_name):
    chars = [char for char in file_name]
    for index, char in enumerate(chars):
        if char == '-':
            chars.pop(index)
            if index < len(chars) and chars[index].isalpha():
                chars[index] =chars[index].upper()
    chars[0] = chars[0].upper()
    return ('').join(chars)

def create_component(comp_dir, file_name):
    path = f"{dir_path}/{comp_dir}/{file_name}.tsx"
    if os.path.isfile(path):
        return f"file {path} already exists"
    file = open(path, 'w')
    file.write("import React from 'react'\n")
    file.write("type Props = {};\n")
    file.write("\n")
    file.write(f"function {file_name}(props: Props){{\n")
    file.write("    return(\n")
    file.write(f"       <div>{file_name}</div>\n")
    file.write("    )\n")
    file.write("}\n")
    file.write("\n")
    file.write(f"export default {file_name};")
    file.close()
    return f"{path} created"

def create_stylesheet(comp_dir,file_name):
    path = f"{dir_path}/{comp_dir}/{file_name}.scss"
    if os.path.isfile(path):
        return f"file {path} already exists"
    file = open(path, 'w')
    file.write(f".{file_name}{{\n")
    file.write("\n")
    file.write("}")
    file.close()
    return(f"{path} created")

def create_test_file(comp_dir,file_name):
    path = f"{dir_path}/{comp_dir}/{file_name}.test.tsx"
    if os.path.isfile(path):
        return f"file {path} already exists"
    file = open(path, 'w')
    file.write("import React from 'react';\n")
    file.write("import ReactDOM from 'react-dom';\n")
    file.write(f"import {file_name} from './{file_name}';\n")
    file.write("\n")
    file.write("let container: HTMLElement | null = null;\n")
    file.write("beforeEach(() => {\n")
    file.write("    container = document.createElement('div');\n")
    file.write("    document.body.appendChild(container);\n")
    file.write("});\n")
    file.write("\n")
    file.write("afterEach(() =>{\n")
    file.write("    if(container){\n")
    file.write("    ReactDOM.unmountComponentAtNode(container);\n")
    file.write("    container.remove();\n")
    file.write("    }")
    file.write("    container = null;\n")
    file.write("})\n")
    file.write("\n")
    file.write("it('renders without crashing', () => {\n")
    file.write("    const div = document.createElement('div');\n")
    file.write(f"   ReactDOM.render(<{file_name} />, div);\n")
    file.write("    });\n")
    file.close()
    return(f"{path} created")

def create_story(comp_dir,file_name):
    path = f"{dir_path}/{comp_dir}/{file_name}.stories.tsx"
    if os.path.isfile(path):
        return f"file {path} already exists"
    file = open(path, 'w')
    file.write("import React from 'react'\n")
    file.write("import {Story, Meta} from '@storybook/react'\n")
    file.write(f"import {file_name} from './{file_name}';\n")
    file.write("\n")
    file.write("export default {\n")
    file.write(f"    component: {file_name},\n")
    file.write(f"    title: '{dir_path}/{comp_dir}/{file_name}',\n")
    file.write("} as Meta;\n")
    file.write("\n")
    file.write(f"const Template: Story = (args) => <{file_name} {{...args}} />;\n")
    file.write("\n")
    file.write(" export const Primary = Template.bind({});\n")
    file.write("\n")
    file.write("Primary.args = {\n")
    file.write("};\n")
    file.close()
    return(f"{path} created")

def create_files(component):
    x = '/'
    if dir_path[-1] == '/':
        x = ''
    comp_path = dir_path + x + component
    if not os.path.isdir(comp_path):
        os.makedirs(comp_path)
    file_name = replace_dash(component)
    print(create_component(component, file_name))
    print(create_stylesheet(component, file_name))
    print(create_test_file(component, file_name))
    print(create_story(component, file_name))

for component in components:
    create_files(component)
