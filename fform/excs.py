# coding=utf-8

""" Custom application-wide exception classes.

This module contains custom exception classes that can be used to wrap other
exception and allow for consistent error-handling across the application.
"""


class InvalidArguments(Exception):
    """Exception raised when the arguments to a function/method call are
    invalid."""
    def __init__(self, message, *args):
        super(InvalidArguments, self).__init__(message, *args)
