# Week 5: Make the code run outside its own folder

Module M02 · [Course lesson](../../../site/phase-1.html#w5)

## Script

Your code imports successfully because your terminal happens to be sitting beside the file. Then a scheduled job starts somewhere else and the import fails. This week, remove that accidental dependency on your current directory.

Turn your earthquake script into an installable package. Give it a `pyproject.toml` that declares a build backend, project metadata, supported Python version, and dependencies. Put the importable modules together under the `quakes` package. The package name is how Python finds your code after installation.

Separate the responsibilities. Your client handles HTTP. Your parser converts an input document into clean records. Your report writer creates the output. Your main module connects those pieces. Keep the imports flowing in that direction so the parser does not import the client and the client does not import the parser back.

A class earns its place when related operations share state. A `QuakeClient` can own a session, feed URL, and timeout. Parsing one already-downloaded feature can remain a plain function. You do not need a class for every verb. Think of the client as a reusable connection at the front desk; the individual paperwork still goes through small, independent checks.

During development, install with `python -m pip install -e .`. Editable installation makes your working source importable while you change it. It does not prove you have packaged every necessary file correctly for distribution. We test the built artifact next week.

Add a main entry point, and support `python -m quakes`. Put execution behind the main guard so importing a module does not unexpectedly download data or write a report. A teammate should be able to import your parser in a test without triggering the entire application.

Now change directories. Run the package from outside the project folder. Use an explicit output location, and use the same saved input when checking repeatability. If you call a live feed twice, changing source records can change the report even when your write policy is correct.

For your lab, show the clean environment installation, successful import, and command run from another directory. Explain why the HTTP session lives on a class, how the parser stays independent, and what the report overwrites. The useful result is a component somebody can install and call, with its dependencies written down.

## Screen example — not spoken

From the learner's package root:

```bash
python -m pip install -e .
python -c 'from quakes.client import QuakeClient; print(QuakeClient)'
cd /tmp
python -m quakes
```

Record the report's configured output location. Show that importing `quakes.parse` causes no network request or file write.
