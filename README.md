# CVgen

> A tool for easily creating a good-looking CV in PDF format from .yaml data, HTML & CSS.

Built with:

- Python 3
- Jinja2
- WeasyPrint
- PyYAML
- Pydantic
- Click
- Poetry

## Install

```bash
pip install cvgen
```

## Usage

CVgen expects an input YAML file in this format:

```yaml
---
name: Mr Job Man

personalia:
  phone: +31 6 1234 5678
  address: Noordeinde 68, 2514 GL Den Haag
  email: mr.job.man@gmail.com
  nationality: Dutch

experience:
  - title: Widget Engineer @ Widget Inc
    industry: widget manufacturing
    dates: April 2007 - present
    description: >-
      Various widget manufacturing tasks.

education:
  - diploma: MSc Widget Management
    institution: University of Widgetry
    dates: 2006 - 2007
    description: >-
      Various widget management topics.

skills:
  - category: Computer
    keywords:
      - Ctrl + Alt + Delete
      - Minesweeper
      - Lotus Notes

projects:
  - title: DIY widget 3D printer
    description: >-
      Made a 3D printer for widgets

activities:
  - title: Cricket player
    organization: Cricket club
    dates: 2015 - 2016
    description: >-
      Whatever cricket players do
```

Run it like:

```bash
$ cvgen [input_file]
```

## Contributing

PRs accepted for additional templates/styles/features.

To build & publish to PyPI:

```bash
$ poetry build && poetry publish
```

## License

MIT © Vadim Galaktionov
