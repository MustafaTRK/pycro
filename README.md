# pycro

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Contributors][contributors-shield]][contributors-url]
[![License][license-shield]][license-url]

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About](#about)
  - [Do I Recommend](#do-i-recommend)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Using Git](#using-git)
    - [Manuel](#manuel)
- [Usage](#usage)
  - [Option for Only Windows](#an-option-for-only-windows)
  - [On Windows, macOS and Linux](#on-windows-macos-and-linux)
- [License](#license)

## About
A simple and impressive macro, made with Python 3.9.1!
### Do I Recommend
Remember, this will give you unfair power. You are free to use it, but the responsibility is yours. Using "pycro" may be prohibited and you may be punished for using it.

## Getting Started
Pycro has been kept as customizable as possible. You will be able to set the following after starting pycro:
- How many clicks per second (CPS)
- Toggle key
- Maximum number of clicks in each period (CPS Limit)
- Mouse button (Left, Right and Middle)
- Force exit key
### Requirements
[Python 3](https://www.python.org/downloads/ "Recommended: Python 3.9 or above") <br>
[pynput library](https://pypi.org/project/pynput/ "Recommended: pynput 1.7.3 or above") <br>
[Git](https://git-scm.com/downloads "Recommended: Git 2.30.1 or above") (Optional)
### Installation
#### Using Git
```shell
git clone https://github.com/MustafaTRK/pycro
```
#### Manually
[GitHub Archive](https://github.com/MustafaTRK/pycro/archive/main.zip)

## Usage
### Option for Only Windows
You can use [these scripts](https://github.com/MustafaTRK/pycro/blob/main/scripts) prepared for you or follow the steps in the other option.
### On Windows, macOS and Linux
1. If you haven't installed the pynput library, install it with:
```shell
# Windows and macOS
pip install pynput
# If pip not added to path
python -m pip install pynput

# Linux
# Install python3-pip if not installed.
pip3 install pynput
```
2. Go to the directory where the "src" folder is.
3. Use the following command to start pycro using python:
```shell
# Windows and macOS
python src/pycro.py
# Linux
python3 src/pycro.py
```
4. Answer the questions asked to you according to your wishes.
5. Now pycro is running, enjoy yourself ;)

## License
Pycro is available under the [MIT license](https://opensource.org/licenses/MIT). Pycro also includes external libraries that are available under a variety of licenses. See [LICENSE][license-url] for the full license text.

[forks-shield]: https://img.shields.io/github/forks/MustafaTRK/pycro.svg?style=flat-square
[forks-url]: https://github.com/MustafaTRK/pycro/network/members
[stars-shield]: https://img.shields.io/github/stars/MustafaTRK/pycro.svg?style=flat-square
[stars-url]: https://github.com/MustafaTRK/pycro/stargazers
[issues-shield]: https://img.shields.io/github/issues/MustafaTRK/pycro.svg?style=flat-square
[issues-url]: https://github.com/MustafaTRK/pycro/issues
[contributors-shield]: https://img.shields.io/github/contributors/MustafaTRK/pycro.svg?style=flat-square
[contributors-url]: https://github.com/MustafaTRK/pycro/graphs/contributors
[license-shield]: https://img.shields.io/github/license/MustafaTRK/pycro.svg?style=flat-square
[license-url]: https://github.com/MustafaTRK/pycro/blob/main/LICENSE
