# Coding Challenge 2025 - Robot đại chiến

This is the repository of the interactor (also called the backend or the judge) of the game "Robot đại chiến", used to run the matches between the bots.

## Requirements

The judge is written in Python, with several packages used. To begin with, you need to have Python installed on your machine, specifically [Python 3.11](https://www.python.org/downloads/release/python-3110/) or higher.

You should also have a package manager to insall said dependencies for the interactor. The most commonly used one is [pip](https://pip.pypa.io/en/stable/); an alternative like [conda](https://docs.conda.io/en/latest/) can also be used (and recommended).

If you're a conda user, run this script beforehand.

```bash
conda create -n CodingChallenge2025 python=3.12
conda activate CodingChallenge2025
```

Now with a package manager available, install the necessary requirements.

```bash
pip install -r requirements.txt
```

## Usage

If cloned correctly, your folder structure should look like this:

```
.
├── Simulator
│   ├── Map
│   ├── Match
│   └── Players
└── Source
```

### Run the matches

First create a *folder* of your bot's name in `Simulator/Players` and put your executable file in it. Your executable **must be named** `main.exe`**, regardless of your operating system**.

Besides the executable the folder **should not** have any other files, as these files **will be deleted** during the interaction. The directory should then look like this:

```
.
├── Simulator
│   ├── Map
│   ├── Match
│   └── Players
│       └── mybot
│           └── main.exe
└── Source
```

Maps that are to be used in the matches should also be included, specifically in the folder `Simulator/Map`. An example `blank.txt` map has been given to you in the directory.

To start interacting, run the `run.bat` file in the following manner:

```
./run.bat <map file> <bot 1> <bot 2> <...>
```

Or if you're using Linux, run the `run.sh` file instead:

```bash
bash run.sh <map file> <bot 1> <bot 2> <...>
```

With `<bot 1>`, `<bot 2>`,... being the bot names (folder names) and `<map name>` being the map file. Only *2 or 4 bots* can be competing at the same time for a match interaction.

Example command for running 2 bots on Windows:
```ps
./run.bat blank.txt bot1 bot2
```

> [!NOTE]
> The map file `.\Simulator\Map\blank.txt` is already included in the repository. You have to compile the bot and put it in the folder `.\Simulator\Players\<bot name>\main.exe` before running the command. The example code for 2 bots is included in `\Source\`.


### After the matches

The results of the matches after interaction will be available in the `Simulator/Match` folder with the name of `<map name>_<bot 1>_<bot 2>.json`. The file stores the states of the game on each turn throughout the match.

A similarly named `.txt` file can also be found; this file records the executions of the executables, and errors with it if any (for instance executable not found or execution error).

To assist you while building the bots, the specific interacting files (`MAP.INP`, `MOVE.OUT`, `STATE.DAT`) for every player on each turn of the matches are also stored. You can access them in the folder `Simulator/Match/Players`.

## Bug report

Should any bug happen, report us through the organizer's official email (the one which mailed you this repo). Attach to it the match's `.json` file and state folders of the bot in `Simulator/Match/Players/`.