from packed import packed

@packed
def header():
    return (
        Elem(
            'div',
            {},
            '
            ',
            Elem(
                'header',
                {},
                'This is a header',
            ),
            '
            ',
            Elem(
                'code',
                {},
                'Here is some code for you',
            ),
            '
        ',
        )
    )

def body():
    return (
        Elem(
            'main',
            {},
            '
            ',
            Elem(
                'div',
                {},
                '
                ',
                Elem(
                    'p',
                    {},
                    '
                    This is the main body
                ',
                ),
                '
            ',
            ),
            '
        ',
        )
    )
