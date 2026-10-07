# data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logger.info(f"Removed duplicates: {before - after} rows dropped.")


def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""
    if axis == "rows":
        before = len(df)
        df = df.dropna(axis=0)
        after = len(df)
        logger.info(f"Removed missing values: {before - after} rows dropped.")
    elif axis == "columns":
        before = len(df.columns)
        df = df.dropna(axis=1)
        after = len(df.columns)
        logger.info(f"Removed missing values: {before - after} columns dropped.")
    else:
        logger.error(f"Invalid axis: {axis}")

def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    for column in columns:
        if method == "zscore":
            mean = df[column].mean()
            std = df[column].std()
            z_scores = (df[column] - mean) / std
            before = len(df)
            df = df[abs(z_scores) < threshold]
            after = len(df)
            logger.info(f"Outliers removed from {column}: {before - after} rows dropped.")
        elif method == "iqr":
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            before = len(df)
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
            after = len(df)
            logger.info(f"Outliers removed from {column}: {before - after} rows dropped.")
        else:
            logger.error(f"Unknown method: {method}")


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    if config.get("remove_duplicates", False):
        remove_duplicates(df)
    if config.get("handle_missing", False):
        axis = config.get("missing_axis", "rows")
        handle_missing(df, axis=axis)
    if config.get("remove_outliers", False):
        col = config.get("outlier_columns", [])
        method = config.get("outlier_method", "zscore")
        threshold = config.get("outlier_threshold", 3)
        remove_outliers(df, columns=col, method=method, threshold=threshold)


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    return {
        "rows_before": len(df_before),
        "rows_after": len(df_after),
        "rows_removed": len(df_before) - len(df_after),
        "columns_before": len(df_before.columns),
        "columns_after": len(df_after.columns),
        "columns_removed": len(df_before.columns) - len(df_after.columns),
    }
