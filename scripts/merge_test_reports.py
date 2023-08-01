#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import sys

from argparse import ArgumentParser
from glob import iglob
from junitparser import JUnitXml, TestSuite
from pathlib import Path


class ReportsMerger:
    __total_test_count = 0

    def merge(self, dir:str, mergeFile:str) -> int:
        mergedXML = JUnitXml()
        logging.info(f"Collecting test reports with pattern '{dir}/**/*.xml' ...")
        files = iglob(dir+"/**/*.xml", recursive=True)
        if len(files) < 1:
            return 1
        for f in files:
            filename=Path(f).stem
            index=filename.find("report-")
            if index == -1:
                logging.error('No files found under: '+ str(dir))
                continue
            xmTestReport = self.__udpate_testsuite_name(f, filename[index + len("report-"):].replace("-", "."))
            mergedXML = mergedXML + xmTestReport
        mergedXML.tests = self.__total_test_count

        logging.info(f"Writing merged report to '{mergeFile}' ...")
        mergedXML.write(mergeFile)

    def __udpate_testsuite_name(self, filename: str, prefix: str):
        xml = JUnitXml.fromfile(filename)
        for suite in xml:
            self.__total_test_count += int(suite.tests)
            if not prefix in suite.name:
                suite.name = prefix+"."+ suite.name 
                for case in suite:
                    case.classname = suite.name
        return xml

def main() -> int:
    try:
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        parser = ArgumentParser()
        parser.add_argument("-i", "--input", default=".", help="Directory to search for test results.")
        parser.add_argument("-o", "--outfile", default="Merged.xml", help="Merged Output file path.")
        args = parser.parse_args()

        logging.info("Merging test reports...")       
        merger = ReportsMerger()
        return merger.merge(args.input, args.outfile)

    except Exception as err:
        logging.error('Failed to merge files: '+ str(err))
        return 1

if __name__ == '__main__':
    sys.exit(main())
