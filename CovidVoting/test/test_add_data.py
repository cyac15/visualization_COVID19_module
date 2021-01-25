"""This module has tests for add_data.py
class TestAddData(unittest.TestCase)
test_oneshot(self)
test_smoke(self)
test_edge(self)
"""
import unittest
import sys
import pandas as pd
from CovidVoting.add_data import (add_data_csv)
sys.path.append('..')

# Define all states
all_states = ["Maryland", "Iowa", "Delaware", "Ohio",
              "Pennsylvania", "Nebraska", "Washington",
              "Alabama", "Arkansas", "New Mexico", "Texas",
              "California", "Kentucky", "Georgia", "Wisconsin",
              "Oregon", "Missouri", "Virginia", "Tennessee",
              "Louisiana", "New York", "Michigan", "Idaho",
              "Florida", "Illinois", "Montana", "Minnesota",
              "Indiana", "Massachusetts", "Kansas", "Nevada", "Vermont",
              "Connecticut", "New Jersey", "District of Columbia",
              "North Carolina", "Utah", "North Dakota", "South Carolina",
              "Mississippi", "Colorado", "South Dakota", "Oklahoma", "Wyoming",
              "West Virginia", "Maine", "New Hampshire", "Arizona",
              "Rhode Island"]

class TestAddData(unittest.TestCase):
    """
    This class defines the tests for add_data_csv
    """

    def test_smoke_add_data_csv(self):
        """smoke test"""
        base_data = "./data/raw_2_covid_latest.csv"
        new_data = "./data/use_election.csv"
        base_state_col = 'State/Territory'
        new_state_col = 'state'
        use_state = all_states
        how_join = 'right'
        df_covid_election = add_data_csv(base_data, new_data, base_state_col,
                                         new_state_col, use_state, how_join)
        self.assertIsNotNone(df_covid_election)


    def test_oneshot_add_data_csv(self):
        """oneshot test"""
        base_data = "./data/raw_2_covid_latest.csv"
        new_data = "./data/use_election.csv"
        base_state_col = 'State/Territory'
        new_state_col = 'state'
        use_state = all_states
        how_join = 'right'
        df_covid_election = add_data_csv(base_data,
                                         new_data, base_state_col,
                                         new_state_col, use_state,
                                         how_join)
        pd.testing.assert_frame_equal(df_covid_election, merge_covid_election)


    def test_edge_add_data_csv(self):
        """Edge Tests
        Args:
            self
        Returns:
            True: Test passed
            False: Test failed
        """
        base_data = "./data/raw_2_covid_latest.csv"
        new_data = "./data/use_election.csv"
        base_state_col = "wrongname"
        new_state_col = 'state'
        use_state = all_states
        how_join = 'right'
        with self.assertRaises(KeyError):
            add_data_csv(base_data, new_data, base_state_col,
                         new_state_col, use_state, how_join)


if __name__ == '__main__':
    unittest.main()
