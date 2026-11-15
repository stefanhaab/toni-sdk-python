# Contributing

Thanks for helping. Bug reports, questions and pull requests are welcome.

## Set up

```bash
python3 scripts/generate.py                  # rebuild src/toni_sdk/_generated from the live OpenAPI document
python3 -m unittest discover -s tests -v
```

The tests run against a small local copy of the API. They need no key and cost nothing.

## Good to know

- `src/toni_sdk/_generated` is generated from the live OpenAPI document. Change the generator in `scripts/`, not the generated files.
- The agent never sets `bestaetigt` on its own. Deleting and publishing need a human or an explicit `confirmed`. A change that weakens this will not be merged.
- Messages a user can see are in German and name no model provider.
- Keep the package free of runtime dependencies.
- A change in behaviour needs a test and a line in `CHANGELOG.md`.

## Pull requests

One topic per pull request, with a short description of what changes for the user of the SDK. CI has to be green.

## Security

Please report security problems privately, see [SECURITY.md](SECURITY.md).
