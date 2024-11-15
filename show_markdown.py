#!/usr/bin/env python3

import panflute as pf


def action(elem, doc):
    pass


def finalize(doc):
    pf.debug(doc.content)


def main(doc=None):
    return pf.run_filter(action, finalize=finalize)


if __name__ == "__main__":
    main()
