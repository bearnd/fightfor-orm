## Changelog

### v0.4.5

- `orm_ct.py`: Added missing schema in the `AnalysisGroup` class.

### v0.4.4

- `orm_pubmed.py`: Added schema name to the foreign key and relationship definitions.

### v0.4.3

- `orm_pubmed.py`: Fixed bug in the `CitationIdentifier` class where the unique constraint was erroneously configured.

### v0.4.2

- `orm_pubmed.py`: Fixed bug in the `ArticleAbstractText` class where the unique constraint was wrongly configured.

### v0.4.1

- `orm_pubmed.py`: Fixed bug where default enum values were not renamed.

### v0.4.0

Issue No.5: Move the `pubmed-ingester` ORM and DALs to `fightfor-orm`:

- `excs.py`: Renamed the `InvalidArguments` class to `InvalidArgumentsError`.
- `excs.py`: Added a new `MissingAttributeError` class.
- Updated the `DalFightForBase` class and removed the `get_by_md5` and `bget_by_md5s` methods which were replaced by attribute-agnostic variants.
- `orm_base.py`: Updated the `OrmBase` class and added a new `pk_name` property which returns the name of the primary-key field of the ORM class.
- `dal_base.py`: Updated the `DalFightForBase` class and added a new `order_objs_by_attr` method that orders a list of record objects by their attribute values.
- `dal_base.py`: Updated the `bget_by_attr` method of the `DalFightForBase` class to allow for sorting of the returned record objects by the attribute values.
- Added a new `orm_pubmed.py` module with the ORM classes ported from `pubmed-ingester`.
- Added a new `dals_pubmed.py` module with the DAL class ported from `pubmed-ingester` and simplified using the classes and methods under the base-classes.

### v0.3.0

- Added a new `excs.py` module with a custom exception class.
- `orm_mt.py`: Added the new synonyms tables.
- `utils.py`: Added a new decorator to check that all `list` arguments to a function are of the same length.
- `dal_base.py`: Added a new `bget_by_md5s` method to the `DalFightForBase` class to batch-retrieve objects through their MD5s.
- `dals_mt.py`: Added new methods to the `DalMesh` to upsert synonym records in a BIODI manner.

### v0.2.0

- Moved the CT ORM enums to `orm_ct.py` and removed `orm_enums.py`.
- Added a new `DalFightForBase` class to `dal_base.py` and had `DalClinicalTrials` inherit from that.
- Updated Python dependencies.
- Moved the `mt-ingester` ORMs and DALs to new modules under this project.

### v0.1.0

- Initial release.
