#!/usr/bin/env python

##
## This file is part of the sigrok-meter project.
##
## Copyright (C) 2015 Jens Steinhauser <jens.steinhauser@gmail.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
##

import unittest
import sigrok_meter.qtcompat as qtcompat
qtcompat.load_modules(False)
import sigrok_meter.samplingthread as samplingthread

class TestDriverstringParsing(unittest.TestCase):
    def setUp(self):
        self.w = samplingthread.SamplingThread.Worker(None, None)
    
    def test_valid_driverstring(self):
        self.assertEqual(
            self.w.parse_driverstring('demo'),
            ('demo', {}))
        self.assertEqual(
            self.w.parse_driverstring('demo:samplerate=1'),
            ('demo', {'samplerate': 1}))
        self.assertEqual(
            self.w.parse_driverstring('demo:samplerate=1:analog_channels=1'),
            ('demo', {'samplerate': 1, 'analog_channels': 1}))
    
    def test_invalid_driverstring(self):
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, '')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, ':')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, ':a')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, 'd:a')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, 'd:a=')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, 'd:a=:')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, 'd:a=b:')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, 'd:=b:')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, 'd:=:')
        self.assertRaisesRegexp(ValueError, 'is not a valid driver string',
            self.w.parse_driverstring, 'd:=')

if __name__ == '__main__':
    unittest.main()
