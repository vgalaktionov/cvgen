import datetime
import subprocess
from os import PathLike
from pathlib import Path

import click
import yaml
from cvgen.models import CV
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pydantic import ValidationError
from weasyprint import CSS, HTML


jinja2_env = Environment(
    loader=FileSystemLoader("./templates"), autoescape=select_autoescape(["html"])
)


def load_data(path: PathLike) -> CV:
    with open(path) as f:
        data = yaml.safe_load(f)
    try:
        data = CV(**data)
        return data
    except ValidationError as e:
        click.echo("Input data file invalid", err=True)
        click.echo(e, err=True)
        raise


def render(data: CV, to: PathLike):
    template = jinja2_env.get_template("index.html.j2")
    rendered = template.render(
        cv=data, timestamp=datetime.datetime.now().strftime("%d-%m-%Y")
    )
    HTML(string=rendered).write_pdf(to, stylesheets=[CSS("./templates/style.css")])


@click.command()
@click.argument("input_data")
def main(input_data: PathLike):
    click.echo("CVGen started!")
    cv = load_data(input_data)
    click.echo("Data has been loaded successfully.")
    output_file = Path(f"{cv.name} CV @ {datetime.datetime.now():%d-%m-%Y}.pdf")

    click.echo(f'Rendering pdf to "{output_file}" ...')
    render(cv, output_file)
    click.echo("PDF has rendered.")
    subprocess.Popen(["open", output_file])
