## Changelog

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
