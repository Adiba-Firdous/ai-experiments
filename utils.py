"""Small reusable helpers for AI experiments."""


def print_section(title: str) -> None:
    """Print a readable section heading."""
    line = "=" * len(title)
    print(f"\\n{title}\\n{line}")
