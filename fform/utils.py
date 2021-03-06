# -*- coding: utf-8 -*-

import enum

from fform.excs import InvalidArgumentsError


class EnumBase(enum.Enum):
    """Enumeration base-class."""

    @classmethod
    def get_member(
        cls,
        value: str,
    ):
        """Returns an enumeration member with a value matching `value`.

        Args:
            value (str): The value of the member to match.

        Returns:
            The matching member or `None` if `value` is undefined or no member
                was found.
        """

        if not value:
            return None

        members = [
            (member, member.value)
            for member in cls.__members__.values()
        ]
        for member, member_value in members:
            if member_value == value:
                return member

        return None


def return_first_item(func):
    """Decorator that can be used to return the first item of a callable's
    `list` return."""

    # Define the wrapper function.
    def wrapper(self, *args, **kwargs):

        # Execute the decorated method with the provided arguments.
        result = func(self, *args, **kwargs)

        # If the function returned a result and that result is a list then
        # return the first item on that list.
        if result and isinstance(result, list):
            result = result[0]

        return result

    return wrapper


def lists_equal_length(func):
    """Decorator that ensures all ``list`` objects in a method's arguments
    have the same length"""
    # Define the wrapper function.
    def wrapper(self, *args, **kwargs):

        # Collect all `list` objects from `args`.
        lists_args = [arg for arg in args if isinstance(arg, list)]
        # Collecgt all `list` object from `kwargs`.
        lists_kwargs = [arg for arg in kwargs.values() if isinstance(arg, list)]
        # Concatenate the lists of `list` objects.
        lists = lists_args + lists_kwargs

        # Check whether all the `list` objects have the same length.
        do_have_same_length = len(set(map(len, lists))) == 1

        # Raise an `InvalidArgumentsError` exception if there's a length
        # mismatch.
        if not do_have_same_length:
            msg_fmt = "The argument lists must have the same length."
            raise InvalidArgumentsError(msg_fmt)

        # Simply execute the decorated method with the provided arguments
        # and return the result.
        return func(self, *args, **kwargs)

    return wrapper
