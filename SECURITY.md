# Security

## Reporting a vulnerability

Please do not open a public issue for a security problem.

Report it privately through GitHub: open the [Security tab](https://github.com/stefanhaab/toni-sdk-python/security/advisories/new) of this repository and choose "Report a vulnerability". You get an answer within five working days.

A problem in the API or in the platform itself, not in this SDK, can be reported the same way.

## Supported versions

Fixes go into the latest release.

## Keys

- An API key (`km_live_…`) gives access to a company's data. Keep it out of the repository, out of logs and out of the browser. This SDK is meant for the server and the terminal.
- Give a key only the rights it needs. There are four: read, write, publish, delete.
- If a key leaked, revoke it in the account under "API" and create a new one.
