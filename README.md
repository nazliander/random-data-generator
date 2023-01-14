# Random Data Generator

This is a mock application that aims to provide random data for API calls or Kafka applications.

You can use the mock application for your tutorials. It provides a CLI interface and a basic Flask setup.

## Example Cases

To install the project:

```bash
pip install poetry && poetry export --output=requirements.txt && pip install -e .
```

You can then start using the CLI tool:

```bash
data-producer payouts
```

Docker is also available as in:

```bash
docker build . -t random-data-generator 
docker run --name data-generator --rm -it random-data-generator data-producer payouts
```
