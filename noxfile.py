# noxfile.py
import nox


@nox.session(python=["3.9", "3.8"])
def tests(session):
    args = session.posargs or ["--cov"]  # noqa: F841
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")
