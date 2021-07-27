import pytest
import importlib
from . import ltem
from . import quick_plots
from . import mfm
from . import util
from . import x_ray
from . import sans


__version__ = importlib.metadata.version(__name__)


def test():
    """Run all package tests.

    Examples
    --------
    1. Run all tests.

    >>> import mag2exp
    ...
    >>> # mag2exp.test()

    """
    return pytest.main(['-v', '--pyargs',
                        'mag2exp', '-l'])  # pragma: no cover
