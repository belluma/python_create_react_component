#!/usr/bin/python3

import sys
import os



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
    file.write("\n")
    file.write("//component imports\n")
    file.write("\n")
    file.write("//interface imports\n")
    file.write("\n")
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
    file.write("import {render, screen} from '@testing-library/react';\n")
    file.write(f"import {file_name} from './{file_name}';\n")
    file.write("\n")
    file.write("\n")
    file.write("it('renders without crashing', () => {\n")
    file.write(f"    render(<{file_name} />);")
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

for component in components:
    if len(sys.argv) < 3:
        print("not enough arguments given")
        break
    create_files(component)
