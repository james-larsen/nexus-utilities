#%%
import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from nexus_utils.src.package_utils import add_package_to_path

#%%
class TestAddPackageToPath(unittest.TestCase):

    def test_add_package_to_path(self):
        """Test the add_package_to_path function of the package_utils module"""

        # Save the current working directory
        initial_dir = os.getcwd()

        # Navigate to the directory where the test package is located
        tests_dir = os.path.dirname(__file__)
        os.chdir(tests_dir)

        # Call the add_package_to_path function
        package_root_name = add_package_to_path()

        # Verify that the package root name is correct
        self.assertEqual(package_root_name, "nexus_utils")

        # Verify that the package root directory has been added to the path
        package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        self.assertIn(package_root, os.environ["PATH"])

        # Restore the initial working directory
        os.chdir(initial_dir)


#%%

if __name__ == '__main__':
    unittest.main()
