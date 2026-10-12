# MP1 Data Pipeline

## Pipeline Overview:

This pipeline is a command-line program that loads a CSV file, validates it, cleans it, and saves the result. `pipeline.py` helps run everything in order, while code helping is stored in the `src/` folder. `utils.py` sets up logging and checks file paths, and `data_loaders.py` reads CSV, JSON, and YAML files. `data_validator.py` checks for required columns and removes non-numeric values, and `data_processor.py` removes duplicates, missing values, and outliers. `data_output.py` saves the cleaned data, and all column names and settings come from `config/config.yaml`, so the code works on other datasets.

## Example Input
```
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

## Example Output

```
23:23:33 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, config=config/config.yaml, output=output/clean.csv
23:23:33 INFO     src.utils — Input file validated: fixtures/sample_data.csv
23:23:33 INFO     src.utils — Input file validated: config/config.yaml
23:23:33 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv (100 rows)
23:23:33 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
23:23:33 WARNING  src.data_validator — A non-numeric value was found in 'rating' at index 94: not_available
23:23:33 WARNING  src.data_validator — A non-numeric value was found in 'rating' at index 95: error
23:23:33 DEBUG    src.data_validator — Validated DataFrame: 98 rows, and 2 rows removed
23:23:33 INFO     __main__ — Validation finished: 100 rows before, 98 rows after
23:23:33 DEBUG    src.data_processor — Removed duplicates: 98 rows to 96 rows
23:23:33 DEBUG    src.data_processor — Removed missing rows: 96 rows to 94 rows
23:23:33 DEBUG    src.data_processor — rating: method=iqr, threshold=1.5, lower=43.625, upper=106.625, removed=2
23:23:33 INFO     __main__ — Processing finished: 98 rows to 92 rows
23:23:33 DEBUG    src.data_output — Saved 92 rows to output/clean.csv
23:23:33 INFO     __main__ — Saved cleaned data to output/clean.csv
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```
