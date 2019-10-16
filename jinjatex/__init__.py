"""Jinja environment setup facilities."""

import os
import re
import pkg_resources


import jinja2


__version__ = pkg_resources.require("jinjatex")[0].version


def escape_latex(text: str) -> str:
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile(
        '|'.join(
            re.escape(str(key)) for key in sorted(conv.keys(),
                                                  key=lambda item: - len(item))
        )
    )
    return regex.sub(lambda match: conv[match.group()], text)


def escape_underscores(text: str) -> str:
    return text.replace("_", "\_")


# Jinja LaTeX environment (see here for customised, LaTeX-compatible markup)
base_conf = dict(
    block_start_string=r'\BLOCK{',
    block_end_string='}',
    variable_start_string=r'\VAR{',
    variable_end_string='}',
    comment_start_string=r'\#{',
    comment_end_string='\#}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.abspath(".")),
)


def new_env(**kwargs):
    env = jinja2.Environment(**{**base_conf, **kwargs})
    env.globals["escape_underscores"] = escape_underscores
    env.globals["escape_latex"] = escape_latex
    return env
