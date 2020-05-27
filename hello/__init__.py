import check50
import check50.c

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("hello.py")

@check50.check(exists)
def veronica():
    """responds to name Veronica."""
    check50.run("python3 hello.py").stdin("Veronica").stdout("Veronica").exit()

@check50.check(exists)
def brian():
    """responds to name Brian."""
    check50.run("python3 hello.p<").stdin("Brian").stdout("Brian").exit()
