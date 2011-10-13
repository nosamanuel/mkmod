import os
import shutil
import sys
import unittest

from mkmod import INIT_PY, main, mkmod, touch

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
SUPPORT_DIR = os.path.join(TEST_DIR, 'support')


class TestMkmod(unittest.TestCase):
    def setUp(self):
        self.original_sys_argv = sys.argv
        os.chdir(SUPPORT_DIR)

    def tearDown(self):
        if os.path.exists(SUPPORT_DIR):
            shutil.rmtree(SUPPORT_DIR)
        os.makedirs(SUPPORT_DIR)
        sys.argv = self.original_sys_argv

    def test_touch(self):
        self.assertTrue(not os.path.exists(INIT_PY))

        touch(INIT_PY)

        self.assertTrue(os.path.exists(INIT_PY))

    def test_mkmod_makes_new_module(self):
        full_path = os.path.join(SUPPORT_DIR, 'top', 'sub')
        self.assertTrue(not os.path.exists('top'))
        self.assertTrue(not os.path.exists(full_path))

        mkmod('top.sub')

        self.assertTrue(os.path.exists('top'))
        self.assertTrue(os.path.exists(os.path.join('top', INIT_PY)))
        self.assertTrue(os.path.exists(full_path))
        self.assertTrue(os.path.exists(os.path.join(full_path, INIT_PY)))

    def test_mkmod_creates_directory_when_path_ends_with_sep(self):
        full_path = os.path.join(SUPPORT_DIR, 'top', 'sub')
        self.assertTrue(not os.path.exists('top'))
        self.assertTrue(not os.path.exists(full_path))

        mkmod('top.sub' + os.path.sep)

        self.assertTrue(os.path.exists('top'))
        self.assertTrue(os.path.exists(os.path.join('top', INIT_PY)))
        self.assertTrue(os.path.exists(full_path))
        self.assertTrue(os.path.exists(os.path.join(full_path, INIT_PY)))

    def test_mkmod_does_not_override_existing_init_py(self):
        init_path = os.path.join('top', INIT_PY)
        init_contents = "still_alive = True"
        os.mkdir('top')
        with open(init_path, 'w') as f:
            f.write(init_contents)

        full_path = os.path.join(SUPPORT_DIR, 'top', 'sub')
        self.assertTrue(not os.path.exists(full_path))

        mkmod('top.sub')

        self.assertTrue(os.path.exists(full_path))
        with open(init_path) as f:
            self.assertEqual(f.read(), init_contents)

    def test_mkmod_dot_creates_init_py(self):
        self.assertTrue(not os.path.exists(INIT_PY))

        mkmod('.')

        self.assertTrue(os.path.exists(INIT_PY))

    def test_main_creates_init_py_by_default(self):
        self.assertTrue(not os.path.exists(INIT_PY))

        main()

        self.assertTrue(os.path.exists(INIT_PY))


if __name__ == '__main__':
    unittest.main()
