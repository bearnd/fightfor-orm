## Changelog

### v0.12.3

- Renamed all enumeration classes to remove the word ‘type’ as it conflicts with auto-generated classes in Graphene-SQLAlchemy.

### v0.12.2

- Updated the enumeration classes so that their values are lowercased and are using underscores instead of dashes. This is so that the values match those in PostgreSQL.

### v0.12.1

- Fixed bug in the `iodu_study_facility` method of the `DalClinicalTrials` class.

### v0.12.0

- Added a new ORM `AffiliationCanonical` class which will be used to store canonicalized affiliations.
- Added a foreign-key column to the `affiliations_canonical` table under the `affiliations` table.
- Added a foreign-key column to the `affiliations_canonical` table under the `article_authors_affiliations` table.
- Added an `affiliations_canonical` relationship to the `Article` class.
- Added a new `iodu_affiliation_canonical` method to the `DalPubmed` class to store `AffiliationCanonical` records.
- Updated the methods of the `DalPubmed` class to store foreign-keys to the `affiliations_canonical` table.
- Added unit-tests for the new `AffiliationCanonical` class.

### v0.11.3

- Updated the `iodu_facility_canonical` method of the `DalClinicalTrials` class to only assemble the coordinates point expression if coordinates have been defined.

### v0.11.2

- Updated the `iodu_facility_canonical` method to only require the `google_place_id` argument.

### v0.11.1

- Updated the `FacilityCanonical` ORM class and set all columns but `google_place_id` to nullable so that the place ID can be populated separately to the rest of the details.

### v0.11.0

- Updated the `Study` class and added an index to the `start_date` column.
- Updated the `Eligibility` class and added an index to the `gender` column.

### v0.10.3

- Updated the `Citation` class and added `descriptors` and `qualifiers` relationships.

### v0.10.2

- Prefixed the PubMed ORM classes `Keyword`, `Descriptor`, and `Qualifier` with `Pm` to distinguish them from the classes of the same name in other schemata as the conflicting names are causing issues in `fightfor-graphql`.

### v0.10.1

- Added a `iodu_study_facility` method to the `DalClinicalTrials` class to create a new `StudyFacility` record in an IODU manner.

### v0.10.0

- Updated Python dependencies.
- Updated the Ansible role to install the PostGIS extension to the PostgreSQL server.
- Added a new `FacilityCanonical` ORM class to store canonicalised facilities.
- Added a new `StudyFacility` ORM class to represent an associative table between `studies`, `facilities`, and `facilities_canonical`.
- Updated the `Facility` class and added a new foreign-key to a `FacilityCanonical` record as well as a corresponding relationship.
- Updated the `Facility` class and added a relationship to a list of `Study` records through the new `study_facilities` table.
- Updated the `Facility` class and added indices to the `city`, `state`, and `country` columns.
- Updated the `Facility` class and added a relationship to a list of `Study` records through the new `study_facilities` table.
- Updated the `Study` class and added relationships to the `Facility` and `FacilityCanonical` records.
- Updated the `DalClinicalTrials` class and added a new `iodu_facility_canonical` method to upsert `FacilityCanonical` records.
- Added unit-tests for the new `FacilityCanonical` table.

### v0.9.1

- Fixed typo in `Study` class where the `eligibility` relationship was spelled as `elligibility`.

### v0.9.0

- Refactored the entire Ansible role and updated it to create PostgreSQL schemata to be used for unit-testing and local development.
- Updated the `Study` and `StudyMeshTerm` classes and added a relationship between them. In addition, added a relationship to `MeshTerm` in `StudyMeshTerm`.

### v0.8.2

- Updated `Makefile` to run the unit-tests properly using `unittest`.
- Updated `.gitignore`.
- Cleaned up Ansible role.

### v0.8.1

- `orm_ct.py`: Updated the `Location` class and added a relationship to the `Facility` class.

### v0.8.0

Issue No.2: Improper unique-ing and study-updates (Round 02):
- `orm_base.py`: Added a new `OrmFightForBase` class and moved the primary-key retrieval methods to that class instead of `OrmBase`.
- `orm_base.py`: Added a new `calculate_md5` method to the `OrmFightForBase` class to calculate an MD5 hash out of the values of an attribute dictionary. This method will be used to calculate MD5 fields for the different ORM classes that depend on MD5 to signify record uniqueness.
- `orm_ct.py`: Updated all ORM classes to derive the new `OrmFightForBase` class instead of `OrmBase`.
- `orm_mt.py`: Updated all ORM classes to derive the new `OrmFightForBase` class instead of `OrmBase`.
- `orm_pubmed.py`: Updated all ORM classes to derive the new `OrmFightForBase` class instead of `OrmBase`.
- `orm_ct.py`: Updated the `update_md5` method in all corresponding ORM classes to use the `calculate_md5` method of the `OrmFightForBase` class instead of calculating the MD5 individually.
- `orm_mt.py`: Updated the `update_md5` method in all corresponding ORM classes to use the `calculate_md5` method of the `OrmFightForBase` class instead of calculating the MD5 individually.
- `orm_pubmed.py`: Updated the `update_md5` method in all corresponding ORM classes to use the `calculate_md5` method of the `OrmFightForBase` class instead of calculating the MD5 individually.


### v0.7.3

- Updated all `md5` fields and changed their type to a 16-byte `LargeBinary` instead of a `Binary` which is now deprecated.
- `orm_ct.py`: Updated the `Location` class and replaced the FK unique constraint with an MD5 field as the contact FKs are nullable and NULL values are not considered unique in PostgreSQL.
- `dals_ct.py`: Updated the `iodu_location` method of the `DalClinicalTrials` class to reflect the replacement of the FK unique constraint with an MD5.
- Added a new `tests.dals_ct_location_test.py` module with unit-tests for the `Location` ORM class and its corresponding methods under the `DalClinicalTrials` class.

### v0.7.2

- `dals_ct.py`: Typing fixes.
- `excs.py`: Fixed typo.
- `excs.py`: Added a new `RecordMissingError` exception class.
- `dal_base.py`: Typing fixes in the `DalFightForBase` class methods.
- `dal_base.py`: Updated the `DalFightForBase` class and added a `update_attr_value` method to update the value of a specific attribute of a specific record.
- `dals_ct_condition_test.py`: Added a unit-test to test the newly added `update_attr_value` method.

### v0.7.1

- `dals_ct.py`: Fixed bug in the `iodi_intervention` method of the `DalClinicalTrials` class where the upsert wasn’t including the MD5 field or the correct way to retrieve the PK.
- Added a new `tests.dals_ct_intervention_test.py` module with unit-tests for the `Intervention` ORM class and its corresponding methods under the `DalClinicalTrials` class.

### v0.7.0

Issue No.48: Update `fightfor-orm` with Vagrant+Ansible deployment in order to allow unit-testing:

- `.gitignore`: Added the `.ansible-vault-password` file.
- Added a `Vagrantfile` and a development-only Ansible role so that the package can be tested in a VM with a local PostgreSQL instance.
- Removed the unit-test placeholder.
- `dals_ct.py`: Fixed bug in the `iodi_facility` method of the `DalClinicalTrials` where the name was passed as a tuple due to a trailing comma.
- `dals_ct.py`: Updated the `DalClinicalTrials` class and replaced any calls to `get_by_md5` with `get_by_attr` as the former has been removed.

Issue No.2: Improper unique-ing and study-updates:

- Removed tables that aren’t actively used in the clinical-trials ingestion.
- Added MD5 calculation and unique-constraints to tables that were missing uniqueness constraints before.
- Added lowercasing to MD5 calculations to preclude duplication when case isn’t well defined.
- `dals_ct.py`: Updated the `DalClinicalTrials` class and removed unused methods.
- `dals_ct.py`: Updated the `iodi_location` method of the `DalClinicalTrials` class and converted from IODI to IODU including renaming the method.
- `dals_ct.py`: Updated the `iodi_reference` method of the `DalClinicalTrials` class and converted from IODI to IODU including renaming the method.
- `dals_ct.py`: Updated the `iodi_study` method of the `DalClinicalTrials` class and converted from IODI to IODU including renaming the method.
- `dals_ct.py`: Updated the `iodi_study_sponsor` method of the `DalClinicalTrials` class and converted from IODI to IODU including renaming the method.
- `dals_ct.py`: Updated the `iodi_study_outcome` method of the `DalClinicalTrials` class and converted from IODI to IODU including renaming the method.
- `dals_ct.py`: Updated the `iodi_study_reference` method of the `DalClinicalTrials` class and converted from IODI to IODU including renaming the method.
- `dals_ct.py`: Updated the `iodi_study_mesh_term` method of the `DalClinicalTrials` class and converted from IODI to IODU including renaming the method.
- `orm_base.py`: Updated the `OrmBase` class and added class-methods and properties to retrieve the primary-key name and attribute of the ORM class.
- `dal_base.py`: Updated the `DalFightForBase` class and added a `get` and a `delete` method to retrieve and delete record via its primary-key ID.
- `dals_ct.py`: Updated all IODI/IODU methods of the `DalClinicalTrials` so that the values to be inserted are first set in an object of the record to be inserted and then used in the upsert statement via the object in order to any transformations they’re meant to have to kick in, e.g., lowercasing for keywords.
- `dals_ct.py`: Updated many of the `DalClinicalTrials` methods and included typing information on the method arguments to signify which arguments correspond to nullable fields.
- Added a new `tests/utils.py` module with a basic function to load configuration settings for unit-testing.
- Added a new `tests/bases.py` module with unit-test base-classes.
- Added a new `tests.dals_ct_sponsor.py` module with unit-tests for the `Sponsor` ORM class and its corresponding methods under the `DalClinicalTrials` class.
- Added a new `tests.dals_ct_contact.py` module with unit-tests for the `Contact` ORM class and its corresponding methods under the `DalClinicalTrials` class.
- `orm_ct.py`: Updated the `update_md5` class of the `Sponsor` class to not lowercase the attributes but rather use the lowercase versions to calculate the MD5.
- `tests/dals_ct_contact.py`: Added a unit-test to test duplication-prevention.
- Added a new `tests.dals_ct_keyword.py` module with unit-tests for the `Keyword` ORM class and its corresponding methods under the `DalClinicalTrials` class.
- Renames.
- Added a new `tests.dals_ct_facility_test.py` module with unit-tests for the `Facility` ORM class and its corresponding methods under the `DalClinicalTrials` class.
- Added a new `tests.dals_ct_person_test.py` module with unit-tests for the `Person` ORM class and its corresponding methods under the `DalClinicalTrials` class.
- Added a new `tests.dals_ct_person_test.py` module with unit-tests for the `Person` ORM class and its corresponding methods under the `DalClinicalTrials` class.

### v0.6.0

Issue No.38: Add synonym relationships to the corresponding MeSH entity classes:

- `orm_my.py`: Added relationships between the synonym tables and the MeSH entity tables they refer to.

### v0.5.0

Issue No.33: Remove the `concept_synonyms` table:

- `orm_mt.py`: Removed the `ConceptSynonym` class (and therefore the `concept_synonyms` table).
- `dals_mt.py`: Removed the `biodi_concept_synonyms.py` method from the `DalMesh` class.

Issue No. 35: Add `pg_tgrm` index to synonym columns:

- `orm_mt.py`: Added Trigram indices to the remaining synonym tables.

### v0.4.6

- `orm_mt.py`: Added a new `SupplementalSynonym` class representing a new `supplemental_synonyms` table to store synonyms for `Supplemental` entities.
- `dals_mt.py`: Added a new `biodi_supplemental_synonyms` method to the `DalMesh` class to store `SupplementalSynonym` records.

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
