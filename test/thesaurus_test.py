"""thesaurus_test.py - test classes for thesaurus module

This file is part of cMonkey Python. Please see README and LICENSE for
more information and licensing details.
"""
import unittest
import thesaurus


class MockDelimitedFile1:
    """just a mocked DelimitedFile"""

    def lines(self):
        """mocked lines() method"""
        return [['alt1', 'gene1'], ['alt2', 'gene1'], ['alt3', 'gene2']]


class MockDelimitedFile2:
    """just a mocked DelimitedFile"""

    def lines(self):
        """mocked lines() method"""
        return [['gene1', 'alt1;alt2'], ['gene2', 'alt3']]


class MockRsatFeatureNameFile:
    """a mocked RSAT feature names delimited file"""

    def lines(self):
        """mocked lines() method"""
        return [['NAME1', 'NAME1', 'primary'], ['NAME1', 'ALT1', 'alternate'],
                ['NAME2', 'NAME2', 'primary']]


class DelimitedFileFactoryTest(unittest.TestCase):  # pylint: disable-msg=R0904
    """Test class for DelimitedFileThesaurusFactory"""

    def test_create_from_delimited_file1(self):
        """test the delimited file simple version"""
        thes = thesaurus.create_from_delimited_file1(MockDelimitedFile1())
        self.assertEquals('gene1', thes['alt1'])
        self.assertEquals('gene1', thes['alt2'])
        self.assertEquals('gene2', thes['alt3'])

    def test_create_from_delimited_file2(self):
        """test the delimited file second version"""
        thes = thesaurus.create_from_delimited_file2(MockDelimitedFile2())
        self.assertEquals('gene1', thes['alt1'])
        self.assertEquals('gene1', thes['alt2'])
        self.assertEquals('gene2', thes['alt3'])

    def test_create_from_rsat_feature_names(self):
        """test the creation from RSAT feature names file"""
        thes = thesaurus.create_from_rsat_feature_names(
            MockRsatFeatureNameFile())
        self.assertEquals('NAME1', thes['ALT1'])