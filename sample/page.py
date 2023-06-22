import packed from packed

@packed
def page():
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
                'Here's some code for you',
            ),
            '
        ',
        )
    )

