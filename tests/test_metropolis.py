from unittest.mock import patch

import numpy as np
from numpy.testing import assert_array_equal
import pytest
import scipy.stats as stats

from sampling.metropolis import MetropolisHastings


@pytest.fixture(scope='function')
def sampler(data, iterations, multivariate_normal):
    return MetropolisHastings(target=multivariate_normal, iterations=iterations,
                              data=data)


class TestMetropolisHastings:
    """Automated test suite for Metropolis-Hastings algorithm."""

    def test_data_shape(self, observations, iterations, multivariate_normal):
        """When instiatiating  a *MetropolisHastings* object, the *dimensions*
        variable should correctly recognise the right number of dimensions in
        the *numpy.array* object passed in the *data* parameters.
        """
        test_dimensions = [1, 100]
        for dimensions in test_dimensions:
            # NOTE: this test doesn't use *self.data*, hence we need to
            # instantiate a new sampler
            data = np.random.randn(dimensions, observations)
            sampler = MetropolisHastings(target=stats.norm(),
                                         iterations=iterations,
                                         data=data)
            assert sampler.shape == (dimensions, observations)

    def test_starting_point_shape(self, data, sampler):
        """The *_random_initialisation* method should generate a NumPy array
        with the correct number of dimensions, representing a random point in
        the problem space, that will be used by the algorithm as the first
        point in the Markov chain.
        """
        starting_point = sampler._random_initialisation()
        assert starting_point.shape == (data.shape[0], )

    def test_suggested_move_shape(self, sampler, dimensions):
        """The *_suggest_move* method should return a NumPy array with a new
        point in the domain of the target function.
        """
        proposed_point = sampler._suggest_move(
            current_position=np.zeros(dimensions)
        )
        assert proposed_point.shape == (dimensions, )

    def test_accept_better_point(self, dimensions, sampler):
        """When the suggested point has a higher posterior density the proposal
        should always be accepted.
        """
        current = np.ones(dimensions)
        proposal = np.zeros(dimensions)
        result = sampler._evaluate_proposal(current=current, proposal=proposal)
        assert result == True

    def test_reject_worse_point(self, dimensions, sampler):
        """When the suggested point has a lower posterior density the proposal
        should only probabilistically be accepted.
        """
        # mock pick form from uniform distribution in order to reject the
        # proposal if the proposal point is worse than the current point
        with patch('numpy.random.uniform', return_value=1):
            current = np.zeros(dimensions)
            proposal = np.random.randn(dimensions)
            result = sampler._evaluate_proposal(current=current,
                                                     proposal=proposal)
            assert result == False

    def test_element_added_to_trace(self, monkeypatch, multivariate_normal,
                                    iterations, dimensions, data):
        """At every iteration one point is added to the trace. Given the
        proposal point has a higher posterior density than the current point,
        the former should be added to the traces.
        """
        # given
        def monkeyreturn1(random):
            return np.ones(dimensions)
        def monkeyreturn2(random):
            return np.ones(dimensions) * -1
        monkeypatch.setattr(np.random, 'rand', monkeyreturn1)  # starting point
        monkeypatch.setattr(np.random, 'randn', monkeyreturn2) # proposal
    
        # when
        sampler = MetropolisHastings(target=multivariate_normal,
                                     iterations=iterations,
                                     data=data)

        # when
        traces = sampler.optimise()

        # then
        assert len(traces) == iterations
        assert_array_equal(traces[0], np.zeros(dimensions))

    def test_trace(self, iterations, multivariate_normal, data):
        """At every iteration one point should be added to the traces."""
        sampler = MetropolisHastings(target=multivariate_normal,
                                     iterations=iterations,
                                     data=data)
        traces = sampler.optimise()
        assert len(traces) == iterations
