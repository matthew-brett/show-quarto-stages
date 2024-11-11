#!/usr/bin/env python3

import panflute as pf

REPLACEMENT_SECTION = '## My filtered header {#sec-my-filtered-section}'


def action(elem, doc):
    if isinstance(elem, pf.Header) and 'mark-for' in pf.stringify(elem):
        return pf.convert_text(REPLACEMENT_SECTION)


def main(doc=None):
    return pf.run_filter(action)


if __name__ == "__main__":
    main()
