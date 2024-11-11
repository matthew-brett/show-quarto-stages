#!/usr/bin/env python3

import panflute as pf

REPLACEMENT_NOTE = '''\
::: {#nte-my-filtered-note .callout-note}
## My filtered heading
:::'''

def action(elem, doc):
    if (isinstance(elem, pf.Div) and
        'callout-note' in elem.classes and
        'filtered' in pf.stringify(elem)):
        return pf.convert_text('''\
::: {#nte-my-filtered-note .callout-note}
## My filtered heading
:::''', input_format='markdown', output_format='panflute')


def main(doc=None):
    return pf.run_filter(action)


if __name__ == "__main__":
    main()
