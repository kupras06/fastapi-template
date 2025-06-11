"""Helpers Module"""
import datetime


def get_current_timestamp():
    """Get Current Timestamp"""
    return datetime.datetime.now(datetime.UTC)  # type: ignore
