from lib.db.setup import Base, engine
from lib.cli import start_cli

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    start_cli()
