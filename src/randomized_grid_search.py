import random
from dvc.repo import Repo

repo = Repo(".")

random.seed(0)
N_EXPERIMENTS = 5

for _ in range(N_EXPERIMENTS):

    n_est = random.randint(10, 100)
    max_depth = random.choice([5, 10, 15, 20])

    repo.experiments.run(
        queue=True,
        params=[
            f"train.params.n_estimators={n_est}",
            f"train.params.max_depth={max_depth}",
        ],
    )
