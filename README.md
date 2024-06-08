![Cover image](img/legendary_pokemon.png)

# Data Science Summit 2024, ML Edition  
Repository containing the code used for my presentation at Data Science Summit 2024, ML Edition

## Classifying Legendary Pokémon

A demo project showcasing experiment tracking capabilities of DVC.
The example is built on the case of classifying Pokémon as legendary.

## Known limitations
* Generation is based on Pokédex number. That does not reflect regional forms (Galarian, Alolan, etc.), Mega Evolutions, etc.
* Until generation 8 (incl.), the legendary classification consisted of the following: Sub-Legendary Pokémon | Legendary Pokémon | Mythical Pokémon. We treat them all as legendary for the sake of this exercise.
* From generation 9 onwards, the legendary classification is slightly different, that is, there are groups called: Sub-Legendary Pokémon | Ultra Beasts | Paradox Pokémon | Restricted Legendary Pokémon | Mythical Pokémon. For example, Ultra Beasts are now a separate class and are not considered Legendary.

## References

Docs:
* https://dvc.org/doc

My articles on setting up experimentation with DVC:
* https://towardsdatascience.com/turn-vs-code-into-a-one-stop-shop-for-ml-experiments-49c97c47db27
* https://towardsdatascience.com/enhance-your-ml-experimentation-workflow-with-real-time-plots-434106b1a1c2
* https://towardsdatascience.com/the-minimalists-guide-to-experiment-tracking-with-dvc-f07e4636bdbb
* https://towardsdatascience.com/keep-track-of-your-backtests-with-dvcs-experiment-tracking-38977cbba4a9
* https://towardsdatascience.com/experiment-tracking-hyperparameter-tuning-organize-your-trials-with-dvc-d17f47f38754

How DVC uses git references for experiment tracking:
* https://iterative.ai/blog/experiment-refs

Misc:
* https://www.kaggle.com/datasets/mariotormo/complete-pokemon-dataset-updated-090420/?select=pokedex_%28Update_04.21%29.csv
* https://pokemondb.net/pokedex/all
* https://www.serebii.net/pokemon/legendary.shtml
* https://www.serebii.net/pokemon/specialpokemon.shtml

Icons:
* https://www.flaticon.com/free-icon/csv_9159105
* https://www.flaticon.com/free-icon/cloud_3222791
* https://www.flaticon.com/free-icon/laptop_114734