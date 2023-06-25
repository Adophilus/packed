from packed import packed

@packed
def header():
    return (
        <div>
            <header>This is a header</header>
            <code>Here is some code for you</code>
        </div>
    )

def body():
    return (
        <main>
            <div>
                <p>
                    This is the main body
                </p>
            </div>
        </main>
    )
