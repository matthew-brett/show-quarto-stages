#!/usr/bin/env python3

import panflute as pf


def action(elem, doc):
    if not isinstance(elem, pf.Div):
        return
    if not 'callout-marker' in elem.classes:
        return
    return pf.convert_text('''\
::: {#nte-my-marker .callout-note}
## My heading
:::''', input_format='markdown', output_format='panflute')


def main(doc=None):
    return pf.run_filter(action)


if __name__ == "__main__":
    main()
