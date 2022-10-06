# Califorknia
Califorknia is a simple 2D 8-bit sprite-based RPG game set in present day California, post-alien invasion.  
In this game, foodstuffs have come alive following the alien invasion of Califorknia, and your job is to tame them and use them to defeat the aliens and liberate Califorknia.  
BAA Studios has created this game for use in a sister project, where we train a neural network to play a game (using the NEAT method developed by Kenneth O. Stanley).

## Set-up
1. [Install Python](https://community.chocolatey.org/packages/python/3.10.7) (3.10 or higher)
2. Run `setup.bat` (if on Windows)  
    - For Bash on Linux, navigate to the project directory, then create a virtual environment: `python -m venv venv`
    - Next, activate the virtual environment the `source venv/bin/activate`
    - Then, install all dependencies: `pip install -r requirements.txt`
3. Run the game using the entry point `califorknia/main.py`

## Tools
This project targets Python 3.10 and up, and makes use of [PyGame](https://pypi.org/project/pygame/). YAML configuration files are parsed with [ruamel.yaml](https://pypi.org/project/ruamel.yaml/), which supports the use of comments.

## Style
This project should follow [Google Style Guides](https://github.com/google/styleguide) where possible. We recommended the use of [PyLint](https://stackoverflow.com/questions/38134086/how-to-run-pylint-with-pycharm/46409649#46409649); Google's linting rules has already been included in the project directory as `pylintrc`.
For more details on versioning and git commit logs, refer to [this](https://github.com/TEAM-SPIRIT-Productions/styleguide).

## Disclaimer

*Califorknia is a platform-agnostic open-source standalone RPG game. Califorknia is non-monetised, and provided as is. Every effort has been taken to ensure correctness and reliability of Califorknia. We will not be liable for any special, direct, indirect, or consequential damages or any damages whatsoever resulting from loss of use, data or profits, whether in an action if contract, negligence or other tortious action, arising out of or in connection with the use of Califorknia (in part or in whole).*