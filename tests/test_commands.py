import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
import unittest
from unittest.mock import MagicMock
from commands import ls, cd, chown, history
from emulator import ShellEmulator

class TestShellCommands(unittest.TestCase):
    
    def setUp(self):

        self.fs = MagicMock()
        self.shell = ShellEmulator(username='user1', tar_path='vfs.tar', log_path='test.log')
        self.shell.fs = self.fs
        self.shell.current_dir = '/home/user' 

        self.fs.list_dir.return_value = ['file1.txt', 'file2.txt']
        self.fs.change_dir.side_effect = lambda current, new: new if new in ['/home/user', '/home'] else FileNotFoundError
        self.fs.change_owner.return_value = None  

    def test_ls_command(self):
        output = ls.ls(self.fs, self.shell.current_dir)
        self.fs.list_dir.assert_called_with(self.shell.current_dir)
        self.assertIsNone(output) 

    def test_cd_command_success(self):
        new_dir = '/home'
        result = cd.cd(self.fs, self.shell, [new_dir])
        self.assertEqual(result, new_dir)  
        self.fs.change_dir.assert_called_with(self.shell.current_dir, new_dir)

    def test_cd_command_failure(self):
        self.fs.change_dir.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            cd.cd(self.fs, self.shell, ['/non_existing_directory'])

    def test_chown_command_success(self):
        chown.chown(self.fs, ['user1', 'file1.txt'])
        self.fs.change_owner.assert_called_with('/file1.txt', 'user1')

    def test_chown_command_failure(self):
        self.fs.change_owner.side_effect = FileNotFoundError  
        with self.assertRaises(FileNotFoundError):
            chown.chown(self.fs, ['user1', 'non_existing_file.txt'])

    def test_history_command(self):
        self.shell.history.append('ls')
        self.shell.history.append('cd /home')
        output = history.history(self.shell)
        self.assertEqual(len(self.shell.history), 2)

if __name__ == '__main__':
    unittest.main()
