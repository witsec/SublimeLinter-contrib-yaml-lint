#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Mark Overduin
# Copyright (c) 2017 Mark Overduin
#
# License: MIT
#

"""This module exports the Yaml Lint plugin class."""

from SublimeLinter.lint import Linter, util


class YamlLint(Linter):

	"""Provides an interface to yaml-lint."""

	syntax = 'yaml'
	cmd = ('yaml-lint', '-q', '*')
	executable = None
	regex = (
		r'^.+? ((?P<warning>warning)|(?P<error>error)):.*\): (?P<message>.+) at line (?P<line>\d+) column (?P<col>\d+)'
	)
	tempfile_suffix = '-'
	error_stream = util.STREAM_STDOUT
	word_re = r'^(".*?"|[-\w]+)'
