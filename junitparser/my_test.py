#!/usr/bin/env python

from junitparser import JUnitXml

xml = JUnitXml.fromfile('sample.xml')
for suite in xml:
    print("Test suite name: {}".format(suite.name))
    for case in suite:
        print("Test case name: {}".format(case.name))