import itertools
from dvc.repo import Repo

repo = Repo(".")

# param values
n_estimators_grid = [10, 20]
max_depth_grid = [5, 10]

for n_est, max_depth in itertools.product(n_estimators_grid, max_depth_grid):
    repo.experiments.run(
        queue=True,
        params=[
            f"train.params.n_estimators={n_est}",
            f"train.params.max_depth={max_depth}",
        ],
    )
