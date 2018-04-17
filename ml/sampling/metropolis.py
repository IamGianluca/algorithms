import numpy as np


class MetropolisHastings(object):
    """Implementation of the Metropolis-Hastings algorithm to efficiently
    sample from a desired probability distributioni for which direct sampling
    is difficult.
    """

    def __init__(self, target, data, iterations=1000):
        """Instantiate a *MetropolisHastings* object.

        Args:
            target (scipy.stats.Distribution): The target distribution. This
                distribution should proportionally approximate the desired
                distribution. NOTE: Any object implementing a *logpdf* method
                would do the job.
            data (numpy.array): N-dimensional array containing the observed
                data. NOTE: Will be soon deprecated.
            iterations (int): The number of iterations the algorithm needs to
                run.

        Attributes:
            shape (tuple): The dimensions of the *data* array.
            traces (list): The points sampled through the Markov chain sampling
                algorithm.
        """
        self.target = target
        self.data = data  # NOTE: will be deprecated in future release
        self.iterations = iterations
        self.shape = data.shape
        self.traces = list()

    def optimise(self):
        """Sample from target distribution.

        Returns:
            list: A sample of points from the target distribution.
        """
        current_position = self._random_initialisation()
        for iteration in range(self.iterations):
            proposal = self._suggest_move(current_position=current_position)
            if self._evaluate_proposal(current_position, proposal):
                current_position = proposal
            self.traces.extend([current_position])
        return self.traces

    def _random_initialisation(self):
        """Find random point to start Markov chain.

        """
        # TODO: make sure point is within function domain
        return np.random.rand(self.shape[0])

    def _suggest_move(self, current_position):
        """Suggest new point.

        Args:
            current_position (numpy.array): Current position.

        Returns:
            numpy.array: New candidate point.
        """
        # TODO: use current_position as mean of randn, to improve efficiency
        jump = np.random.randn(self.shape[0])
        return np.sum((current_position, jump), axis=0)

    def _evaluate_proposal(self, current, proposal):
        """Evaluate proposed move.

        Args:
            current (numpy.array): Current position.
            proposal (numpy.array): Proposed move.

        Returns:
            bool: Whether the proposed move is accepted.
        """
        acceptance_probability = min(
            np.exp(self.target.logpdf(x=proposal) - \
                   self.target.logpdf(x=current)),
            1
        )
        return np.random.uniform() < acceptance_probability
