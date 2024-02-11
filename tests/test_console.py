#!/usr/bin/env python3
"""Unittest for the console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import uuid


class TestConsole(unittest.TestCase):
    """
    Test Class for our Console
    """

    def test_prompt(self):
        """Testing the console prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand().prompt)

    def test_help_command(self):
        """Testing help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            self.assertEqual(
                "\nDocumented commands (type help <topic>):\n" +
                "========================================\n" +
                "EOF  all  count  create  destroy  help  " +
                "quit  show  update\n\n",
                f.getvalue())

    def test_quit_EOF_commands(self):
        """Testing quit and EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('quit')
            self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('EOF')
            self.assertEqual(f.getvalue(), '')

    def test_emptyline(self):
        """Testing emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('')
            self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('\n')
            self.assertEqual(f.getvalue(), '')

    def test_create(self):
        """Testing create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create random')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertNotEqual(f.getvalue(), '')

    def test_show(self):
        """Testing show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show random')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User')
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User 123')
            self.assertEqual(f.getvalue(), "** no instance found **\n")
