#!/usr/bin/env python3
"""
Take the sources from lib/builtins/ and embed them into an OCaml file.
"""

def read_file_to_string(path: str) -> str:
    with open(path, "r") as stream:
        return stream.read()

pervasive_int: str = read_file_to_string("lib/builtin/Pervasive.aui")
pervasive_body: str = read_file_to_string("lib/builtin/Pervasive.aum")
memory_int: str = read_file_to_string("lib/builtin/Memory.aui")
memory_body: str = read_file_to_string("lib/builtin/Memory.aum")

contents: str = f"""
let pervasive_interface_source: string = {{code|
{pervasive_int}
|code}}

let pervasive_body_source: string = {{code|
{pervasive_body}
|code}}

let memory_interface_source: string = {{code|
{memory_int}
|code}}

let memory_body_source: string = {{code|
{memory_body}
|code}}
"""

with open("lib/BuiltInModules.ml", "w") as stream:
    stream.write(contents)
