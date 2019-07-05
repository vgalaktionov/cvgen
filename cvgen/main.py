import datetime
import subprocess
from os import PathLike
from pathlib import Path
from pprint import pprint

import click
import yaml
from cvgen.models import CV
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pydantic import ValidationError
from weasyprint import CSS, HTML


CURRENT_DIR = Path(__file__).parent
jinja2_env = Environment(
    loader=FileSystemLoader(str(CURRENT_DIR / "templates")),
    autoescape=select_autoescape(["html"]),
)


def load_data(path: PathLike, debug: bool) -> CV:
    with open(path) as f:
        data = yaml.safe_load(f)
    try:
        data = CV(**data)
        if debug:
            pprint(data)
        return data
    except ValidationError as e:
        click.echo("Input data file invalid", err=True)
        click.echo(e, err=True)
        raise


def render(data: CV, to: PathLike, debug: bool = False):
    template = jinja2_env.get_template("index.html.j2")
    rendered = template.render(
        cv=data, timestamp=datetime.datetime.now().strftime("%d-%m-%Y")
    )

    if debug:
        click.echo("Rendering template for debugging")
        with open(CURRENT_DIR / "templates" / "rendered.html", "w") as f:
            f.write(rendered)

    HTML(string=rendered).write_pdf(
        to, stylesheets=[CSS(CURRENT_DIR / "templates" / "style.css")]
    )


@click.command()
@click.argument("input_data")
@click.option("--debug/--no-debug", default=False)
def main(input_data: PathLike, debug: bool):
    click.echo("CVGen started!")

    cv = load_data(input_data, debug)
    click.echo("Data has been loaded successfully.")
    output_file = Path(f"{cv.name} CV @ {datetime.datetime.now():%d-%m-%Y}.pdf")

    click.echo(f'Rendering pdf to "{output_file}" ...')
    render(cv, output_file, debug)
    click.echo("PDF has rendered.")

    click.echo("Opening rendered pdf...")
    subprocess.Popen(["open", output_file])
