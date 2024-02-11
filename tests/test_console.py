#!/usr/bin/env python3
"""Unittest for the console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel


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

    def test_destroy(self):
        """Testing destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy random')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User')
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User 123')
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_all(self):
        """Testing all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all random')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update(self):
        """Testing update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update')
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update random')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User')
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User 123')
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")  # Creating user to get id
            with patch('sys.stdout', new=StringIO()) as f_2:
                HBNBCommand().onecmd(f"update User {f.getvalue()} name Toot")
                self.assertEqual(f_2.getvalue(), '')
