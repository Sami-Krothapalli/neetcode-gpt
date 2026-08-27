class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        i = 0
        update = init
        while i != iterations:
            i += 1
            # Objective function: f(x) = x^2
            # Derivative:         f'(x) = 2x
            fxdx = 2 * update
            # Update rule:        x = x - learning_rate * f'(x)
            update = update - learning_rate * fxdx
            # Round final answer to 5 decimal places
        return round(update, 5)
        pass
