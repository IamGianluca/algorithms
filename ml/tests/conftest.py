import numpy as np
import pytest
import scipy.stats as stats


@pytest.fixture(scope='function')
def dimensions():
    return 3

@pytest.fixture(scope='function')
def observations():
    return 25

@pytest.fixture(scope='function')
def iterations():
    return 1000

@pytest.fixture(scope='function')
def data(dimensions, observations):
    np.random.seed(1234)
    return np.random.randn(dimensions, observations)

# TODO: parametrise this, so that we can test multiple distributions (i.e.
# multivariate gaussian, uniform, cauchy, mixture of gaussians
@pytest.fixture(scope='function')
def multivariate_normal(dimensions):
    return stats.multivariate_normal(mean=np.zeros(dimensions),
                                     cov=np.eye(dimensions))
