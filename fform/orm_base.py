# coding: utf-8

from __future__ import unicode_literals

import inspect
import datetime
import binascii
import hashlib
from typing import Dict, Any

import sqlalchemy
import sqlalchemy.sql.sqltypes
import sqlalchemy.types
from sqlalchemy.sql.schema import Column

import uuid
import decimal
from sqlalchemy.ext.declarative import declarative_base


# Create schema metadata with a constraint naming convention so that all
# constraints are named automatically based on the tables and columns they're
# defined upon. This ensures that all constraints will be given a unique name
# regardless of the backend database which allows for `alembic` to create
# comprehensive migrations of the defined schemata.
metadata = sqlalchemy.MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      }
)
# create declarative base
Base = declarative_base(metadata=metadata)


class OrmBase(object):
    # take sqla type and value, produce converted value
    _sqla_types_convert = {
        bytes: lambda t, v: binascii.hexlify(v),
        sqlalchemy.types.Binary: lambda t, v: binascii.hexlify(v),
    }

    _python_instance_convert = {
        datetime.datetime: lambda v: v.isoformat() if v else None,
        datetime.date: lambda v: v.isoformat() if v else None,
        decimal.Decimal: lambda v: float(v),
        uuid.UUID: lambda v: v.hex,
    }

    @staticmethod
    def _dictify_scalar(scalar, column, serialisable=False):

        val = scalar

        # if data must be serialisable, apply conversions into base types
        if serialisable:
            # first check for conversions of the underlying column type
            col_type = None
            try:
                col_type = getattr(column, "type")
            except:
                # "col" might be a list in the case of a one to many join, skip.
                # we'll see it again when the outer loop opens the container
                pass
            if col_type:
                col_type_type = type(col_type)
                if col_type_type in OrmBase._sqla_types_convert:
                    val = OrmBase._sqla_types_convert[col_type_type](
                        col_type,
                        scalar
                    )

            # Convert (some) complex python types into base types
            for instance, converter in OrmBase._python_instance_convert.items():
                if isinstance(scalar, instance):
                    val = converter(scalar)
                    break

        return val

    def _collect_attributes(self):
        """Return {column: (type,value)}. Handles removal of any
        meta/internal data that is not from our underlying table."""

        attributes = {}

        obj_type = type(self)
        column_inspection = sqlalchemy.inspect(obj_type).c
        relationship_inspection = sqlalchemy.inspect(obj_type).relationships

        for member_name, member_value in self.__dict__.items():
            # drop magic sqla keys.
            if member_name.startswith("_"):
                continue

            if (
                    inspect.isfunction(member_value) or
                    inspect.ismethod(member_value)
            ):
                continue

            if member_name in column_inspection:
                member_inspection = column_inspection[member_name]
            elif member_name in relationship_inspection:
                member_inspection = relationship_inspection[member_name]
            else:
                continue

            attributes[member_name] = (member_inspection, member_value)

        return attributes

    def to_dict(self, deep=False, serialisable=False):

        results = {}

        # walk top level
        attributes = self._collect_attributes()
        for attr_name, (attr_column, attr_value) in attributes.items():

            # if value is compound type and deep=True
            # recursively collect contents.
            if isinstance(attr_value, OrmBase):
                if not deep:
                    continue
                val = attr_value.to_dict(
                    deep=deep,
                    serialisable=serialisable
                )

            elif isinstance(attr_value, list):
                if not deep:
                    continue

                val = []
                for sub_attr_value in attr_value:
                    val.append(sub_attr_value.to_dict(
                        deep=deep,
                        serialisable=serialisable
                    ))

            elif isinstance(attr_value, dict):
                if not deep:
                    continue

                val = {}
                for sub_attr_name, sub_attr_value in attr_value.items():
                    val[sub_attr_name] = sub_attr_value.to_dict(
                        deep=deep,
                        serialisable=serialisable
                    )

            # value if scalar, perform any final conversions
            else:
                val = self._dictify_scalar(
                    scalar=attr_value,
                    column=attr_column,
                    serialisable=serialisable
                )

            results[attr_name] = val

        return results

    def to_string(self, deep=False):
        """"""

        attributes = self._collect_attributes()

        msg = "<{0}("
        for attr_idx, attr_name in enumerate(attributes.keys()):
            msg += attr_name + "='{" + str(attr_idx + 1) + "}'"
            if attr_idx < len(attributes) - 1:
                msg += ", "
        msg += ")>"

        values = [type(self).__name__]

        for attr_name, (attr_column, attr_value) in attributes.items():

            if isinstance(attr_value, OrmBase):
                if not deep:
                    val = "<{0}()>".format(type(attr_value).__name__)
                else:
                    val = attr_value.to_string(deep=deep)
            else:
                val = self._dictify_scalar(
                    scalar=attr_value,
                    column=attr_column,
                    serialisable=True
                )

            values.append(val)

        return msg.format(*values)

    def __repr__(self):
        return self.to_string(deep=False)


class OrmFightForBase(OrmBase):

    @classmethod
    def get_pk(cls) -> Column:
        """Returns the class' primary-key attribute.

        Returns:
            Column: The class' primary-key attribute.
        """

        pk = sqlalchemy.inspect(cls).primary_key[0]

        return pk

    @classmethod
    def get_pk_name(cls) -> str:
        """Returns the name of the class' primary-key field.

        Returns:
            str: The name of the class' primary-key field.
        """

        pk = cls.get_pk()

        return pk.name

    @property
    def pk(self) -> Column:
        """Returns the class' primary-key attribute.

        Returns:
            Column: The class' primary-key attribute.
        """

        return self.get_pk()

    @property
    def pk_name(self) -> str:
        """Returns the name of the class' primary-key field.

        Returns:
            str: The name of the class' primary-key field.
        """

        pk = self.get_pk()

        return pk.name

    @staticmethod
    def calculate_md5(
        attrs: Dict[str, Any],
        do_lowercase=False,
    ) -> bytes:
        """Calculates the MD5 hash of the concatenated values of a `dict`
        ordered by the sorted `dict` keys.

        This method takes a `dict` of name:value pairs, sorts the dictionary
        keys, and uses the sorted keys to concatenate the `dict` values into a
        single string, over which it then calculates an MD5 hash.

        Args:
            attrs (Dict[str, Any]): The dictionary of name:value pairs over
                which the hash will be calculated
            do_lowercase (bool, optional): Whether to calculate the hash on the
                lowercased version of the concatenated values. Defaults to
                `False`.

        Returns:
            bytes: The binary digest of the calculated MD5 hash.
        """

        # Sort the attribute names.
        keys_sorted = sorted(attrs.keys())

        # Concatenate the attribute values in order of the ordered keys.
        values_concatenated = " ".join([str(attrs[key]) for key in keys_sorted])

        # Lowercase the concatenated values (if required).
        if do_lowercase:
            values_concatenated = values_concatenated.lower()

        # Encode the concatenated values to UTF8.
        values_encoded = values_concatenated.lower().encode("utf-8")

        # Calculate the MD5 hash and retrieve the binary digest.
        md5 = hashlib.md5(values_encoded).digest()

        return md5
