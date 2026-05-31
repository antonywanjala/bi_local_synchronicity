import ta
import inspect

# Get a list of all sub-modules within the 'ta' library
modules = [ta.momentum, ta.volatility, ta.trend, ta.volume, ta.others]

print("=== COMPLETE SYSTEM INDICATOR REGISTRY ===")
for mod in modules:
    print(f"\n[Category: {mod.__name__.split('.')[-1].upper()}]")

    # Extract every class/function inside that module (returns a list of tuples)
    members = inspect.getmembers(mod, inspect.isfunction) or inspect.getmembers(mod, inspect.isclass)

    # Correctly unpack the tuple (name, object) to filter by the string name
    names = sorted(list(set([name for name, _ in members if not name.startswith('_')])))
    print(", ".join(names))
