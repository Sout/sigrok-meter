#!/usr/bin/env python
##
## This file is part of the sigrok-meter project.
##
## Copyright (C) 2013 Uwe Hermann <uwe@hermann-uwe.de>
## Copyright (C) 2014 Jens Steinhauser <jens.steinhauser@gmail.com>
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

import argparse
import sigrok.core as sr
import sys
import textwrap
import signal

default_drivers = [('demo:analog_channels=4', 'samplerate=4')]
default_loglevel = 2

def parse_cli():
    parser = argparse.ArgumentParser(
        description='Simple sigrok GUI for multimeters and dataloggers.',
        epilog=textwrap.dedent('''\
            The DRIVER string is the same as for sigrok-cli(1). Multiple
            DRIVER and CONFIG items can be supplied. The nth CONFIG is applied
            to the nth DRIVER. If there are more drivers than configs, the
            remaining drivers use the default configuration.

            Examples:

              %(prog)s --driver tecpel-dmm-8061-ser:conn=/dev/ttyUSB0

              %(prog)s --driver uni-t-ut61e:conn=1a86.e008

              %(prog)s --driver demo:analog_channels=1 \\
                       --config samplerate=10

              %(prog)s --driver voltcraft-k204:conn=/dev/ttyUSB0 \\
                       --driver uni-t-ut61d:conn=1a86.e008 \\
                       --driver uni-t-ut61e-ser:conn=/dev/ttyUSB1
        '''),
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-d', '--driver',
        action='append',
        default=[],
        help='The driver to use')
    parser.add_argument('-c', '--config',
        action='append',
        default=[],
        help='Specify device configuration options')
    parser.add_argument('-l', '--loglevel',
        type=int,
        default=default_loglevel,
        help='Set loglevel (5 is most verbose)')
    parser.add_argument('--pyside',
        action='store_true',
        default=False,
        help='Force use of PySide (default is to use PyQt4)')
    args = parser.parse_args()

    if len(args.config) > len(args.driver):
        sys.exit('Error: More configurations than drivers given.')

    # Merge drivers and configurations into a list of tuples.
    setattr(args, 'drivers', [])
    if not args.driver:
        args.drivers = default_drivers
        sys.stderr.write('No driver given, using demo driver.\n')
    if args.driver:
        args.config.extend([''] * (len(args.driver) - len(args.config)))
        args.drivers = zip(args.driver, args.config)
    del args.driver
    del args.config

    return args


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    args = parse_cli()

    import qtcompat
    qtcompat.load_modules(args.pyside)
    QtCore = qtcompat.QtCore
    QtGui = qtcompat.QtGui
    import mainwindow

    context = sr.Context_create()
    try:
        loglevel = sr.LogLevel.get(args.loglevel)
        context.log_level = loglevel
    except:
        sys.exit('Error: invalid log level.')

    app = QtGui.QApplication([])
    s = mainwindow.MainWindow(context, args.drivers)
    s.show()

    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
