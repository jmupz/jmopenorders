#!/usr/bin/env python
#
# Copyright (c) 2019-2020 Jürgen Mülbert. All rights reserved.
#
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
#
# Lizenziert unter der EUPL, Version 1.2 oder - sobald
#  diese von der Europäischen Kommission genehmigt wurden -
# Folgeversionen der EUPL ("Lizenz");
# Sie dürfen dieses Werk ausschließlich gemäß
# dieser Lizenz nutzen.
# Eine Kopie der Lizenz finden Sie hier:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Sofern nicht durch anwendbare Rechtsvorschriften
# gefordert oder in schriftlicher Form vereinbart, wird
# die unter der Lizenz verbreitete Software "so wie sie
# ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
# ausdrücklich oder stillschweigend - verbreitet.
# Die sprachspezifischen Genehmigungen und Beschränkungen
# unter der Lizenz sind dem Lizenztext zu entnehmen.
#
"""Console script for jmopenorders."""

import typer
from rich.console import Console

from jmopenorders import __version__

from .api import report

app = typer.Typer(
    name="jmopenorders", help="Open Orders Generator", add_completion=False,
)
console = Console()


@app.command(name="")
def version_callback(value: bool) -> None:
    """Prints the version of the Package."""
    if value:
        console.print(
            f"[yellow]jmopenorders[/] version: [bold blue]{__version__}[/]"
        )
        raise typer.Exit()


@app.command()
def main(
    inputpath: str = typer.Option(
        None,
        "-i",
        "--inputpath",
        "--ipath",
        case_sensitive=False,
        help="The Inputpath for the data",
    ),
    outputpath: str = typer.Option(
        None,
        "-o",
        "--outputpath",
        "--opath",
        help="The Outputpath for the data",
    ),
    personfile: str = typer.Option(
        None,
        "-p",
        "--personfile",
        "--persondata",
        help="The Name of the personfile",
    ),
    datafile: str = typer.Option(
        None, "-d", "--datafile", "--data", help="The Name of the datafile"
    ),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the jmopenorders package.",
    ),
) -> None:
    """Console script for jmopenorders."""
    report(personfile, datafile, inputpath, outputpath)

    return 0


# Make the module executable.
if __name__ == "__main__":
    typer.run(main)  # pragma: no cover
