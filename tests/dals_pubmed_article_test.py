# coding=utf-8

from fform.orm_pubmed import Article

from tests.bases import DalPubmedTestBase
from tests.assets.items import create_article


class DalPubmedArticleTest(DalPubmedTestBase):

    def test_iodi_get_article(self):
        """ Tests the insertion of `Article` records via the `iodi_article`
            method of the `DalPubmed` class and its retrieval via the `get`
            method.
        """

        # Create an `Article` record.
        obj_id, refr = create_article(dal=self.dal)

        # Retrieve the new record.
        obj = self.dal.get(Article, obj_id)  # type: Article

        # Assert that the different fields of the record match.
        self.assertEqual(obj.article_id, obj_id)
        self.assertEqual(obj.publication_year, refr["publication_year"])
        self.assertEqual(obj.publication_month, refr["publication_month"])
        self.assertEqual(obj.publication_day, refr["publication_day"])
        self.assertEqual(
            obj.date_published,
            refr["date_published"],
        )
        self.assertEqual(obj.publication_model, refr["publication_model"])
        self.assertEqual(obj.journal_id, refr["journal_id"])
        self.assertEqual(obj.journal_volume, refr["journal_volume"])
        self.assertEqual(obj.journal_issue, refr["journal_issue"])
        self.assertEqual(obj.title, refr["title"])
        self.assertEqual(obj.pagination, refr["pagination"])
        self.assertEqual(obj.language, refr["language"])
        self.assertEqual(obj.title_vernacular, refr["title_vernacular"])

    def test_iodi_article_duplicate(self):
        """ Tests the insertion of duplicate `Article` records to ensure
            deduplication functions as intended.
        """

        # Create an `Article` record.
        obj_id, refr = create_article(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Create the same `Article` record as before.
        obj_id, refr = create_article(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Create a new `Article` record.
        obj_id, refr = create_article(
            dal=self.dal,
            title="New article title"
        )

        self.assertEqual(obj_id, 3)

    def test_delete_article(self):
        """Tests the deletion of an `Article` record via the `delete` method of
        the `DalPubmed` class."""

        # Create an `Article` record.
        obj_id, refr = create_article(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Article, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Article, obj_id)  # type: Article

        self.assertIsNone(obj)
